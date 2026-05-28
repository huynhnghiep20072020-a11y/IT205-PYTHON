"""
1 PHÂN TÍCH & ĐỀ XUẤT GIẢI PHÁP

1. Phân tích Input / Output:
- Input: Người dùng nhập vào một chuỗi (str) từ bàn phím. Hệ thống cần 
  ép kiểu ngay sang số nguyên (int) để thực hiện các phép so sánh toán học.
- Output: 
  + Nếu nhập <= 0 (Dính bẫy 1 hoặc 2): Báo lỗi và bắt nhập lại.
  + Nếu nhập > 0 (Hợp lệ): In thông báo [THÀNH CÔNG] và thoát vòng lặp.

2. Đề xuất 2 giải pháp tạo vòng lặp (Validation loop):
- Giải pháp 1: Dùng vòng lặp `while True` kết hợp `break`.
  (Tạo một vòng lặp chạy mãi mãi, kiểm tra dữ liệu bên trong, nếu dữ liệu 
  hợp lệ thì dùng `break` để chủ động phá vòng lặp).
- Giải pháp 2: Dùng vòng lặp `while condition` (Kiểm tra ngay ở cửa).
  (Phải tạo một biến mồi, ví dụ `so_luong = 0` ở ngoài vòng lặp. Sau đó 
  chạy `while so_luong <= 0:`, vòng lặp sẽ tự động dừng khi số > 0).

3. Bảng so sánh 2 giải pháp:
 Tiêu chí                  Giải pháp 1 (while True + break)   Giải pháp 2 (while condition)       |
-------------------------------------------------------------------------------------------------|
 Độ ngắn gọn của code      Tối ưu (Không cần đẻ thêm biến)    Dài hơn (Tốn 1 dòng tạo biến mồi)   |
 Mức độ dễ hiểu (Logic)    Trực quan, luồng suy nghĩ đi thẳng Hơi ngược logic tự nhiên một chút   |

4. Chốt lựa chọn:
- Chọn Giải pháp 1 (while True + break). 
- Lý do: Đây là "thiết kế chuẩn mực" (Design Pattern) trong Python dành 
  riêng cho việc ép buộc nhập liệu. Nó giúp code gọn gàng, không bị sinh 
  ra các "biến rác" (như gán tạm số lượng = -1) chỉ để lừa cho vòng lặp chạy.
"""


# 2 TRIỂN KHAI CODE 

print("--- HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ---")

# Khởi tạo Validation Loop bằng vòng lặp vô hạn
while True:
    # Tiếp nhận Input và ép kiểu sang int
    new_employees_count = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này: "))
    
    # Xử lý Edge Cases: Bẫy 1 (Số 0) và Bẫy 2 (Số âm)
    if new_employees_count <= 0:
        print("[LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0.\n")
    
    # Luồng xử lý chính (Happy Path)
    else:
        print(f"\n[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho {new_employees_count} nhân sự mới!")
        print("--- CHƯƠNG TRÌNH KẾT THÚC ---")
        
        # Dữ liệu đã chuẩn xác, dùng break để đập vỡ vòng lặp, cho phép hệ thống đi tiếp
        break