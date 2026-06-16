from datetime import datetime

def parse_and_inspect_date(date_str):
    """Kiểm tra và bẫy lỗi dữ liệu ngày tháng không hợp lệ."""
    try:
        valid_date = datetime.strptime(date_str, "%Y-%m-%d")
        return valid_date
    except ValueError:
        return None