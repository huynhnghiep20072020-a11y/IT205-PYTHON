# Tên Class: MenuItem

# Class Attributes (Thuộc tính Lớp):

# service_charge: Lưu trữ mức phụ phí dịch vụ chung (kiểu float, mặc định 0.0). Dùng chung cho toàn bộ các đối tượng đồ uống được khởi tạo.

# Instance Attributes (Thuộc tính Đối tượng):

# item_id: Mã đồ uống (Public).

# item_name: Tên đồ uống (Public).

# __base_price: Giá gốc (Private - che giấu bằng Name Mangling).

# __is_available: Trạng thái bán hàng (Private - che giấu bằng Name Mangling).

# Methods (Các Phương thức):

# __init__(self, item_id, item_name, base_price): Khởi tạo thông tin món. Thuộc tính __is_available mặc định được gán là True.

# Getters/Setters:

# @property base_price: Đọc giá trị __base_price.

# @base_price.setter: Kiểm tra dữ liệu đầu vào. Nếu giá trị > 0 mới cho phép gán vào __base_price, ngược lại từ chối cập nhật.

# @property is_available: Đọc trạng thái __is_available.

# Instance Methods:

# toggle_availability(self): Đảo ngược giá trị boolean của __is_available và in ra thông báo trạng thái mới.

# calculate_selling_price(self): Tính toán giá bán cuối cùng dựa trên __base_price và biến class service_charge.

# Class Methods:

# @classmethod update_service_charge(cls, new_rate): Nhận tham số cls để cập nhật biến service_charge của hệ thống.

# Static Methods:

# @staticmethod is_valid_item_id(item_code): Nhận chuỗi kiểm tra độc lập, trả về True nếu đúng định dạng 2 chữ cái in hoa + 2 chữ số.

class MenuItem:
    service_charge = 0.0

    def __init__(self, item_id, item_name, base_price):
        """Khởi tạo đối tượng đồ uống với dữ liệu được đóng gói an toàn."""
        self.item_id = item_id.upper()
        self.item_name = item_name.title()
        self.__base_price = 0
        self.base_price = base_price
        self.__is_available = True

    @property
    def base_price(self):
        """Lấy thông tin giá gốc của đồ uống."""
        return self.__base_price

    @base_price.setter
    def base_price(self, value):
        """Kiểm duyệt giá trị trước khi cho phép cập nhật giá gốc."""
        if type(value) is int and value > 0:
            self.__base_price = value
        else:
            print("Giá đồ uống phải lớn hơn 0!\nGiá cũ được giữ nguyên.")

    @property
    def is_available(self):
        """Lấy thông tin trạng thái kinh doanh của đồ uống."""
        return self.__is_available

    def toggle_availability(self):
        """Đảo ngược trạng thái bán hàng và hiển thị kết quả."""
        self.__is_available = not self.__is_available
        status_text = "ĐANG BÁN" if self.__is_available else "HẾT HÀNG"
        print(f">> Đã cập nhật {self.item_name} thành {status_text}!")

    def calculate_selling_price(self):
        """Tính toán giá niêm yết dựa trên giá gốc và phụ phí toàn hệ thống."""
        return self.__base_price + (self.__base_price * MenuItem.service_charge)

    @classmethod
    def update_service_charge(cls, new_rate):
        """Cập nhật tỷ lệ phụ phí dịch vụ chung cho toàn bộ thực đơn."""
        if new_rate >= 0:
            cls.service_charge = new_rate

    @staticmethod
    def is_valid_item_id(item_code):
        """Kiểm tra định dạng mã món độc lập không phụ thuộc đối tượng."""
        if len(item_code) == 4:
            if item_code[:2].isalpha() and item_code[:2].isupper():
                if item_code[2:].isdigit():
                    return True
        return False


def get_item_by_id(menu_db, item_id):
    """Hàm phụ trợ tìm kiếm đối tượng đồ uống trong cơ sở dữ liệu."""
    for item in menu_db:
        if item.item_id == item_id.upper():
            return item
    return None


def main():
    """Hệ thống menu điều hướng vòng lặp chính của phần mềm."""
    menu_db = [
        MenuItem("CF01", "Cà Phê Đen", 30000),
        MenuItem("CF02", "Bạc Xỉu", 45000),
        MenuItem("TE01", "Trà Đào Cam Sả", 50000)
    ]

    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE =====")
        print("1. Xem thực đơn & Giá niêm yết")
        print("2. Thêm món mới vào menu")
        print("3. Cập nhật trạng thái (Hết hàng/Còn hàng)")
        print("4. Điều chỉnh giá gốc của món")
        print("5. Cập nhật phụ phí dịch vụ toàn hệ thống")
        print("6. Thoát chương trình")
        print("======================================================")

        choice = input("Chọn chức năng (1-6): ").strip()

        if choice == "1":
            print("\n--- THỰC ĐƠN RIKKEI COFFEE ---")
            for idx, item in enumerate(menu_db, 1):
                status = "Đang bán" if item.is_available else "Hết hàng"
                selling_price = item.calculate_selling_price()
                print(f"{idx}. Mã: {item.item_id} | Tên: {item.item_name:<15} | Trạng thái: {status:<10} | Giá niêm yết: {selling_price:,.0f} VNĐ")

        elif choice == "2":
            print("\n--- THÊM MÓN MỚI VÀO MENU ---")
            item_id = input("Nhập mã món: ").strip().upper()

            if not MenuItem.is_valid_item_id(item_id):
                print("Mã món không hợp lệ!\nMã món phải gồm 2 chữ cái in hoa và 2 chữ số. Ví dụ: CF01.")
                continue

            if get_item_by_id(menu_db, item_id) is not None:
                print("Mã món đã tồn tại trong hệ thống!")
                continue

            item_name = input("Nhập tên món: ").strip()
            
            try:
                base_price = int(input("Nhập giá gốc: "))
                if base_price > 0:
                    new_item = MenuItem(item_id, item_name, base_price)
                    menu_db.append(new_item)
                    print("Thêm món mới thành công!")
                else:
                    print("Giá đồ uống phải lớn hơn 0!")
            except ValueError:
                print("Vui lòng nhập giá trị là một số nguyên.")

        elif choice == "3":
            print("\n--- CẬP NHẬT TRẠNG THÁI MÓN ---")
            item_id = input("Nhập mã món cần cập nhật: ").strip().upper()
            item = get_item_by_id(menu_db, item_id)
            
            if item:
                item.toggle_availability()
            else:
                print("Không tìm thấy mã món trong hệ thống.")

        elif choice == "4":
            print("\n--- ĐIỀU CHỈNH GIÁ GỐC CỦA MÓN ---")
            item_id = input("Nhập mã món cần đổi giá: ").strip().upper()
            item = get_item_by_id(menu_db, item_id)
            
            if item:
                try:
                    new_price = int(input("Nhập giá tiền mới: "))
                    if new_price > 0:
                        item.base_price = new_price
                        print("Cập nhật giá gốc thành công!")
                    else:
                        item.base_price = new_price
                except ValueError:
                    print("Vui lòng nhập giá trị là một số nguyên.")
            else:
                print("Không tìm thấy mã món trong hệ thống.")

        elif choice == "5":
            print("\n--- CẬP NHẬT PHỤ PHÍ DỊCH VỤ TOÀN HỆ THỐNG ---")
            print(f"Phụ phí hiện tại: {MenuItem.service_charge * 100:.0f}%")
            try:
                new_rate = float(input("Nhập phụ phí mới. Ví dụ 0.1 tương ứng 10%: "))
                MenuItem.update_service_charge(new_rate)
                print("Cập nhật phụ phí dịch vụ thành công!")
            except ValueError:
                print("Vui lòng nhập tỷ lệ là một số hợp lệ.")

        elif choice == "6":
            print("Cảm ơn bạn đã sử dụng hệ thống Rikkei Coffee!")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 6.")


if __name__ == "__main__":
    main()