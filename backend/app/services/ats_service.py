from app.models.ats import ATSResult

def calculate_skill_match(
    resume_skills: list[str],
    jd_skills: list[str]
) -> ATSResult:

    resume_set = {skill.lower() for skill in resume_skills}
    jd_set = {skill.lower() for skill in jd_skills}

    matched = sorted(resume_set & jd_set)
    missing = sorted(jd_set - resume_set)

    percentage = (
        (len(matched) / len(jd_set)) * 100
        if jd_set else 0
    )

    return ATSResult(
        matched_skills=matched,
        missing_skills=missing,
        match_percentage=round(percentage, 2)
    )