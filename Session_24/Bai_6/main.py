class Drink:
    """Lớp đại diện cho một món đồ uống trong thực đơn."""
    
    def __init__(self, code: str, name: str, price: int):
        self.code = code.strip().upper()
        self.name = name.strip()
        self.__price = price  # Đóng gói thuộc tính giá bán
        self.is_available = True

    @property
    def price(self) -> int:
        """Getter để đọc giá trị của thuộc tính private __price."""
        return self.__price

    def toggle_available(self):
        """Phương thức đảo ngược trạng thái kinh doanh của món đồ uống."""
        self.is_available = not self.is_available
        status_str = "Đang bán" if self.is_available else "Ngừng bán"
        print(f"\nĐã cập nhật trạng thái món {self.code}.")
        print(f"Trạng thái hiện tại: {status_str}")


def main():
    """Hàm điều phối vòng lặp chính của chương trình."""
    # Khởi tạo dữ liệu mẫu (Danh sách chứa các Object Drink)
    menu = [
        Drink("CF01", "Cà phê sữa", 35000),
        Drink("TS01", "Trà sữa matcha", 45000),
        Drink("TD01", "Trà đào cam sả", 40000)
    ]

    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===")
        print("1. Xem danh sách đồ uống")
        print("2. Thêm đồ uống mới")
        print("3. Cập nhật trạng thái kinh doanh")
        print("4. Thoát chương trình")
        print("==============================================")
        
        choice = input("Chọn chức năng (1-4): ").strip()

        if choice == '1':
            print("\n--- DANH SÁCH ĐỒ UỐNG ---")
            if not menu:
                print("Thực đơn hiện đang trống.")
                continue
                
            # Căn lề bảng hiển thị
            print(f"{'Mã món':<8} | {'Tên món':<20} | {'Giá bán':<10} | {'Trạng thái'}")
            print("-" * 60)
            
            for drink in menu:
                status = "Đang bán" if drink.is_available else "Ngừng bán"
                # Gọi drink.price để sử dụng @property
                print(f"{drink.code:<8} | {drink.name:<20} | {drink.price:<10,d} | {status}")

        elif choice == '2':
            print("\n--- THÊM ĐỒ UỐNG MỚI ---")
            code = input("Nhập mã món: ").strip().upper()
            
            # Kiểm tra mã món trùng lặp
            is_duplicate = False
            for drink in menu:
                if drink.code == code:
                    is_duplicate = True
                    break
                    
            if is_duplicate:
                print("Lỗi: Mã món đã tồn tại trong hệ thống!")
                continue

            name = input("Nhập tên món: ").strip()
            
            # Bẫy lỗi nhập giá bán không phải là số
            try:
                price = int(input("Nhập giá bán: "))
                if price <= 0:
                    print("Lỗi: Giá bán không hợp lệ (phải lớn hơn 0)!")
                    continue
            except ValueError:
                print("Lỗi: Giá bán không hợp lệ (vui lòng nhập số nguyên)!")
                continue

            # Khởi tạo Object mới và thêm vào danh sách
            new_drink = Drink(code, name, price)
            menu.append(new_drink)
            print(f"\nThành công: Đã thêm món {name} vào thực đơn!")

        elif choice == '3':
            print("\n--- CẬP NHẬT TRẠNG THÁI KINH DOANH ---")
            code = input("Nhập mã món cần cập nhật: ").strip().upper()
            
            # Tìm kiếm đối tượng và gọi phương thức cập nhật
            found = False
            for drink in menu:
                if drink.code == code:
                    drink.toggle_available()
                    found = True
                    break
                    
            if not found:
                print("Lỗi: Không tìm thấy món có mã này!")

        elif choice == '4':
            print("\nCảm ơn bạn đã sử dụng hệ thống quản lý thực đơn Rikkei Coffee!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")


if __name__ == "__main__":
    main()