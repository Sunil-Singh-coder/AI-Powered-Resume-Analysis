## For implement Sentence Transformer
Ab workflow

Hum ek-ek step karenge:

Step 15.1 → Sentence Transformers install
↓
Step 15.2 → Model load/test
↓
Step 15.3 → Resume & JD embeddings
↓
Step 15.4 → Semantic similarity score
↓
Step 15.5 → Analyzer mein integrate


<!-- Traditional step  -->
Resume PDF
      ↓
Text Extraction
      ↓
Text Cleaning
      ↓
Skill Extraction
      ↓
      ↘
       Resume Skills
             ↓
        Skill Matching
             ↑
       Job Skills
      ↗
JD Text
      ↓
JD Processing


This is the our that we are following 
✅ PDF Extraction
✅ Text Cleaning
✅ spaCy Processing
✅ Skill Dictionary
✅ Skill Aliases
✅ PhraseMatcher
✅ Resume Skill Extraction
✅ JD Extraction
✅ Skill Matching
🔄 Match Score ← WE ARE HERE
⬜ Semantic Matching
⬜ Skill Gap Analysis
⬜ LLM Recommendations
⬜ FastAPI
⬜ PostgreSQL
⬜ React

