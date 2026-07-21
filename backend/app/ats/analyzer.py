from app.ats.extractor import extract_skills
from app.ats.matcher import match_skills
from app.ats.scorer import calculate_score


def analyze(
    resume_text: str,
    jd_text: str
):

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    matched, missing = match_skills(
        resume_skills,
        jd_skills
    )

    score = calculate_score(
        matched,
        jd_skills
    )

    return {
        "ats_score": score,
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing)
    }