"""

1 PHÂN TÍCH VÀ ĐỀ XUẤT GIẢI PHÁP


1. Phân tích Input / Output:
- Input (Đầu vào): Mọi dữ liệu thu thập từ hàm input() đều mặc định 
  được hệ thống ghi nhận là chuỗi ký tự (str).
- Output (Đầu ra mong muốn): 
  + Mã bệnh nhân: Giữ nguyên kiểu chuỗi (str)
  + Nhiệt độ cơ thể: Bắt buộc ép sang kiểu số thực (float)
  + Nhịp tim: Bắt buộc ép sang kiểu số nguyên (int)

2. Đề xuất 2 giải pháp Ép kiểu (Type Casting):
- Giải pháp 1 (Inline Type Casting - Ép kiểu trực tiếp): 
  Gộp chung hàm ép kiểu và hàm nhập liệu trên cùng 1 dòng code.
  VD: nhiet_do = float(input("Nhập nhiệt độ: "))
- Giải pháp 2 (Two-step Type Casting - Ép kiểu 2 bước): 
  Lưu dữ liệu vào một biến chuỗi tạm thời (raw data), sau đó 
  tiến hành ép kiểu ở một dòng lệnh riêng biệt bên dưới.
  VD: raw_nhiet_do = input("Nhập nhiệt độ: ")
      nhiet_do = float(raw_nhiet_do)

3. Bảng so sánh 2 giải pháp:
 Tiêu chí               Giải pháp 1 (Trực tiếp)      Giải pháp 2 (Hai bước)       
----------------------------------------------------------------------------------
 Số lượng biến (Bộ nhớ) Ít (Tiết kiệm biến)          Nhiều hơn (Cần biến tạm)     
 Độ ngắn gọn của code   Rất ngắn (1 dòng)            Dài hơn (2 dòng)             
 Khả năng dễ debug      Rất thấp (Khó bắt lỗi)       Rất cao (Dễ dàng tra vết)    

4. Chốt lựa chọn:
- Chọn Giải pháp 2 (Ép kiểu hai bước).
- Lý do: Trong môi trường Khoa Cấp cứu, tính ổn định của phần mềm là 
  ưu tiên số một. Việc tách rời khâu "Thu thập" và khâu "Xử lý" giúp 
  kỹ sư dễ dàng chèn thêm các khối bắt lỗi (Try-Catch) sau này. Nếu 
  điều dưỡng lỡ tay nhập "37,5" thay vì "37.5", chương trình sẽ không 
  bị sụp đổ (crash) ngay lập tức mà vẫn giữ lại được lịch sử nhập sai 
  để cảnh báo.
"""


# (2) TRIỂN KHAI CODE (PYTHON) - Dùng Giải pháp 2


# 1. Giao diện tiếp nhận
print("--- HỆ THỐNG TIẾP NHẬN SINH HIỆU ---")
ma_bn = input("Nhập mã bệnh nhân: ")
raw_nhiet_do = input("Nhập nhiệt độ cơ thể (vd: 37.5): ")
raw_nhip_tim = input("Nhập nhịp tim (vd: 85): ")

# 2. Xử lý chuẩn hóa (Type Casting)
nhiet_do = float(raw_nhiet_do)
nhip_tim = int(raw_nhip_tim)

# 3. Hiển thị xác nhận
print("\n--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU ---")
print(f"Mã bệnh nhân: {ma_bn}")

print(f"Nhiệt độ cơ thể: {nhiet_do} độ C")
print(f"=> Kiểu dữ liệu hệ thống ghi nhận: {type(nhiet_do)}")

print(f"Nhịp tim: {nhip_tim} nhịp/phút")
print(f"=> Kiểu dữ liệu hệ thống ghi nhận: {type(nhip_tim)}")

print("-" * 50)
print("Thông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!")