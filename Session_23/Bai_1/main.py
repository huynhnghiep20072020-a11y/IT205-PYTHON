# Lý do from ast import Global
# from math import * là Anti-pattern: Cú pháp này được gọi là "Wildcard Import".
# nạp toàn bộ các hàm và biến của thư viện math vào không gian tên hiện tại chung (Global Namespace).
# Điều này gây ô nhiễm bộ nhớ và rất dễ dẫn đến hiện tượng Xung đột định danh (Namespace Collision) — 
# vô tình ghi đè lên các hàm hoặc biến do lập trình viên tự viết. Cách khắc phục: Nên import tường minh bằng cách dùng import math (khi dùng gọi math.sqrt())
# hoặc chỉ nạp đúng hàm mình cần như from math import radians, sin, cos.

#  cấu hình Package: Để biến một thư mục thông thường thành một Package
#  cần tạo một tệp trống có tên là __init__.py. Tệp này đóng vai trò như một "tấm biển báo" (Marker) giúp trình thông dịch Python hiểu rằng thư mục này chứa mã nguồn có thể được import.

# (Folder Tree
# Rikkei_Logistics/
# ├── main.py
# ├── core/
# │   ├── __init__.py
# │   ├── geo_calculator.py
# │   └── time_estimator.py
# └── utils/
#     ├── __init__.py
#     └── file_helper.py

import datetime
from utils.file_helper import create_log_dir
from core.geo_calculator import calculate_distance
from core.time_estimator import predict_eta

def main():
    """Hàm chạy luồng chính xử lý và điều phối các chuyến xe giao hàng."""
    shipments = [
        {"id": "TRK-001", "from_lat": 21.0285, "from_lon": 105.8542, "to_lat": 10.8231, "to_lon": 106.6297, "depart": "2026-06-10 08:00:00", "deadline": "2026-06-11 12:00:00"},
        {"id": "TRK-002", "from_lat": 21.0285, "from_lon": 105.8542, "to_lat": 16.0544, "to_lon": 108.2022, "depart": "2026-06-10 09:30:00", "deadline": "2026-06-10 15:00:00"},
    ]

    print("====== HỆ THỐNG ĐIỀU PHỐI RIKKEI LOGISTICS =======")
    
    create_log_dir("logs")
    print("[INFO] Khởi tạo hệ thống lưu trữ log hành trình... Thành công.")
    print("-" * 75)

    for s in shipments:
        distance = calculate_distance(s["from_lat"], s["from_lon"], s["to_lat"], s["to_lon"])
        eta = predict_eta(s["depart"], distance)
        eta_formatted = eta.replace(microsecond=0)
        
        deadline_obj = datetime.datetime.strptime(s["deadline"], "%Y-%m-%d %H:%M:%S")
        deadline_time_str = deadline_obj.strftime("%H:%M:%S")

        print(f"[CHUYẾN XE {s['id']}]")
        print(f" + Khoảng cách vận chuyển: {distance:.2f} km")
        print(f" + Thời gian khởi hành: {s['depart']}")
        print(f" + Dự kiến cập bến (ETA): {eta_formatted}")

        if eta <= deadline_obj:
            print(" + Trạng thái: 🟢 AN TOÀN (Kịp tiến độ trước deadline)\n")
        else:
            print(f" + Trạng thái: 🔴 CẢNH BÁO (Trễ hạn! Deadline yêu cầu lúc {deadline_time_str})\n")

    print("========================================================")

if __name__ == "__main__":
    main()