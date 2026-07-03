from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def write_file(path: str, content: str) -> None:
    file_path = ROOT / path
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if file_path.exists():
        print(f"[SKIP] {path}")
        return

    file_path.write_text(content, encoding="utf-8")
    print(f"[GIT ] {path}")


def create_github_files() -> None:
    print("\nCreating GitHub community files...")

    write_file(
        ".github/ISSUE_TEMPLATE/feature_request.md",
        "---\n"
        "name: Feature Request\n"
        "about: Suggest a new feature for OpenEyes\n"
        "title: \"[Feature] \"\n"
        "labels: enhancement\n"
        "---\n\n"
        "## Feature Summary\n\n"
        "## Why is it useful?\n\n"
        "## Related Module\n\n"
        "- [ ] Vision\n"
        "- [ ] Memory\n"
        "- [ ] Tracking\n"
        "- [ ] Robotics\n"
        "- [ ] Pi App\n"
        "- [ ] Documentation\n",
    )

    write_file(
        ".github/ISSUE_TEMPLATE/bug_report.md",
        "---\n"
        "name: Bug Report\n"
        "about: Report a bug in OpenEyes\n"
        "title: \"[Bug] \"\n"
        "labels: bug\n"
        "---\n\n"
        "## What happened?\n\n"
        "## Steps to reproduce\n\n"
        "1.\n"
        "2.\n"
        "3.\n\n"
        "## Expected behavior\n\n"
        "## Environment\n\n"
        "- OS:\n"
        "- Python:\n"
        "- Camera:\n"
        "- OpenCV:\n",
    )

    write_file(
        ".github/pull_request_template.md",
        "# Pull Request\n\n"
        "## Summary\n\n"
        "## Type\n\n"
        "- [ ] Bug fix\n"
        "- [ ] New feature\n"
        "- [ ] Documentation\n"
        "- [ ] Refactor\n"
        "- [ ] Pi app\n"
        "- [ ] Robotics\n\n"
        "## Checklist\n\n"
        "- [ ] Code runs locally\n"
        "- [ ] Documentation updated\n"
        "- [ ] Changes are focused\n",
    )
