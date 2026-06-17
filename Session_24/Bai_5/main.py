"""
===================================================================
TÀI LIỆU THIẾT KẾ LỚP BISTROTABLE
===================================================================
1. Class Attributes (Thuộc tính Lớp):
   - Tên biến: _vat_rate | Ý nghĩa: Tỷ lệ thuế VAT áp dụng chung cho toàn nhà hàng.

2. Instance Attributes (Thuộc tính Đối tượng):
   - Quyền Public: capacity | Ý nghĩa: Sức chứa tối đa của bàn.
   - Quyền Private (Có dấu __): __table_id | Ý nghĩa: Mã định danh của bàn.
   - Quyền Private (Có dấu __): __current_bill | Ý nghĩa: Số tiền tạm tính của bàn.

3. Methods (Các Phương thức):
   - Hàm khởi tạo __init__(self, table_id, capacity): Khởi tạo mã bàn, sức chứa và đặt hóa đơn tạm tính mặc định bằng 0.
   - Getters (Các @property): table_id, current_bill, status, final_total để tính toán động và chỉ cho phép đọc dữ liệu.
   - Instance Methods: order_dish, cancel_dish, checkout | Tương tác cộng trừ tiền và reset hóa đơn.
   - Class Methods: update_vat_rate | Thay đổi tỷ lệ thuế VAT của toàn bộ hệ thống.
   - Static Methods: validate_id | Kiểm tra mã bàn có hợp lệ hay không trước khi xử lý.
===================================================================
"""

class BistroTable:
    _vat_rate = 0.08

    def __init__(self, table_id, capacity):
        """Khởi tạo đối tượng bàn ăn với các thông tin mặc định."""
        self.__table_id = table_id.strip().upper()
        self.capacity = capacity
        self.__current_bill = 0

    @property
    def table_id(self):
        """Đọc mã bàn."""
        return self.__table_id

    @property
    def current_bill(self):
        """Đọc số tiền tạm tính hiện tại."""
        return self.__current_bill

    @property
    def status(self):
        """Tính toán trạng thái bàn ăn dựa trên số tiền tạm tính."""
        if self.__current_bill == 0:
            return "Đang trống"
        return "Có khách"

    @property
    def final_total(self):
        """Tính tổng tiền thanh toán cuối cùng bao gồm thuế VAT."""
        return self.__current_bill * (1 + BistroTable._vat_rate)

    def order_dish(self, amount):
        """Cộng thêm tiền món ăn vào hóa đơn tạm tính."""
        if amount > 0:
            self.__current_bill += amount
            return True
        return False

    def cancel_dish(self, amount):
        """Giảm trừ tiền khỏi hóa đơn nếu đáp ứng đủ điều kiện."""
        if amount <= 0:
            return -1
        if amount > self.__current_bill:
            return 0
        self.__current_bill -= amount
        return 1

    def checkout(self):
        """Thanh toán và đưa bàn về trạng thái trống."""
        self.__current_bill = 0

    @classmethod
    def update_vat_rate(cls, new_rate):
        """Cập nhật thuế suất VAT cho toàn bộ nhà hàng."""
        if 0.0 <= new_rate <= 0.2:
            cls._vat_rate = new_rate
            return True
        return False

    @staticmethod
    def validate_id(table_id):
        """Kiểm tra tính hợp lệ của mã bàn nhập vào."""
        clean_id = table_id.strip().upper()
        if clean_id.startswith("TB") and len(clean_id) >= 3:
            return True
        return False


def find_table(table_records, table_id):
    """Tìm kiếm đối tượng bàn ăn dựa trên mã bàn."""
    clean_id = table_id.strip().upper()
    for table in table_records:
        if table.table_id == clean_id:
            return table
    return None


def main():
    """Hàm điều phối vòng lặp chức năng chính của chương trình."""
    table_records = [
        BistroTable("TB01", 4),
        BistroTable("TB02", 2),
        BistroTable("TB03", 8)
    ]

    while True:
        print("\n===== HỆ THỐNG ĐIỀU PHỐI BÀN ĂN - RIKKEI BISTRO =====")
        print("1. Hiển thị sơ đồ & Trạng thái bàn ăn")
        print("2. Gọi món mới (Tăng tiền hóa đơn)")
        print("3. Hủy món / Giảm trừ hóa đơn (Sự cố nhà bếp)")
        print("4. Cập nhật thuế suất VAT toàn nhà hàng")
        print("5. Thanh toán hóa đơn & Trả bàn trống")
        print("6. Thoát chương trình")
        print("=====================================================")
        choice = input("Chọn chức năng (1-6): ").strip()

        if choice == "1":
            print("\n--- SƠ ĐỒ BÀN ĂN RIKKEI BISTRO ---")
            for idx, table in enumerate(table_records, 1):
                print(f"{idx}. Mã bàn: {table.table_id} | Sức chứa: {table.capacity} người | Tạm tính: {table.current_bill:,}đ | Trạng thái: {table.status}")
            print("----------------------------------")

        elif choice == "2":
            print("\n--- GỌI MÓN MỚI ---")
            table_id = input("Nhập mã bàn gọi món: ")
            
            if not BistroTable.validate_id(table_id):
                print("Mã bàn không hợp lệ!")
                continue

            table = find_table(table_records, table_id)
            if not table:
                print("Không tìm thấy mã bàn này trong hệ thống!")
                continue

            try:
                amount = int(input("Nhập giá tiền món ăn mới: "))
                if table.order_dish(amount):
                    print(f">> Thành công: Đã ghi nhận món ăn {amount:,}đ vào Bàn '{table.table_id}'.")
                    print(f">> Số tiền tạm tính hiện tại của bàn: {table.current_bill:,}đ.")
                else:
                    print("Vui lòng nhập số tiền là một số nguyên dương!")
            except ValueError:
                print("Vui lòng nhập số tiền là một số nguyên dương!")

        elif choice == "3":
            print("\n--- HỦY MÓN / GIẢM TRỪ HÓA ĐƠN ---")
            table_id = input("Nhập mã bàn cần hủy món: ")
            
            if not BistroTable.validate_id(table_id):
                print("Mã bàn không hợp lệ!")
                continue

            table = find_table(table_records, table_id)
            if not table:
                print("Không tìm thấy mã bàn này trong hệ thống!")
                continue

            try:
                amount = int(input("Nhập giá trị món muốn giảm trừ: "))
                result = table.cancel_dish(amount)
                
                if result == -1:
                    print("Vui lòng nhập số tiền là một số nguyên dương!")
                elif result == 0:
                    print("Lỗi: Số tiền giảm trừ vượt quá giá trị hóa đơn hiện tại!")
                else:
                    print(f">> Thành công: Đã giảm trừ {amount:,}đ khỏi Bàn '{table.table_id}' do sự cố bếp.")
                    print(f">> Số tiền tạm tính còn lại: {table.current_bill:,}đ.")
                    if table.current_bill == 0:
                        print(f">> Bàn '{table.table_id}' hiện đã chuyển về trạng thái Đang trống.")
            except ValueError:
                print("Vui lòng nhập số tiền là một số nguyên dương!")

        elif choice == "4":
            print("\n--- CẬP NHẬT THUẾ SUẤT VAT TOÀN NHÀ HÀNG ---")
            print(f"[HỆ THỐNG] Thuế suất VAT hiện tại là: {BistroTable._vat_rate * 100:.0f}% ({BistroTable._vat_rate})")
            
            try:
                new_rate = float(input("Nhập thuế suất VAT mới (ví dụ: 0.1 cho 10%): "))
                if BistroTable.update_vat_rate(new_rate):
                    print(f">> Thông báo: Rikkei Bistro cập nhật thuế suất VAT mới ở mức {new_rate * 100:.0f}% thành công!")
                else:
                    print("Tỷ lệ thuế không hợp lệ! Vui lòng nhập từ 0.0 đến 0.2.")
            except ValueError:
                print("Tỷ lệ thuế không hợp lệ!")

        elif choice == "5":
            print("\n--- THANH TOÁN HÓA ĐƠN ---")
            table_id = input("Nhập mã bàn thanh toán: ")
            
            if not BistroTable.validate_id(table_id):
                print("Mã bàn không hợp lệ!")
                continue

            table = find_table(table_records, table_id)
            if not table:
                print("Không tìm thấy mã bàn này trong hệ thống!")
                continue

            if table.current_bill == 0:
                print("Lỗi: Bàn này hiện đang trống, không có hóa đơn để thanh toán!")
                continue

            print(f"\n--- HÓA ĐƠN THANH TOÁN BÀN {table.table_id} ---")
            print(f"Số tiền món ăn: {table.current_bill:,}đ")
            print(f"Thuế suất VAT áp dụng: {BistroTable._vat_rate * 100:.0f}%")
            print(f"Tổng tiền cần thanh toán (gồm thuế): {table.final_total:,.0f}đ")
            print("-----------------------------------")
            
            table.checkout()
            print(f">> Thanh toán thành công! Bàn '{table.table_id}' đã được dọn sạch và chuyển sang trạng thái Đang trống.")

        elif choice == "6":
            print("Cảm ơn bạn đã sử dụng hệ thống điều phối bàn ăn Rikkei Bistro!")
            break

        else:
            print("Chức năng không hợp lệ, vui lòng chọn từ 1 đến 6.")


if __name__ == "__main__":
    main()