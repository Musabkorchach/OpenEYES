from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def check_yolo_model():
    """
    Verify that the default YOLO model exists.
    If it does not exist, OpenEyes will download it automatically
    the first time the detector is used.
    """

    print("\nChecking AI models...")

    model = ROOT / "yolov8n.pt"

    if model.exists():
        print("[OK ] YOLO model found.")
    else:
        print("[INFO] YOLO model not found.")
        print("[INFO] It will be downloaded automatically on first launch.")