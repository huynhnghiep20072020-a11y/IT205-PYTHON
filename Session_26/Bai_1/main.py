# Giải thích lỗi AttributeError và cú pháp còn thiếu:
#     Dòng print(f"Chiến binh {w1.name}...") văng lỗi vì thuộc tính name chưa từng được tạo ra trong đối tượng w1. 
#     Trong Lập trình hướng đối tượng, lớp con không tự động sao chép các thuộc tính của lớp cha nếu bạn ghi đè hàm __init__ mà không gọi lại nó. 
#     Lập trình viên đã thiếu cú pháp super().__init__(name, hp, attack_power) bên trong hàm khởi tạo của Warrior.

# Cách gọi hàm khởi tạo khác (không dùng super()):
# Dù không được khuyến khích trong Python hiện đại,
# bạn vẫn có thể gọi trực tiếp hàm khởi tạo của lớp cha bằng cú pháp:
#     Character.__init__(self, name, hp, attack_power).

# Bài toán Toán tử và nguyên nhân vô tác dụng:
# Nếu Lỗi 1 được sửa, khi chạy đến w1 > w2, hệ thống sẽ ném ra ngoại lệ TypeError: 
#     '>' not supported between instances of 'Warrior' and 'Warrior'.
#     Dấu > vô tác dụng vì Python không tự đoán được tiêu chí so sánh giữa 2 đối tượng tự định nghĩa 
#     (ví dụ: máy không biết nên so sánh máu, sát thương, hay giáp).

# Dunder method cần khai báo:
# Để dấu > hoạt động, bạn cần khai báo Dunder method __gt__ (viết tắt của greater than).
# Hàm này nhận vào 2 tham số: self (đại diện cho chiến binh nằm bên trái dấu lớn hơn) và other (đại diện cho chiến binh nằm bên phải).


class Character:
    """Lớp đại diện cho một nhân vật cơ bản trong game."""
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power


class Warrior(Character):
    """Lớp đại diện cho chiến binh, kế thừa từ Character."""
    def __init__(self, name, hp, attack_power, bonus_armor):
        super().__init__(name, hp, attack_power)
        self.bonus_armor = bonus_armor

    def get_total_power(self):
        """Tính toán và trả về tổng sức mạnh chiến đấu của chiến binh."""
        return self.attack_power + self.bonus_armor

    def __gt__(self, other):
        """Nạp chồng toán tử lớn hơn (>) để so sánh tổng sức mạnh."""
        return self.get_total_power() > other.get_total_power()


w1 = Warrior("Arthur", 1000, 150, 50)
w2 = Warrior("Lancelot", 900, 180, 10)

print(f"Chiến binh {w1.name} xuất trận!")

if w1 > w2:
    print(f"{w1.name} mạnh hơn {w2.name}!")
else:
    print(f"{w2.name} mạnh hơn hoặc hòa!")