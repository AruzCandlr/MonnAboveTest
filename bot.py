# bot.py
import os
from github import Github
from google import genai
from sentence_transformers import SentenceTransformer
def main():
    # === Environment Variables ===
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    REPO_NAME = os.getenv("GITHUB_REPOSITORY")  
    ISSUE_NUMBER = os.getenv("ISSUE_NUMBER")

    # if not all([GITHUB_TOKEN, OPENAI_API_KEY, REPO_NAME, ISSUE_NUMBER]):
    #     raise EnvironmentError("no key lmao")

    # === Initialize Clients ===
   
    model = SentenceTransformer("all-MiniLM-L6-v2")

    texts = [
    "GitHub Actions is great for CI",
    "Sentence transformers create embeddings"
    ]
    
    embeddings = model.encode(
        texts,
        normalize_embeddings=True
    )

    print(len(embeddings), len(embeddings[0]))

    
if __name__ == "__main__":
    main()
