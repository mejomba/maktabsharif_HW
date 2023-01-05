import unittest
from .bank_account import Customer, BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self) -> None:
        self.akbar = Customer('akbar', 'ahmadi', '0936123456', 'akbar@gmail.com')
        self.jafar = Customer('jafar', 'mohamadi', '093612000', 'jafar@gmail.com')
        self.akbar_acc = BankAccount(self.akbar, 50000)
        self.jafar_acc = BankAccount(self.jafar, 20000)
        BankAccount.WAGE_AMOUNT = 600
        BankAccount.MIN_BALANCE = 10000

    def test_full_name(self):
        self.assertEqual(self.akbar.full_name(), 'akbar ahmadi')
        self.assertNotEqual(self.akbar.full_name(), 'abc', 'efg')
        self.assertIsInstance(self.akbar.full_name(), str)
        self.assertNotIsInstance(self.akbar.full_name(), (int, tuple, dict, float))

    def test_set_owner(self):
        self.akbar_acc.set_owner(self.jafar)
        self.assertEqual(self.akbar_acc.get_owner(), self.jafar_acc.get_owner())

    def test_get_owner(self):
        self.assertEqual(self.akbar_acc.get_owner(), self.akbar)
        self.assertNotEqual(self.akbar_acc.get_owner(), self.jafar)

    def test_withdraw(self):
        self.assertRaises(BankAccount.MinBalanceError, self.akbar_acc.withdraw, 45000)
        # OR
        with self.assertRaises(BankAccount.MinBalanceError) as error:
            self.akbar_acc.withdraw(45000)
        self.assertTrue("NOT Enough balance to withdraw!" in str(error.exception))

        self.akbar_acc.withdraw(10000)
        self.assertEqual(self.akbar_acc.get_balance(), 40000 - (2 * BankAccount.WAGE_AMOUNT))

        self.assertRaises(ValueError, self.akbar_acc.withdraw, -1000)
        # OR
        with self.assertRaises(ValueError) as error2:
            self.akbar_acc.withdraw(-10000)
        self.assertTrue("amount must be positive" in str(error2.exception))

    def test_deposit(self):
        self.akbar_acc.deposit(5000)
        self.assertEqual(self.akbar_acc.get_balance(), 50000 + 5000 - BankAccount.WAGE_AMOUNT)

    def test_get_balance(self):
        self.assertEqual(self.akbar_acc.get_balance(), 50000 - BankAccount.WAGE_AMOUNT)
        self.assertIsInstance(self.akbar_acc.get_balance(), int)

    def test_transfer(self):
        self.akbar_acc.transfer(self.jafar_acc, 5000)
        self.assertEqual(self.akbar_acc.get_balance(), 50000 - 5000 - (2 * BankAccount.WAGE_AMOUNT))
        self.assertEqual(self.jafar_acc.get_balance(), 20000 + 5000 - BankAccount.WAGE_AMOUNT)
        self.assertIsInstance(self.akbar_acc.get_balance(), int)
        self.assertIsInstance(self.jafar_acc.get_balance(), int)

    def test_change_wage(self):
        BankAccount.change_wage(1000)
        self.assertEqual(BankAccount.WAGE_AMOUNT, 1000)
        self.assertRaises(ValueError, BankAccount.change_wage, "1000")
        self.assertRaises(ValueError, BankAccount.change_wage, "dsfdsf")

        self.assertEqual(BankAccount.WAGE_AMOUNT, 1000)

        BankAccount.change_wage(-2000)
        self.assertEqual(BankAccount.WAGE_AMOUNT, 0)

        BankAccount.change_wage(0)
        self.assertEqual(BankAccount.WAGE_AMOUNT, 0)

    def test_change_min_balance(self):
        BankAccount.change_min_balance(5000)
        self.assertEqual(BankAccount.MIN_BALANCE, 5000)
        self.assertRaises(ValueError, BankAccount.change_min_balance, "1000")
        self.assertRaises(ValueError, BankAccount.change_min_balance, "dsfdsf")

        self.assertEqual(BankAccount.MIN_BALANCE, 5000)
        #
        BankAccount.change_min_balance(-2000)
        self.assertEqual(BankAccount.MIN_BALANCE, 0)
        #
        BankAccount.change_min_balance(0)
        self.assertEqual(BankAccount.MIN_BALANCE, 0)


if __name__ == "__main__":
    unittest.main()