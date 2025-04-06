import logging
import subprocess
from datetime import date, datetime, timedelta
from pathlib import Path
from tempfile import TemporaryDirectory

from rich.logging import RichHandler
from rich.progress import track
from rich.prompt import Prompt, IntPrompt

logger = logging.getLogger("ChronoCommits")
cwd = Path(__file__).parent.resolve()


def run_from_path_silent(args, cwd: str):
    return subprocess.run(args, cwd=cwd, stdout=subprocess.DEVNULL)


def iter_dates(start: date, end: date):
    delta = end - start
    for i in range(delta.days + 1):
        day = start + timedelta(days=i)
        yield day


def create_empty_past_commit(d: date, directory: str) -> None:
    dt = datetime.combine(d, datetime.min.time())
    iso_string = dt.isoformat()
    subprocess.run(
        [
            "git",
            "commit",
            "--allow-empty",
            "--message",
            "Testing ChronoCommits",
            "--date",
            iso_string,
        ],
        env={
            "GIT_AUTHOR_DATE": iso_string,
            "GIT_COMMITTER_DATE": iso_string,
        },
        cwd=directory,
        check=True,
        stdout=subprocess.DEVNULL,
    )
    logger.info("Created empty commit at %s", iso_string)


def setup_git_dir(email: str, path: str | Path) -> None:
    run_from_path_silent(["git", "init"], cwd=path)
    run_from_path_silent(["git", "config", "user.email", email], cwd=path)
    logger.info("Created git repository at %s", path)
    run_from_path_silent(["git", "config", "user.name", "ChronoCommits"], cwd=path)
    logger.info("Set github credentials for repository.")


def push_to_remote(remote: str, path: str | Path) -> None:
    run_from_path_silent(["git", "remote", "add", "origin", remote], cwd=path)
    run_from_path_silent(["git", "branch", "-M", "main"], cwd=path)
    run_from_path_silent(["git", "push", "-u", "origin", "main"], cwd=path)
    logger.info("Pushed to remote repository: %s", remote)


def main() -> None:
    with TemporaryDirectory(prefix="ChronoCommits-", delete=True) as git_dir:
        logger.info("Created temporary directory at %s", git_dir)
        git_email = Prompt.ask(
            "An email linked to your GitHub account (can be private)"
        )
        setup_git_dir(git_email, git_dir)
        start_year = IntPrompt.ask(
            "What year would you like your commits to start from?", default=2025
        )
        for fake_date in track(
            iter_dates(date(start_year, 1, 1), date.today()),
            description="Creating fake commits in repository..",
        ):
            create_empty_past_commit(fake_date, git_dir)
        remote_url = Prompt.ask("Whats your GitHub repository URL?")
        push_to_remote(remote_url, git_dir)


if __name__ == "__main__":
    logging.basicConfig(
        level="INFO", datefmt="[%X]", handlers=[RichHandler(show_path=False)]
    )
    main()
