from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def write_file(path: str, content: str) -> None:
    file_path = ROOT / path
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if file_path.exists():
        print(f"[SKIP] {path}")
        return

    file_path.write_text(content, encoding="utf-8")
    print(f"[DOC ] {path}")


def create_docs() -> None:
    print("\nCreating documentation...")

    write_file(
        "docs/INSTALL.md",
        "# Installation\n\n"
        "Install dependencies:\n\n"
        "```bash\n"
        "py -3.12 -m pip install -r requirements.txt\n"
        "```\n\n"
        "Run OpenEyes:\n\n"
        "```bash\n"
        "py -3.12 app.py\n"
        "```\n",
    )

    write_file(
        "docs/ARCHITECTURE.md",
        "# OpenEyes Architecture\n\n"
        "OpenEyes is designed as a Vision Operating System.\n\n"
        "## Core Flow\n\n"
        "```text\n"
        "Camera\n"
        "  ↓\n"
        "Object Detector\n"
        "  ↓\n"
        "Tracker\n"
        "  ↓\n"
        "Memory Engine\n"
        "  ↓\n"
        "Scene Analyzer\n"
        "  ↓\n"
        "AI Brain\n"
        "  ↓\n"
        "Action Engine\n"
        "```\n",
    )

    write_file(
        "docs/BRANDING.md",
        "# OpenEyes Branding\n\n"
        "## Name\n\n"
        "OpenEyes Vision OS\n\n"
        "## Tagline\n\n"
        "See • Understand • Remember • Act\n\n"
        "## Slogan\n\n"
        "The Open Vision Operating System\n\n"
        "## Mission\n\n"
        "To build an AI vision platform for robots and intelligent systems.\n",
    )