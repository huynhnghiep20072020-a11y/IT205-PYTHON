import unittest
from main import (
    Wallet,
    TransactionLogger,
    InvalidAmountError,
    InsufficientBalanceError
)


class TestWallet(unittest.TestCase):
    """Unit tests for the Wallet class operations."""

    def setUp(self):
        """Initializes a new wallet and logger before each test case."""
        self.logger = TransactionLogger("test_momo_transactions.log")
        self.wallet = Wallet(self.logger)

    def test_deposit_success(self):
        """Tests if a valid deposit correctly updates the wallet balance."""
        self.wallet.deposit(500000)
        self.assertEqual(self.wallet.balance, 500000)

    def test_transfer_insufficient_balance(self):
        """Tests if transferring more than balance raises an exception."""
        self.wallet.deposit(300000)
        with self.assertRaises(InsufficientBalanceError):
            self.wallet.transfer("0987654321", 500000)

    def test_invalid_amount(self):
        """Tests if depositing a negative amount raises an exception."""
        with self.assertRaises(InvalidAmountError):
            self.wallet.deposit(-100000)


if __name__ == "__main__":
    unittest.main()