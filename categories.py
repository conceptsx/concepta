def get_category_data(category_name):
    if category_name == 'pta':
        quizzes = [
            {"title": "PTA Abbreviations Quiz", "url": "/quiz/pta-abbreviations"},
            {"title": "Ankle And Foot OIAN Quiz", "url": "/quiz/ankle-and-foot-oian"},
            {"title": "Elbow And Forearm OIAN Quiz", "url": "/quiz/elbow-and-forearm-oian"},
            {"title": "Hip OIAN Quiz", "url": "/quiz/hip-oian"},
            {"title": "Knee OIAN Quiz", "url": "/quiz/knee-oian"},
            {"title": "Neck OIAN Quiz", "url": "/quiz/neck-oian"},
            {"title": "Shoulder OIAN Quiz", "url": "/quiz/shoulder-oian"},
            {"title": "Wrist And Hand OIAN Quiz", "url": "/quiz/wrist-and-hand-oian"},
            {"title": "Spine And Trunk OIAN Quiz", "url": "/quiz/spine-and-trunk-oian"}
        ]
        category_title = "PTA Quizzes"
    elif category_name == 'other':
        quizzes = [
            {"title": "Other Quiz", "url": "/quiz/other"},
            # Add more Other quizzes here
        ]
        category_title = "Other Quizzes"
    elif category_name == 'science':
        quizzes = [
            {"title": "Science Quiz", "url": "/quiz/science"},
            # Add more Science quizzes here
        ]
        category_title = "Science Quizzes"
    else:
        quizzes = []
        category_title = "Unknown Category"
    
    return category_title, quizzes
