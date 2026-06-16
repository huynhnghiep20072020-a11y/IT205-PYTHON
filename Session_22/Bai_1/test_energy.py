import unittest
from main import calculate_energy_financials

class TestEnergyFinancials(unittest.TestCase):
    """Bộ kiểm thử cho hàm tính toán chi phí năng lượng."""

    def test_no_discount_below_50000(self):
        """Kiểm thử trường hợp tổng điện năng dưới 50,000 kWh (0% chiết khấu)."""
        devices = [
            {'old_index': 1000, 'new_index': 2000},
            {'old_index': 0, 'new_index': 3000}
        ]
        total_kwh, discount_pct, final_cost = calculate_energy_financials(devices)
        self.assertEqual(total_kwh, 4000)
        self.assertEqual(discount_pct, 0.0)
        self.assertEqual(final_cost, 12000000.0)

    def test_discount_applied_above_50000(self):
        """Kiểm thử trường hợp tổng điện năng trên 50,000 kWh (Được hưởng 3% chiết khấu)."""
        devices = [
            {'old_index': 10000, 'new_index': 40000},
            {'old_index': 5000, 'new_index': 30000}
        ]
        total_kwh, discount_pct, final_cost = calculate_energy_financials(devices)
        self.assertEqual(total_kwh, 55000)
        self.assertEqual(discount_pct, 0.03)
        self.assertEqual(final_cost, 55000 * 3000 * 0.97)

    def test_discount_applied_exact_50000(self):
        """Kiểm thử trường hợp ranh giới: Tổng điện năng đạt chính xác 50,000 kWh."""
        devices = [
            {'old_index': 0, 'new_index': 50000}
        ]
        total_kwh, discount_pct, final_cost = calculate_energy_financials(devices)
        self.assertEqual(total_kwh, 50000)
        self.assertEqual(discount_pct, 0.03)
        self.assertEqual(final_cost, 50000 * 3000 * 0.97)

if __name__ == '__main__':
    unittest.main()