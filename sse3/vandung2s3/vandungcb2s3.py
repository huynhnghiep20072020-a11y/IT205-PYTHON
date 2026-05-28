"""

1 PHÂN TÍCH LỖI 


1. Dò luồng thực thi (Trace code) với trường hợp ngày công = 0:
- Vòng lặp bắt đầu: Kế toán nhập số ngày công = 0.
- Máy tính chạy đến câu lệnh if kiểm tra ngày công == 0: Điều kiện ĐÚNG.
- Máy tính thực hiện in ra dòng Cảnh báo trên màn hình cho HR.
- TUY NHIÊN, sau khi in xong, do không có lệnh điều hướng để "quay xe", 
  máy tính tiếp tục đi thẳng xuống các dòng code nằm bên dưới khối if.
- Hậu quả: Nó lấy 0 ngày nhân với định mức thưởng (ra 0 VNĐ), và vô tư 
  chạy luôn dòng lệnh gửi email chúc mừng.

2. Vấn đề về cấu trúc điều kiện trong vòng lặp:
- Vòng lặp đang bị thiếu lệnh điều khiển luồng `continue`. 
- Lệnh `continue` đóng vai trò như một biển báo "Quay đầu". Khi gặp 
  trường hợp 0 ngày công, đáng lẽ hệ thống phải in cảnh báo rồi `continue` 
  (bỏ qua toàn bộ phần tính tiền và gửi mail phía dưới, lập tức quay lên 
  đầu vòng lặp để xử lý nhân viên tiếp theo).
"""


# 2 TRIỂN KHAI CODE

print("--- PHẦN MỀM TÍNH THƯỞNG TẾT NHÂN SỰ ---")

# Giả sử HR cần nhập liệu cho 3 nhân viên thử việc
for employee_num in range(1, 4):
    print(f"\n--- Đang xử lý nhân viên số {employee_num} ---")
    
    # Nhập số ngày công
    working_days = int(input("Nhập số ngày công của nhân viên: "))
    
    # 1. Trạm kiểm soát Kiểm tra ngày công = 0
    if working_days == 0:
        print("-> [CẢNH BÁO HR]: Nhân viên nghỉ không lương cả tháng. Không xét thưởng.")
        
        # SỬA LỖI TẠI ĐÂY: Dùng continue để ngắt ngay lập tức lần lặp này.
        # Hệ thống sẽ bỏ qua đoạn code gửi email bên dưới và quay lên đầu.
        continue
    
    # 2. Luồng xử lý chính (Chỉ những ai có ngày công > 0 mới chạy được đến đây)
    
    # Giả sử quy định mức thưởng thử việc là 200,000 VNĐ / ngày công
    bonus_amount = working_days * 200000
    
    print("-> Đang tính toán quỹ thưởng...")
    # Thêm :, dể phân cách hàng nghìn cho số tiền đẹp mắt hơn (VD: 200,000)
    print(f"-> [HỆ THỐNG EMAIL]: Chúc mừng bạn nhận được {bonus_amount:,} VNĐ tiền thưởng Tết!")

print("\n--- HOÀN TẤT XỬ LÝ. ĐÓNG CHƯƠNG TRÌNH ---")