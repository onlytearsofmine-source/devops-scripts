import os
import subprocess
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Define constants
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    WORKDIR = os.path.join(BASE_DIR, 'work')
    LOG_FILE = os.path.join(WORKDIR, 'log.txt')

    # Create log file if it doesn't exist
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, 'w').close()

    # Get current working directory
    current_dir = os.getcwd()

    # Get list of files in current directory
    files = [f for f in os.listdir(current_dir) if os.path.isfile(f)]

    # Iterate over files and run script on each file
    for file in files:
        if file.endswith('.py'):
            script_path = os.path.join(current_dir, file)
            try:
                # Run script using subprocess
                subprocess.run(['python', script_path])
            except subprocess.CalledProcessError as e:
                logger.error(f"Error running script: {e}")
            except Exception as e:
                logger.error(f"Error running script: {e}")

if __name__ == '__main__':
    main()