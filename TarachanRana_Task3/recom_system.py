# recommendation_system.py
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Load questions data from JSON file
with open('data/questions.json', 'r') as file:
    questions_data = json.load(file)

@app.route('/recommend', methods=['POST'])
def recommend_questions():
    # Get user inputs from JSON request
    user_inputs = request.json

    # Filter questions based on user inputs
    relevant_questions = filter_questions(user_inputs)

    # Save recommended questions to recommended.json
    save_recommended_questions(relevant_questions)

    # Return recommended questions in JSON format
    return jsonify({'recommended_questions': relevant_questions})

def filter_questions(user_inputs):
    # Get the user inputs
    skills = user_inputs.get('skills', [])

    # Filter questions based on user inputs
    relevant_questions = []
    for question in questions_data:
       if any(skill.lower() == tag.lower() for skill in skills for tag in question['tags']):
            relevant_questions.append(question['question'])

    return relevant_questions

def save_recommended_questions(relevant_questions):
    # Save recommended questions to recommended.json in data folder
    data_folder = 'data'
    recommended_file = os.path.join(data_folder, 'recommended.json')
    with open(recommended_file, 'w') as file:
        json.dump(relevant_questions, file, indent=4)

if __name__ == '__main__':
    app.run(debug=True)
