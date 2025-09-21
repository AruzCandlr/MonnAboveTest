import os
from github import Github

# Get the token from the workflow
TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("GITHUB_REPOSITORY")       # e.g., "AruzCandlr/MonnAboveTest"
ISSUE_NUMBER = int(os.getenv("ISSUE_NUMBER"))    # injected by the workflow

BOT_MESSAGE = "👋 Monn Above ALL!!!!!!"

g = Github(TOKEN)
repo = g.get_repo(REPO_NAME)
issue = repo.get_issue(number=ISSUE_NUMBER)
issue.create_comment(BOT_MESSAGE)

print(f"💬 Commented on issue #{ISSUE_NUMBER} in {REPO_NAME}")
