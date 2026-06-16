from hrm_package.ui_display import display_records
from hrm_package.attendance_logic import clock_in, clock_out
from hrm_package.time_calc import evaluate_flex_time

def main():
    """Vòng lặp điều hướng menu chính của chương trình quản lý chấm công."""
    attendance_book = [
        {"id": "NV01", "name": "Nguyễn Văn A", "times": ("08:30", "17:30")},
        {"id": "NV02", "name": "Trần Thị B", "times": ("09:30", None)},
        {"id": "NV03", "name": "Lê Văn C", "times": ("10:15", "19:15")}
    ]

    while True:
        print("\n=== HỆ THỐNG CHẤM CÔNG RIKKEI (FLEX-TIME) ===")
        print("1. Xem bảng chấm công ngày")
        print("2. Chấm công Vào (Clock-in)")
        print("3. Chấm công Ra (Clock-out)")
        print("4. Đánh giá vi phạm")
        print("5. Thoát chương trình")
        print("=================================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()

        match choice:
            case "1":
                display_records(attendance_book)
            case "2":
                clock_in(attendance_book)
            case "3":
                clock_out(attendance_book)
            case "4":
                evaluate_flex_time(attendance_book)
            case "5":
                print("Đã thoát chương trình quản lý chấm công.")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 5.")

if __name__ == "__main__":
    main()