# File: tests/test_personal_account.py

import unittest
from datetime import datetime
from personal_account import PersonalAccount, Amount

class TestPersonalAccount(unittest.TestCase):
    def setUp(self):
        self.account = PersonalAccount(12345, "John Doe")

    def test_deposit(self):
        self.assertTrue(self.account.deposit(1000))
        self.assertEqual(self.account.get_balance(), 1000)
        self.assertFalse(self.account.deposit(-100))

    def test_withdraw(self):
        self.account.deposit(1000)
        self.assertTrue(self.account.withdraw(500))
        self.assertEqual(self.account.get_balance(), 500)
        self.assertFalse(self.account.withdraw(600))
        self.assertFalse(self.account.withdraw(-100))

    def test_print_transaction_history(self):
        self.account.deposit(1000)
        self.account.withdraw(500)
        self.assertEqual(len(self.account.transactions), 2)

    def test_get_balance(self):
        self.account.deposit(1000)
        self.assertEqual(self.account.get_balance(), 1000)

    def test_get_account_number(self):
        self.assertEqual(self.account.get_account_number(), 12345)

    def test_set_account_number(self):
        self.account.set_account_number(54321)
        self.assertEqual(self.account.get_account_number(), 54321)

    def test_get_account_holder(self):
        self.assertEqual(self.account.get_account_holder(), "John Doe")

    def test_set_account_holder(self):
        self.account.set_account_holder("Jane Smith")
        self.assertEqual(self.account.get_account_holder(), "Jane Smith")

    def test_dunder_add(self):
        self.account + 1000
        self.assertEqual(self.account.get_balance(), 1000)

    def test_dunder_sub(self):
        self.account + 1000
        self.account - 500
        self.assertEqual(self.account.get_balance(), 500)