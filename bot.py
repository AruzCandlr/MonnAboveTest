# bot.py
import os
from github import Github
from google import genai

def main():
    # === Environment Variables ===
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    REPO_NAME = os.getenv("GITHUB_REPOSITORY")  
    PR_NUMBER = os.getenv("PR_NUMBER")

    # if not all([GITHUB_TOKEN, OPENAI_API_KEY, REPO_NAME, ISSUE_NUMBER]):
    #     raise EnvironmentError("no key lmao")

    # === Initialize Clients ===
    gh = Github(GITHUB_TOKEN)
    client = genai.Client()
    repo = gh.get_repo(REPO_NAME)
    PR = repo.get_issue(int(PR_NUMBER))

    # === Prepare AI prompt ===
    prompt = (
        f"what is mahidol university?"
    )

    response = client.models.generate_content(
    model="gemini-2.5-flash", contents=prompt)
    print(response.text)
    print(PR)
    # === Post Comment ===
    # bot_comment = response.text
    bot_comment = "“This pull request introduces a GitHub action that uses the microsoft/winget-create tool to automatically submit new stable releases of ollama to the official microsoft/winget-pkgs community manifest repository.”"
    issue.create_comment(bot_comment)
    print(f" Commented on issue #{issue.number}")

if __name__ == "__main__":
    main()
