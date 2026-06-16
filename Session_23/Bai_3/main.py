# Folder Tree

# Rikkei_Aviation/
# ├── main.py
# ├── core/
# │   ├── __init__.py
# │   ├── logistics.py
# │   └── manager.py
# └── utils/
#     ├── __init__.py
#     ├── file_helper.py
#     └── time_helper.py

# Tác hại của from math import *:
# Cú pháp này được gọi là "Wildcard Import". Việc dùng dấu * sẽ nạp toàn bộ tất cả các hàm và biến có trong thư viện đó vào không gian bộ nhớ chung.
# Điều này rất dễ gây ra xung đột định danh (Namespace Collision), làm ghi đè lên các biến hoặc hàm do chính bạn tự viết, khiến chương trình chạy sai logic mà rất khó để dò lỗi (Debug).
# việc sử dụng import math hoặc from math import ceil giúp mã nguồn rõ ràng (tường minh) và an toàn hơn.

from core.logistics import display_flights
from core.manager import add_new_flight
from utils.time_helper import process_eta
from utils.file_helper import create_folder

def main():
    """Vòng lặp chính điều hướng menu cho hệ thống Rikkei Aviation."""
    flights = [
        {"flight_id": "RA001", "passengers": 154, "depart_time": "2026-06-15 08:00:00", "duration_min": 120},
        {"flight_id": "RA002", "passengers": 85,  "depart_time": "2026-06-15 13:30:00", "duration_min": 45}
    ]

    while True:
        print("\n===== HỆ THỐNG ĐIỀU HÀNH BAY RIKKEI AVIATION =====")
        print("1. Hiển thị lịch trình và Thống kê hậu cần")
        print("2. Tiếp nhận chuyến bay mới")
        print("3. Tính thời gian hạ cánh dự kiến (ETA)")
        print("4. Khởi tạo thư mục lưu trữ log hệ thống")
        print("5. Thoát chương trình")
        print("==================================================")
        
        choice = input("Nhập lựa chọn của bạn: ").strip()

        match choice:
            case "1":
                display_flights(flights)
            case "2":
                add_new_flight(flights)
            case "3":
                process_eta(flights)
            case "4":
                create_folder()
            case "5":
                print("Cảm ơn kỹ sư đã sử dụng hệ thống!")
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5.")

if __name__ == "__main__":
    main()