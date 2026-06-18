# Lớp Equipment đóng vai trò là một "Bản hợp đồng" (Contract) cho toàn bộ hệ thống trang bị.
# Bằng việc sử dụng @abstractmethod cho hàm calculate_total_damage, hệ thống ép buộc mọi lớp con (như Weapon,
# MagicSword hay sau này là Bow, Staff) phải tự định nghĩa công thức tính sát thương của riêng mình. Nếu một lập trình viên "hậu bối" tạo ra lớp Bow nhưng quên viết hàm này,
# chương trình sẽ báo lỗi ngay từ lúc khởi tạo đối tượng thay vì đợi đến lúc chạy tính toán mới bị sập (Nguyên lý Fail Fast).

# Multiple Inheritance (Đa kế thừa) & MRO:
# Lớp MagicSword đa kế thừa từ Weapon và MagicMixin. 
# Theo thứ tự phân giải phương thức (MRO - Method Resolution Order) từ trái sang phải,
# Python sẽ ưu tiên tìm các thuộc tính và phương thức trong Weapon trước, sau đó mới đến MagicMixin.
# Để tránh lỗi xung đột tham số khi dùng super(), cách an toàn và dễ hiểu nhất là gọi đích danh hàm khởi tạo của từng lớp cha bên trong __init__ của MagicSword
# (Ví dụ: Weapon.__init__(...) và MagicMixin.__init__(...)).

# Tính Đa hình (Polymorphism) ở Chức năng 1:
# Trong vòng lặp duyệt kho đồ, hệ thống gọi item.calculate_total_damage().
# Nhờ tính Đa hình và Duck Typing, vòng lặp không cần dùng các câu lệnh if/else để kiểm tra xem item đang là Weapon thường hay MagicSword.
# Mỗi đối tượng sẽ tự động "biết" cách áp dụng đúng công thức sát thương của hệ phái mình.

# Nạp chồng toán tử (Operator Overloading):
# Hàm __add__(self, other) nhận vào 2 tham số là chính nó (self) và vũ khí bị đem đi dung hợp (other). 
# Hàm này sẽ kiểm tra xem other có phải là một trang bị hay không. Nếu đúng, nó cộng dồn sát thương cơ bản và cấp cường hóa,
# ghép tên lại và return về một đối tượng Weapon hoàn toàn mới.



from abc import ABC, abstractmethod

class Equipment(ABC):
    """Lớp cơ sở trừu tượng làm khuôn mẫu cho mọi trang bị trong game."""

    @abstractmethod
    def calculate_total_damage(self):
        """Phương thức trừu tượng ép buộc mọi vũ khí phải tự định nghĩa công thức tính sát thương."""
        pass


class Weapon(Equipment):
    """Lớp đại diện cho các vũ khí vật lý thông thường."""

    def __init__(self, name, base_damage, upgrade_level=0):
        self.name = name.title()
        self.base_damage = base_damage
        self.upgrade_level = upgrade_level

    def calculate_total_damage(self):
        """Tính toán tổng sát thương cho vũ khí vật lý."""
        return self.base_damage + (self.upgrade_level * 10)

    def __gt__(self, other):
        """Nạp chồng toán tử (>) để so sánh sát thương tổng giữa 2 trang bị."""
        if not isinstance(other, Equipment):
            raise TypeError("Chỉ có thể dung hợp/so sánh giữa các trang bị!")
        return self.calculate_total_damage() > other.calculate_total_damage()

    def __add__(self, other):
        """Nạp chồng toán tử (+) để dung hợp 2 trang bị thành một vũ khí mới."""
        if not isinstance(other, Equipment):
            raise TypeError("Chỉ có thể dung hợp/so sánh giữa các trang bị!")
        
        new_name = f"Fusion({self.name} + {other.name})"
        new_base_damage = self.base_damage + other.base_damage
        new_upgrade_level = self.upgrade_level + other.upgrade_level
        
        return Weapon(new_name, new_base_damage, new_upgrade_level)


class MagicMixin:
    """Lớp hỗ trợ (Mixin) cung cấp sức mạnh phép thuật."""

    def __init__(self, magic_power):
        self.magic_power = magic_power

    def cast_glow(self):
        """Tạo hiệu ứng phát sáng cho vũ khí mang sức mạnh phép thuật."""
        print(f"Vũ khí đang tỏa ra ánh sáng ma thuật với sức mạnh {self.magic_power}!")


class MagicSword(Weapon, MagicMixin):
    """Lớp đại diện cho thanh kiếm mang sức mạnh ma thuật, sử dụng đa kế thừa."""

    def __init__(self, name, base_damage, upgrade_level, magic_power):
        Weapon.__init__(self, name, base_damage, upgrade_level)
        MagicMixin.__init__(self, magic_power)

    def calculate_total_damage(self):
        """Tính toán tổng sát thương kết hợp cả vật lý và phép thuật."""
        return self.base_damage + (self.upgrade_level * 10) + self.magic_power


def main():
    """Hàm điều phối luồng chạy chính và giao diện Menu tương tác."""
    inventory = []

    while True:
        print("\n===== LÒ RÈN VŨ KHÍ RIKKEI STUDIOS ===================")
        print("1. Xem kho vũ khí & Sát thương tổng")
        print("2. Rèn Vũ khí Vật lý (Tạo Weapon)")
        print("3. Rèn Kiếm Ma Thuật (Tạo MagicSword)")
        print("4. Thẩm định vũ khí (So sánh lớn hơn)")
        print("5. Dung hợp vũ khí (Cộng dồn cấp độ)")
        print("6. Thoát game")
        print("======================================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()

        if choice == "1":
            print("\n--- KHO VŨ KHÍ CỦA NGƯỜI CHƠI ---")
            if not inventory:
                print("Kho vũ khí hiện đang trống.")
                print("Vui lòng rèn vũ khí bằng Chức năng 2 hoặc Chức năng 3.")
            else:
                print(f"{'STT':<5} | {'Tên vũ khí':<25} | {'Loại':<12} | {'Cấp':<5} | {'Sát thương tổng'}")
                print("-" * 80)
                for index, item in enumerate(inventory, 1):
                    item_type = "MagicSword" if isinstance(item, MagicSword) else "Weapon"
                    total_dmg = item.calculate_total_damage()
                    print(f"{index:<5} | {item.name:<25} | {item_type:<12} | {item.upgrade_level:<5} | {total_dmg}")

        elif choice == "2":
            print("\n--- RÈN VŨ KHÍ VẬT LÝ ---")
            name = input("Nhập tên vũ khí: ").strip()
            
            try:
                base_damage = int(input("Nhập sát thương gốc: "))
                if base_damage <= 0:
                    print("Giá trị phải lớn hơn 0!")
                    continue
                    
                upgrade_level = int(input("Nhập cấp cường hóa: "))
                if upgrade_level <= 0:
                    print("Giá trị phải lớn hơn 0!")
                    continue
                
                new_weapon = Weapon(name, base_damage, upgrade_level)
                inventory.append(new_weapon)
                
                print("\n>> Rèn vũ khí vật lý thành công!")
                print(f"Tên vũ khí: {new_weapon.name}")
                print("Loại: Weapon")
                print(f"Cấp cường hóa: {new_weapon.upgrade_level}")
                print(f"Sát thương tổng: {new_weapon.calculate_total_damage()}")
            except ValueError:
                print("Lỗi: Dữ liệu nhập vào phải là số!")

        elif choice == "3":
            print("\n--- RÈN KIẾM MA THUẬT ---")
            name = input("Nhập tên kiếm ma thuật: ").strip()
            
            try:
                base_damage = int(input("Nhập sát thương gốc: "))
                if base_damage <= 0:
                    print("Giá trị phải lớn hơn 0!")
                    continue
                    
                upgrade_level = int(input("Nhập cấp cường hóa: "))
                if upgrade_level <= 0:
                    print("Giá trị phải lớn hơn 0!")
                    continue
                    
                magic_power = int(input("Nhập sức mạnh phép thuật: "))
                if magic_power <= 0:
                    print("Giá trị phải lớn hơn 0!")
                    continue
                
                new_magic_sword = MagicSword(name, base_damage, upgrade_level, magic_power)
                inventory.append(new_magic_sword)
                
                print("\n>> Rèn kiếm ma thuật thành công!")
                print(f"Tên vũ khí: {new_magic_sword.name}")
                print("Loại: MagicSword")
                print(f"Cấp cường hóa: {new_magic_sword.upgrade_level}")
                print(f"Sát thương gốc: {new_magic_sword.base_damage}")
                print(f"Sức mạnh phép thuật: {new_magic_sword.magic_power}")
                print(f"Sát thương tổng: {new_magic_sword.calculate_total_damage()}")
            except ValueError:
                print("Lỗi: Dữ liệu nhập vào phải là số!")

        elif choice == "4":
            print("\n--- THẨM ĐỊNH VŨ KHÍ ---")
            if len(inventory) < 2:
                print("Cần ít nhất 2 vũ khí trong kho để thẩm định!")
                continue
                
            w1 = inventory[0]
            w2 = inventory[1]
            
            t1 = "MagicSword" if isinstance(w1, MagicSword) else "Weapon"
            t2 = "MagicSword" if isinstance(w2, MagicSword) else "Weapon"
            
            print("Vũ khí thứ nhất:")
            print(f"{w1.name} | Loại: {t1} | Sát thương: {w1.calculate_total_damage()}\n")
            print("Vũ khí thứ hai:")
            print(f"{w2.name} | Loại: {t2} | Sát thương: {w2.calculate_total_damage()}\n")
            
            try:
                if w1 > w2:
                    print(f"Kết quả: {w1.name} mạnh hơn {w2.name}.")
                elif w2 > w1:
                    print(f"Kết quả: {w2.name} mạnh hơn {w1.name}.")
                else:
                    print("Kết quả: Hai vũ khí có sức mạnh ngang nhau.")
            except TypeError as e:
                print(f"Lỗi hệ thống thẩm định: {e}")

        elif choice == "5":
            print("\n--- DUNG HỢP VŨ KHÍ ---")
            if len(inventory) < 2:
                print("Cần ít nhất 2 vũ khí trong kho để dung hợp!")
                continue
                
            print("Đang dung hợp 2 vũ khí đầu tiên trong kho...\n")
            w1 = inventory[0]
            w2 = inventory[1]
            
            print(f"Vũ khí 1: {w1.name} | Cấp: {w1.upgrade_level} | Sát thương gốc: {w1.base_damage}")
            print(f"Vũ khí 2: {w2.name} | Cấp: {w2.upgrade_level} | Sát thương gốc: {w2.base_damage}\n")
            
            try:
                new_weapon = w1 + w2
                print(">> Dung hợp vũ khí thành công!")
                print(f"Đã xóa khỏi kho: {w1.name}")
                print(f"Đã xóa khỏi kho: {w2.name}\n")
                
                inventory.pop(0)
                inventory.pop(0)
                inventory.append(new_weapon)
                
                print(f"Vũ khí mới: {new_weapon.name}")
                print("Loại: Weapon")
                print(f"Cấp cường hóa: {new_weapon.upgrade_level}")
                print(f"Sát thương tổng: {new_weapon.calculate_total_damage()}")
            except TypeError as e:
                print(f"Lỗi hệ thống dung hợp: {e}")

        elif choice == "6":
            print("Thoát Lò Rèn. Hẹn gặp lại Anh hùng!")
            break

        else:
            print("Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 6.")


if __name__ == "__main__":
    main()