from flask import Flask, jsonify, render_template
from data import (
    pta_abbreviations_quiz, other_quiz, science_quiz, ankle_and_foot_oian_quiz,
    elbow_and_forearm_oian_quiz, hip_oian_quiz, knee_oian_quiz, neck_oian_quiz,
    shoulder_oian_quiz, wrist_and_hand_oian_quiz, spine_and_trunk_oian_quiz
)
from categories import get_category_data

app = Flask(__name__)

# Dictionary to map quiz names to data
quiz_data_map = {
    "pta_abbreviations": pta_abbreviations_quiz,
    "ankle_and_foot_oian": ankle_and_foot_oian_quiz,
    "elbow_and_forearm_oian": elbow_and_forearm_oian_quiz,
    "hip_oian": hip_oian_quiz,
    "knee_oian": knee_oian_quiz,
    "neck_oian": neck_oian_quiz,
    "shoulder_oian": shoulder_oian_quiz,
    "wrist_and_hand_oian": wrist_and_hand_oian_quiz,
    "spine_and_trunk_oian": spine_and_trunk_oian_quiz,
    "other": other_quiz,
    "science": science_quiz,
}

# Home route (splash page)
@app.route('/')
def index():
    print("Home route accessed")
    return render_template('index.html')

# Route for category pages
@app.route('/category/<category_name>')
def category(category_name):
    category_title, quizzes = get_category_data(category_name)
    for quiz in quizzes:
        quiz_data_variable = quiz["url"].split("/")[-1].replace("-", "_")
        if quiz_data_variable in quiz_data_map:
            quiz["questions_count"] = len(quiz_data_map[quiz_data_variable])
        else:
            quiz["questions_count"] = 0
    print(f"Category route accessed: {category_name}")
    return render_template('category.html', category_title=category_title, quizzes=quizzes)

# Route for the quiz page
@app.route('/quiz/<quiz_name>')
def quiz_page(quiz_name):
    quiz_title = quiz_name.replace('-', ' ').title() + " Quiz"
    print(f"Quiz page accessed: {quiz_name}")
    return render_template('quiz.html', quiz_title=quiz_title)

# Route for the quiz API
@app.route('/api/<quiz_name>')
def get_quiz_data(quiz_name):
    quiz_data_variable = quiz_name.replace('-', '_')
    quiz_data = quiz_data_map.get(quiz_data_variable)
    if quiz_data is None:
        print(f"Quiz data not found for: {quiz_name}")
        return jsonify({"error": "Quiz not found"}), 404
    print(f"Quiz data accessed for: {quiz_name}")
    return jsonify(quiz_data)

if __name__ == '__main__':
    app.run(debug=True)
