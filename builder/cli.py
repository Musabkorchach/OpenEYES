import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from docs import create_docs
from github import create_github_files
from environment import create_environment, verify_environment
from models import check_yolo_model

ROOT = Path(__file__).resolve().parent.parent


def run_command(command):
    subprocess.run(command, shell=True, cwd=ROOT)


def run_init():
    create_docs()
    create_github_files()
    create_environment()
    verify_environment()
    check_yolo_model()


def run_doctor():
    verify_environment()
    check_yolo_model()


def run_docs():
    create_docs()


def run_github():
    create_github_files()


def run_models():
    check_yolo_model()


def run_install():
    run_command(f"{sys.executable} -m pip install -r requirements.txt")


def run_update():
    run_command("git pull")


def run_clean():
    folders = ["__pycache__", ".pytest_cache"]

    for folder in folders:
        for path in ROOT.rglob(folder):
            shutil.rmtree(path, ignore_errors=True)
            print(f"[CLEAN] {path}")

    for file in ROOT.rglob("*.pyc"):
        file.unlink(missing_ok=True)
        print(f"[CLEAN] {file}")


def run_test():
    run_command(f"{sys.executable} -m pytest")


def run_benchmark():
    print("Benchmark coming soon.")


def run_camera():
    run_command(f"{sys.executable} app.py")


def run_memory():
    print("Memory diagnostics coming soon.")


def run_plugins():
    plugins = ROOT / "plugins"
    plugins.mkdir(exist_ok=True)
    print("Plugins folder:", plugins)

    for item in plugins.iterdir():
        print("-", item.name)


def run_export():
    print("Export coming soon.")


def run_package():
    print("Package builder coming soon.")


def run_release():
    print("Release workflow coming soon.")


def main():
    parser = argparse.ArgumentParser(
        prog="builder",
        description="OpenEyes Builder Tool"
    )

    parser.add_argument(
        "command",
        choices=[
            "init",
            "doctor",
            "github",
            "docs",
            "models",
            "install",
            "update",
            "clean",
            "test",
            "benchmark",
            "camera",
            "memory",
            "plugins",
            "export",
            "package",
            "release",
        ],
        help="Command to run",
    )

    args = parser.parse_args()

    commands = {
        "init": run_init,
        "doctor": run_doctor,
        "github": run_github,
        "docs": run_docs,
        "models": run_models,
        "install": run_install,
        "update": run_update,
        "clean": run_clean,
        "test": run_test,
        "benchmark": run_benchmark,
        "camera": run_camera,
        "memory": run_memory,
        "plugins": run_plugins,
        "export": run_export,
        "package": run_package,
        "release": run_release,
    }

    commands[args.command]()


if __name__ == "__main__":
    main()