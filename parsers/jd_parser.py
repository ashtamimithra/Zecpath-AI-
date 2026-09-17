import re 

SKILL_DB = { 
    "python": ["python", "py"], 
    "django": ["django"], 
    "javascript": ["javascript", "js"], 
    "react": ["react", "reactjs"], 
    "node": ["node", "nodejs"], 
    "sql": ["sql", "mysql", "postgresql"] 
} 

def clean_text(text): 
    text = text.lower() 
    text = re.sub(r"[^a-z0-9\s\.\,\-]", "", text) 
    text = re.sub(r"\s+", " ", text) 
    return text.strip()

def extract_skills(text): 
    found_skills = [] 
    for skill, variants in SKILL_DB.items(): 
        for variant in variants: 
            if variant in text: 
                found_skills.append(skill) 
    return list(set(found_skills)) 

def extract_experience(text): 
    match = re.findall(r"(\d+)\+?\s*(years|yrs)", text) 
    if match: 
        return int(match[0][0]) 
    return None

def extract_role(text): 
    roles = ["developer", "engineer", "manager", "analyst"] 
    for role in roles: 
        if role in text:
            return role 
    return "unknown" 


def extract_education(text): 
    if "btech" in text or "b.e" in text: 
        return "B.Tech" 
    elif "mtech" in text or "m.e" in text: 
        return "M.Tech" 
    elif "mba" in text: 
        return "MBA" 
    return "Not Specified"

 
def parse_job_description(jd_text): 
    cleaned = clean_text(jd_text) 
    return { 
        "job_title": extract_role(cleaned), 
        "required_skills": extract_skills(cleaned), 
        "min_experience_years": extract_experience(cleaned), 
        "education_required": extract_education(cleaned), 
        "raw_text": jd_text, 
        "cleaned_text": cleaned
    }
 
# with open(r"parsers\jd.txt","r") as jd:
#     jd_data = jd.read()
#     pjd=parse_job_description(jd_data)
#     print(pjd)
    