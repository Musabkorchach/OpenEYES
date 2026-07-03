from docs import create_docs
from github import create_github_files
from environment import verify_environment
from models import check_yolo_model


def main():
    print("=" * 60)
    print("OpenEyes Builder")
    print("The Open Vision Operating System")
    print("=" * 60)

    create_docs()
    create_github_files()
    verify_environment()
    check_yolo_model()

    print("=" * 60)
    print("OpenEyes Builder completed successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()