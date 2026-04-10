import gradio as gr
from datetime import datetime
import os

from crewai_stock_picker.crew import StockPicker

def run_research(sector):
    """
    Function called by Gradio to run the CrewAI research.
    """
    # Quick check for environment variables inside the UI thread
    required_keys = ["OPENAI_API_KEY", "SERPER_API_KEY"]
    for key in required_keys:
        if not os.environ.get(key):
            return f"❌ **Error**: Missing environment variable `{key}`. Please set it in your environment."
            
    inputs = {
        'sector': sector,
        "current_year": str(datetime.now().year)
    }
    
    try:
        # Run the Crew
        result = StockPicker().crew().kickoff(inputs=inputs)
        return result.raw
    except Exception as e:
        return f"❌ **An error occurred during execution:**\n\n```text\n{str(e)}\n```"

def main():
    """
    Launch the Gradio interface
    """
    with gr.Blocks(title="CrewAI Stock Picker") as demo:
        gr.Markdown("# 📈 CrewAI Stock Picker")
        gr.Markdown("Enter a sector (e.g. Technology, Healthcare, Energy) to find trending companies and get the best stock recommendation powered by AI agents.")
        
        with gr.Row():
            with gr.Column():
                sector_input = gr.Textbox(label="Sector", placeholder="Technology", value="Technology")
                run_btn = gr.Button("🔍 Run AI Research", variant="primary")
            
            with gr.Column():
                output_markdown = gr.Markdown("### Results will appear here...", label="Final Decision Report")
                
        run_btn.click(fn=run_research, inputs=sector_input, outputs=output_markdown)
        
    # Expose the port commonly used by Docker/Gradio
    demo.launch(server_name="0.0.0.0", server_port=7850)

if __name__ == "__main__":
    main()
