import datetime

def predict_eta(departure_str, distance_km, speed=60):
    """Tính toán thời gian dự kiến đến nơi dựa trên chuỗi thời gian khởi hành, khoảng cách và vận tốc."""
    dep_time = datetime.datetime.strptime(departure_str, "%Y-%m-%d %H:%M:%S")
    hours_needed = distance_km / speed
    eta = dep_time + datetime.timedelta(hours=hours_needed)
    return eta