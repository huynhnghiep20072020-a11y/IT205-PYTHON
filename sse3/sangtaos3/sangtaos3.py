"""
1 THIẾT KẾ KIẾN TRÚC & LUỒNG DỮ LIỆU


1. Bảng Thiết kế Dữ liệu (5 trường thông tin):
 Tên biến (snake_case)  Câu hỏi Input (Prompt)                                Kiểu dữ liệu | Điều kiện Validation                  |
-------------------------------------------------------------------------------------------|---------------------------------------|
 employee_id            1. Enter Employee ID:                                 str          | Không được bỏ trống                   |
 employee_name          2. Enter Full Name:                                   str          | Không được bỏ trống                   |
 current_salary         3. Enter current Salary in VND (Number > 0):          float        | Phải là số và > 0                     |
 performance_score      4. Enter Performance Score (1.0 to 5.0):              float        | Phải là số và nằm trong [1.0, 5.0]    |
 experience_years       5. Enter Year of Experience (Integer >= 0):            int          | Phải là số nguyên và >= 0             |

2. Thiết kế luồng chương trình (Pseudocode):
- Bắt đầu Vòng lặp Tổng (while True) cho phép nhập nhiều nhân viên:
    - In tiêu đề "KIOSK HR: CẬP NHẬT HỒ SƠ & ĐÁNH GIÁ KPI"
    - Thu thập employee_id và employee_name (dùng .strip() để xóa khoảng trắng).
    - Vòng lặp Validation cho Lương (current_salary):
        - Bắt nhập liệu -> Ép kiểu float.
        - NẾU <= 0: In cảnh báo đỏ và lặp lại.
        - NGƯỢC LẠI: Break (Thoát vòng lặp lương).
    - Vòng lặp Validation cho KPI (performance_score):
        - Bắt nhập liệu -> Ép kiểu float.
        - NẾU < 1.0 HOẶC > 5.0: In cảnh báo đỏ và lặp lại.
        - NGƯỢC LẠI: Break (Thoát vòng lặp KPI).
    - Vòng lặp Validation cho Số năm kinh nghiệm (experience_years):
        - Bắt nhập liệu -> Ép kiểu int.
        - NẾU < 0: In cảnh báo đỏ và lặp lại.
        - NGƯỢC LẠI: Break (Thoát vòng lặp Kinh nghiệm).
    - In HỒ SƠ ĐIỆN TỬ (E-PROFILE) định dạng đẹp mắt.
    - In LOG HỆ THỐNG kèm hàm type() cho IT.
    - Hỏi Quản lý có muốn tiếp tục không? (y/n)
    - NẾU 'n': In "Tạm biệt" và Break Vòng lặp Tổng để tắt Kiosk.
"""

# 2 TRIỂN KHAI CODE 


# VÒNG LẶP NGOÀI CÙNG  Cho phép nhập liên tục nhiều nhân sự
while True:
    print("\n========================================")
    print(" KIOSK HR: CẬP NHẬT HỒ SƠ & ĐÁNH GIÁ KPI")
    print("========================================")
    print("\n[Nhập thông tin nhân viên]")
    
    # Dùng vòng lặp cơ bản để chống nhập khoảng trắng hoặc để trống
    while True:
        employee_id = input("1. Enter Employee ID: ").strip()
        if employee_id: 
            break
        print("   [!] LỖI: Mã nhân viên không được để trống!")

    while True:
        employee_name = input("2. Enter Full Name: ").strip()
        if employee_name: 
            break
        print("   [!] LỖI: Tên nhân viên không được để trống!")

    
    # 2.1. Xác thực Lương (Float, > 0)
    while True:
        try:
            current_salary = float(input("3. Enter current Salary in VND (Number > 0): "))
            if current_salary <= 0:
                print("   [!] LỖI: Lương không thể là số âm hoặc bằng 0. Vui lòng nhập lại!")
            else:
                break # Dữ liệu đúng chuẩn -> Thoát vòng lặp nhập lương
        except ValueError:
            print("   [!] LỖI: Vui lòng chỉ nhập số (không chứa chữ cái hay dấu phẩy)!")

    # 2.2. Xác thực Điểm KPI 
    while True:
        try:
            performance_score = float(input("4. Enter Performance Score (1.0 to 5.0): "))
            if performance_score < 1.0 or performance_score > 5.0:
                print("   [!] LỖI: Điểm KPI phải nằm trong khoảng từ 1.0 đến 5.0!")
            else:
                break # Dữ liệu đúng chuẩn -> Thoát vòng lặp nhập KPI
        except ValueError:
            print("   [!] LỖI: Vui lòng chỉ nhập số hợp lệ!")

    # 2.3. Xác thực Số năm kinh nghiệm
    while True:
        try:
            experience_years = int(input("5. Enter Year of Experience (Integer >= 0): "))
            if experience_years < 0:
                print("   [!] LỖI: Số năm kinh nghiệm không thể là số âm!")
            else:
                break # Dữ liệu đúng chuẩn -> Thoát vòng lặp nhập năm kinh nghiệm
        except ValueError:
            print("   [!] LỖI: Vui lòng nhập một số nguyên hợp lệ!")

    
    # In Hồ sơ Điện tử
    print("\n========================================")
    print("           E-PROFILE CẬP NHẬT           ")
    print("========================================")
    print(f"- ID: {employee_id.upper()}")
    print(f"- Name: {employee_name.title()}")
    # Ép kiểu int khi in lương để cắt bỏ phần thập phân .0 dư thừa nếu có
    print(f"- Salary: {int(current_salary)} VND") 
    print(f"- KPI Score: {performance_score} / 5.0")
    print(f"- Experience: {experience_years} years")
    
    # In Log Hệ Thống cho phòng IT
    print("========================================")
    print("             IT SYSTEM LOG              ")
    print("========================================")
    # Dùng \t (tab) hoặc ljust() để căn lề cột cho đẹp mắt
    print(f"employee_id        | {type(employee_id)}")
    print(f"employee_name      | {type(employee_name)}")
    print(f"current_salary     | {type(current_salary)}")
    print(f"performance_score  | {type(performance_score)}")
    print(f"experience_years   | {type(experience_years)}")
    print("========================================")

    tiep_tuc = input("\nDo you want to enter another employee? (y/n): ").strip().lower()
    if tiep_tuc == 'n':
        print("\nĐang tắt Kiosk... Tạm biệt!")
        break # Đập vỡ vòng lặp ngoài cùng, kết thúc toàn bộ chương trình