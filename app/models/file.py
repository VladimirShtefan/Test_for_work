import json

from app.constants import COMPETITORS_FILE, RESULT_FILE


class File:
    def __init__(self):
        self._competitors_file_path: str = COMPETITORS_FILE
        self._result_file_path: str = RESULT_FILE

    def _get_all_competitors(self) -> dict[dict]:
        """
        Функция чтения файла с персональными данными об участниках.
        :return: JSON
        """
        with open(self._competitors_file_path, 'r', encoding='utf-8-sig') as json_file:
            return json.load(json_file)

    def _get_results(self) -> list[str]:
        """
        Функция чтения файла с данными о забегах.
        :return: List[Str]
        """
        with open(self._result_file_path, 'r', encoding='utf-8-sig') as txt_file:
            return txt_file.readlines()
