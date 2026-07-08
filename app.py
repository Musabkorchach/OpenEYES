from kernel.runtime import OpenEyesRuntime
from camera.manager import CameraManager


def main():
    runtime = OpenEyesRuntime()
    runtime.boot()

    try:
        runtime.logger.info("Starting Camera Manager...")
        camera = CameraManager()
        camera.start()

    except KeyboardInterrupt:
        runtime.logger.warning("OpenEyes interrupted by user.")

    except Exception as error:
        runtime.logger.error(f"OpenEyes error: {error}")

    finally:
        runtime.shutdown()


if __name__ == "__main__":
    main()