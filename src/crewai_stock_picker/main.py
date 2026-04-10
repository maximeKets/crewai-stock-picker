#!/usr/bin/env python
import sys
import warnings
import os
import logging
from datetime import datetime

from crewai_stock_picker.crew import StockPicker

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def check_env_vars():
    """Verify required environment variables are set."""
    required_keys = ["OPENAI_API_KEY", "SERPER_API_KEY"]
    missing_keys = [key for key in required_keys if not os.environ.get(key)]
    if missing_keys:
        logger.error(f"Missing required environment variables: {', '.join(missing_keys)}")
        logger.error("Please ensure they are set in your .env file or environment.")
        sys.exit(1)

def run():
    """
    Run the research crew.
    """
    check_env_vars()

    inputs = {
        'sector': 'Technology',
        "current_year": str(datetime.now().year)
    }
    logger.info(f"Starting CrewAI Stock Picker with inputs: {inputs}")

    try:
        # Create and run the crew
        result = StockPicker().crew().kickoff(inputs=inputs)

        # Print the result
        print("\n\n=== FINAL DECISION ===\n\n")
        print(result.raw)

    except Exception as e:
        logger.error(f"An error occurred during crew execution: {e}")
        logger.debug("Exception details:", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    run()