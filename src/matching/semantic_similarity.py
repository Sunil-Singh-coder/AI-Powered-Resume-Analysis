from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load pre-trained model
model = SentenceTransformer("all-MiniLM-L6-v2")

def calculate_semantic_similarity(resume_text, jd_text):
    resume_embedding = model.encode([resume_text])
    jd_embedding = model.encode([jd_text])

    similarity = cosine_similarity(
        resume_embedding,
        jd_embedding
    )[0][0]

    score = float(similarity * 100)

    return round(score, 2)

