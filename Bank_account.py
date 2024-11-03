#Write python program to demonstrate Bank Account, where users can deposit, 
#withdraw, check balance and transfer money
class BankAccount:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.account_number = None
        self.pin = None
        self.balance = 0
    def display_bank_name_details(self):
        print(f"{self.bank_name.upper()}")
    
    def display_options(self):
        print("Select an option:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Transfer Money")
        print("5. Exit")
        
    #Method to allow user to enter account number and pin
    def enter_account_details(self):
        try:
            self.account_number = int(input("Enter your account number: "))
            self.pin = int(input("Enter your PIN: "))
        except ValueError:
            print("Acount number and pin must be a digit")
        
    def deposit_money(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        print(f"${amount} deposited successfully into your account. New account balance is: ${self.balance}")
    
    def withdraw_money(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from your account. Your new balance is: {self.balance}")
        else:
            print("insufficient amount to withdraw")
    
    def check_balance(self):
        print(f"Current balance: {self.balance}")
    
    def transfer_money(self):
        amount = float(input("Enter amount to transfer: "))
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"${amount} transferred successfully from your account. Your new balance is: ${self.balance}")
        else:
            print("insufficient amount to transfer")
    
    
