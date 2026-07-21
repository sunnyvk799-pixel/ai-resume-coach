from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import shutil

from app.parsers.pdf_parser import extract_pdf_text
from app.services.analysis_services import analysis_service

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent

RESUME_UPLOAD_DIR = BASE_DIR / "uploads" / "resumes"
JD_UPLOAD_DIR = BASE_DIR / "uploads" / "job_descriptions"

RESUME_UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
JD_UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def save_pdf(upload_file: UploadFile, upload_dir: Path) -> str:
    if not upload_file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    file_path = upload_dir / upload_file.filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return extract_pdf_text(str(file_path))


@router.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    job_description: UploadFile = File(...)
):
    resume_text = save_pdf(resume, RESUME_UPLOAD_DIR)
    jd_text = save_pdf(job_description, JD_UPLOAD_DIR)

    result = analysis_service.analyze(
        resume_text=resume_text,
        jd_text=jd_text
    )

    return result