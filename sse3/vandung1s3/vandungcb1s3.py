"""
1 PHÂN TÍCH LỖI 


1. Dò luồng thực thi (Trace code):
- Lần lặp 1: total_budget = 0 -> Nhập lương 5.000.000 -> total_budget = 0 + 5.000.000 = 5.000.000
- Lần lặp 2: total_budget = 0 (BỊ RESET!) -> Nhập lương 4.000.000 -> total_budget = 0 + 4.000.000 = 4.000.000
- Lần lặp 3: total_budget = 0 (BỊ RESET!) -> Nhập lương 6.000.000 -> total_budget = 0 + 6.000.000 = 6.000.000
=> Kết thúc vòng lặp, in ra kết quả cuối cùng là 6.000.000.

2. Giải thích nguyên nhân:
- Lỗi nằm ở việc đặt câu lệnh `total_budget = 0` ở BÊN TRONG vòng lặp for.
- Hệ quả là mỗi khi vòng lặp quay lại từ đầu để xử lý nhân viên tiếp theo, 
  "chiếc hộp" đựng tiền total_budget lại bị vứt đi và thay bằng một chiếc hộp 
  mới trống rỗng (0 đồng). Nó hoàn toàn "mất trí nhớ" về số tiền đã cộng ở vòng trước.

3. Lỗi logic kinh điển:
- Đây là lỗi "Khởi tạo biến tích lũy (accumulator) sai vị trí".
- Nguyên tắc cốt lõi: Khi muốn cộng dồn hoặc đếm một cái gì đó qua nhiều vòng lặp, 
  biến lưu trữ kết quả bắt buộc phải được tạo ra ở BÊN NGOÀI và TRƯỚC KHI vòng lặp bắt đầu.
"""


# 2 TRIỂN KHAI CODE (PYTHON) - ĐÃ SỬA LỖI

print("--- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ---")

# SỬA LỖI TẠI ĐÂY: Dời biến cộng dồn ra khỏi vòng lặp để không bị reset
total_budget = 0

# Vòng lặp chạy 3 lần để nhập lương cho 3 nhân viên
for employee_number in range(1, 4):
    print("Đang xử lý nhân viên số", employee_number)
    
    # Nhập mức lương
    salary = int(input("  Nhập mức lương (VNĐ): "))
    
    # Thực hiện thao tác cộng dồn tiền vào chiếc hộp
    total_budget = total_budget + salary

# Sau khi nhập xong cả 3 người (kết thúc vòng lặp), mới in tổng tiền ra màn hình
print("=> KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:", total_budget, "VNĐ")