# 1. Index trong Python bắt đầu từ 0, nên mã sản phẩm nằm ở vị trí [0] và tên sản phẩm ở [1].
# 2. Tuple không có phương thức .length(), để đếm số phần tử ta bắt buộc phải dùng hàm len().
# 3. Tuple mang tính chất bất biến (immutable), nên không thể dùng dấu = để gán đè dữ liệu trực tiếp.
# 4. Để cập nhật được giá bán, cách an toàn và dễ hiểu nhất là ép kiểu Tuple sang dạng List tạm thời.
# 5. Sau khi sửa giá trị trên List, ta ép kiểu ngược lại thành Tuple để bảo vệ cấu trúc dữ liệu.

# Thông tin sản phẩm ban đầu
product_info = ("SP001", "Áo polo nam", "Size L", 299000)

# Lấy mã sản phẩm (Sửa lại index thành 0)
product_code = product_info[0]

# Lấy tên sản phẩm (Sửa lại index thành 1)
product_name = product_info[1]

# Đếm số lượng thông tin sản phẩm (Dùng hàm len)
product_length = len(product_info)

# Cập nhật giá bán thành 279000 bằng cách ép kiểu qua lại
temp_list = list(product_info)   # Ép sang List để có quyền chỉnh sửa
temp_list[3] = 279000            # Sửa giá trị ở vị trí index 3
product_info = tuple(temp_list)  # Đóng gói ngược lại thành Tuple

# In kết quả (giữ nguyên như đề bài yêu cầu)
print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", product_info)