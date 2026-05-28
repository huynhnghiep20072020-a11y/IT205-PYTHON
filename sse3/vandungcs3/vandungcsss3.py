"""
1 PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP


1. Phân tích Input / Output:
- Input: 3 vòng lặp, mỗi vòng yêu cầu nhập 3 chuỗi (str):
  + Mã nhân viên (employee_id)
  + Họ và tên (employee_name)
  + Phòng ban (department)
- Output: 
  + Nếu hợp lệ: In ra Phiếu Hồ sơ Điện tử trình bày đẹp mắt.
  + Nếu rơi vào bẫy dữ liệu (Edge Cases): In ra câu [CẢNH BÁO] đỏ và 
    chuyển sang người tiếp theo, KHÔNG in phiếu.

2. Đề xuất giải pháp (Xử lý Edge Cases):
- Sử dụng vòng lặp `for` chạy đúng 3 lần (range(1, 4)).
- Áp dụng hàm `.strip()` ngay sau hàm `input()`. Hàm này sẽ dọn sạch mọi 
  khoảng trắng (dấu cách, tab) ở đầu và cuối chuỗi. Nếu HR lỡ tay bấm 
  toàn dấu cách (Bẫy 2), `.strip()` sẽ biến nó thành chuỗi rỗng "".
- Sử dụng câu lệnh điều kiện `if`: Kiểm tra xem độ dài chuỗi có bằng 0 
  hay không (Bẫy 1 - Bỏ trống). Nếu bằng 0, in cảnh báo và dùng lệnh 
  `continue` để ngắt luồng xử lý hiện tại, ép hệ thống vòng lên hỏi người tiếp theo.

3. Thiết kế thuật toán (Pseudocode):
- Bắt đầu vòng lặp i từ 1 đến 3:
    - Nhập ID, gán vào employee_id (nhớ cắt khoảng trắng).
    - Nhập Tên, gán vào employee_name (nhớ cắt khoảng trắng).
    - Nhập Phòng ban, gán vào department.
    - NẾU len(employee_id) == 0 HOẶC len(employee_name) == 0:
        - In ra "[CẢNH BÁO]..."
        - CONTINUE (Quay lại đầu vòng lặp)
    - In ra "PHIẾU HỒ SƠ NHÂN SỰ" với dữ liệu hợp lệ.
- Kết thúc vòng lặp, in thông báo hoàn tất.
"""

# 2 TRIỂN KHAI CODE 


print("=" * 60)
print("        HỆ THỐNG KHỞI TẠO HỒ SƠ NHÂN SỰ SỐ")
print("=" * 60)

# Chạy vòng lặp đúng 3 lần cho 3 nhân sự
for i in range(1, 4):
    print(f"\n--- Đang tiếp nhận Nhân sự thứ {i}/3 ---")
    
    # Dùng .strip() ngay lúc nhập để "hóa giải" Bẫy 2 (Dữ liệu rác khoảng trắng)
    employee_id = input("Nhập Mã nhân viên : ").strip()
    employee_name = input("Nhập Họ và tên    : ").strip()
    department = input("Nhập Phòng ban    : ").strip()
    
    # Xử lý Edge Cases: Bẫy 1 (Bỏ trống) và Bẫy 2 (Sau khi strip sẽ thành rỗng)
    # len() == 0 nghĩa là chuỗi không có bất kỳ ký tự hợp lệ nào
    if len(employee_id) == 0 or len(employee_name) == 0:
        print("\n[CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên này.")
        # Lệnh continue ép hệ thống bỏ qua các dòng in phiếu bên dưới, quay lên vòng mới
        continue
        
    # --- LUỒNG XỬ LÝ CHÍNH (HAPPY PATH) ---
    # Chỉ những dữ liệu hoàn toàn "sạch" mới có thể lọt qua trạm kiểm soát trên và đến được đây
    print("\n" + "*" * 50)
    print("             HỒ SƠ NHÂN SỰ ĐIỆN TỬ")
    print("*" * 50)
    print(f"- Mã nhân viên : {employee_id.upper()}")
    print(f"- Họ và tên    : {employee_name.title()}")
    print(f"- Phòng ban    : {department.title()}")
    print("*" * 50)

# Khối lệnh này nằm ngoài vòng lặp, chỉ chạy khi vòng lặp đã hoàn tất 3 lần
print("\n[HỆ THỐNG] Đã hoàn tất phiên làm việc. Đóng Kiosk Nhập liệu.")