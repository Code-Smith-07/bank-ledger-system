"""
Simple test file (test.py) to test Account and BankLedger classes.
Author: Vishwateja S B
"""

lc = __import__("ledger-classe")

# Test creating accounts
acc1 = lc.Account("Vishwateja", "1001", 500)
acc2 = lc.Account("Alice", "1002", 300)

# Test deposit and withdraw
acc1.deposit(200)
acc1.withdraw(100)
acc1.show_details()

# Test ledger collection
ledger = lc.BankLedger()
ledger.add_account(acc1)
ledger.add_account(acc2)
ledger.display_ledger()
