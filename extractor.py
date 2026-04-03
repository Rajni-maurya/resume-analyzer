import json
import re

skills_list = json.load(open("skills.json"))

def clean_text(text):
    text = text.replace('\n', ' ')
    text = text.replace('\t', ' ')
    return text.strip()

def extract_skills(text):
    text = text.lower()
    found = []
    for skill in skills_list:
        if re.search(rf"\b{skill.lower()}\b", text):
            found.append(skill)
    return found

def extract_skills_by_dict(text, skills_list):
    text_lower = text.lower()
    found = []

    for skill in skills_list:
        if skill.lower() in text_lower:
            found.append(skill)
            return found