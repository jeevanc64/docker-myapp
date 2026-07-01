from flask import Flask, render_template, request
app = Flask(__name__)
QUIZ_DATA = [
    {"id": 1, "q": "What is 5 + 5?", 
     "options": ["8", "10", "12"], 
     "ans": "10"},
    {"id": 2, "q": "Capital of France?",
      "options": ["Berlin", "Madrid", "Paris"],
    "ans": "Paris"},
    {"id": 3, "q": "Which is a programming language?", 
     "options": ["Python", "Snake", "Lizard"], 
     "ans": "Python"},
     {"id": 4, "q": "what is the square of 64?", 
     "options": ["8", "3", "9"], "ans": "8"}
]
@app.route('/')
def quiz():
    return render_template('index.html',questions=QUIZ_DATA)
@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for q in QUIZ_DATA:
        user_answer = request.form.get(str(q['id']))
        if user_answer == q['ans']:
            score += 1
    return render_template(
        'result.html',
        score=score,
        total=len(QUIZ_DATA)
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)