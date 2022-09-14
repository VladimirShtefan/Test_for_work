from app.models.convert_data import ConvertData


class Statistic(ConvertData):
    def _get_difference_in_time(self) -> dict:
        """
        Функция подсчета времени забега всех участников.
        :return: Dict[Dict]
        """
        data: dict[dict] = self._build_dict_for_results()
        result = {}
        for competitor_number, data_competitor in data.items():
            result[competitor_number] = data_competitor['finish'] - data_competitor['start']
        return result

    def _sort_dict_by_time(self) -> dict:
        """
        Функция сортировки словаря.
        :return: Dict
        """
        data = self._get_difference_in_time()
        # сортируем словарь по кортежам (номер участника, время), выбором через lambda второго порядкового элемента
        # в этом кортеже и далее преобразуем в словарь
        sorted_data = dict(sorted(data.items(), key=lambda k: k[1]))
        return sorted_data

    def get_statistic(self, number_of_entries: int = 0) -> list:
        """
        Функция формирования статистики
        :param number_of_entries: колличество записей для вывода
        :return: List
        """
        result = []
        counter = 0
        sorted_data: dict = self._sort_dict_by_time()
        competitor_data: dict[dict] = self._get_all_competitors()
        for competitor, data in sorted_data.items():
            counter += 1
            if counter > number_of_entries != 0:
                break
            result.append((counter,
                           competitor,
                           competitor_data[competitor]['Name'],
                           competitor_data[competitor]['Surname'],
                           str(data).replace('.', ',')))
        return result
