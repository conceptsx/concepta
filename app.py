from flask import Flask, jsonify, render_template
from data import (
    pta_abbreviations_quiz, other_quiz, science_quiz, 
    ankle_and_foot_oian_quiz, elbow_forearm_oian_quiz, 
    hip_oian_quiz, knee_oian_quiz, neck_oian_quiz, 
    shoulder_oian_quiz, wrist_and_hand_oian_quiz, spine_and_trunk_oian_quiz
)
from categories import get_category_data

app = Flask(__name__)

# Home route (splash page)
@app.route('/')
def index():
    return render_template('index.html')

# Route for category pages
@app.route('/category/<category_name>')
def category(category_name):
    category_title, quizzes = get_category_data(category_name)
    for quiz in quizzes:
        if quiz["title"] == "PTA Abbreviations":
            quiz["questions_count"] = len(pta_abbreviations_quiz)
        elif quiz["title"] == "Ankle and Foot OIAN":
            quiz["questions_count"] = len(ankle_and_foot_oian_quiz)
        elif quiz["title"] == "Elbow and Forearm OIAN":
            quiz["questions_count"] = len(elbow_forearm_oian_quiz)
        elif quiz["title"] == "Hip OIAN":
            quiz["questions_count"] = len(hip_oian_quiz)
        elif quiz["title"] == "Knee OIAN":
            quiz["questions_count"] = len(knee_oian_quiz)
        elif quiz["title"] == "Neck OIAN":
            quiz["questions_count"] = len(neck_oian_quiz)
        elif quiz["title"] == "Shoulder OIAN":
            quiz["questions_count"] = len(shoulder_oian_quiz)
        elif quiz["title"] == "Wrist and Hand OIAN":
            quiz["questions_count"] = len(wrist_and_hand_oian_quiz)
        elif quiz["title"] == "Spine and Trunk OIAN":
            quiz["questions_count"] = len(spine_and_trunk_oian_quiz)
        elif quiz["title"] == "Other":
            quiz["questions_count"] = len(other_quiz)
        elif quiz["title"] == "Science":
            quiz["questions_count"] = len(science_quiz)
    return render_template('category.html', category_title=category_title, quizzes=quizzes)

# Route for the PTA Abbreviations Quiz
@app.route('/quiz/pta-abbreviations')
def pta_abbreviations():
    return render_template('quiz.html', quiz_title="PTA Abbreviations Quiz")

@app.route('/api/pta-abbreviations')
def get_pta_abbreviations():
    print('getting api for pta abbrev')
    return jsonify(pta_abbreviations_quiz)

# Routes for the new quizzes
@app.route('/quiz/ankle-and-foot-oian')
def ankle_and_foot_oian():
    return render_template('quiz.html', quiz_title="Ankle and Foot OIAN Quiz")

@app.route('/api/ankle-and-foot-oian')
def get_ankle_and_foot_oian():
    print('api ankle foot loading')
    return jsonify(ankle_and_foot_oian_quiz)

@app.route('/quiz/elbow-and-forearm-oian')
def elbow_and_forearm_oian():
    return render_template('quiz.html', quiz_title="Elbow and Forearm OIAN Quiz")

@app.route('/api/elbow-and-forearm-oian')
def get_elbow_and_forearm_oian():
    return jsonify(elbow_forearm_oian_quiz)

@app.route('/quiz/hip-oian')
def hip_oian():
    return render_template('quiz.html', quiz_title="Hip OIAN Quiz")

@app.route('/api/hip-oian')
def get_hip_oian():
    return jsonify(hip_oian_quiz)

@app.route('/quiz/knee-oian')
def knee_oian():
    return render_template('quiz.html', quiz_title="Knee OIAN Quiz")

@app.route('/api/knee-oian')
def get_knee_oian():
    return jsonify(knee_oian_quiz)

@app.route('/quiz/neck-oian')
def neck_oian():
    return render_template('quiz.html', quiz_title="Neck OIAN Quiz")

@app.route('/api/neck-oian')
def get_neck_oian():
    return jsonify(neck_oian_quiz)

@app.route('/quiz/shoulder-oian')
def shoulder_oian():
    return render_template('quiz.html', quiz_title="Shoulder OIAN Quiz")

@app.route('/api/shoulder-oian')
def get_shoulder_oian():
    return jsonify(shoulder_oian_quiz)

@app.route('/quiz/wrist-and-hand-oian')
def wrist_and_hand_oian():
    return render_template('quiz.html', quiz_title="Wrist and Hand OIAN Quiz")

@app.route('/api/wrist-and-hand-oian')
def get_wrist_and_hand_oian():
    return jsonify(wrist_and_hand_oian_quiz)

@app.route('/quiz/spine-and-trunk-oian')
def spine_and_trunk_oian():
    return render_template('quiz.html', quiz_title="Spine and Trunk OIAN Quiz")

@app.route('/api/spine-and-trunk-oian')
def get_spine_and_trunk_oian():
    return jsonify(spine_and_trunk_oian_quiz)

# Route for the Other Quiz
@app.route('/quiz/other')
def other_quiz_route():
    return render_template('quiz.html', quiz_title="Other Quiz")

@app.route('/api/other')
def get_other_quiz():
    return jsonify(other_quiz)

# Route for the Science Quiz
@app.route('/quiz/science')
def science_quiz_route():
    return render_template('quiz.html', quiz_title="Science Quiz")

@app.route('/api/science')
def get_science_quiz():
    return jsonify(science_quiz)

if __name__ == '__main__':
    app.run(debug=True)
