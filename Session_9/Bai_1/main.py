# Danh sách đơn hàng ban đầu
delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]

# Thêm đơn hàng mới vào cuối danh sách
delivery_orders.append("GE004")

# Chèn đơn hàng hỏa tốc vào đầu danh sách (index 0)
delivery_orders.insert(0, "GE000")

# Sửa mã đơn hàng GE002 thành GE002-UPDATED
#  Sau khi dùng insert, các phần tử cũ bị lùi về sau 1 bước.
# Nên "GE002" bị dời từ index 1 sang index 2.
delivery_orders[2] = "GE002-UPDATED"

# Xóa đơn hàng bị khách hủy
#  Phương thức remove() yêu cầu truyền vào đúng GIÁ TRỊ của phần tử, 
# không phải truyền vào chỉ số (index) như kiểu số 3.
delivery_orders.remove("GE003-CANCEL")

# Lấy đơn hàng cuối cùng ra để bàn giao
#  pop() sẽ lấy và trả về phần tử cuối, nhưng code cũ không có biến để 
# hứng giá trị này. Phải tạo biến transferred_order để lưu lại dùng cho lệnh print.
transferred_order = delivery_orders.pop()

print("Danh sách đơn hàng còn lại:", delivery_orders)
print("Đơn hàng được bàn giao:", transferred_order)