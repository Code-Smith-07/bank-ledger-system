"""
Test script for the Bank Ledger System classes and edge cases.
"""

import ledger_classes as lc


def test_bank_ledger() -> None:
    ledger = lc.BankLedger("Test Bank")

    # Test account creation
    acc1 = ledger.create_account("A100", "Vishwateja", 1000.0)
    acc2 = ledger.create_account("A200", "Tanvir", 500.0)
    assert acc1.balance == 1000.0
    assert acc2.balance == 500.0

    # Test deposit and withdrawal
    ledger.record_deposit("A100", 250.0, "Bonus")
    assert acc1.balance == 1250.0

    ledger.record_withdrawal("A200", 100.0, "ATM")
    assert acc2.balance == 400.0

    # Test transfer
    ledger.transfer("A100", "A200", 300.0, "Rent share")
    assert acc1.balance == 950.0
    assert acc2.balance == 700.0
    assert ledger.total_bank_deposits() == 1650.0

    # Test insufficient funds protection
    try:
        ledger.record_withdrawal("A200", 5000.0)
        assert False, "Expected ValueError for insufficient funds"
    except ValueError:
        pass

    print("All Bank Ledger System tests passed successfully!")


if __name__ == "__main__":
    test_bank_ledger()
