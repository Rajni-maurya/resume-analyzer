from flask import Flask, render_template, request
from parser import extract_text
from matcher import calculate_match

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']
    job_desc = request.form['job_description']

    resume_text = extract_text(file)

    score, matched, missing = calculate_match(resume_text, job_desc)

    return render_template(
        'result.html',
        score=score,
        matched=matched,
        missing=missing
    )

if __name__ == '__main__':
    app.run(debug=True)