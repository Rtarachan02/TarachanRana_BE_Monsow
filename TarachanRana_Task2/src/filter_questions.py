def filter_questions(data, difficulty_level=None, tags=None):
    filtered_questions = []
    for question in data:
        if (difficulty_level is None or question['difficulty_level'] == difficulty_level) and \
           (tags is None or any(tag in question['tags'] for tag in tags)):
            filtered_questions.append(question)
    return filtered_questions
