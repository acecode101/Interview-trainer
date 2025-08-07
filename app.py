from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_interview_data(role):
    role = role.lower()

    question_bank = {
        "software engineer": [
            "Explain the concept of multithreading and multiprocessing.",
            "What are SOLID principles in object-oriented design?",
            "Tell me about a production issue you resolved recently."
        ],
        "data analyst": [
            "How would you handle missing values in a dataset?",
            "What's the difference between an inner join and outer join?",
            "Explain a scenario where data storytelling helped stakeholders."
        ]
    }

    industry_expectations = {
        "software engineer": "Proficiency in data structures, system design, clean code practices, and teamwork in Agile environments.",
        "data analyst": "Strong skills in SQL, data visualization, reporting, and stakeholder communication."
    }

    behavioral_scenarios = {
        "software engineer": "Describe a time you disagreed with a technical decision. How did you handle it?",
        "data analyst": "Share a project where your analysis led to a major business decision."
    }

    hr_guidelines = {
        "software engineer": "Be honest about experience gaps. Emphasize willingness to learn, past collaborations, and ownership.",
        "data analyst": "Highlight curiosity, business acumen, and the ability to simplify complex insights."
    }

    improvement_tips = {
        "software engineer": "Practice coding problems on LeetCode. Prepare system design basics. Be clear and structured in answers.",
        "data analyst": "Use STAR format for behavioral questions. Familiarize yourself with business KPIs and storytelling."
    }

    default_questions = [
        "Why do you want this role?",
        "Describe your strengths and weaknesses.",
        "Where do you see yourself in 5 years?"
    ]

    return {
        "questions": question_bank.get(role, default_questions),
        "expectations": industry_expectations.get(role, "Stay updated with latest tools and practices in your domain."),
        "behavioral": behavioral_scenarios.get(role, "Talk about a challenge you overcame at work and what you learned."),
        "hr_guidelines": hr_guidelines.get(role, "Be professional, honest, and show your enthusiasm for the role."),
        "tips": improvement_tips.get(role, "Practice mock interviews, review common questions, and build confidence.")
    }

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        # Extract role from the prompt
        try:
            role_title = prompt.split("role of ")[1].strip().rstrip(".")
        except IndexError:
            role_title = "general"

        data = generate_interview_data(role_title)

        return render_template("index.html",
                               prompt=prompt,
                               role_title=role_title.title(),
                               questions=data["questions"],
                               expectations=data["expectations"],
                               behavioral=data["behavioral"],
                               hr_guidelines=data["hr_guidelines"],
                               tips=data["tips"],
                               submitted=True)
    return render_template("index.html", submitted=False)
