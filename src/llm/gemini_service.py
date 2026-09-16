from google import genai
from pathlib import Path
import os


# Project root
BASE_DIR = Path(__file__).resolve().parents[2]

# Load Gemini API key from .env
env_path = BASE_DIR / ".env"

with open(env_path, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if line.startswith("GEMINI_API_KEY="):
            api_key = line.split("=", 1)[1].strip()
            os.environ["GEMINI_API_KEY"] = api_key


api_key = os.getenv("GEMINI_API_KEY")
print("Gemini key loaded:", bool(api_key))
print("Gemini key length:", len(api_key) if api_key else 0)
print("Gemini key prefix:", api_key[:6] if api_key else "None")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found")


# Gemini client
client = genai.Client(api_key=api_key)


def generate_career_recommendation(analysis_result):

    prompt = f"""
You are an AI career assistant.

Analyze the following resume and job matching information.

Resume Skills:
{analysis_result["resume_skills"]}

Job Required Skills:
{analysis_result["job_skills"]}

Matched Skills:
{analysis_result["skill_analysis"]["matched_skills"]}

Missing Skills:
{analysis_result["skill_analysis"]["missing_skills"]}

Skill Score:
{analysis_result["scores"]["skill_score"]}%

TF-IDF Score:
{analysis_result["scores"]["tfidf_score"]}%

Semantic Score:
{analysis_result["scores"]["semantic_score"]}%

Final Match Score:
{analysis_result["scores"]["final_score"]}%

Give a simple and practical career analysis.

Include:

1. Overall assessment
Keep the response clear and concise and small.
"""
# 2. Main skill gaps
    
# 3. Priority skills to learn
# 4. Resume improvement suggestions
# 5. Interview preparation suggestions


    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":

    test_result = {
        "resume_skills": [
            "Python",
            "Flask",
            "Git",
            "GitHub",
            "Machine Learning"
        ],

        "job_skills": [
            "Python",
            "FastAPI",
            "Flask",
            "PostgreSQL",
            "Docker",
            "Git",
            "GitHub"
        ],

        "skill_analysis": {
            "matched_skills": [
                "Python",
                "Flask",
                "Git",
                "GitHub"
            ],

            "missing_skills": [
                "FastAPI",
                "PostgreSQL",
                "Docker"
            ]
        },

        "scores": {
            "skill_score": 57.14,
            "tfidf_score": 30.50,
            "semantic_score": 62.40,
            "final_score": 53.52
        }
    }

    result = generate_career_recommendation(test_result)

    print("\n----- AI CAREER RECOMMENDATION -----\n")
    print(result)    