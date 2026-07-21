# app/ats/extractor.py

KNOWN_SKILLS = {
    "python",
    "sql",
    "fastapi",
    "flask",
    "docker",
    "react",
    "javascript",
    "typescript",
    "html",
    "css",
    "linux",
    "git",
    "github",
    "machine learning",
    "deep learning",
    "nlp",
    "scikit-learn",
    "pandas",
    "numpy",
    "tensorflow",
    "pytorch",
    "aws",
    "azure",
    "gcp",
    "rest api",
}


def extract_skills(text: str) -> set[str]:
    text = text.lower()

    found = set()

    for skill in KNOWN_SKILLS:
        if skill in text:
            found.add(skill)

    return found