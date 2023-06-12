import unittest

from lesson14 import Bank, SavingsAccount


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_open_account(self):
        self.bank.open_account('savings', 'SA2', 1000.0, 0.02)

        opened_account = None
        for account in self.bank._accounts:
            if account.get_account_number() == 'SA2':
                opened_account = account
                break

        self.assertIsNotNone(opened_account, "Account was not opened")
        self.assertEqual(opened_account.get_balance(), 1000.0, "The balance of the new account is not correct")
        self.assertTrue(isinstance(opened_account, SavingsAccount), "The opened account is not a savings account")

        if isinstance(opened_account, SavingsAccount):
            opened_account.add_interest()
            self.assertEqual(opened_account.get_balance(), 1020.0, "Interest doesnt work properly")

        print("The Bank class works correct")


if __name__ == "__main__":
    unittest.main()
