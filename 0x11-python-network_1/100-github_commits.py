#!/usr/bin/python3
"""
script that utilizes the requests and sys packages
to retrieve and display the ten most recent commits
of a specified repository by a given owner
"""
import requests
import sys


def fetch_commits(repo_name, owner_name):
    """
    helper fumctikn to print the commits from the
    repo
    """
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")


if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    fetch_commits(repository_name, owner_name)
