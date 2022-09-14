from prettytable import PrettyTable
from app.models.statistic import Statistic


if __name__ == '__main__':
    header = ['Занятое место', 'Нагрудный номер', 'Имя', 'Фамилия', 'Результат']
    table = PrettyTable(header)

    statistic = Statistic().get_statistic(10)
    for competitor in statistic:
        table.add_row(competitor)
    print(table)
