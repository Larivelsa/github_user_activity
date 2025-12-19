# GitHub User Activity CLI

A simple command-line tool written in Python that fetches and displays the recent public activity of a GitHub user directly in the terminal.

This project is based on the GitHub User Activity challenge from roadmap.sh and is designed to practice API consumption, JSON handling, and CLI application development.

## Features

- Fetches recent public activity from GitHub for a given username
- Displays common event types such as Push, Issues, Stars, Forks, and Create events
- Outputs human-readable activity messages in the terminal
- Handles invalid usernames and API errors gracefully

## Requirements

- Python 3.10 or higher
- Internet connection

The project uses Python standard libraries and/or common HTTP libraries (such as `requests`) to communicate with the GitHub REST API.

## How It Works

1. The application receives a GitHub username as a command-line argument
2. It sends a request to the GitHub REST API to retrieve the user's public events
3. The returned JSON data is parsed
4. The activity is formatted and printed to the terminal


GitHub API endpoint used:
```bash
https://api.github.com/users/<username>/events
```

Replace <username> with the desired GitHub username.

## Usage

```bash
python github_activity.py <username>
```bash
github-activity <username>
```

Example output:

```text
Pushed 3 commits to repository-name
Opened an issue in user/repository
Starred user/repository
```

The exact output may vary depending on the implementation and formatting choices made in Python.

## References

- GitHub REST API Documentation: https://docs.github.com/en/rest
- Project challenge: https://roadmap.sh/projects/github-user-activity
- Proposal for the challenge solution by: https://github.com/Larivelsa/github_user_activity