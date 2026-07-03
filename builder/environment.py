from pathlib import Path
import os
import platform

ROOT = Path(__file__).resolve().parent.parent


def create_environment():
    print("\nCreating environment...")

    env = ROOT / ".env"

    if not env.exists():
        env.write_text(
            """# OpenEyes Configuration

DEBUG=True

CAMERA_INDEX=0

YOLO_MODEL=yolov8n.pt

MEMORY_DB=data/memory.db

LOG_LEVEL=INFO

PI_ENABLED=False

API_PORT=8080

""",
            encoding="utf-8",
        )

        print("[ENV ] .env created")

    else:
        print("[SKIP] .env")


def verify_environment():

    print("\nEnvironment")

    print(f"OS : {platform.system()}")

    print(f"Python : {platform.python_version()}")

    print(f"Project : {ROOT}")

    folders = [
        "logs",
        "data",
        "plugins",
        "docs",
        ".github",
    ]

    for folder in folders:
        path = ROOT / folder
        path.mkdir(exist_ok=True)
        print(f"[DIR ] {folder}")