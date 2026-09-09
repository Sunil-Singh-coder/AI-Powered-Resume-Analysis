from pathlib import Path
from src.preprocessing.text_cleaner import clean_text
from src.skills.skill_extractor import extract_skills


def extract_text_from_jd(file_path):

    file_path = Path(file_path)

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return text




if __name__ == "__main__":

    BASE_DIR = Path(__file__).resolve().parents[2]

    jd_path = BASE_DIR / "data" / "job_descriptions" / "job1.txt"

    jd_text = extract_text_from_jd(jd_path)
    jd_cleaned=clean_text(jd_text)
    jd_skills=extract_skills(jd_cleaned)
    print("----- JOB DESCRIPTION -----")
    print(jd_text)
    print("----- JOB skills -----")
    print(jd_skills)