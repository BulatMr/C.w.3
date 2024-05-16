from src.utils import get_load_file, get_sorted_executed_operation, get_sorted_date_operation, get_operation_add


def main():
    # Загрузка данных
    load_all_operation = get_load_file()
    # Сортировка операций
    sort_operation = get_sorted_executed_operation(load_all_operation)
    # Создание экземпляра класса пяти последних операций
    last_five_operation = get_operation_add(get_sorted_date_operation(sort_operation))
    for items_operation in last_five_operation:
        print(items_operation)


if __name__ == "__main__":
    main()
