inventory_stock = 100
total_revenue = 0.0

def main():
    while True:
        print("\n---------------- SKYBOOKING SYSTEM -----------------")
        print("Chuyến bay: VN2026 | Khởi hành: Hà Nội")
        print("1. Đặt vé máy bay")
        print("2. Hủy vé & Hoàn tiền")
        print("3. Xem tình trạng chuyến bay")
        print("4. Đóng hệ thống")
        print("------------------------------------------------------")
        
        choice = input("Chọn chức năng (1-4): ").strip()
        
        if choice == "1":
            print("--- ĐẶT VÉ MÁY BAY ---")
            try:
                quantity = int(input("Nhập số lượng vé: "))
                if quantity <= 0:
                    print("Số lượng vé phải lớn hơn 0.")
                    continue
                    
                ticket_class = int(input("Chọn hạng vé (1: Economy, 2: Business): "))
                if ticket_class not in [1, 2]:
                    print("Hạng vé không hợp lệ.")
                    continue
                    
                process_booking(quantity, ticket_class)
            except ValueError:
                print("Lỗi nhập liệu. Vui lòng nhập số hợp lệ.")
                
        elif choice == "2":
            print("--- HỦY VÉ & HOÀN TIỀN ---")
            try:
                quantity = int(input("Nhập số lượng vé muốn hủy: "))
                if quantity <= 0:
                    print("Số lượng vé phải lớn hơn 0.")
                    continue
                    
                process_refund(quantity)
            except ValueError:
                print("Lỗi nhập liệu. Vui lòng nhập số hợp lệ.")
                
        elif choice == "3":
            display_flight_status()
            
        elif choice == "4":
            print("Đóng hệ thống. Cảm ơn quý khách!")
            break
            
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")

if __name__ == "__main__":
    main()

def add_stock(amount):
    """
    Cộng thêm số lượng hàng mới nhập vào tổng tồn kho hiện tại.
    """
    global inventory_stock
    inventory_stock += amount
    print(f"Đã nhập thành công {amount} sản phẩm.")
    print(f"Tồn kho hiện tại: {inventory_stock}")

def calculate_final_price(quantity, price):
    """
    Tính toán và trả về tổng tiền hóa đơn sau khi đã áp dụng chiết khấu 10% (nếu có) và thuế VAT 8%.
    """
    total = quantity * price
    discount = 0.0
    
    if total >= 1000:
        discount = total * 0.1
        
    total_after_discount = total - discount
    vat = total_after_discount * 0.08
    final_total = total_after_discount + vat
    
    return final_total

def process_sale(quantity, price):
    """
    Kiểm tra điều kiện tồn kho, gọi hàm tính toán chi phí, cập nhật trạng thái hệ thống và in hóa đơn chi tiết.
    """
    global inventory_stock, total_revenue
    
    if quantity > inventory_stock:
        print(f"Lỗi: Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {inventory_stock}.")
        return
        
    final_total = calculate_final_price(quantity, price)
    
    inventory_stock -= quantity
    total_revenue += final_total
    
    total = quantity * price
    discount = 0.0
    if total >= 1000:
        discount = total * 0.1
    vat = (total - discount) * 0.08
    
    print("-> Hóa đơn chi tiết:")
    print(f"Số lượng: {quantity} | Đơn giá: ${float(price)}")
    print(f"Tạm tính: ${float(total)}")
    print(f"Giảm giá (10%): ${float(discount)}")
    print(f"Thuế VAT (8%): ${float(vat)}")
    print(f"Tổng thanh toán: ${float(final_total)}")
    print("Đã bán thành công!")

def print_report():
    """
    Hiển thị báo cáo tổng quan về số lượng tồn kho hiện tại và tổng doanh thu đã đạt được.
    """
    print("--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
    print(f"Tổng doanh thu: ${total_revenue}")