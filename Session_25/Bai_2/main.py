# Thiết kế Class với Name Mangling:
# Việc đặt hai dấu gạch dưới trước biến __password và __plan kích hoạt cơ chế Name Mangling,
# giúp che giấu dữ liệu khỏi việc truy cập trực tiếp từ bên ngoài đối tượng. 
# Người dùng không thể in trực tiếp mật khẩu thật ra màn hình hay dùng lệnh gán đè gói cước.
# Mọi tương tác đọc/ghi đều phải đi qua "cửa kiểm duyệt" là các Decorator @property và @setter.
# tính bảo mật và tính toàn vẹn của dữ liệu được đảm bảo tuyệt đối.

# Tác động của Class Method:
# Phương thức cấp Lớp (Class Method) sử dụng tham số cls thay vì self,
# cho phép tương tác thẳng vào cấu trúc gốc của toàn bộ Class.
# Khi ta dùng update_max_profiles để thay đổi biến max_profiles,
# hệ thống chỉ cần cập nhật dữ liệu đúng một lần tại bộ nhớ trung tâm.
# quy định này sẽ được áp dụng tự động cho hàng triệu tài khoản (Instance)
# hiện đang tồn tại hoặc sắp được tạo mới, giúp tiết kiệm tối đa tài nguyên hệ thống.


class NetflixAccount:
    """Lớp đại diện cho một tài khoản người dùng trên hệ thống Netflix."""

    platform_name = "Netflix"
    max_profiles = 5

    def __init__(self, email):
        """Khởi tạo tài khoản với email, thiết lập các thuộc tính ẩn và danh sách profile rỗng."""
        self.email = email
        self.__password = ""
        self.__plan = "Basic"
        self.profiles = []

    @property
    def password(self):
        """Trả về chuỗi ẩn danh khi hệ thống hoặc người dùng cố gắng đọc mật khẩu."""
        return "********"

    @password.setter
    def password(self, new_password):
        """Kiểm duyệt độ dài mật khẩu trước khi lưu trữ vào hệ thống."""
        if len(new_password) < 6:
            raise ValueError("Password is too short")
        self.__password = new_password

    @property
    def plan(self):
        """Cho phép đọc thông tin gói cước hiện tại một cách an toàn."""
        return self.__plan

    @staticmethod
    def validate_email(email):
        """Kiểm tra tính hợp lệ cơ bản của chuỗi email truyền vào."""
        if "@" in email and "." in email:
            return True
        return False

    @classmethod
    def update_max_profiles(cls, new_limit):
        """Cập nhật giới hạn số lượng Profile dùng chung cho mọi tài khoản toàn cầu."""
        cls.max_profiles = new_limit

    def add_profile(self, profile_name):
        """Kiểm tra giới hạn hiện tại của hệ thống và thêm người xem mới vào tài khoản."""
        if len(self.profiles) >= NetflixAccount.max_profiles:
            print("Đã đạt giới hạn số lượng Profile trên tài khoản này")
        else:
            self.profiles.append(profile_name)
            print(f"Thêm Profile '{profile_name}' thành công.")

    def upgrade_plan(self, new_plan):
        """Kiểm tra và cập nhật gói cước của người dùng nếu giá trị truyền vào hợp lệ."""
        valid_plans = ["Basic", "Standard", "Premium"]
        if new_plan in valid_plans:
            self.__plan = new_plan
            print(f"Đã nâng cấp gói cước thành: {self.__plan}")
        else:
            print("Gói cước không hợp lệ.")

    def display_info(self):
        """Hiển thị toàn bộ thông tin công khai của tài khoản ra màn hình."""
        print("\n--- THÔNG TIN TÀI KHOẢN ---")
        print(f"Platform: {NetflixAccount.platform_name}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        print(f"Plan: {self.plan}")
        print(f"Profiles: {self.profiles}")


def main():
    """Hàm điều hướng menu quản lý ứng dụng trên CLI."""
    current_account = None

    while True:
        print("\n===== NETFLIX ACCOUNT MANAGER =====")
        print("1. Đăng ký tài khoản mới")
        print("2. Xem thông tin tài khoản")
        print("3. Thêm người xem")
        print("4. Nâng cấp gói cước")
        print("5. Cập nhật chính sách Netflix")
        print("6. Thoát chương trình")
        print("===================================")

        choice = input("Chọn chức năng (1-6): ")

        if choice == "1":
            email = input("Nhập Email: ")
            if not NetflixAccount.validate_email(email):
                print("Email không hợp lệ, vui lòng chứa ký tự '@' và '.'")
                continue

            account = NetflixAccount(email)

            while True:
                password = input("Nhập Mật khẩu (>= 6 ký tự): ")
                try:
                    account.password = password
                    break
                except ValueError as e:
                    print(e)

            current_account = account
            print("Đăng ký tài khoản thành công!")

        elif choice == "2":
            if current_account is None:
                print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
            else:
                current_account.display_info()

        elif choice == "3":
            if current_account is None:
                print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
            else:
                profile_name = input("Nhập tên Profile mới: ")
                current_account.add_profile(profile_name)

        elif choice == "4":
            if current_account is None:
                print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
            else:
                print("Các gói cước: Basic, Standard, Premium")
                new_plan = input("Nhập gói cước muốn nâng cấp: ")
                current_account.upgrade_plan(new_plan)

        elif choice == "5":
            try:
                new_limit = int(input("Nhập số lượng Profile tối đa mới: "))
                if new_limit > 0:
                    NetflixAccount.update_max_profiles(new_limit)
                    print(f"Đã cập nhật giới hạn Profile toàn hệ thống thành {new_limit}")
                else:
                    print("Số lượng phải lớn hơn 0.")
            except ValueError:
                print("Vui lòng nhập một số nguyên.")

        elif choice == "6":
            print("Đã thoát chương trình. Hẹn gặp lại!")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 6.")


if __name__ == "__main__":
    main()