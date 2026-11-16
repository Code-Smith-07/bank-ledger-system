"""
Bank Ledger System - Classes Module
Defines Transaction, BankAccount, and BankLedger classes.
Author: Vishwateja S B
"""

from datetime import datetime


class Transaction:
    """Represents a single financial transaction on a bank account."""

    _next_id = 1

    def __init__(self, account_number: str, tx_type: str, amount: float, balance_after: float, note: str = ""):
        self.tx_id = Transaction._next_id
        Transaction._next_id += 1
        self.account_number = account_number
        self.tx_type = tx_type
        self.amount = float(amount)
        self.balance_after = float(balance_after)
        self.note = note
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self) -> str:
        note_str = f" ({self.note})" if self.note else ""
        return (
            f"[#{self.tx_id:03d}] {self.timestamp} | Acct: {self.account_number} | "
            f"{self.tx_type:<12} | ${self.amount:>9.2f} | Bal: ${self.balance_after:>10.2f}{note_str}"
        )


class BankAccount:
    """Represents a customer bank account with balance validation and transaction history."""

    total_accounts = 0

    @classmethod
    def _increment_accounts(cls) -> None:
        cls.total_accounts += 1

    def __init__(self, account_number: str, owner_name: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self._balance = float(initial_balance)
        self.transactions: list[Transaction] = []
        type(self)._increment_accounts()

        if self._balance > 0:
            self._record_transaction("OPENING", self._balance, "Initial deposit")

    @property
    def owner_name(self) -> str:
        return self._owner_name

    @owner_name.setter
    def owner_name(self, name: str) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Owner name must be a non-empty string.")
        self._owner_name = name.strip()

    @property
    def balance(self) -> float:
        return self._balance

    def _record_transaction(self, tx_type: str, amount: float, note: str = "") -> Transaction:
        tx = Transaction(self.account_number, tx_type, amount, self._balance, note)
        self.transactions.append(tx)
        return tx

    def deposit(self, amount: float, note: str = "Cash deposit") -> Transaction:
        """Deposit a positive amount into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self._balance += float(amount)
        return self._record_transaction("DEPOSIT", amount, note)

    def withdraw(self, amount: float, note: str = "Cash withdrawal") -> Transaction:
        """Withdraw a positive amount from the account if sufficient funds exist."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self._balance:
            raise ValueError(
                f"Insufficient funds in account {self.account_number}: "
                f"attempted ${amount:.2f}, available ${self._balance:.2f}."
            )
        self._balance -= float(amount)
        return self._record_transaction("WITHDRAWAL", amount, note)

    def display_statement(self) -> None:
        """Print the account summary and all recorded transactions."""
        print(f"\n--- Account Statement: {self.account_number} ({self.owner_name}) ---")
        if not self.transactions:
            print("  No transactions recorded yet.")
        else:
            for tx in self.transactions:
                print(f"  {tx}")
        print(f"  Current Balance: ${self._balance:,.2f}")

    def __str__(self) -> str:
        return f"Account[{self.account_number}] Owner: {self.owner_name:<15} | Balance: ${self._balance:>10.2f}"


class BankLedger:
    """Central bank ledger managing multiple accounts and inter-account transfers."""

    def __init__(self, bank_name: str = "Python National Bank"):
        self.bank_name = bank_name
        self.accounts: dict[str, BankAccount] = {}
        self.master_entries: list[Transaction] = []

    def create_account(self, account_number: str, owner_name: str, initial_balance: float = 0.0) -> BankAccount:
        """Create and register a new bank account in the ledger."""
        if account_number in self.accounts:
            raise ValueError(f"Account {account_number} already exists.")
        account = BankAccount(account_number, owner_name, initial_balance)
        self.accounts[account_number] = account
        if account.transactions:
            self.master_entries.extend(account.transactions)
        return account

    def get_account(self, account_number: str) -> BankAccount:
        """Retrieve an account by account number or raise KeyError."""
        if account_number not in self.accounts:
            raise KeyError(f"Account {account_number} not found.")
        return self.accounts[account_number]

    def record_deposit(self, account_number: str, amount: float, note: str = "Deposit") -> Transaction:
        """Deposit money into an account and log it in the master ledger."""
        account = self.get_account(account_number)
        tx = account.deposit(amount, note)
        self.master_entries.append(tx)
        return tx

    def record_withdrawal(self, account_number: str, amount: float, note: str = "Withdrawal") -> Transaction:
        """Withdraw money from an account and log it in the master ledger."""
        account = self.get_account(account_number)
        tx = account.withdraw(amount, note)
        self.master_entries.append(tx)
        return tx

    def transfer(self, from_acct_num: str, to_acct_num: str, amount: float, note: str = "") -> tuple[Transaction, Transaction]:
        """Transfer funds atomically between two accounts in the ledger."""
        if from_acct_num == to_acct_num:
            raise ValueError("Cannot transfer to the same account.")
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero.")

        sender = self.get_account(from_acct_num)
        receiver = self.get_account(to_acct_num)

        transfer_note = f" ({note})" if note else ""
        out_tx = sender.withdraw(amount, f"Transfer to {to_acct_num}{transfer_note}")
        out_tx.tx_type = "TRANSFER_OUT"

        in_tx = receiver.deposit(amount, f"Transfer from {from_acct_num}{transfer_note}")
        in_tx.tx_type = "TRANSFER_IN"

        self.master_entries.extend([out_tx, in_tx])
        return out_tx, in_tx

    def total_bank_deposits(self) -> float:
        """Return the sum of balances across all accounts in the bank."""
        return sum(acct.balance for acct in self.accounts.values())

    def display_all_accounts(self) -> None:
        """Print all accounts currently registered in the ledger."""
        print(f"\n=== {self.bank_name} - Accounts Summary ===")
        if not self.accounts:
            print("  No accounts in ledger.")
            return
        for acct in self.accounts.values():
            print(f"  {acct}")
        print(f"  Total Bank Deposits: ${self.total_bank_deposits():,.2f}")

    def display_master_ledger(self) -> None:
        """Print every transaction recorded across the entire bank."""
        print(f"\n=== {self.bank_name} - Master Transaction Ledger ===")
        if not self.master_entries:
            print("  No transactions in master ledger.")
            return
        for entry in self.master_entries:
            print(f"  {entry}")
