# ConcePTA Quiz Platform

ConcePTA is a web-based quiz platform designed for Physical Therapy Assistant (PTA) exam preparation and other educational quizzes. The platform allows users to take quizzes, view results, and retake quizzes. This project uses Flask for the backend and vanilla JavaScript for the frontend.

## Features

- Multiple categories of quizzes (PTA, Science, Other)
- Dynamic quiz generation
- Progress tracking
- Interactive quiz interface with immediate feedback
- Summary of results with percentage and letter grade
- Option to retake quizzes

## File Structure

```plaintext
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

