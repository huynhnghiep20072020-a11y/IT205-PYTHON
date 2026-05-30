student_name = "  nguYEn vAn a  "
student_code = " rk-001-python  "
email = "  Student01@GMAIL.COM  "

# Gán đè kết quả trả về vào chính biến cũ và nối phương thức (chaining)
student_name = student_name.strip().title()
student_code = student_code.strip().upper()
email = email.strip().lower()

# In kết quả
print("Họ tên:", student_name)
print("Mã học viên:", student_code)
print("Email:", email)



# 1. Chuỗi (String) trong Python có tính bất biến, không thể thay đổi trực tiếp.
# 2. Các hàm xử lý (strip, upper, lower...) chỉ tạo ra chuỗi mới chứ không sửa biến gốc.
# 3. Bắt buộc phải gán lại kết quả trả về vào biến (VD: email = email.lower()) để lưu lại.