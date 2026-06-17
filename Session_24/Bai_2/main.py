# Hậu quả của việc để thuộc tính public: Việc để points tự do chỉnh sửa sẽ phá vỡ tính toàn vẹn dữ liệu (Data Integrity). 
# Dữ liệu rác (số âm, chuỗi văn bản) lọt vào hệ thống sẽ làm sập (crash) chương trình khi thực hiện các phép toán cộng trừ điểm tiếp theo,
# đồng thời làm sai lệch dữ liệu trong cơ sở dữ liệu.

# Sử dụng Decorator làm "bộ lọc": Khi đã che giấu thành __points, để tạo bộ lọc kiểm tra dữ liệu trước khi gán,
# ta cần sử dụng Decorator @property (để tạo hàm Getter đọc dữ liệu) và Decorator @points.setter (để tạo hàm Setter kiểm duyệt giá trị đầu vào).

# Truyền self bị coi là dư thừa: Hàm is_eligible_for_voucher hoàn toàn không sử dụng bất kỳ dữ liệu nội tại nào của đối tượng thẻ thành viên (không gọi self.thuoc_tinh). 
# Việc ép dùng self là thiết kế tồi vì nó bắt buộc thu ngân phải khởi tạo một chiếc thẻ "ảo" vô nghĩa thì mới dùng được thuật toán kiểm tra chung này.

# Decorator cho hàm độc lập: Ta cần dùng Decorator @staticmethod (Phương thức tĩnh).
# Sự khác biệt cốt lõi: @staticmethod không nhận tham số ngầm định nào (không có self hay cls) và hoạt động như một hàm tiện ích thuần túy. Trong khi đó,
# @classmethod bắt buộc nhận tham số ngầm định cls để thao tác trực tiếp với các thuộc tính cấp độ Class.

class MemberCard:
    def __init__(self, customer_name, points=0):
        """Khởi tạo thẻ thành viên với tên và điểm tích lũy an toàn."""
        self.customer_name = customer_name
        self.__points = 0
        self.points = points

    @property
    def points(self):
        """Trả về điểm tích lũy hiện tại của thẻ."""
        return self.__points

    @points.setter
    def points(self, value):
        """Kiểm duyệt dữ liệu đầu vào trước khi cho phép cập nhật điểm."""
        if type(value) is int and value >= 0:
            self.__points = value
        else:
            print("Dữ liệu điểm không hợp lệ!")

    def add_points(self, amount):
        """Thực hiện logic cộng dồn điểm tích lũy."""
        if type(amount) is int and amount > 0:
            self.points += amount
        else:
            print("Số điểm cộng thêm không hợp lệ!")

    @staticmethod
    def is_eligible_for_voucher(bill_amount):
        """Kiểm tra hóa đơn độc lập, không phụ thuộc vào dữ liệu của bất kỳ thẻ nào."""
        return bill_amount >= 200000


card1 = MemberCard("Le Van C", 100)

card1.points = -50

result = MemberCard.is_eligible_for_voucher(250000)

print(f"Khách hàng: {card1.customer_name} | Điểm hiện tại: {card1.points}")
print(f"Hóa đơn 250k có được tặng Voucher không? {result}")