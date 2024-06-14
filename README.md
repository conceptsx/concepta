# ConcePTA Quiz Platform

This is a project I used to familiarize myself with JavaScript, and Flask for the backend. Reason for creating was to help my wife study for her Physical Therapy exams.

ConcePTA is a web-based quiz platform designed for Physical Therapy Assistant (PTA) exam preparation and other educational quizzes. The platform allows users to take quizzes, view results, and retake quizzes. This project uses Flask for the backend and vanilla JavaScript for the frontend.

## Live Server
[https://conceptsx.pythonanywhere.com/](url)

## Features

- Multiple categories of quizzes (PTA, Science, Other)
- Dynamic quiz generation
- Progress tracking
- Interactive quiz interface with immediate feedback
- Summary of results with percentage and letter grade
- Option to retake quizzes

## File Structure

~~~
project/
│
├── app.py
├── categories.py
├── data/
│   ├── __init__.py
│   ├── pta_abbreviations_quiz.py
│   ├── ankle_and_foot_oian_quiz.py
│   ├── elbow_forearm_oian_quiz.py
│   ├── hip_oian_quiz.py
│   ├── knee_oian_quiz.py
│   ├── neck_oian_quiz.py
│   ├── shoulder_oian_quiz.py
│   ├── wrist_and_hand_oian_quiz.py
│   ├── spine_and_trunk_oian_quiz.py
│   ├── other_quiz.py
│   └── science_quiz.py
├── templates/
│   ├── index.html
│   ├── category.html
│   └── quiz.html
├── static/
│   ├── styles.css
│   └── script.js
└── README.md
~~~

## Getting Started

### Prerequisites
* Python 3.x
* Flask

### Installation
1. Clone the repository:
~~~
git clone https://github.com/yourusername/concepta.git
cd concepta
~~~

2. Create a virtual enviroment:
~~~
python -m venv .venv
~~~

3. Activate virtual enviroment:
  * Windows
    ~~~
    .venv\Scripts\activate
    ~~~
  * Linux
    ~~~
    source .venv/bin/activate
    ~~~

4. Install dependencies
   ~~~
   pip install -r requirements.txt

### Running the Application
1. Start the Flask app.
   ~~~
   python app.py
   ~~~
2. Open web browser and go to 'http://127.0.0.1:5000'

### Adding new quizzes
1. Create a new quiz file in the 'data' directory and define quiz data.
2. Update 'data/__init__.py' to include the new quiz:
   ~~~
   from .new_quiz import new_quiz
   ~~~
3. Import the new quiz data in 'app.py'
   ~~~
   from data import new_data
   ~~~
4. Add the new quiz to the appropiate category in 'categories.py'
   ~~~
   def get_category_data(category_name):
    if category_name == 'pta':
        quizzes = [
            {"title": "PTA Abbreviations Quiz", "url": "/quiz/pta-abbreviations"},
            {"title": "Ankle and Foot OIAN Quiz", "url": "/quiz/ankle-and-foot-oian"},
            # Add your new quiz here
        ]
        category_title = "PTA Quizzes"
    # Repeat for other categories
   ~~~
5. Add routes for the new quiz in 'app.py'
   ~~~
   @app.route('/quiz/new-quiz')
   def new_quiz_route():
     return render_template('quiz.html', quiz_title="New Quiz")

   @app.route('/api/new-quiz')
   def get_new_quiz():
     return jsonify(new_quiz)
   ~~~
   

