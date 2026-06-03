# 1. Dictionary truy cập phần tử bằng Key chứ không dùng chỉ số (Index), nên thay employee[0] thành employee["employee_id"].
# 2. Phải gọi chính xác tên Key đã khai báo ban đầu, sửa "name" thành "full_name" và "employee_status" thành "status".
# 3. Kiểu Dictionary không có phương thức append(), để thêm lương cơ bản ta dùng cú pháp gán trực tiếp: dict[key] = value.
# 4. Để xóa phòng ban, phải truyền đúng Key là "department", nếu truyền sai là "team" hệ thống sẽ báo lỗi KeyError.
# 5. Sau khi thay đổi bằng đúng các đặc tính của Dictionary, chương trình sẽ chạy mượt mà và cho ra kết quả như ý muốn.

# Thông tin nhân viên ban đầu
employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

# Lấy mã nhân viên (Truy cập bằng đúng Key)
employee_id = employee["employee_id"]

# Lấy họ tên nhân viên (Truy cập bằng đúng Key)
full_name = employee["full_name"]

# Cập nhật trạng thái nhân viên (Gọi đúng Key và gán giá trị mới)
employee["status"] = "official"

# Thêm lương cơ bản (Gán trực tiếp Key mới và Value)
employee["base_salary"] = 15000000

# Xóa phòng ban (Dùng lệnh del với đúng tên Key)
del employee["department"]

print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)