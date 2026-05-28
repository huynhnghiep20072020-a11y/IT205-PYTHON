"""

(1) PHÂN TÍCH LỖI (BUG ANALYSIS)


1. Dò luồng thực thi (Trace code):
- Bước Nhập liệu (Input): Code chạy đúng. Các biến name_patient, age, 
  và symptom đã lưu giữ chính xác giá trị mà lễ tân nhập vào.
- Bước Xuất liệu (Output): Lỗi phát sinh ở khối lệnh print() cuối cùng 
  do ghép sai biến với nhãn thông tin.

2. Vì sao chương trình không bị crash (không lỗi cú pháp)?
- Hàm print() trong Python cho phép in nhiều giá trị liên tiếp nhau 
  (phân cách bằng dấu phẩy). Việc ghép nhãn văn bản (kiểu chuỗi) với 
  bất kỳ biến nào (chuỗi, số nguyên...) đều hoàn toàn hợp lệ về ngữ pháp.
- Máy tính chỉ làm theo lệnh chứ không hiểu ngữ nghĩa tiếng Việt của từ 
  "Tên" hay "Triệu chứng", nên nó không thể báo lỗi.

3. Nguyên nhân gây lỗi logic:
- Lập trình viên trước đó đã "râu ông nọ cắm cằm bà kia" khi gọi biến.
- Đáng lẽ 'Tên bệnh nhân:' phải đi với name_patient, thì lại gọi symptom.
- Đáng lẽ 'Tuổi:' phải đi với age, thì lại gọi name_patient.
- Đáng lẽ 'Triệu chứng:' phải đi với symptom, thì lại gọi age.
"""

# (2) MÃ NGUỒN ĐÃ SỬA LỖI (REFACTORED CODE)
#

print(' --- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN --- ')
name_patient = input('Nhập tên bệnh nhân: ')
age = int(input('Mời bạn nhập tuổi: '))
symptom = input('Mời bạn nhập triệu chứng bệnh: ')

print('\n --- PHIẾU KHÁM BỆNH --- ')
# Đã sắp xếp lại vị trí các biến cho khớp chính xác với nhãn thông tin
print('Tên bệnh nhân:', name_patient)
print('Tuổi:', age)
print('Triệu chứng:', symptom)