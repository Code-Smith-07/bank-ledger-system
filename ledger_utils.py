"""
Bank Ledger System - Utility Functions
Helper functions for formatting, menu display, and user input.
Author: Vishwateja S B
"""


def format_currency(amount: float) -> str:
    """Format a numeric amount as USD currency string."""
    return f"${amount:,.2f}"


def print_banner(title: str) -> None:
    """Print a formatted section banner."""
    border = "=" * (len(title) + 8)
    print(f"\n{border}")
    print(f"   {title}")
    print(f"{border}")


def display_menu() -> None:
    """Display the interactive Bank Ledger System menu options."""
    print("\n*** BANK LEDGER MENU ***")
    print("1. Create a new account")
    print("2. Deposit funds")
    print("3. Withdraw funds")
    print("4. Transfer funds between accounts")
    print("5. View account statement")
    print("6. View all accounts summary")
    print("7. View master transaction ledger")
    print("8. Exit")


def get_user_choice() -> int:
    """Prompt the user for a menu selection and return it as an integer."""
    raw = input("Select an option (1-8): ").strip()
    return int(raw)
