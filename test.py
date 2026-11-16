"""
Test script (test.py) for testing the Bank Ledger System classes and edge cases.
"""

import importlib

lc = importlib.import_module("ledger-classe")


def test_bank_ledger() -> None:
    ledger = lc.BankLedger("Test Bank")

    # 1. Test account creation
    acc1 = ledger.create_account("A100", "Vishwateja", 1000.0)
    acc2 = ledger.create_account("A200", "Tanvir", 500.0)
    assert acc1.balance == 1000.0
    assert acc2.balance == 500.0
    print("✓ Account creation test passed:", acc1, "|", acc2)

    # 2. Test deposit and withdrawal
    ledger.record_deposit("A100", 250.0, "Bonus")
    assert acc1.balance == 1250.0

    ledger.record_withdrawal("A200", 100.0, "ATM")
    assert acc2.balance == 400.0
    print("✓ Deposit and withdrawal test passed.")

    # 3. Test transfer between accounts
    ledger.transfer("A100", "A200", 300.0, "Rent share")
    assert acc1.balance == 950.0
    assert acc2.balance == 700.0
    assert ledger.total_bank_deposits() == 1650.0
    print("✓ Transfer test passed.")

    # 4. Test insufficient funds protection
    try:
        ledger.record_withdrawal("A200", 5000.0)
        assert False, "Expected ValueError for insufficient funds"
    except ValueError as err:
        print(f"✓ Insufficient funds check passed ({err})")

    # 5. Test negative deposit protection
    try:
        ledger.record_deposit("A100", -50.0)
        assert False, "Expected ValueError for negative deposit"
    except ValueError as err:
        print(f"✓ Negative deposit check passed ({err})")

    print("\nAll Bank Ledger System tests in test.py passed successfully!")


if __name__ == "__main__":
    test_bank_ledger()

