import random
class Bank:
    def __init__(self):
        self.users = {}
        self.loan_features = True
        self.isBankrupt = False

    def total_loan_amount(self):
        total_loan_amount = sum(user.loan_amount for user in self.users.values())
        return total_loan_amount

class User:
    def __init__(self,bank,name,email,address,account_type,password) -> None:
        self.bank = bank
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.password = password
        self.__balance = 0
        self.transaction_history = []
        self.account_number = random.randint(1,1000)
        self.loan_cnt = 0
        self.loan_amount = 0

    def create_account(self, name, email, address, account_type,password):
        user = User(name, email, address, account_type,password)
        self.bank.users[user.account_number] = user
        return user

    def deposite_money(self,amount):
        self.__balance += amount
        self.transaction_history.append(f"Deposited : {amount}")
        print("Money has been deposited successfully!!")

    def withdraw_money(self,amount):
        if bank.isBankrupt:
            print("The bank is bankrupt!!")
        else:
            if amount > self.__balance:
                print("Withdrawal amount exceeded!!")
            else:
                self.__balance -= amount
                self.transaction_history.append(f"Withdraw : {amount}")
                print("Money withdrawn successfully!!")

    def check_balance(self):
        return self.__balance
    
    def check_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)


    def take_loan(self,loan_amount):
        if not self.bank.loan_features:
            print("Sorry! We can't provide any loan")
        else:
                if self.loan_cnt < 2:
                    self.__balance += loan_amount
                    self.loan_cnt += 1
                    self.transaction_history.append(f"Taken loan : {loan_amount}.")
                    print(f"Loan of {loan_amount} has been given successfully to {self.name}.")
                    total_loan_amount = self.bank.total_loan_amount() + loan_amount  
                    self.bank.users[self.account_number].loan_amount = total_loan_amount  
                    return total_loan_amount
                else:
                    print("You're not eligible for taking loan more than twice.")
                    return self.bank.total_loan_amount() 

    def transfer_money(self, transfer_amount, recipient_account_number):
        if bank.isBankrupt:
            print("There's no money in the bank. You can't transfer any money.")
        else:
            if self.__balance < transfer_amount:
                print("Insufficient balance.")
            else:
                account_numbers = list(self.bank.users.keys())
                if recipient_account_number not in account_numbers:
                    print("Recipient account does not exist!!")
                else:
                    recipient = self.bank.users[recipient_account_number]
                    recipient.deposite_money(transfer_amount)
                    self.withdraw_money(transfer_amount)
                    print("Money transferred successfully!!")

class Admin:
    def __init__(self, bank):
        self.bank = bank
        self.admin_password = 123

    def admin_login(self, password):
        return password == self.admin_password

    def create_account(self, name, email, address, account_type,password):
        user = User(name, email, address, account_type,password)
        self.bank.users[user.account_number] = user
        return user

    def delete_account(self, account_number):
        if account_number in self.bank.users:
            del self.bank.users[account_number]
            print(f"Account {account_number} deleted successfully.")
        else:
            print("Account not found.")

    def show_all_accounts(self):
        print("All User Accounts:")
        for account_number, user in self.bank.users.items():
            print(f"Account Number: {account_number} Name: {user.name} Email: {user.email}")


    def total_bank_balance(self):
        bank_balance = sum(user.check_balance() or 0 for user in self.bank.users.values())
        print(f"Total Bank Balance: {bank_balance}")

    def total_loan(self):
        total_loan_amount = sum(user.bank.total_loan_amount() for user in self.bank.users.values())
        print(f"Total Loan Amount: {total_loan_amount}")
    
    def toggle_loan_feature(self):
        self.bank.loan_features = not self.bank.loan_features
        print("Toggling Successfully done!!")


bank = Bank()
admin = Admin(bank)

def user_menu():
    while True:
        print("1. User Login")
        print("2. Create a new User")
        print("3. Exit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            password = int(input("Enter your password : "))
            for key,user in bank.users.items(): 
                if password == user.password: 
                    while True:
                        print(f" Welcome !!")
                        print("1. Deposit Money")
                        print("2. Withdraw Money")
                        print("3. Check Balance")
                        print("4. Check Transaction History")
                        print("5. Take Loan")
                        print("6. Transfer Money")
                        print("7. Exit")

                        user_choice = int(input("Enter your choice : "))

                        if user_choice == 1:
                            amount = int(input("Enter deposit amount : "))
                            user.deposite_money(amount)
                        elif user_choice == 2:
                            amount = int(input("Enter withdraw amount : "))
                            user.withdraw_money(amount)
                        elif user_choice == 3:
                            print(f"Available balance : {user.check_balance()}") 
                        elif user_choice == 4:
                            user.check_transaction_history()
                        elif user_choice == 5:
                            loan_amount = int(input("Enter amount of loan : "))
                            user.take_loan(loan_amount)
                        elif user_choice == 6:
                            transfer_amount = int(input("Enter transfer amount : "))
                            recipient_account_number = int(input("Enter recipient account number : "))
                            user.transfer_money(transfer_amount, recipient_account_number)
                        elif user_choice == 7:
                            break
                        else:
                            print("Invalid input")
                    break  
            else:
                print("Incorrect password or user account doesn't exist!")
        elif choice == 2:
            name = input("Enter your name : ")
            email = input("Enter your email : ")
            address = input("Enter your address : ")
            account_type = input("Enter your account type (Savings/Current) : ")
            password = int(input("Enter password : "))
            new_user = User(bank,name, email, address, account_type, password) 
            bank.users[new_user.account_number] = new_user  
            print(f"{new_user.name} your account with account_number: {new_user.account_number} has been created successfully!! ")
        elif choice == 3:
            break
        else:
            print("Invalid input")


def admin_menu():
    while True:
        print("1.Admin Login")
        print("2.Exit")

        option = int(input("Enter your choice : "))

        if option == 1:
            name = input("Enter admin name : ")
            password = int(input("Enter password : "))

            if password:
                while True:
                    print("1.Create account")
                    print("2.Delete account")
                    print("3.Show users")
                    print("4.Show total balance")
                    print("5.Show loan amount")
                    print("6.toggle_loan_feature")
                    print("7.Exit")

                    choice = int(input("Enter your choice : "))

                    if choice == 1:
                        name = input("Enter your name : ")
                        email = input("Enter your email : ")
                        address = input("Enter your address : ")
                        account_type = input("Enter your account type(Savings/Current) : ")
                        password = int(input("Enter pasword : "))
                        admin.create_account(name,email,address,account_type,password)
                    elif choice == 2:
                        account_number = int(input("Enter account number : "))
                        admin.delete_account(account_number)
                    elif choice == 3:
                        admin.show_all_accounts()
                    elif choice == 4:
                        admin.total_bank_balance()
                    elif choice == 5:
                        admin.total_loan()
                    elif choice == 6:
                        admin.toggle_loan_feature()
                    elif choice == 7:
                        break
                    else:
                        print("Invalid input")


        elif option == 2:
            break
        else:
            print("Invalid input")



while True:
    print("----Welcome to Bank_Management_System--------\n")
    print("1.User")
    print("2.Admin")
    print("3.Exit")

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        user_menu()  
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid input")
