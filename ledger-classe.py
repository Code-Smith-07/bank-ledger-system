"""
Bank Ledger System - Classes and Menu Functions
Author: Vishwateja S B
"""


class Account:
    """Account class stores user account details and transactions."""

    def __init__(self, name, account_number, balance=0.0):
        self.name = name
        self.account_number = account_number
        self.balance = float(balance)
        self.history = [f"Account opened with ${self.balance:.2f}"]

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited: +${amount:.2f}")
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            self.history.append(f"Withdrew:  -${amount:.2f}")
            print(f"${amount:.2f} withdrawn successfully.")

    def show_details(self):
        print("\n--- Account Details ---")
        print(f"Account Holder : {self.name}")
        print(f"Account Number : {self.account_number}")
        print(f"Current Balance: ${self.balance:.2f}")
        print("Transactions:")
        for item in self.history:
            print(f"  - {item}")

    def __str__(self):
        return f"Account[{self.account_number}] {self.name} - Balance: ${self.balance:.2f}"


class BankLedger:
    """BankLedger class stores a list of accounts."""

    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print("Account added to bank ledger.")

    def display_ledger(self):
        print("\n--- All Accounts in Bank Ledger ---")
        for acc in self.accounts:
            print(acc)


def display_menu():
    print("\n*** BANK LEDGER MENU ***")
    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Show my account details")
    print("4. Exit")


def get_user_choice():
    return int(input("Choose an option (1, 2, 3, or 4): "))
