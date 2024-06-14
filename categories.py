def get_category_data(category_name):
    if category_name == 'pta':
        quizzes = [
            {"title": "PTA Abbreviations", "url": "/quiz/pta-abbreviations"},
            {"title": "Ankle and Foot OIAN", "url": "/quiz/ankle-and-foot-oian"},
            {"title": "Elbow and Forearm OIAN", "url": "/quiz/elbow-and-forearm-oian"},
            {"title": "Hip OIAN", "url": "/quiz/hip-oian"},
            {"title": "Knee OIAN", "url": "/quiz/knee-oian"},
            {"title": "Neck OIAN", "url": "/quiz/neck-oian"},
            {"title": "Shoulder OIAN", "url": "/quiz/shoulder-oian"},
            {"title": "Wrist and Hand OIAN", "url": "/quiz/wrist-and-hand-oian"},
            {"title": "Spine and Trunk OIAN", "url": "/quiz/spine-and-trunk-oian"}
        ]
        category_title = "Physical Therapy Exam Assistance"
    elif category_name == 'other':
        quizzes = [
            {"title": "Other", "url": "/quiz/other"},
            # Add more Other quizzes here
        ]
        category_title = "Other"
    elif category_name == 'science':
        quizzes = [
            {"title": "Science", "url": "/quiz/science"},
            # Add more Science quizzes here
        ]
        category_title = "Science"
    else:
        quizzes = []
        category_title = "Unknown Category"
    
    return category_title, quizzes
