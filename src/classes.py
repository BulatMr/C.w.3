from datetime import datetime


class Operation:
    def __init__(self, operation_state: str, operation_date: str, operation_description: str, operation_from: str,
                 operation_to: str, operation_amount: str, currency_name: str):
        self.operation_state = operation_state
        self.operation_date = operation_date
        self.operation_description = operation_description
        self.operation_from = operation_from
        self.operation_to = operation_to
        self.operation_amount = operation_amount
        self.currency_name = currency_name

    def get_formatting_date(self) -> str:
        """
        Функция форматирования даты
        :return:
        """
        if self.operation_date:
            date = datetime.strptime(self.operation_date, '%Y-%m-%dT%H:%M:%S.%f')
            return f"{date:%d.%m.%y}"
        else:
            return ""

    def formatting_payment(self, payment_data: str):
        """
        Форматирует информацию платежных данных операции.
        """
        if payment_data:
            # Шифрование номера карты или номера счета
            number_values_split = 4
            card_number = payment_data.split()[-1]
            title_card = " ".join(payment_data.split()[:-1])
            if title_card == "Счет":
                private_number_to = f"**{card_number[-4:]}"
                return f"{title_card} {private_number_to}"
            else:
                private_number_from = (
                    f"{card_number[:4]}{card_number[6:8]}******{card_number[-4:]}"
                )
                grouped_private_number = [private_number_from[i:i + number_values_split] for i in
                                          range(0, len(private_number_from), number_values_split)]

                return f"{title_card} {' '.join(grouped_private_number)}"
        return ""

    def __str__(self):
        """
        Содержимое объекта класса Operation в строковом виде
        :return:
        """
        if self.operation_from:
            return (f"{self.get_formatting_date()} {self.operation_description}\n"
                    f"{self.formatting_payment(self.operation_from)} -> {self.formatting_payment(self.operation_to)}\n"
                    f"{self.operation_amount} {self.currency_name}\n")
        return (f"{self.get_formatting_date()} {self.operation_description}\n"
                f"{self.formatting_payment(self.operation_from)}{self.formatting_payment(self.operation_to)}\n"
                f"{self.operation_amount} {self.currency_name}\n")
