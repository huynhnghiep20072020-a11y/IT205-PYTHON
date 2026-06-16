import unittest
from logic_hight import (
    add_to_order,
    calculate_total,
    InvalidQuantityError,
    ItemNotFoundError
)


class TestHighlandsPOS(unittest.TestCase):
    """Unit tests for the Highlands Mini POS logic."""

    def test_calculate_total(self):
        """Tests if the total calculation of a mock order is correct."""
        mock_order = [
            {"code": "P1", "name": "Phin Sữa Đá", "price": 35000, "quantity": 2},
            {"code": "F1", "name": "Freeze Trà Xanh", "price": 55000, "quantity": 1}
        ]
        result = calculate_total(mock_order)
        self.assertEqual(result, 125000)

    def test_invalid_quantity(self):
        """Tests if adding a negative quantity raises InvalidQuantityError."""
        mock_order = []
        with self.assertRaises(InvalidQuantityError):
            add_to_order("T1", -1, mock_order)

    def test_item_not_found(self):
        """Tests if adding an invalid drink code raises ItemNotFoundError."""
        mock_order = []
        with self.assertRaises(ItemNotFoundError):
            add_to_order("INVALID_CODE", 2, mock_order)


if __name__ == "__main__":
    unittest.main()