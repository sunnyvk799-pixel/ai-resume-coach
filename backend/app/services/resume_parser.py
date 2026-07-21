import re

from app.models.resume import Resume


def parse_resume(text: str) -> Resume:

    resume = Resume()

    email = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    if email:
        resume.email = email.group()

    phone = re.search(
        r"\+?\d[\d\s\-]{8,}\d",
        text
    )

    if phone:
        resume.phone = phone.group()

    return resume