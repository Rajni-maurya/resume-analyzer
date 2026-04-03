import json

def calculate_match(resume_text, job_desc):
    with open("skills.json") as f:
        skills = json.load(f)

    resume_text = resume_text.lower()
    job_desc = job_desc.lower()

    resume_skills = []
    job_skills = []

    # ✅ Resume se skills extract
    for skill in skills:
        if skill in resume_text:
            resume_skills.append(skill)

    # ✅ JD se automatic skills extract
    for skill in skills:
        if skill in job_desc:
            job_skills.append(skill)

    # 🔥 Fallback: agar JD me skills nahi mile
    if len(job_skills) == 0:

        if "web developer" in job_desc:
            job_skills = ["html", "css", "javascript", "react", "api", "git"]

        elif "python developer" in job_desc:
            job_skills = ["python", "flask", "django", "sql"]

        elif "digital marketing" in job_desc:
            job_skills = ["seo", "marketing", "ads", "social media"]

    # ✅ Matching
    matched = set(resume_skills).intersection(set(job_skills))

    # ✅ Score calculation
    if len(job_skills) == 0:
        score = int((len(resume_skills) / len(skills)) * 100)
    else:
        score = int((len(matched) / len(job_skills)) * 100)

    missing = list(set(job_skills) - set(matched))
    return score, list(matched), missing