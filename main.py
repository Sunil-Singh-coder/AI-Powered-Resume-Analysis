from fastapi import FastAPI, UploadFile, File, Form
from pathlib import Path
import shutil

from src.analysis.analyzer import analyze_resume


app = FastAPI(
    title="AI-Powered Resume API",
    description="AI-powered resume analysis backend",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "AI-Powered Resume API is running!"
    }


@app.post("/analyze-resume")
async def analyze_resume_api(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    # Temporary directory
    temp_dir = Path("temp")
    temp_dir.mkdir(exist_ok=True)

    # Resume path
    resume_path = temp_dir / resume.filename

    # Save uploaded resume
    with open(resume_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    # Save Job Description as temporary text file
    jd_path = temp_dir / "job_description.txt"

    with open(jd_path, "w", encoding="utf-8") as file:
        file.write(job_description)

    # Existing analyzer expects:
    # resume PDF path + JD file path
    result = analyze_resume(
        resume_path=resume_path,
        jd_path=jd_path
    )

    return result