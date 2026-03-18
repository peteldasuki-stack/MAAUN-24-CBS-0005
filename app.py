from flask import Flask, render_template, request
from models import Question, QuizHistory

app = Flask(__name__)
history = QuizHistory()

# Setup Quiz Data
quiz_data = [
    Question("What is the keyword for a function?", "a) def, b) func", "a"),
    Question("Is Python OOP?", "a) Yes, b) No", "a")
]

# [span_17](start_span)Requirement: Route 1 - Home/Quiz Page[span_17](end_span)
@app.route('/')
def home():
    return render_template('index.html', questions=quiz_data)

# [span_18](start_span)Requirement: Route 2 - Results Page[span_18](end_span)
@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for i, q in enumerate(quiz_data):
        answer = request.form.get(f"question_{i}")
        if q.check_answer(answer):
            score += 1
    
    history.add_result(score, len(quiz_data))
    latest = history.get_recent()
    return f"<h1>Quiz Finished!</h1><p>{latest}</p><a href='/'>Try Again</a>"

if __name__ == '__main__':
    app.run(debug=True)