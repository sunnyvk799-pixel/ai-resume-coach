from app.services.ats_service import calculate_skill_match

resume = [
    "Python",
    "SQL",
    "Docker",
    "Git",
    "Linux"
]

jd = [
    "Python",
    "Docker",
    "AWS",
    "FastAPI"
]

result = calculate_skill_match(resume, jd)

print(result.model_dump())