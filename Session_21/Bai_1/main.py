import logging


class InvalidAmountError(Exception):
    """Ngoại lệ khi số tiền giao dịch không hợp lệ."""
    pass


class InsufficientBalanceError(Exception):
    """Ngoại lệ khi số dư ví không đủ để giao dịch."""
    pass


class TransactionLogger:
    """Lớp xử lý việc ghi log lịch sử giao dịch cho ví MoMo."""

    def __init__(self, log_file: str = "momo_transactions.log"):
        self.logger = logging.getLogger("MoMoWallet")
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(message)s'
            )
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def info(self, message: str):
        """Ghi log thông tin thành công (INFO)."""
        self.logger.info(message)

    def warning(self, message: str):
        """Ghi log cảnh báo (WARNING)."""
        self.logger.warning(message)

    def error(self, message: str):
        """Ghi log sự cố hoặc lỗi (ERROR)."""
        self.logger.error(message)


class Wallet:
    """Lớp đại diện cho ví MoMo xử lý các giao dịch tài chính cốt lõi."""

    def __init__(self, logger: TransactionLogger):
        self.balance = 0
        self.logger = logger

    def deposit(self, amount: int):
        """Nạp tiền vào ví và cập nhật số dư."""
        if amount <= 0:
            self.logger.error(
                f"InvalidAmountError: Attempted to process {amount} VND."
            )
            raise InvalidAmountError("Số tiền giao dịch phải lớn hơn 0.")

        self.balance += amount
        self.logger.info(
            f"Deposit successful: +{amount} VND. "
            f"Current Balance: {self.balance}"
        )

    def transfer(self, phone: str, amount: int):
        """Chuyển tiền đến số điện thoại khác."""
        if amount <= 0:
            self.logger.error(
                f"InvalidAmountError: Attempted to process {amount} VND."
            )
            raise InvalidAmountError("Số tiền giao dịch phải lớn hơn 0.")

        if amount > self.balance:
            self.logger.error(
                f"InsufficientBalanceError: Attempted to transfer {amount} "
                f"VND with balance {self.balance} VND."
            )
            raise InsufficientBalanceError(
                "Giao dịch thất bại: Số dư của bạn không đủ."
            )

        if amount >= 10000000:
            self.logger.warning(
                f"High value transaction detected: {amount} VND to {phone}"
            )

        self.balance -= amount
        self.logger.info(
            f"Transfer successful: -{amount} VND to {phone}. "
            f"Current Balance: {self.balance}"
        )

    def get_balance(self) -> int:
        """Lấy và ghi log số dư hiện tại của ví."""
        self.logger.info(
            f"Balance checked. Current Balance: {self.balance}"
        )
        return self.balance


def display_menu():
    """Hiển thị menu giao diện dòng lệnh (CLI)."""
    print("\n========== VÍ MOMO GIẢ LẬP ==========")
    print("1. Nạp tiền vào ví")
    print("2. Chuyển tiền")
    print("3. Xem số dư hiện tại")
    print("4. Thoát chương trình")
    print("=======================================")


def main():
    logger = TransactionLogger()
    wallet = Wallet(logger)

    while True:
        display_menu()
        choice = input("Chọn chức năng (1-4): ").strip()

        match choice:
            case "1":
                print("\n--- NẠP TIỀN VÀO VÍ ---")
                while True:
                    try:
                        amount = int(input("Nhập số tiền cần nạp: "))
                        wallet.deposit(amount)
                        print(f"\nNạp tiền thành công: +{amount:,.0f} VND")
                        print(f"Số dư hiện tại: {wallet.balance:,.0f} VND")
                        break
                    except ValueError:
                        print("\nLỗi: Vui lòng nhập số tiền hợp lệ.")
                        logger.error(
                            "ValueError: Invalid numeric input for deposit."
                        )
                    except InvalidAmountError as e:
                        print(f"\nLỗi: {e}")
                        break

            case "2":
                print("\n--- CHUYỂN TIỀN ---")
                phone = input("Nhập số điện thoại người nhận: ").strip()
                while True:
                    try:
                        amount = int(input("Nhập số tiền cần chuyển: "))
                        wallet.transfer(phone, amount)
                        print(
                            f"\nChuyển tiền thành công tới số điện thoại "
                            f"{phone}."
                        )
                        print(f"Số tiền đã chuyển: {amount:,.0f} VND")
                        print(f"Số dư còn lại: {wallet.balance:,.0f} VND")
                        break
                    except ValueError:
                        print("\nLỗi: Vui lòng nhập số tiền hợp lệ.")
                        logger.error(
                            "ValueError: Invalid numeric input for transfer."
                        )
                    except (InvalidAmountError, InsufficientBalanceError) as e:
                        print(f"\n{e}")
                        print(f"Số dư hiện tại: {wallet.balance:,.0f} VND")
                        break

            case "3":
                print("\n--- SỐ DƯ VÍ MOMO ---")
                current_balance = wallet.get_balance()
                print(f"Số dư hiện tại: {current_balance:,.0f} VND")

            case "4":
                print("\nCảm ơn bạn đã sử dụng dịch vụ")
                logger.info("System shutdown")
                break

            case _:
                print("\nLựa chọn không hợp lệ, vui lòng chọn từ 1 đến 4.")


if __name__ == "__main__":
    main()