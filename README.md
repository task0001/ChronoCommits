
# ChronoCommits

ChronoCommits allows you to "fake" your activity on your github profile by creating a temporary git repository on your local machine, filling it with an empty commit every day from the 1st day of the specified year until today, and then pushing it to your remote repository on GitHub.


## Disclaimer: Ethical and Practical Considerations

This tool is for educational purposes only. Faking GitHub activity (e.g., backdating commits, generating artificial contributions) may violate:

**GitHub's Terms of Service**: [Section B.3](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service#3-user-content) prohibits "false or misleading" activity.

**Employer/OSS Trust**: Many organizations audit commit history. Artificial activity can damage credibility.

**Personal Integrity**: Authentic contributions matter more than green squares.

**Automated activity may lead to**:
- Account suspension (GitHub detects bulk/fake commits).
- Loss of trust in professional or open-source contexts.
- Diluted value of real achievements.

**This tool does not endorse or encourage misuse. You assume all risks.**
## Installation

From source:
```
git clone https://github.com/task0001/ChronoCommits.git
cd ChronoCommits
pip install .
```
## Usage

1. Create a new GitHub repository
2. Run ChronoCommits: `python3 ChronoCommits.py`
3. Check your profile!
## Authors

- [@task0001](https://www.github.com/task0001)

