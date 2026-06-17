# Lý do point_value_vnd là Class Attribute: là một chính sách quy định chung áp dụng cho toàn bộ chuỗi cửa hàng. 
# Nếu đặt nó làm Instance Attribute (khai báo trong __init__), khi Ban giám đốc muốn thay đổi tỷ giá (Chức năng 5), 
# hệ thống sẽ phải chạy vòng lặp cập nhật từng chiếc thẻ một, gây lãng phí tài nguyên và dễ dẫn đến sai sót dữ liệu. 
# Khai báo ở cấp độ Class giúp mọi đối tượng thẻ tự động tham chiếu đến cùng một giá trị duy nhất.

# Lý do dùng @staticmethod cho is_valid_card_id: kiểm tra định dạng mã thẻ là bước cần thiết phải làm trước khi quyết định có tạo ra thẻ mới hay không.
# Nếu không dùng @staticmethod, thu ngân bắt buộc phải khởi tạo thẻ thành công rồi mới kiểm tra xem thẻ đó có hợp lệ không (điều này rất phi logic).
# Phương thức tĩnh cho phép sử dụng chức năng kiểm duyệt trực tiếp từ tên Lớp mà không cần bận tâm đến Đối tượng.

# Giải quyết việc áp dụng Name Mangling che giấu biến __points giúp khóa chặt quyền can thiệp trực tiếp từ bên ngoài (ví dụ gán card.points = 1000). 
# Mọi thay đổi về điểm số bắt buộc phải đi qua các hàm nghiệp vụ hợp lệ là earn_points (tích điểm) và redeem_points (tiêu điểm). Kết hợp với việc chỉ cung cấp @property để đọc mà không viết hàm Setter,
# điểm số của khách hàng được bảo vệ tuyệt đối.


class MemberCard:
    point_value_vnd = 1000

    def __init__(self, card_id, name):
        """Khởi tạo thẻ thành viên với các thuộc tính mặc định và đóng gói dữ liệu điểm, hạng thẻ."""
        self.card_id = card_id.upper()
        self.name = name.title()
        self.__points = 0
        self.__tier = "Standard"

    @property
    def points(self):
        """Lấy thông tin điểm tích lũy hiện tại (Chỉ đọc)."""
        return self.__points

    @property
    def tier(self):
        """Lấy thông tin hạng thẻ hiện tại (Chỉ đọc)."""
        return self.__tier

    @staticmethod
    def is_valid_card_id(card_id):
        """Kiểm tra mã thẻ có đúng định dạng bắt đầu bằng 'RC' và theo sau là 2 chữ số hay không."""
        if len(card_id) == 4 and card_id.startswith("RC") and card_id[2:].isdigit():
            return True
        return False

    @classmethod
    def update_point_value(cls, new_value):
        """Cập nhật tỷ giá quy đổi điểm cho toàn bộ hệ thống thẻ."""
        if new_value > 0:
            cls.point_value_vnd = new_value

    def earn_points(self, bill_amount):
        """Tính toán điểm thưởng từ hóa đơn, cộng dồn vào thẻ và tự động thăng hạng nếu đủ điều kiện."""
        points_earned = int(bill_amount / 10000)
        self.__points += points_earned

        print(f"\nKhách hàng: {self.name}")
        print(f"Hóa đơn: {bill_amount:,} VNĐ")
        print(f"Số điểm được tích: {points_earned}")
        print(f"Tổng điểm hiện tại: {self.__points}")

        if self.__points >= 100 and self.__tier == "Standard":
            self.__tier = "VIP"
            print("\nChúc mừng! Khách hàng đã được nâng hạng lên VIP.")
        
        print(f"Hạng thẻ hiện tại: {self.__tier}")

    def redeem_points(self, points_to_use):
        """Kiểm tra số dư điểm, thực hiện trừ điểm và quy đổi ra số tiền giảm giá."""
        if points_to_use <= 0 or points_to_use > self.__points:
            print("\nKhông thể đổi điểm!")
            print("Số điểm muốn sử dụng vượt quá số điểm hiện có.")
            print(f"Điểm hiện tại của khách: {self.__points}")
            print(f"Số điểm sau giao dịch: {self.__points}")
            return

        self.__points -= points_to_use
        discount_amount = points_to_use * MemberCard.point_value_vnd

        print(f"\nĐã trừ {points_to_use} điểm.")
        print(f"Khách hàng được giảm giá {discount_amount:,} VNĐ vào hóa đơn!")
        print(f"Số điểm còn lại: {self.__points}")
        print(f"Hạng thẻ hiện tại: {self.__tier}")


def get_card_by_id(database, card_id):
    """Hàm phụ trợ giúp tìm kiếm đối tượng thẻ trong cơ sở dữ liệu dựa trên mã thẻ."""
    for card in database:
        if card.card_id == card_id.upper():
            return card
    return None


def main():
    """Hệ thống menu điều hướng và xử lý luồng hoạt động chính của phần mềm."""
    cards_database = []

    mock_card_1 = MemberCard("RC01", "Nguyen Van A")
    mock_card_1._MemberCard__points = 150
    mock_card_1._MemberCard__tier = "VIP"
    
    mock_card_2 = MemberCard("RC02", "Tran Thi B")
    mock_card_2._MemberCard__points = 20
    
    cards_database.extend([mock_card_1, mock_card_2])

    while True:
        print("\n===== HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE =====")
        print("1. Xem danh sách thẻ thành viên")
        print("2. Đăng ký thẻ mới")
        print("3. Khách mua hàng (Tích điểm)")
        print("4. Khách dùng điểm (Đổi ưu đãi)")
        print("5. Cập nhật tỷ giá quy đổi điểm (Hệ thống)")
        print("6. Thoát chương trình")
        print("======================================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()

        if choice == "1":
            print("\n--- DANH SÁCH THẺ THÀNH VIÊN ---")
            for idx, card in enumerate(cards_database, 1):
                print(f"{idx}. Mã: {card.card_id} | Tên: {card.name:<15} | Điểm: {card.points:<3} | Hạng: {card.tier}")

        elif choice == "2":
            print("\n--- ĐĂNG KÝ THẺ THÀNH VIÊN MỚI ---")
            card_id = input("Nhập mã thẻ: ").strip().upper()
            
            if not MemberCard.is_valid_card_id(card_id):
                print("Mã thẻ không hợp lệ! Vui lòng nhập đúng định dạng (VD: RC01, RC99).")
                continue
                
            if get_card_by_id(cards_database, card_id):
                print("Mã thẻ đã tồn tại trong hệ thống!\nVui lòng kiểm tra lại.")
                continue

            name = input("Nhập tên khách hàng: ").strip()
            new_card = MemberCard(card_id, name)
            cards_database.append(new_card)
            
            print("\nĐăng ký thẻ thành viên thành công!")
            print(f"Mã thẻ: {new_card.card_id}")
            print(f"Tên khách hàng: {new_card.name}")
            print(f"Điểm ban đầu: {new_card.points}")
            print(f"Hạng thẻ: {new_card.tier}")

        elif choice == "3":
            print("\n--- KHÁCH MUA HÀNG - TÍCH ĐIỂM ---")
            card_id = input("Nhập mã thẻ: ").strip().upper()
            card = get_card_by_id(cards_database, card_id)
            
            if card:
                try:
                    bill_amount = int(input("Nhập tổng tiền hóa đơn: "))
                    if bill_amount > 0:
                        card.earn_points(bill_amount)
                    else:
                        print("Số tiền hóa đơn không hợp lệ.")
                except ValueError:
                    print("Vui lòng nhập số tiền là một số nguyên.")
            else:
                print("Không tìm thấy mã thẻ trong hệ thống.")

        elif choice == "4":
            print("\n--- KHÁCH DÙNG ĐIỂM - ĐỔI ƯU ĐÃI ---")
            print(f"Tỷ giá hiện tại: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")
            card_id = input("Nhập mã thẻ: ").strip().upper()
            card = get_card_by_id(cards_database, card_id)
            
            if card:
                try:
                    points_to_use = int(input("Nhập số điểm muốn sử dụng: "))
                    card.redeem_points(points_to_use)
                except ValueError:
                    print("Vui lòng nhập số điểm là một số nguyên.")
            else:
                print("Không tìm thấy mã thẻ trong hệ thống.")

        elif choice == "5":
            print("\n--- CẬP NHẬT TỶ GIÁ QUY ĐỔI ĐIỂM ---")
            print(f"Tỷ giá hiện tại: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")
            try:
                new_rate = int(input("Nhập tỷ giá mới cho 1 điểm: "))
                MemberCard.update_point_value(new_rate)
                print("\nCập nhật tỷ giá thành công!")
                print(f"Tỷ giá mới: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")
            except ValueError:
                print("Vui lòng nhập số tiền là một số nguyên.")

        elif choice == "6":
            print("\nCảm ơn bạn đã sử dụng hệ thống thẻ thành viên Rikkei Coffee!")
            break
            
        else:
            print("Chức năng không hợp lệ, vui lòng chọn từ 1 đến 6.")


if __name__ == "__main__":
    main()