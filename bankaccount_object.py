from Bank_account import BankAccount

#display welcome message

user_account = BankAccount("Welcome to I & M Bank")
user_account.display_bank_name_details() 

#Allow user to enter account number and pin
user_account.enter_account_details()

while True:
    try:
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                user_account.deposit_money()
            case 2:
                user_account.withdraw_money()
            case 3:
                user_account.check_balance()
            case 4:
                user_account.transfer_money()
            case 5:
                print("Exiting. Thank you for using our service!")
                break
            case _:
                print("Invalid choice. Please try again.")
    except ValueError:
        print("Please enter a valid number.")