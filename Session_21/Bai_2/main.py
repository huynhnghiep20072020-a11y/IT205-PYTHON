import logging
from logic_hight import (
    DRINK_MENU,
    ItemNotFoundError,
    InvalidQuantityError,
    get_menu_display,
    add_to_order,
    calculate_total,
    get_order_receipt
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def main():
    """Main CLI loop for the Highlands Mini POS system."""
    current_order = []

    while True:
        print("\n========== HIGHLANDS MINI POS ==========")
        print("1. Xem thực đơn")
        print("2. Thêm món vào giỏ")
        print("3. Xem giỏ hàng & Tính tổng tiền")
        print("4. Thanh toán & Xóa giỏ hàng")
        print("5. Thoát ca làm việc")
        print("========================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()

        match choice:
            case "1":
                print(get_menu_display())

            case "2":
                print("--- THÊM MÓN VÀO GIỎ ---")
                drink_code = input("Nhập mã đồ uống: ")
                raw_quantity = input("Nhập số lượng: ")

                try:
                    quantity = int(raw_quantity)
                    add_to_order(drink_code, quantity, current_order)
                    clean_code = drink_code.strip().upper()
                    drink_name = DRINK_MENU[clean_code]["name"]
                    print(f"Đã thêm {quantity} x {drink_name} vào giỏ hàng.")
                except ValueError:
                    logging.error("ValueError - Invalid quantity input")
                    print("Vui lòng nhập số lượng là một số nguyên!")
                except ItemNotFoundError as e:
                    print(e)
                except InvalidQuantityError as e:
                    print(e)

            case "3":
                print(get_order_receipt(current_order))

            case "4":
                if not current_order:
                    print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
                else:
                    print("--- THANH TOÁN ---")
                    total = calculate_total(current_order)
                    print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")
                    
                    confirm = input(f"Xác nhận thanh toán {total:,} VNĐ? (y/n): ").strip().lower()
                    if confirm == 'y':
                        print("Thanh toán thành công.")
                        logging.info("Checkout successful")
                        current_order.clear()
                        print("Giỏ hàng đã được làm trống.")
                    elif confirm == 'n':
                        print("Đã hủy thao tác thanh toán. Quay lại menu chính.")
                    else:
                        print("Lựa chọn không hợp lệ. Thanh toán đã bị hủy.")

            case "5":
                logging.info("Cashier logged out. System shutdown.")
                print("Đã thoát ca làm việc. Hẹn gặp lại!")
                break

            case _:
                print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 5.")


if __name__ == "__main__":
    main()