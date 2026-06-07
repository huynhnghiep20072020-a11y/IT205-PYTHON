# Sai thứ tự tham số: Ở mã cũ, giá trị truyền vào là (100000, 15000, 0.1) 
# khiến biến discount nhận giá trị 15000 (tức giảm giá 1.500.000%),
# gây ra số âm khổng lồ. Đã sửa lại đúng thứ tự định nghĩa là (100000, 0.1, 15000).

# Thiếu lệnh return: Hàm cũ dùng print nên không trả về dữ liệu tính toán, khiến biến order_total bị gán giá trị 
# None (dẫn đến lỗi crash khi cộng với 5000). Đã thay thế bằng lệnh return total để đẩy kết quả ra ngoài.

def calculate_final_price(price, discount, shipping_fee):
    """
    Tính tổng tiền khách hàng phải trả dựa trên giá gốc, tỉ lệ giảm giá và phí giao hàng.

    :param price: Giá gốc của sản phẩm.
    :param discount: Tỉ lệ giảm giá (dưới dạng số thập phân, ví dụ 0.1 tương ứng 10%).
    :param shipping_fee: Phí giao hàng.
    :return: Tổng tiền đơn hàng sau khi tính toán.
    """
    total = price - (price * discount) + shipping_fee
    return total

order_total = calculate_final_price(100000, 0.1, 15000)

final_payment = order_total + 5000

print("Khách hàng cần thanh toán:", final_payment)