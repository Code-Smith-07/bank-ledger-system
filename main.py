"""
BANK LEDGER SYSTEM
Main entry point demonstrating ledger operations and interactive CLI menu.
Author: Vishwateja S B
"""

import sys
import ledger_classes as lc
import ledger_utils as lu


def run_demo() -> lc.BankLedger:
    """Run a demonstration of the Bank Ledger System with sample accounts and transactions."""
    lu.print_banner("Welcome to the Bank Ledger System")

    ledger = lc.BankLedger("Python Class Community Bank")

    # 1. Create sample accounts
    ledger.create_account("ACC-1001", "Vishwateja", 1500.00)
    ledger.create_account("ACC-1002", "Alice", 800.00)
    ledger.create_account("ACC-1003", "Bob", 250.00)

    # 2. Record deposits and withdrawals
    ledger.record_deposit("ACC-1001", 500.00, "Paycheck deposit")
    ledger.record_withdrawal("ACC-1002", 120.00, "Grocery shopping")
    ledger.record_deposit("ACC-1003", 75.50, "Freelance payment")

    # 3. Perform an inter-account transfer
    ledger.transfer("ACC-1001", "ACC-1003", 300.00, "Project split")

    # 4. Display account statements and master ledger
    ledger.display_all_accounts()
    ledger.get_account("ACC-1001").display_statement()
    ledger.display_master_ledger()

    print(
        f"\nTotal liquidity across {len(ledger.accounts)} accounts: "
        f"{lu.format_currency(ledger.total_bank_deposits())}"
    )
    return ledger


def run_interactive(ledger: lc.BankLedger | None = None) -> None:
    """Run the interactive CLI menu loop for the Bank Ledger System."""
    if ledger is None:
        ledger = lc.BankLedger("Python Class Community Bank")

    running = True
    while running:
        lu.display_menu()
        try:
            choice = lu.get_user_choice()
            match choice:
                case 1:
                    acct_num = input("Account number (e.g. ACC-1004): ").strip()
                    owner = input("Owner name: ").strip()
                    opening = float(input("Initial deposit amount: "))
                    acct = ledger.create_account(acct_num, owner, opening)
                    print(f"Created: {acct}")
                case 2:
                    acct_num = input("Account number: ").strip()
                    amount = float(input("Deposit amount: "))
                    note = input("Note (optional): ").strip() or "Deposit"
                    tx = ledger.record_deposit(acct_num, amount, note)
                    print(f"Recorded: {tx}")
                case 3:
                    acct_num = input("Account number: ").strip()
                    amount = float(input("Withdrawal amount: "))
                    note = input("Note (optional): ").strip() or "Withdrawal"
                    tx = ledger.record_withdrawal(acct_num, amount, note)
                    print(f"Recorded: {tx}")
                case 4:
                    from_acct = input("From account number: ").strip()
                    to_acct = input("To account number: ").strip()
                    amount = float(input("Transfer amount: "))
                    note = input("Note (optional): ").strip()
                    out_tx, in_tx = ledger.transfer(from_acct, to_acct, amount, note)
                    print(f"Transfer complete:\n  {out_tx}\n  {in_tx}")
                case 5:
                    acct_num = input("Account number: ").strip()
                    ledger.get_account(acct_num).display_statement()
                case 6:
                    ledger.display_all_accounts()
                case 7:
                    ledger.display_master_ledger()
                case 8:
                    running = False
                    print("\nThank you for using the Bank Ledger System!\n")
                case _:
                    print("Please choose a valid option between 1 and 8.")
        except (ValueError, KeyError) as err:
            print(f"Error: {err}")


def main() -> None:
    """Entry point: runs the ledger demonstration (pass --interactive for CLI menu)."""
    ledger = run_demo()
    if "--interactive" in sys.argv:
        run_interactive(ledger)


if __name__ == "__main__":
    main()
