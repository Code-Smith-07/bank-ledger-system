# Bank Ledger System

A modular Python application that models a bank ledger with accounts, deposits, withdrawals, atomic inter-account transfers, and transaction statements.

## Project Structure

- `main.py` — Main entry point that runs a full ledger demonstration (or interactive menu with `--interactive`).
- `ledger-classe.py` — Core classes (`Transaction`, `BankAccount`, `BankLedger`) and helper functions.
- `test.py` — Automated verification tests for account operations and edge cases.

## How to Run

Run the ledger demonstration:
```bash
python3 main.py
```

Launch the interactive CLI menu:
```bash
python3 main.py --interactive
```

Run tests:
```bash
python3 test.py
```
