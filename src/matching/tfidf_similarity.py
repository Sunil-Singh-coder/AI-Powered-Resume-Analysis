from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# resume_text = """
# I am a Python developer with experience in Flask,
# SQL and REST API development.
# """


# job_text = """
# We are looking for a Python developer with experience
# in backend development, REST APIs and SQL.
# """


def calculate_tfidf_similiarity(resume_text,job_text):

   documents = [
    resume_text,
    job_text
    ] 


   vectorizer = TfidfVectorizer()

   tfidf_matrix = vectorizer.fit_transform(documents)


   similarity = cosine_similarity(
    tfidf_matrix[0:1],
    tfidf_matrix[1:2]
)


   score = similarity[0][0] * 100
   return round(score,2)


# print("TF-IDF Similarity Score:")
# print(f"{score:.2f}%")