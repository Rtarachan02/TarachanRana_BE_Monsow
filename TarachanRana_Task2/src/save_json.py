import json
import logging
def save_json(data, output_file):
    try:
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)
        logging.info(f"Data saved to {output_file}")
    except Exception as e:
        logging.error(f"Error saving JSON file: {e}")
