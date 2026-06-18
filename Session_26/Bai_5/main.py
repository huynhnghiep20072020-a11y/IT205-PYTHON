# Input: Thông tin sinh vật (Tên, Atk, Speed). Hành động gộp 2 sinh vật bằng toán tử +.

# Output: Đối tượng mới với chỉ số cộng dồn. Dòng text mô tả kỹ năng thi triển. Báo lỗi khi lai tạo sai quy tắc hoặc vi phạm kiến trúc khởi tạo.

# 2. Đề xuất giải pháp (Architecture & Logic):

# Lớp trừu tượng (Bẫy 1): Dùng thư viện abc, lớp Companion kế thừa ABC và có @abstractmethod cho unleash_skill. Điều này khóa hoàn toàn việc khởi tạo trực tiếp Companion().

# Toán tử dung hợp (Bẫy 2): Hàm __add__ được định nghĩa ngay ở lớp cha Companion. 
# hàm type(self) == type(other) đảm bảo hai sinh vật phải giống hệt nhau về class (Pet lai với Pet,
# không lai với Mount hay số nguyên).
# Nạp chồng toán tử tạo ra sự linh hoạt và tái sử dụng code.

# Đa kế thừa & MRO (Bẫy 3): Lớp Dragon kế thừa từ Pet và Mount. 
# Để tránh lỗi mất tham số, hàm __init__ sử dụng kwargs truyền qua các hàm super() dọc theo sơ đồ MRO.
# Điều này đảm bảo cả thuộc tính bonus_atk và bonus_speed đều được nhận diện và khởi tạo.

# 3. Thiết kế các bước thực hiện:

# Import thư viện trừu tượng.

# Code lớp Companion chứa logic dùng chung và hàm cộng dồn chỉ số bằng __add__.

# Tạo lớp Pet và Mount, ghi đè hàm unleash_skill riêng.

# Tạo lớp Dragon đa kế thừa.

# Viết khối Main Menu chạy test các bẫy dữ liệu và biểu diễn tính đa hình qua vòng lặp.


from abc import ABC, abstractmethod

class Companion(ABC):
    """Lớp cơ sở trừu tượng làm khuôn mẫu cho hệ sinh thái Bạn đồng hành."""

    def __init__(self, name, level=1, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.level = level

    @abstractmethod
    def unleash_skill(self):
        """Phương thức bắt buộc các sinh vật phải tự định nghĩa kỹ năng đặc trưng."""
        pass

    def __add__(self, other):
        """Hỗ trợ toán tử cộng để lai tạo 2 sinh vật cùng loài."""
        if type(self) is not type(other):
            raise TypeError("Chỉ có thể lai tạo 2 sinh vật cùng loài!")
        
        new_name = f"{self.name} {other.name}"
        new_level = self.level + 1
        
        if isinstance(self, Dragon):
            new_atk = self.bonus_atk + other.bonus_atk
            new_speed = self.bonus_speed + other.bonus_speed
            return Dragon(name=new_name, level=new_level, bonus_atk=new_atk, bonus_speed=new_speed)
        elif isinstance(self, Pet):
            new_atk = self.bonus_atk + other.bonus_atk
            return Pet(name=new_name, level=new_level, bonus_atk=new_atk)
        elif isinstance(self, Mount):
            new_speed = self.bonus_speed + other.bonus_speed
            return Mount(name=new_name, level=new_level, bonus_speed=new_speed)


class Pet(Companion):
    """Lớp đại diện cho Thú cưng, thiên về hỗ trợ tấn công."""

    def __init__(self, name, bonus_atk, level=1, **kwargs):
        super().__init__(name=name, level=level, **kwargs)
        self.bonus_atk = bonus_atk

    def unleash_skill(self):
        """Thi triển kỹ năng đặc trưng của Thú cưng."""
        print(f">> {self.name} gầm gừ: Tấn công kẻ thù, gây {self.bonus_atk} sát thương!")


class Mount(Companion):
    """Lớp đại diện cho Thú cưỡi, thiên về hỗ trợ di chuyển."""

    def __init__(self, name, bonus_speed, level=1, **kwargs):
        super().__init__(name=name, level=level, **kwargs)
        self.bonus_speed = bonus_speed

    def unleash_skill(self):
        """Thi triển kỹ năng đặc trưng của Thú cưỡi."""
        print(f">> {self.name} hí vang: Tăng tốc độ di chuyển thêm {self.bonus_speed} điểm!")


class Dragon(Pet, Mount):
    """Lớp đại diện cho Rồng Thần, đa kế thừa từ cả Thú cưng và Thú cưỡi."""

    def __init__(self, name, bonus_atk, bonus_speed, level=1, **kwargs):
        super().__init__(name=name, bonus_atk=bonus_atk, bonus_speed=bonus_speed, level=level, **kwargs)

    def unleash_skill(self):
        """Kích hoạt đồng thời cả hai kỹ năng tấn công và di chuyển."""
        print(f">> {self.name} thị uy:")
        Pet.unleash_skill(self)
        Mount.unleash_skill(self)


def main():
    """Hàm chạy giả lập mô phỏng các kịch bản test để kiểm chứng bẫy lỗi."""
    print("--- TEST BẪY 1: KHỞI TẠO COMPANION TRỰC TIẾP ---")
    try:
        c = Companion("Lỗi")
    except TypeError as e:
        print(f"Bẫy 1 thành công. Lỗi bắt được: {e}")

    print("\n--- TEST LAI TẠO BÌNH THƯỜNG ---")
    p1 = Pet(name="Sói Trắng", bonus_atk=50)
    p2 = Pet(name="Sói Đen", bonus_atk=60)
    p3 = p1 + p2
    print(f"Lai tạo thành công! Nhận được: {p3.name} (Cấp {p3.level}, Atk: {p3.bonus_atk})")

    print("\n--- TEST BẪY 2: LAI TẠO KHÁC LOÀI ---")
    m1 = Mount(name="Ngựa", bonus_speed=10)
    try:
        error_breed = p1 + m1
    except TypeError as e:
        print(f"Bẫy 2 thành công. Lỗi bắt được khi cộng Pet với Mount: {e}")
        
    try:
        error_breed_num = p1 + 10
    except TypeError as e:
        print(f"Bẫy 2 thành công. Lỗi bắt được khi cộng Pet với Số nguyên: {e}")

    print("\n--- TEST BẪY 3: ĐA KẾ THỪA RỒNG THẦN ---")
    d1 = Dragon(name="Rồng Lửa", bonus_atk=500, bonus_speed=200)
    print(f"Rồng thần {d1.name} được khởi tạo thành công với Atk: {d1.bonus_atk} và Speed: {d1.bonus_speed}")

    print("\n--- TEST ĐA HÌNH (POLYMORPHISM) ---")
    equipped = [p3, m1, d1]
    for companion in equipped:
        companion.unleash_skill()


if __name__ == "__main__":
    main()