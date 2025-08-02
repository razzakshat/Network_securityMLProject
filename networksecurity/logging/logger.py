import logging
import os
from datetime import datetime

# Step 1: Create a logs directory if it doesn't exist
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Step 2: Create a timestamped log filename
log_filename = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Step 3: Full path to the log file inside the logs directory
log_file_path = os.path.join(logs_dir, log_filename)

# Step 4: Configure logging to write INFO (and above) messages to this file
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Example usage
logging.info("Logging setup complete.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")


