# main.py
import logging
from src.data_handler import read_json
from src.filter_questions import filter_questions
from src.save_json import save_json

def main():
    # Set up logging
    logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Read data from JSON file
    input_file = 'data/input_questions.json'
    questions_data = read_json(input_file)
    if not questions_data:
        logging.error('Failed to read input JSON file. Exiting...')
        return

    # Filter questions based on difficulty level and tags
    filtered_questions = filter_questions(questions_data, difficulty_level='Medium', tags=['History'])

    # Save filtered questions to a new JSON file
    output_file = 'data/filtered_questions.json'
    save_json(filtered_questions, output_file)

if __name__ == '__main__':
    main()
