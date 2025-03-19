# Personal Account Management (OOP)

This project implements a personal bank account management system using Object-Oriented Programming (OOP) principles. It includes classes for `Amount` and `PersonalAccount`.

## Project Structure

## Classes

### `Amount`

Represents a transaction amount.

**Attributes:**

* `amount` (float): The transaction amount.
* `timestamp` (datetime): The transaction date and time.
* `transaction_type` (str): A string indicating the transaction type ('DEPOSIT' or 'WITHDRAWAL').

**Methods:**

* `__init__(self, amount, transaction_type)`: Initializes a new `Amount` object.
* `__str__(self)`: Returns a string representation of the `Amount` object.

### `PersonalAccount`

Represents a personal bank account.

**Attributes:**

* `account_number` (int): A unique identifier for the account.
* `account_holder` (str): The name of the account holder.
* `balance` (float): The current balance in the account.
* `transactions` (list): A list to store `Amount` objects representing transactions.

**Methods:**

* `__init__(self, account_number, account_holder)`: Initializes a new `PersonalAccount` object.
* `deposit(self, amount)`: Deposits money into the account.
* `withdraw(self, amount)`: Withdraws money from the account.
* `print_transaction_history(self)`: Prints the transaction history of the account.
* `get_balance(self)`: Returns the current balance.
* `get_account_number(self)`: Returns the account number.
* `set_account_number(self, account_number)`: Sets the account number.
* `get_account_holder(self)`: Returns the account holder's name.
* `set_account_holder(self, account_holder)`: Sets the account holder's name.
* `__str__(self)`: Returns a string representation of the `PersonalAccount` object.
* `__add__(self, amount)`: Allows adding an amount to the account (deposit).
* `__sub__(self, amount)`: Allows subtracting an amount from the account (withdrawal).

## How to Run

1.  **Clone the Repository:**

```bash
git clone <repository_url>
cd personal-account-oop
