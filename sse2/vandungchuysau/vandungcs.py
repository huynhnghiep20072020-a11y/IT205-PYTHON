"""
1 PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP

1. Phân tích Input / Output:
- Input (Đầu vào): Hệ thống cần tiếp nhận 3 trường thông tin từ người dùng.
  Cả 3 trường này đều mang kiểu dữ liệu chuỗi văn bản (str) vì chúng 
  chứa các chữ cái, khoảng trắng và ký tự chữ số kết hợp:
  + Họ và tên bệnh nhân (str)
  + Mã bệnh án (str)
  + Khoa/Phòng khám chỉ định (str)
- Output (Đầu ra): Một chuỗi văn bản duy nhất hiển thị thông báo thành công 
  và Phiếu khám bệnh điện tử theo đúng format yêu cầu.

2. Đề xuất giải pháp:
- Sử dụng hàm input() để thu thập dữ liệu từ bàn phím.
- Sử dụng F-string (f"...") để ghép nối các biến vào khung văn bản của phiếu 
  khám. F-string là công cụ tối ưu và chuyên nghiệp nhất trong Python để 
  định dạng chuỗi, giúp tránh lỗi thiếu khoảng trắng khi dùng toán tử cộng (+).
- Sử dụng hàm print() để xuất kết quả ra màn hình CLI.

3. Thiết kế thuật toán (Pseudocode):
- Bước 1: In ra màn hình dòng tiêu đề hệ thống.
- Bước 2: Dùng input() yêu cầu nhập Họ tên, gán vào biến ho_ten.
- Bước 3: Dùng input() yêu cầu nhập Mã bệnh án, gán vào biến ma_ba.
- Bước 4: Dùng input() yêu cầu nhập Khoa khám, gán vào biến khoa_kham.
- Bước 5: Tạo biến phieu_kham, dùng f-string nhúng 3 biến trên vào chuỗi template.
- Bước 6: In thông báo xác nhận thành công và hiển thị biến phieu_kham.
"""

# (2) TRIỂN KHAI CODE (PYTHON)

# 1. Hiển thị tiêu đề
print("--- HỆ THỐNG TIẾP NHẬN BỆNH ÁN ---")

# 2. Thu thập dữ liệu (Input)
ho_ten = input("Nhập họ và tên bệnh nhân: ")
ma_ba = input("Nhập mã bệnh án (VD: BN1024): ")
khoa_kham = input("Nhập Khoa/Phòng khám chỉ định: ")

# 3. Xử lý định dạng (Process) bằng F-string
phieu_kham_dien_tu = f"Bệnh nhân: [{ho_ten}] - Mã BA: [{ma_ba}] - Chuyển tới: [{khoa_kham}]"

# 4. Hiển thị kết quả (Output)
print("\n[HỆ THỐNG] Đã tiếp nhận và tạo Phiếu khám điện tử thành công!")
print("-" * 75)
print(phieu_kham_dien_tu)
print("-" * 75)