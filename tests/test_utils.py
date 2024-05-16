from src.classes import Operation
from src.utils import get_sorted_executed_operation, get_sorted_date_operation, get_operation_add


def test_get_sorted_executed_operation():
    operations_test = [{"state": "EXECUTED"},
                       {"state": "CANCELED"},
                       {"state": "EXECUTED"}]
    assert get_sorted_executed_operation(operations_test) == [{"state": "EXECUTED"},
                                                              {"state": "EXECUTED"}]


def test_get_sorted_date_operation():
    operations_test = [{"date": "10.10.2018"},
                       {"date": "10.10.2024"},
                       {"date": "10.10.2022"},
                       {"date": "10.10.2014"}]
    assert get_sorted_date_operation(operations_test) == [{"date": "10.10.2024"},
                                                          {"date": "10.10.2022"},
                                                          {"date": "10.10.2018"},
                                                          {"date": "10.10.2014"}]


def test_get_operation_add():
    operations_test1 = Operation(
        operation_date="2018-09-12T21:27:25.241689",
        operation_state="EXECUTED",
        operation_description="Перевод с карты на счет",
        operation_amount="40.50",
        currency_name="USD",
        operation_to="Счет 84163357546688983493",
        operation_from="Visa Classic 2842878893689012")
    assert operations_test1.formatting_payment(operations_test1.operation_from) == "Visa Classic 2842 88** **** 9012"
    assert operations_test1.formatting_payment(operations_test1.operation_to) == "Счет **3493"
    assert operations_test1.get_formatting_date() == "12.09.2018"
    assert str(operations_test1) == ("12.09.2018 Перевод с карты на счет\n"
                                     "Visa Classic 2842 88** **** 9012 -> Счет **3493\n"
                                     "40.50 USD\n")


def test_get_operation_add_from_for():
    operations_test = [{"id": 594226727,
                        "state": "CANCELED",
                        "date": "2018-09-12T21:27:25.241689",
                        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                        "description": "Перевод организации",
                        "from": "Visa Platinum 1246377376343588",
                        "to": "Счет 14211924144426031657"},
                       {"id": 649467725,
                        "state": "EXECUTED",
                        "date": "2018-04-14T19:35:28.978265",
                        "operationAmount": {"amount": "96995.73", "currency": {"name": "руб.", "code": "RUB"}},
                        "description": "Перевод организации",
                        "from": "Счет 27248529432547658655",
                        "to": "Счет 97584898735659638967"}
                       ]
    operation_test_list = get_operation_add(operations_test)

    assert isinstance(operation_test_list, list)
    for operation in operation_test_list:
        assert isinstance(operation, Operation)

    for items, operation in enumerate(operation_test_list):
        assert operation.operation_state == operations_test[items]["state"]
        assert operation.operation_date == operations_test[items]["date"]
        assert operation.operation_description == operations_test[items]["description"]
        assert operation.operation_from == operations_test[items]["from"]
        assert operation.operation_to == operations_test[items]["to"]
        assert operation.operation_amount == operations_test[items]["operationAmount"]["amount"]
        assert operation.currency_name == operations_test[items]["operationAmount"]["currency"]["name"]
