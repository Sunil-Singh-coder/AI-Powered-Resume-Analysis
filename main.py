from fastapi import FastAPI, UploadFile, File, Form
from pathlib import Path
import shutil
from src.database.save_analysis import save_analysis
from src.database.save_resume import save_resume
from src.database.save_job_description import save_job_description
from src.analysis.analyzer import analyze_resume
from src.database.save_user import get_or_create_user
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="AI-Powered Resume API",
    description="AI-powered resume analysis backend",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "AI-Powered Resume API is running!"
    }


@app.post("/analyze-resume")
async def analyze_resume_api(
    name: str = Form(...),
    email: str = Form(...),
    job_title: str = Form(...),
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    # Database code to save the resume 

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

    user_id = get_or_create_user(
    name=name,
    email=email
)


    result = analyze_resume(
    resume_path=resume_path,
    jd_path=jd_path

)  

   # Save resume in database

    resume_id = save_resume(
        user_id=user_id,
        file_name=resume.filename,
        resume_text=result["resume_text"]
    )

    # Save job description in database
    job_description_id = save_job_description(
        user_id=user_id,
        job_title=job_title,
        job_description=job_description
    )

    analysis_id = save_analysis(
    resume_id= resume_id,
    job_description_id=job_description_id,
    skill_score=result["scores"]["skill_score"],
    tfidf_score=result["scores"]["tfidf_score"],
    semantic_score=result["scores"]["semantic_score"],
    final_score=result["scores"]["final_score"],
    matched_skills=result["skill_analysis"]["matched_skills"],
    missing_skills=result["skill_analysis"]["missing_skills"],
    ai_recommendation=result["ai_recommendation"]
)

    result["resume_id"] = resume_id
    result["job_description_id"] = job_description_id
    result["analysis_id"] = analysis_id
    return result