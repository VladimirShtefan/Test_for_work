from datetime import datetime

from app.models.file import File


class ConvertData(File):
    def _formatting_txt_file(self) -> list[str]:
        """
        Функция для удаления лишних символов в списке с участниками.
        :return: List[Str]
        """
        return list(map(lambda word: word.rstrip('\n'), self._get_results()))

    def _build_dict_for_results(self) -> dict[dict]:
        """
        Функция для формирования словаря с участниками и их данными о забегах из общего списка.
        :return: Dict[Dict]
        """
        dictionary_results = {}
        # список с данными о забегах всех участников
        data = self._formatting_txt_file()
        for index, competitor in enumerate(data):
            # удаление пробелов, для разделения данных
            data_competitor: list = competitor.split()
            # проверка на ошибку в заполнении
            if len(data_competitor) == 3:
                # распаковка данных о текущем участнике
                competitor_number, competitor_action, competitor_time = data_competitor
                # конвертация времени из строки в datetime
                competitor_time = datetime.strptime(competitor_time, "%H:%M:%S,%f")
                # запись данных в словарь
                if dictionary_results.get(competitor_number):
                    dictionary_results[competitor_number].update({competitor_action: competitor_time})
                    continue
                dictionary_results[competitor_number] = {competitor_action: competitor_time}
            else:
                # сообщение при ошибке заполнения исходного файла
                print(f'ошибка данных в строке №{index}, данные - {competitor}')
        return dictionary_results
