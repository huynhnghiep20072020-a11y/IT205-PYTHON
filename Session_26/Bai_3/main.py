# Champion (Lớp cha - ABC): Đóng vai trò là khuôn mẫu gốc, định nghĩa các thuộc tính chung
# (Mã, Tên, HP, ATK) và các hàm dùng chung (tính tổng chiến lực, nạp chồng toán tử).
# Lớp này không thể khởi tạo trực tiếp.

# Warrior và Mage (Lớp con): Kế thừa toàn bộ đặc tính từ Champion, đồng thời bổ sung thêm các thuộc tính chuyên biệt
# (shield_bonus cho Warrior, ability_power cho Mage).

# 2. Phân tích đa hình (Polymorphism)
# Phương thức calculate_skill_damage() được khai báo là @abstractmethod ở lớp cha nhưng không có nội dung. 
# Mỗi lớp con (Warrior, Mage) bắt buộc phải tự viết lại hàm này với công thức riêng.
# Tính đa hình thể hiện ở chỗ: Hệ thống (ví dụ hàm get_combat_power()) chỉ cần gọi self.calculate_skill_damage().
# Nó không cần biết quân cờ hiện tại là Chiến binh hay Pháp sư, hệ thống sẽ tự động đối chiếu và chạy đúng công thức của hệ đó. 
# Điều này giúp Studio dễ dàng tạo thêm hàng trăm hệ phái mới (Assassin, Ranger...) sau này mà không cần sửa lại code tính điểm chiến lực chung.

# 3. Phân tích Nạp chồng toán tử (Operator Overloading)
# Phương thức __add__(self, other) được thiết kế để xử lý phép cộng. 
# Khi ta cộng 2 quân cờ, hệ thống sẽ lấy điểm chiến lực của chúng cộng lại. 
# Khi ta cộng một quân cờ với một số nguyên (ví dụ số 0 khởi điểm của hàm tính tổng),
# nó sẽ trả về điểm chiến lực + số nguyên. Để chạy vòng lặp cộng dồn an toàn từ số 0, ta kết hợp thêm hàm __radd__ (Right Add) 
# để Python biết cách xử lý phép toán 0 + Đối tượng Champion.


from abc import ABC, abstractmethod

class Champion(ABC):
    """Lớp cơ sở trừu tượng định nghĩa khuôn mẫu cho mọi quân cờ trong hệ thống."""

    def __init__(self, champion_id: str, name: str, base_hp: int, base_atk: int):
        self.champion_id = champion_id.strip().upper()
        self.name = name.strip()
        self.base_hp = base_hp if base_hp > 0 else 100
        self.base_atk = base_atk if base_atk > 0 else 100

    @abstractmethod
    def calculate_skill_damage(self) -> float:
        """Phương thức trừu tượng bắt buộc các hệ tướng phải tự triển khai."""
        pass

    def get_combat_power(self) -> float:
        """Tính toán tổng chiến lực dựa trên HP và sát thương kỹ năng."""
        return self.base_hp + (self.calculate_skill_damage() * 1.5)

    def __add__(self, other):
        """Nạp chồng toán tử cộng (+) để cộng chiến lực của 2 quân cờ hoặc với 1 số."""
        if isinstance(other, Champion):
            return self.get_combat_power() + other.get_combat_power()
        elif isinstance(other, (int, float)):
            return self.get_combat_power() + other
        return NotImplemented

    def __radd__(self, other):
        """Hỗ trợ phép cộng đảo ngược (ví dụ: 0 + Champion) để dùng được hàm sum()."""
        return self.__add__(other)

    def __gt__(self, other):
        """Nạp chồng toán tử lớn hơn (>) để so sánh sức mạnh 2 quân cờ."""
        if isinstance(other, Champion):
            return self.get_combat_power() > other.get_combat_power()
        return NotImplemented


class Warrior(Champion):
    """Lớp đại diện cho hệ tướng Chiến Binh."""

    def __init__(self, champion_id: str, name: str, base_hp: int, base_atk: int, shield_bonus: int):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.shield_bonus = shield_bonus if shield_bonus > 0 else 0

    def calculate_skill_damage(self) -> float:
        """Triển khai công thức tính sát thương kỹ năng chuyên biệt cho Chiến Binh."""
        return (self.base_atk * 2) + self.shield_bonus


class Mage(Champion):
    """Lớp đại diện cho hệ tướng Pháp Sư."""

    def __init__(self, champion_id: str, name: str, base_hp: int, base_atk: int, ability_power: float):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.ability_power = ability_power if ability_power > 0 else 1.0

    def calculate_skill_damage(self) -> float:
        """Triển khai công thức tính sát thương kỹ năng chuyên biệt cho Pháp Sư."""
        return self.base_atk * self.ability_power


def get_champion_by_id(pool: list, champ_id: str):
    """Hàm phụ trợ tìm kiếm đối tượng quân cờ trong bể tướng dựa trên mã ID."""
    search_id = champ_id.strip().upper()
    for champ in pool:
        if champ.champion_id == search_id:
            return champ
    return None


def main():
    """Hàm điều phối luồng chạy chính và giao diện Menu tương tác của hệ thống."""
    champion_pool = [
        Warrior("WAR01", "Rikkei Knight", 1200, 300, 150),
        Warrior("WAR02", "Steel Guardian", 1500, 250, 200),
        Mage("MAG01", "Rikkei Wizard", 800, 500, 2.0)
    ]

    while True:
        print("\n===== RIKKEI RPG - AUTO-BATTLER MANAGER =====")
        print("1. Hiển thị bể tướng hiện có")
        print("2. Thêm quân cờ mới")
        print("3. So sánh 2 quân cờ")
        print("4. Tính tổng chiến lực Đội Hình Ra Sân")
        print("5. Thoát chương trình")
        print("=============================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == "1":
            print("\n--- DANH SÁCH QUÂN CỜ TRONG BỂ TƯỚNG ---")
            print(f"{'Mã':<7} | {'Tên tướng':<20} | {'Hệ':<8} | {'HP':<5} | {'ATK':<5} | {'Chỉ số riêng':<17} | {'Chiến lực'}")
            print("-" * 85)
            for champ in champion_pool:
                champ_type = "Warrior" if isinstance(champ, Warrior) else "Mage"
                if isinstance(champ, Warrior):
                    special_stat = f"Armor: {champ.shield_bonus}"
                else:
                    special_stat = f"AP: {champ.ability_power}"
                
                print(f"{champ.champion_id:<7} | {champ.name:<20} | {champ_type:<8} | {champ.base_hp:<5} | {champ.base_atk:<5} | {special_stat:<17} | {champ.get_combat_power():.0f}")
            print("-" * 85)

        elif choice == "2":
            print("\n--- THÊM QUÂN CỜ MỚI ---")
            print("Chọn hệ tướng: 1 - Warrior | 2 - Mage")
            champ_type = input("Lựa chọn (1/2): ").strip()
            
            if champ_type not in ["1", "2"]:
                print("Lựa chọn hệ tướng không hợp lệ!")
                continue
                
            champ_id = input("Nhập mã tướng: ").strip().upper()
            if get_champion_by_id(champion_pool, champ_id) is not None:
                print(f"Mã tướng {champ_id} đã tồn tại trong hệ thống!")
                continue

            name = input("Nhập tên tướng: ").strip()
            
            try:
                base_hp = int(input("Nhập HP: "))
                base_atk = int(input("Nhập ATK: "))
                
                if champ_type == "1":
                    bonus_armor = int(input("Nhập Armor: "))
                    new_champ = Warrior(champ_id, name, base_hp, base_atk, bonus_armor)
                    system_name = "Warrior"
                else:
                    ap = float(input("Nhập AP (Hệ số phép): "))
                    new_champ = Mage(champ_id, name, base_hp, base_atk, ap)
                    system_name = "Mage"

                champion_pool.append(new_champ)
                print(f"\nThêm tướng {system_name} thành công!")
                print(f"Mã: {new_champ.champion_id} | Tên: {new_champ.name} | Chiến lực: {new_champ.get_combat_power():.0f}")

            except ValueError:
                print("Lỗi: Dữ liệu chỉ số nhập vào phải là số!")

        elif choice == "3":
            print("\n--- SO SÁNH SỨC MẠNH 2 QUÂN CỜ ---")
            id1 = input("Nhập mã tướng thứ nhất: ").strip().upper()
            id2 = input("Nhập mã tướng thứ hai: ").strip().upper()

            champ1 = get_champion_by_id(champion_pool, id1)
            champ2 = get_champion_by_id(champion_pool, id2)

            if not champ1:
                print(f"Mã tướng {id1} không hợp lệ, bỏ qua!")
                continue
            if not champ2:
                print(f"Mã tướng {id2} không hợp lệ, bỏ qua!")
                continue

            print("\nThông tin so sánh:")
            type1 = "Warrior" if isinstance(champ1, Warrior) else "Mage"
            type2 = "Warrior" if isinstance(champ2, Warrior) else "Mage"
            
            print(f"{champ1.champion_id} - {champ1.name:<15} | Hệ: {type1:<7} | Chiến lực: {champ1.get_combat_power():.0f}")
            print(f"{champ2.champion_id} - {champ2.name:<15} | Hệ: {type2:<7} | Chiến lực: {champ2.get_combat_power():.0f}")

            print("Kết quả: ", end="")
            if champ1 > champ2:
                print(f"{champ1.champion_id} - {champ1.name} mạnh hơn {champ2.champion_id} - {champ2.name}.")
            elif champ2 > champ1:
                print(f"{champ2.champion_id} - {champ2.name} mạnh hơn {champ1.champion_id} - {champ1.name}.")
            else:
                print("Hai quân cờ có sức mạnh ngang nhau.")

        elif choice == "4":
            print("\n--- TÍNH TỔNG CHIẾN LỰC ĐỘI HÌNH RA SÂN ---")
            id_input = input("Nhập danh sách mã tướng, cách nhau bằng dấu phẩy: ")
            id_list = [i.strip().upper() for i in id_input.split(",")]
            
            lineup = []
            print("Danh sách đội hình:")
            for index, c_id in enumerate(id_list, 1):
                champ = get_champion_by_id(champion_pool, c_id)
                if champ:
                    lineup.append(champ)
                    print(f"{index}. {champ.champion_id} - {champ.name} | Chiến lực: {champ.get_combat_power():.0f}")
                else:
                    print(f"{index}. Mã tướng {c_id} không hợp lệ, bỏ qua!")
            
            if lineup:
                total_power = sum(lineup)
                print(f"Tổng chiến lực đội hình: {total_power:.0f}")
            else:
                print("Đội hình không có tướng nào hợp lệ.")

        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng Rikkei RPG - Auto-Battler Manager!")
            break

        else:
            print("Chức năng không hợp lệ. Vui lòng nhập từ 1 đến 5.")


if __name__ == "__main__":
    main()