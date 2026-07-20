import logging

# Configure logging to write to a file with a specific format
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG, # Capture EVERYTHING from DEBUG level up
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)