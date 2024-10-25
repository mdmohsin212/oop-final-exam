from abc import ABC
import random

class Base(ABC):
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address


class Admin(Base):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.take_loan = True
        
    def delete_user(self, User):
        pass

    def show_all_user(self, user):
        pass

    def total_balance(self):
        pass

    def total_loan(self):
        pass

    def loan_feature(self):
        pass



class User(Base):
    def __init__(self, name, email, address, account_type):
        super().__init__(name, email, address)
        self.account_type = account_type
        self.__balance = 0
        self._account_number = random.randint(1,1000)

    def deposite(self, amount):
        pass

    def withdraw_money(self, amount):
        pass

    def check_balance(self):
        pass

    def transaction_history(self):
        pass

    def take_loan(self):
        pass

    def transfer_money(self):
        pass
    