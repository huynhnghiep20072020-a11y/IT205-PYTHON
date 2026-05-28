"""
(1) PHÂN TÍCH LỖI (BUG ANALYSIS)


1. Dò luồng thực thi (Trace code):
- Dòng 2-3 (Nhập liệu): Hệ thống yêu cầu nhập tên và cân nặng. Người dùng 
  nhập 65.5 vào biến weight.
- Dòng 5-7 (Xuất liệu): Chương trình in ra màn hình. Lúc này, chuỗi ký tự 
  "65.5" và con số 65.5 khi hiển thị trên Console trông hoàn toàn giống nhau.
- Dòng 9-10 (Kiểm tra): Hàm type(weight) bóc trần sự thật rằng dữ liệu 
  đang được lưu trong bộ nhớ là một đoạn văn bản (<class 'str'>).

2. Đặc điểm của hàm input() trong Python:
- Hàm input() có một nguyên tắc hoạt động cố định: Nó LUÔN LUÔN đọc mọi 
  dữ liệu người dùng gõ từ bàn phím dưới dạng một CHUỖI KÝ TỰ (string - str), 
  bất kể người dùng có gõ số nguyên hay số thập phân đi chăng nữa.

3. Nguyên nhân gốc rễ gây lỗi:
- Nguyên nhân là do lập trình viên trước đó chỉ dùng hàm input() đơn thuần 
  để lấy dữ liệu mà quên mất thao tác "Ép kiểu" (Type Casting). Hệ thống nhận 
  được chuỗi "65.5" và gán thẳng vào biến weight. Nếu đem biến này đi tính BMI, 
  chương trình sẽ bị crash ngay lập tức vì không thể làm toán với văn bản.
"""


# (2) MÃ NGUỒN ĐÃ SỬA LỖI (REFACTORED CODE)


print("--- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ---")
name_patient = input("Nhập tên bệnh nhân : ")

# SỬA LỖI TẠI ĐÂY: Sử dụng hàm float() bao bọc bên ngoài hàm input()
# để ép kiểu dữ liệu từ chuỗi (str) sang số thực (float) ngay lập tức.
weight = float(input("Nhập cân nặng bệnh nhân : "))

print("\n--- KIỂM TRA DỮ LIỆU LƯU TRỮ ---")
print("Bệnh nhân : ", name_patient)
print("Cân nặng đã nhập : ", weight)

# Lệnh kiểm tra này bây giờ sẽ trả về <class 'float'> đúng như yêu cầu
print("CẢNH BÁO - Kiểu dữ liệu đang lưu là : ", type(weight))