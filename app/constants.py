from pathlib import Path

# пути к файлам с данными
PROJECT_PATH = Path(__file__).parent.parent
APP_PATH = Path.joinpath(PROJECT_PATH, 'app')
SOURCE_PATH = Path.joinpath(APP_PATH, 'sources')
COMPETITORS_FILE = Path.joinpath(SOURCE_PATH, 'competitors.json')
RESULT_FILE = Path.joinpath(SOURCE_PATH, 'results.txt')
