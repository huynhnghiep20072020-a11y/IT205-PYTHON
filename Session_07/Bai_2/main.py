# 1. Chưa gán lại biến: transaction.strip() không thay đổi chuỗi gốc do tính bất biến, phải gán đè lại.
# 2. Sai ký tự cắt chuỗi (delimiter): Dữ liệu dùng dấu "|" nhưng lại split("-") khiến mảng bị lệch và gây lỗi.
# 3. Thiếu làm sạch phần tử: Sau khi split("|"), các phần tử vẫn còn khoảng trắng thừa, cần .strip() từng cái và ép kiểu int() cho tiền.

transaction = "   nguYEn vAn a | PYTHON-01 | 15000000 | paid   "

parts = transaction.split("|")


student_name = parts[0].strip().title()
course_code = parts[1].strip()
amount = int(parts[2].strip())  
status = parts[3].strip().upper()


print("Học viên:", student_name)
print("Khóa học:", course_code)
print(f"Số tiền: {amount:,} VND") 
print("Trạng thái:", status)