def match_skills(
    resume_skills: set[str],
    jd_skills: set[str]
):
    matched = resume_skills & jd_skills
    missing = jd_skills - resume_skills

    return matched, missing