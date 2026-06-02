# Danh sách đơn hàng ban đầu
express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]

# 1. Thêm đơn hàng mới vào cuối danh sách
express_orders.append("GE104")

# 2. Chèn đơn hàng hỏa tốc vào đầu danh sách (vị trí 0)
express_orders.insert(0, "GE100-FAST")

# 3. Sửa mã đơn hàng bị nhập sai
# GIẢI THÍCH 1: Do lệnh insert ở trên chèn thêm vào đầu, "GE102-WRONG" đã bị đẩy lùi từ vị trí [1] sang vị trí [2].
express_orders[2] = "GE102-UPDATED"

# 4. Xóa đơn hàng bị khách hủy
# GIẢI THÍCH 2: Dùng lệnh remove() truyền đúng giá trị chuỗi sẽ an toàn và chính xác hơn là đoán vị trí index để dùng pop(3).
express_orders.remove("GE103-CANCEL")

# 5. Lấy đơn hàng đầu tiên ra để bắt đầu giao
# GIẢI THÍCH 3: pop() mặc định sẽ lấy phần tử CUỐI CÙNG, muốn lấy phần tử ĐẦU TIÊN ra khỏi danh sách thì phải dùng pop(0).
current_order = express_orders.pop(0)

# In kết quả
print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)