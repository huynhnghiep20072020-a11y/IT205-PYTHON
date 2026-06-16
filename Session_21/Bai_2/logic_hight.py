import logging

class ItemNotFoundError(Exception):
    """Exception raised when the drink code is not in the menu."""
    def __init__(self, drink_code: str):
        self.drink_code = drink_code
        super().__init__(f"Mã đồ uống không hợp lệ, vui lòng kiểm tra lại thực đơn!")


class InvalidQuantityError(Exception):
    """Exception raised when the quantity is 0 or negative."""
    def __init__(self, quantity: int):
        self.quantity = quantity
        super().__init__(f"Số lượng phải lớn hơn 0!")


DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000}
}


def get_menu_display() -> str:
    """Returns a formatted string of the drink menu."""
    lines = ["--- THỰC ĐƠN HIGHLANDS COFFEE ---"]
    for code, details in DRINK_MENU.items():
        lines.append(f"[{code}] - {details['name']} - {details['price']:,} VNĐ")
    return "\n".join(lines)


def add_to_order(drink_code: str, quantity: int, order_list: list):
    """Validates and adds a drink item to the current order list."""
    clean_code = drink_code.strip().upper()

    if clean_code not in DRINK_MENU:
        logging.warning(f"ItemNotFoundError - Code: {clean_code}")
        raise ItemNotFoundError(clean_code)

    if quantity <= 0:
        logging.warning(f"InvalidQuantityError - Quantity: {quantity}")
        raise InvalidQuantityError(quantity)

    drink_info = DRINK_MENU[clean_code]
    
    order_item = {
        "code": clean_code,
        "name": drink_info["name"],
        "price": drink_info["price"],
        "quantity": quantity
    }
    order_list.append(order_item)
    logging.info(f"Added {quantity} of {clean_code} to order")


def calculate_total(order_list: list) -> int:
    """Calculates the total price of all items in the order list."""
    total = 0
    for item in order_list:
        total += item["price"] * item["quantity"]
    return total


def get_order_receipt(order_list: list) -> str:
    """Returns a formatted string of the current order and total."""
    if not order_list:
        return "Giỏ hàng trống, vui lòng chọn món (Chức năng 2)."

    lines = ["--- GIỎ HÀNG HIỆN TẠI ---"]
    lines.append(f"{'Mã SP':<5} | {'Tên đồ uống':<20} | {'Đơn giá':<8} | {'Số lượng':<8} | {'Thành tiền'}")
    lines.append("-" * 64)

    for item in order_list:
        line_total = item['price'] * item['quantity']
        lines.append(
            f"{item['code']:<5} | {item['name']:<20} | {item['price']:<8,} | "
            f"{item['quantity']:<8} | {line_total:,} VNĐ"
        )
    
    lines.append("-" * 64)
    total = calculate_total(order_list)
    lines.append(f"Tổng tiền cần thanh toán: {total:,} VNĐ")
    
    return "\n".join(lines)