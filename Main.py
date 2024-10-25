import random
class Bank:
    def __init__(self):
        self.users = {}
        self.loan_feature = True
        self.isBankrupt = False
        self.total_loan = 0
    
    def loan(self, amount):
        self.total_loan += amount

class User:
    def __init__(self, bank, name, email, address, password,account_type):
        self.bank = bank
        self.name = name
        self.email = email
        self.address = address
        self.password = password
        self.account_type = account_type
        self.account_number = random.randint(1,1000)
        self.loan_cnt = 0
        self.__balance = 0
        self.transaction_history = []
        self.loan_amount = 0

    def create_user(self,bank, name, email, address, password, account_type):
        user = User(bank, name, email, address, password, account_type)
        self.bank.users[user.account_number] = user
        return user

    def show_balance(self):
        return self.__balance
    
    def deposite_balance(self, amount):
        self.__balance += amount
        self.transaction_history.append(f'Deposite Money : {amount}')
        print(f'Money {amount} has been deposited successfully!!')

    def withdraw_money(self, amount):
        if self.bank.isBankrupt:
            print('The bank is bankrupt!!')
        elif self.__balance < amount:
            print('Withdrawl amount exceeded!!')
        else:
            self.__balance -= amount
            self.transaction_history.append(f'Withdrawl Money : {amount}')
            print(f'Money {amount} Withdrawl successfully!!')

    def all_transaction_history(self):
        print('All Transaction History : ')
        for history in self.transaction_history:
            print(history)
    
    def take_loan(self, amount):
        if not self.bank.loan_feature:
            print('Sorry we cant give you loan!!')
        else:
            if self.loan_cnt < 2:
                self.__balance += amount
                self.loan_cnt += 1
                self.transaction_history.append(f'Take Loan : {amount}')
                self.bank.loan(amount)
                print(f'Loan {amount} has been given successfully to {self.name}!!')
            else:
                print('You are not eligible for loan!!')
    
    def transfer_money(self, account_num, amount):
        if self.bank.isBankrupt:
            print('The bank is bankrupt!!')
        elif self.__balance < amount:
            print('Transfer amount exceeded!!')
        else:
            account_numbers = list(self.bank.users.keys())
            if account_num in account_numbers:
                person = self.bank.users[account_num]
                person.__balance += amount
                self.__balance -= amount
                print(f'Money transferred successfully!!')
            else:
                print('Invalid account number!!')
    

class Admin:
    def __init__(self, bank):
        self.bank = bank
        self.password = 12345
    
    def create_user(self,bank, name, email, address, password, account_type):
        user = User(bank, name, email, address, password, account_type)
        bank.users[user.account_number] = user
        return user

    def delete_account(self, account_number):
        if account_number in self.bank.users:
            del self.bank.users[account_number]
            print(f'Account {account_number} has deleted!!')
        else:
            print('Invalid account number!!')
    
    def show_users(self):
        for account_num, user in self.bank.users.items():
            print(f'Name : {user.name} Email : {user.email} Account Number : {account_num}')

    def total_bank_balance(self):
        total_amount = sum(user.show_balance() for user in self.bank.users.values())
        print(f'Total Bank Balance : {total_amount}')

    def total_loan(self):
        print(f'Total Loan Amount: {self.bank.total_loan}')

    def loan_on_off(self):
        if self.bank.loan_feature:
            self.bank.loan_feature = False
            print('Loan feature turn off successfully!!')
        else:
            self.bank.loan_feature = True
            print('Loan feature turn on successfully!!')

    def isBankrupt(self):
        if self.bank.isBankrupt:
            self.bank.isBankrupt = False
            print('Bank working Normally!!')
        else:
            self.bank.isBankrupt = True
            print('The Bank is Bankrupt!!')

bank = Bank()
admin = Admin(bank)

def User_menu():
    while True:
        print('1. Create a account')
        print('2. Login')
        print('3. Exit')

        choise = int(input('Enter your choise : '))

        if choise == 1:
            name = input('Enter Your Name : ')
            email = input('Enter Your Email : ')
            address = input('Enter Your Address : ')
            account_type = input('Enter your account type (Savings/Current) : ')
            password = int(input('Enter Your Password : '))
            user = User(bank,name,email,address,password,account_type)
            bank.users[user.account_number] = user
            print(f'{user.name} Your account with account number {user.account_number} has been created successfully!!')


        elif choise == 2:
            passwrd = int(input('Enter your Password : '))
            for key, user in bank.users.items():
                if passwrd == user.password:
                    while True:
                        print(f'********WELCOME********')
                        print('1. Deposite Money')
                        print('2. Withdraw Money')
                        print("3. Check Balance")
                        print("4. Check Transaction History")
                        print("5. Take Loan")
                        print("6. Transfer Money")
                        print("7. Exit")

                        choise2 = int(input('Enter your choise : '))

                        if choise2 == 1:
                            amount = int(input('Enter deposit Amount : '))
                            user.deposite_balance(amount)
                        elif choise2 == 2:
                            amount = int(input('Enter withdraw Amount : '))
                            user.withdraw_money(amount)
                        elif choise2 == 3:
                            print(f'Available balance : {user.show_balance()}')
                        elif choise2 == 4:
                            user.all_transaction_history()
                        elif choise2 == 5:
                            loan_amount = int(input('Enter Loan Amount : '))
                            user.take_loan(loan_amount)
                        elif choise2 == 6:
                            account_no = int(input('Enter Recevier account number : '))
                            send_amount = int(input("Enter transfer amount : "))
                            user.transfer_money(account_no, send_amount)
                        elif choise2 == 7:
                            break
                        else:
                            print('Invalid choise!!')
                else:
                    print('Incorrect password or user not exist!!')


        elif choise == 3:
            break


        else:
            print('Invalid choise!!')


def Admin_menu():
    while True:
        print('1. Admin login')
        print('2. Exit')

        choise = int(input('Enter Your Choise : '))

        if choise == 1:
            name = input('Enter your name : ')
            password = int(input('Enter your password : '))

            if password:
                while True:
                    print(f'*****WELCOM {name}*****')
                    print('1.Create account')
                    print('2.Delete account')
                    print('3.Show users')
                    print('4.Show total balance')
                    print('5.Show loan amount')
                    print('6.Toggle loan feature')
                    print('7.Is Bankrupt')
                    print('8.Exit')
                
                    option = int(input('Enter Your choise : '))

                    if option == 1:
                        name = input('Enter Your Name : ')
                        email = input('Enter Your Email : ')
                        address = input('Enter Your Address : ')
                        account_type = input('Enter your account type (Savings/Current) : ')
                        password = int(input('Enter Your Password : '))
                        admin.create_user(bank,name,email,address,password, account_type)
                    elif option == 2:
                        account_num = int(input('Enter Account Number : '))
                        admin.delete_account(account_num)
                    elif option == 3:
                        admin.show_users()
                    elif option == 4:
                        admin.total_bank_balance()
                    elif option == 5:
                        admin.total_loan()
                    elif option == 6:
                        admin.loan_on_off()
                    elif option == 7:
                        admin.isBankrupt()
                    elif option == 8:
                        break
                    else:
                        print('Invalid Choise!!')
        
        elif choise == 2:
            break

        else:
            print('Invalid Choise!!')


while True:
    print('\n')
    print('*********WELCOME TO BANK MANAGMENT SYSTEM*********')
    print('1. Admin')
    print('2. User')
    print('3. Exit')

    choise = int(input('Enter your choise : '))

    if choise == 1:
        Admin_menu()
    elif choise == 2:
        User_menu()
    elif choise == 3:
        break
    else:
        print('Invalid Choise!!')