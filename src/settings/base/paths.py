import os
from pathlib import PurePath

BASE_DIR = PurePath(__file__).parent.parent.parent
PROJECT_DIR = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))
