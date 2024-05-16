import json

from src.classes import Operation
from src.settings import JSON_PATH


def get_load_file(path: str = JSON_PATH) -> list:
    """
    Загрузка данных из JSON файла.
    :param path: Путь до файла
    :return: Возвращает список словарей
    """
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def get_sorted_executed_operation(data: list) -> list:

    """
    Сортировка операций по статусу ВЫПОЛНЕНО
    :param data: Список всех операций
    :return: Возвращает список словарей с ключем 'state' == 'EXECUTED'
    """
    sorted_list = []
    for items in data:
        if items.get('state') == 'EXECUTED':
            sorted_list.append(items)
        else:
            continue
    return sorted_list


def get_sorted_date_operation(data: list) -> list:
    """
    Сортировка по дате операций
    :param data: Список словарей операций
    :return: Вывод пяти последних операций списком словарей
    """

    for items in data:
        if items.get("date"):
            data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[0:5]


def get_operation_add(operations: list) -> list:
    """
    Создает экземпляр класса
    :param operations: Список словарей операций
    :return: Список экземпляров класса
    """
    operation_list = []
    for item in operations:
        operation_date = item.get('date')
        operation_description = item.get('description')
        operation_from = item.get('from')
        operation_to = item.get('to')
        operation_state = item.get('state')

        operation_amount = item.get('operationAmount', {}).get('amount')
        currency_name = item.get('operationAmount', {}).get('currency', {}).get('name')
        operation = Operation(operation_state, operation_date,
                              operation_description, operation_from,
                              operation_to, operation_amount, currency_name)
        operation_list.append(operation)
    return operation_list
