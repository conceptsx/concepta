let currentQuestionIndex = 0;
let questions = [];
let correctAnswersCount = 0;

document.addEventListener("DOMContentLoaded", () => {
    const quizTitle = document.querySelector('h1').innerText;
    let quizApiUrl;

    // Determine the API URL based on the quiz title
    switch (quizTitle) {
        case "PTA Abbreviations Quiz":
            quizApiUrl = '/api/pta-abbreviations';
            break;
        case "Ankle and Foot OIAN Quiz":
            quizApiUrl = '/api/ankle-and-foot-oian';
            break;
        case "Elbow and Forearm OIAN Quiz":
            quizApiUrl = '/api/elbow-and-forearm-oian';
            break;
        case "Hip OIAN Quiz":
            quizApiUrl = '/api/hip-oian';
            break;
        case "Knee OIAN Quiz":
            quizApiUrl = '/api/knee-oian';
            break;
        case "Neck OIAN Quiz":
            quizApiUrl = '/api/neck-oian';
            break;
        case "Shoulder OIAN Quiz":
            quizApiUrl = '/api/shoulder-oian';
            break;
        case "Wrist and Hand OIAN Quiz":
            quizApiUrl = '/api/wrist-and-hand-oian';
            break;
        case "Spine and Trunk OIAN Quiz":
            quizApiUrl = '/api/spine-and-trunk-oian';
            break;
        case "Other Quiz":
            quizApiUrl = '/api/other';
            break;
        case "Science Quiz":
            quizApiUrl = '/api/science';
            break;
        default:
            console.error("Unknown quiz title:", quizTitle);
    }

    if (quizApiUrl) {
        console.log(`Fetching quiz data from ${quizApiUrl}`);
        fetch(quizApiUrl)
            .then(response => {
                console.log('Response received:', response);
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                console.log('Data fetched:', data);
                questions = data;
                shuffleArray(questions); // Shuffle the questions
                if (questions.length > 0) {
                    updateProgressBar();
                    showQuestion();
                } else {
                    document.getElementById('question').innerText = 'No questions available';
                }
            })
            .catch(error => console.error('Error fetching questions:', error));
    }
});

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

function updateProgressBar() {
    const progressBar = document.getElementById('progress-bar');
    const progress = ((currentQuestionIndex + 1) / questions.length) * 100;
    progressBar.style.width = progress + '%';
}

function showQuestion() {
    const questionContainer = document.getElementById('question');
    const optionsContainer = document.getElementById('options');
    const currentQuestion = questions[currentQuestionIndex];

    questionContainer.innerText = currentQuestion.question;
    optionsContainer.innerHTML = '';

    currentQuestion.options.forEach((option, index) => {
        const optionButton = document.createElement('button');
        optionButton.classList.add('option');
        optionButton.innerText = option;
        optionButton.addEventListener('click', () => selectOption(index));
        optionsContainer.appendChild(optionButton);
    });
}

function selectOption(selectedIndex) {
    const currentQuestion = questions[currentQuestionIndex];
    const options = document.querySelectorAll('.option');
    const correctIndex = currentQuestion.options.findIndex(option => option.charAt(0).toLowerCase() === currentQuestion.answer);

    console.log(`Selected Index: ${selectedIndex}, Correct Index: ${correctIndex}`);

    options.forEach((button, index) => {
        button.disabled = true; // Disable all buttons

        if (index === correctIndex) {
            button.classList.add('correct'); // Always highlight the correct option in green
        }
        if (index === selectedIndex && selectedIndex !== correctIndex) {
            button.classList.add('wrong'); // Highlight the selected wrong option in red
        }
    });

    if (selectedIndex === correctIndex) {
        correctAnswersCount++;
    }

    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
        document.getElementById('next-btn').style.display = 'block';
    } else {
        showSummary();
    }
}

function nextQuestion() {
    document.getElementById('next-btn').style.display = 'none';
    showQuestion();
    updateProgressBar();
}

function showSummary() {
    const questionContainer = document.getElementById('question');
    const optionsContainer = document.getElementById('options');
    const progressContainer = document.getElementById('progress-container');
    const nextButton = document.getElementById('next-btn');
    const retakeButton = document.getElementById('retake-btn');

    questionContainer.innerText = 'Quiz Completed!';
    optionsContainer.innerHTML = '';
    progressContainer.style.display = 'none';
    nextButton.style.display = 'none';

    const score = (correctAnswersCount / questions.length) * 100;
    const letterGrade = getLetterGrade(score);

    const summary = document.createElement('div');
    summary.innerHTML = `
        <p>You answered ${correctAnswersCount} out of ${questions.length} questions correctly.</p>
        <p>Your score: ${score.toFixed(2)}%</p>
        <p>Your grade: ${letterGrade}</p>
    `;

    optionsContainer.appendChild(summary);
    retakeButton.style.display = 'block';
}

function retakeQuiz() {
    currentQuestionIndex = 0;
    correctAnswersCount = 0;
    shuffleArray(questions);
    showQuestion();
    document.getElementById('progress-container').style.display = 'block';
    document.getElementById('next-btn').style.display = 'block';
    document.getElementById('retake-btn').style.display = 'none';
    updateProgressBar();
}

function getLetterGrade(score) {
    if (score >= 90) return 'A';
    if (score >= 80) return 'B';
    if (score >= 70) return 'C';
    if (score >= 60) return 'D';
    return 'F';
}