class InvalidAmount(Exception):
    pass


class Expense:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount