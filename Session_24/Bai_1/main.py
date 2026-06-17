# Việc gán order_table1.total_amount = 0 từ bên ngoài vi phạm nghiêm trọng Tính Đóng gói (Encapsulation) của Lập trình Hướng đối tượng.
# Dữ liệu bên trong class bị phơi bày và sửa đổi tự do mà không qua hàm kiểm duyệt.

#  Để che giấu thuộc tính, ta cần thêm hai dấu gạch dưới vào trước tên biến, đổi thành __total_amount.
#  Việc này kích hoạt Name Mangling, báo hiệu đây là một biến riêng tư (Private) và Python sẽ tự động làm xáo trộn tên của nó để ngăn các đoạn code bên ngoài gọi thẳng.

#  Ta sử dụng Decorator @property gắn lên một hàm (ví dụ tên là total_amount()). Cách này tạo ra một "Getter", biến hàm đó hoạt động giống như một thuộc tính chỉ đọc. 
#  Bên ngoài có thể lấy ra xem tổng tiền một cách bình thường nhưng hễ cố tình gán (ví dụ = 0) thì chương trình sẽ báo lỗi.

# Bản chất lệnh self.vat_rate = new_rate: Khi chạy lệnh này, Python không hề đi tìm biến Class vat_rate để sửa. 
#  nó tạo ra một biến đối tượng (Instance Variable) cục bộ hoàn toàn mới cũng có tên là vat_rate và gắn riêng cho cái bàn đó. Các bàn khác vẫn sẽ xài biến Class gốc.

# Cần dùng Decorator @classmethod đặt trước tên hàm. Đồng thời, thay tham số self (đại diện cho một bàn cụ thể) bằng cls (đại diện cho cả cái khuôn mẫu lớp CoffeeOrder).
# lệnh cls.vat_rate = new_rate mới thực sự cập nhật biến Class, giúp toàn bộ các bàn đồng loạt đổi thuế.

class CoffeeOrder:
    vat_rate = 0.10  

    def __init__(self, table_number):
        self.table_number = table_number
        self.__total_amount = 0  

    @property
    def total_amount(self):
        """Cho phép hệ thống xem tổng số tiền hóa đơn an toàn (Chỉ đọc)."""
        return self.__total_amount

    def add_item(self, price):
        """Cộng dồn tiền vào hóa đơn nếu giá trị món ăn hợp lệ."""
        if price > 0:
            self.__total_amount += price

    def calculate_final_bill(self):
        """Tính tổng tiền khách phải trả, bao gồm cả thuế VAT hiện tại."""
        return self.__total_amount + (self.__total_amount * CoffeeOrder.vat_rate)

    @classmethod
    def update_vat_rate(cls, new_rate):
        """Cập nhật chính sách thuế VAT áp dụng đồng loạt cho toàn bộ hệ thống quán."""
        cls.vat_rate = new_rate


order_table1 = CoffeeOrder("Bàn 1")
order_table2 = CoffeeOrder("Bàn 2")

order_table1.add_item(50000)
order_table2.add_item(30000)

try:
    order_table1.total_amount = 0
except AttributeError as e:
    print(f"Hệ thống bảo mật kích hoạt! Lỗi chặn gán dữ liệu: {e}")

CoffeeOrder.update_vat_rate(0.08)

print("\n--- BÁO CÁO HỆ THỐNG RIKKEI COFFEE ---")
print(f"Tiền hóa đơn gốc của Bàn 1: {order_table1.total_amount:,.0f} VNĐ")
print(f"Tổng tiền khách Bàn 1 cần thanh toán (Sau thuế): {order_table1.calculate_final_bill():,.0f} VNĐ")
print(f"Thuế VAT đang áp dụng cho Bàn 1: {order_table1.vat_rate}")
print(f"Thuế VAT đang áp dụng cho Bàn 2: {order_table2.vat_rate}")