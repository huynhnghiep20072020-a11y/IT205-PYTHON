import unittest
from main import calculate_total_revenue

class TestTicketRevenue(unittest.TestCase):
    """Bộ Unit Test kiểm tra logic tính tổng doanh thu."""

    def test_revenue_with_mixed_tickets(self):
        """Kiểm tra danh sách chứa cả vé Booked và Cancelled."""
        mock_tickets = [
            {"ticket_id": "T01", "price": 500.0, "status": "Booked"},
            {"ticket_id": "T02", "price": 300.0, "status": "Cancelled"},
            {"ticket_id": "T03", "price": 500.0, "status": "Booked"}
        ]
        result = calculate_total_revenue(mock_tickets)
        self.assertEqual(result, 1000.0)

    def test_revenue_empty_list(self):
        """Kiểm tra danh sách rỗng."""
        mock_tickets = []
        result = calculate_total_revenue(mock_tickets)
        self.assertEqual(result, 0.0)

if __name__ == "__main__":
    unittest.main()