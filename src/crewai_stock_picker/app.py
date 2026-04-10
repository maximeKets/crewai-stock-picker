import gradio as gr
from datetime import datetime
import os

from crewai_stock_picker.crew import StockPicker
from crewai_stock_picker.usage_tracker import has_exceeded_quota, increment_usage, get_usage, MAX_QUOTA

def run_research(sector: str, profile: gr.OAuthProfile | None):
    """
    Function called by Gradio to run the CrewAI research.
    It yields a waiting message, runs the synchronous Crew task, 
    and then yields the final Markdown result.
    """
    if profile is None:
        yield "⚠️ **Authentification requise**\n\nVeuillez vous connecter avec votre compte Hugging Face (bouton 'Sign in with Hugging Face') en haut à droite pour lancer l'analyse."
        return

    username = profile.username

    if has_exceeded_quota(username):
        yield f"⚠️ **Limite de {MAX_QUOTA} recherches atteinte**\n\nVous avez utilisé tout votre quota disponible pour ce profil ({username})."
        return

    # Quick check for environment variables inside the UI thread
    required_keys = ["OPENAI_API_KEY", "SERPER_API_KEY"]
    for key in required_keys:
        if not os.environ.get(key):
            yield f"❌ **Error**: Missing environment variable `{key}`. Please set it in your environment."
            return
            
    inputs = {
        'sector': sector,
        "current_year": str(datetime.now().year)
    }
    
    yield f"⏳ **Lancement de l'analyse pour le secteur `{sector}`...**\n\n*Les agents de CrewAI s'activent pour rechercher les meilleures actions du moment. Veuillez patienter environ 1 à 3 minutes.*"
    
    try:
        # Run the Crew
        result = StockPicker().crew().kickoff(inputs=inputs)
        
        increment_usage(username)
        current_usage = get_usage(username)
        
        final_report = result.raw
        
        yield f"{final_report}\n\n---\n*Recherche effectuée par {username} ({current_usage}/{MAX_QUOTA} requêtes utilisées)*"
    except Exception as e:
        yield f"❌ **An error occurred during execution:**\n\n```text\n{str(e)}\n```"

def main():
    """
    Launch the Gradio interface
    """
    with gr.Blocks(title="CrewAI Stock Picker") as demo:
        with gr.Row():
            gr.Markdown("# 📈 CrewAI Stock Picker")
            gr.LoginButton()
            
        gr.Markdown("Enter a sector (e.g. Technology, Healthcare, Energy) to find trending companies and get the best stock recommendation powered by AI agents.")
        
        with gr.Row():
            with gr.Column():
                sector_input = gr.Textbox(label="Sector", placeholder="Technology", value="Technology")
                run_btn = gr.Button("🔍 Run AI Research", variant="primary")
            
            with gr.Column():
                output_markdown = gr.Markdown("### Results will appear here...", label="Final Decision Report")
                
        run_btn.click(fn=run_research, inputs=sector_input, outputs=output_markdown)
        sector_input.submit(fn=run_research, inputs=sector_input, outputs=output_markdown)
        
    # Expose the port commonly used by Docker/Gradio
    demo.launch(server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
    main()