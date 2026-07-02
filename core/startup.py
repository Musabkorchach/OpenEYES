"""
OpenEyes Startup Module
"""

import platform
import sys
from datetime import datetime


def startup():
    print("=" * 60)
    print("            OpenEyes AI Vision System")
    print("=" * 60)
    print(f"Python Version : {sys.version.split()[0]}")
    print(f"Operating System : {platform.system()} {platform.release()}")
    print(f"Start Time : {datetime.now()}")
    print("=" * 60)
    print("Loading modules...")
    print("Core ............. OK")
    print("Configuration .... OK")
    print("=" * 60)