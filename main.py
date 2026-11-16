"""
BANK LEDGER SYSTEM
Simple menu-driven application with user inputs.
Author: Vishwateja S B
"""

lc = __import__("ledger-classe")


def main():
    print("\nWelcome to the Bank Ledger System!\n")

    ledger = lc.BankLedger()

    # Get user input to create an account
    name = input("Enter your name: ")
    acc_num = input("Enter your account number: ")
    initial_balance = float(input("Enter starting balance: "))

    my_account = lc.Account(name, acc_num, initial_balance)
    ledger.add_account(my_account)
    my_account.show_details()

    play = True
    while play:
        lc.display_menu()
        choice = lc.get_user_choice()

        match choice:
            case 1:
                amount = float(input("Enter amount to deposit: "))
                my_account.deposit(amount)
            case 2:
                amount = float(input("Enter amount to withdraw: "))
                my_account.withdraw(amount)
            case 3:
                my_account.show_details()
            case 4:
                play = False
                print("\nThank you for using the Bank Ledger System!\n")
            case _:
                print("Invalid choice, please pick 1-4.")


if __name__ == "__main__":
    main()
