from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Simulated RAG function (replace with real LLM/RAG later)
def generate_interview_questions(name, experience, role):
    questions = {
        "software engineer": [
            "What is the difference between multithreading and multiprocessing?",
            "Can you explain SOLID principles in OOP?",
            "Describe a time you faced a production bug. How did you fix it?"
        ],
        "data analyst": [
            "How do you handle missing data?",
            "What is the difference between inner join and outer join?",
            "Describe a time when you had to explain complex data to a non-technical stakeholder."
        ]
    }

    sample_questions = questions.get(role.lower(), [
        "Why do you want this role?",
        "Describe your strengths and weaknesses.",
        "Where do you see yourself in 5 years?"
    ])

    random.shuffle(sample_questions)
    return sample_questions[:3]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        experience = request.form["experience"]
        role = request.form["role"]

        questions = generate_interview_questions(name, experience, role)
        return render_template("index.html", questions=questions, submitted=True)

    return render_template("index.html", submitted=False)

if __name__ == "__main__":
    app.run(debug=True)
