# Thuộc tính Private (__account_number, __account_name, __balance): Việc sử dụng Name Mangling (hai dấu gạch dưới) giúp bảo vệ dữ liệu nội tại của đối tượng, 
# ngăn chặn người dùng hoặc các đoạn code bên ngoài can thiệp, gán đè trực tiếp (ví dụ: account.__balance = 1000000000).

# @property balance: Đóng vai trò là một hàm Getter (chỉ đọc). 
# Nó cho phép hệ thống xem số dư một cách an toàn mà không cấp quyền sửa đổi.

# @property và @setter account_name: Cho phép đọc và ghi. 
# Setter đóng vai trò như một màng lọc dữ liệu (Data Validation),
# đảm bảo mọi chuỗi tên khi được gán vào đều phải đi qua bước kiểm tra rỗng, 
# cắt khoảng trắng và viết hoa trước khi lưu vào bộ nhớ.



class BankAccount:
    """Lớp đại diện cho tài khoản ngân hàng Vietcombank."""

    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number, account_name):
        """Khởi tạo tài khoản với số tài khoản, tên chủ thẻ và số dư mặc định là 0."""
        self.__account_number = account_number
        self.__account_name = account_name.strip().upper()
        self.__balance = 0

    @property
    def balance(self):
        """Trả về số dư tài khoản hiện tại (Chỉ đọc)."""
        return self.__balance

    @property
    def account_name(self):
        """Trả về tên chủ tài khoản hiện tại."""
        return self.__account_name

    @account_name.setter
    def account_name(self, new_name):
        """Kiểm duyệt và cập nhật tên chủ tài khoản."""
        clean_name = new_name.strip()
        if not clean_name:
            print("Tên tài khoản không được để trống")
        else:
            self.__account_name = clean_name.upper()
            print(f"Cập nhật thành công. Tên mới: {self.__account_name}")

    @staticmethod
    def validate_account_number(account_number):
        """Kiểm tra số tài khoản có đúng 10 chữ số hay không."""
        if len(account_number) == 10 and account_number.isdigit():
            return True
        return False

    @classmethod
    def update_transaction_fee(cls, new_fee):
        """Cập nhật phí giao dịch áp dụng cho toàn bộ hệ thống."""
        if new_fee < 0:
            print("Phí giao dịch không được âm")
            print(f"Phí giao dịch hiện tại vẫn là {cls.transaction_fee:,} VND")
        else:
            cls.transaction_fee = new_fee
            print(f"Đã cập nhật phí giao dịch toàn hệ thống thành {cls.transaction_fee:,} VND")

    def deposit(self, amount):
        """Thực hiện cộng tiền vào số dư tài khoản."""
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return
        
        self.__balance += amount
        print(f"Nạp tiền thành công: +{amount:,} VND")
        print(f"Số dư mới: {self.balance:,} VND")

    def withdraw(self, amount):
        """Thực hiện rút tiền và trừ phí giao dịch nếu số dư cho phép."""
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return
        
        total_deduction = amount + BankAccount.transaction_fee
        
        if self.__balance < total_deduction:
            print("Giao dịch thất bại. Số dư không đủ để thanh toán số tiền và phí giao dịch")
            print(f"Số dư mới: {self.balance:,} VND")
            return
            
        self.__balance -= total_deduction
        print(f"Rút tiền thành công: -{amount:,} VND")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")
        print(f"Số dư mới: {self.balance:,} VND")

    def display_info(self):
        """Hiển thị toàn bộ thông tin chi tiết của tài khoản."""
        print("--- THÔNG TIN TÀI KHOẢN ---")
        print(f"Ngân hàng: {BankAccount.bank_name}")
        print(f"Số tài khoản: {self.__account_number}")
        print(f"Tên chủ tài khoản: {self.__account_name}")
        print(f"Số dư hiện tại: {self.balance:,} VND")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")


def main():
    """Hàm điều phối vòng lặp Menu CLI."""
    current_account = None

    while True:
        print("\n===== VIETCOMBANK DIGIBANK SIMULATOR =====")
        print("1. Mở tài khoản mới")
        print("2. Xem thông tin tài khoản")
        print("3. Giao dịch Nạp / Rút tiền")
        print("4. Cập nhật Tên chủ tài khoản")
        print("5. Đổi phí giao dịch hệ thống")
        print("6. Thoát chương trình")
        print("==========================================")

        choice = input("Chọn chức năng (1-6): ").strip()

        if choice == "1":
            print("--- MỞ TÀI KHOẢN MỚI ---")
            while True:
                acc_num = input("Nhập số tài khoản 10 chữ số: ").strip()
                if BankAccount.validate_account_number(acc_num):
                    break
                print("Số tài khoản không hợp lệ!")
                print("Số tài khoản phải gồm đúng 10 chữ số.")

            acc_name = input("Nhập tên chủ tài khoản: ").strip()
            current_account = BankAccount(acc_num, acc_name)
            
            print("Mở tài khoản thành công!")
            print(f"Số tài khoản: {acc_num}")
            print(f"Tên chủ tài khoản: {current_account.account_name}")

        elif choice in ["2", "3", "4"]:
            if current_account is None:
                print("Hệ thống chưa có thông tin tài khoản")
                print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
                continue

            if choice == "2":
                current_account.display_info()

            elif choice == "3":
                print("--- GIAO DỊCH NẠP / RÚT TIỀN ---")
                print("1. Nạp tiền")
                print("2. Rút tiền")
                trans_type = input("Chọn loại giao dịch (1-2): ").strip()

                if trans_type in ["1", "2"]:
                    try:
                        amount = int(input("Nhập số tiền giao dịch: "))
                        if trans_type == "1":
                            current_account.deposit(amount)
                        else:
                            current_account.withdraw(amount)
                    except ValueError:
                        print("Số tiền giao dịch không hợp lệ.")
                else:
                    print("Lựa chọn loại giao dịch không hợp lệ.")

            elif choice == "4":
                print("--- CẬP NHẬT TÊN CHỦ TÀI KHOẢN ---")
                new_name = input("Nhập tên mới: ")
                current_account.account_name = new_name

        elif choice == "5":
            print("--- ĐỔI PHÍ GIAO DỊCH HỆ THỐNG ---")
            print(f"Phí giao dịch hiện tại: {BankAccount.transaction_fee:,} VND")
            try:
                new_fee = int(input("Nhập phí giao dịch mới: "))
                BankAccount.update_transaction_fee(new_fee)
            except ValueError:
                print("Phí giao dịch không hợp lệ.")

        elif choice == "6":
            print("Cảm ơn bạn đã sử dụng Vietcombank Digibank!")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 6.")

if __name__ == "__main__":
    main()