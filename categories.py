def get_category_data(category_name, subcategory_name=None):
    if category_name == 'pta':
        if subcategory_name is None:
            quizzes = [
                {"title": "Anatomy", "url": "/category/pta/anatomy"},
                {"title": "Documentation", "url": "/category/pta/documentation"},
                # Add more subcategories here
            ]
            category_title = "Physical Therapy Library"
        elif subcategory_name == 'anatomy':
            quizzes = [
                {"title": "Ankle And Foot OIAN", "url": "/quiz/ankle-and-foot-oian"},
                {"title": "Elbow And Forearm OIAN", "url": "/quiz/elbow-and-forearm-oian"},
                {"title": "Hip OIAN", "url": "/quiz/hip-oian"},
                {"title": "Knee OIAN", "url": "/quiz/knee-oian"},
                {"title": "Neck OIAN", "url": "/quiz/neck-oian"},
                {"title": "Shoulder OIAN", "url": "/quiz/shoulder-oian"},
                {"title": "Wrist And Hand OIAN", "url": "/quiz/wrist-and-hand-oian"},
                {"title": "Spine And Trunk OIAN", "url": "/quiz/spine-and-trunk-oian"}
            ]
            category_title = "Physical Therapy: Anatomy"
        elif subcategory_name == 'documentation':
            quizzes = [
                {"title": "Abbreviations", "url": "/quiz/pta-abbreviations"},
                # Add more abbreviation quizzes here
            ]
            category_title = "Physical Therapy: Documentation"
        else:
            quizzes = []
            category_title = "Unknown Subcategory"
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
