# bot.py
import os
from github import Github
from openai import OpenAI

def main():
    # === Environment Variables ===
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    OPENAI_API_KEY = os.getenv("API_KEY")
    REPO_NAME = os.getenv("GITHUB_REPOSITORY")  
    ISSUE_NUMBER = os.getenv("ISSUE_NUMBER")

    # if not all([GITHUB_TOKEN, OPENAI_API_KEY, REPO_NAME, ISSUE_NUMBER]):
    #     raise EnvironmentError("no key lmao")

    # === Initialize Clients ===
    gh = Github(GITHUB_TOKEN)
    client = OpenAI(api_key=OPENAI_API_KEY)
    repo = gh.get_repo(REPO_NAME)
    issue = repo.get_issue(int(ISSUE_NUMBER))

    # === Prepare AI prompt ===
    prompt = (
        f"what is mahidol university?"
    )

    # === Generate AI response ===
    print(f" Generating response for issue #{issue.number}...")
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful GitHub assistant that comments on issues."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150,
    )

    ai_message = completion.choices[0].message.content.strip()
    bot_comment = f" ai gen: {ai_message}"

    # === Post Comment ===
    issue.create_comment(bot_comment)
    print(f" Commented on issue #{issue.number}")

if __name__ == "__main__":
    main()
