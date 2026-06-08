available_seats = 50
flight_revenue = 0.0
BASE_PRICE = 2000.0

def main():
    while True:
        print("\n================ SKYBOOKING SYSTEM ================")
        print("Chuyến bay: VN2026 | Khởi hành: Hà Nội")
        print("1. Đặt vé máy bay")
        print("2. Hủy vé & Hoàn tiền")
        print("3. Xem tình trạng chuyến bay")
        print("4. Đóng hệ thống")
        print("===================================================")
        
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
    
def calculate_ticket_price(quantity, ticket_class):
    """
    Tính toán chi phí đặt vé dựa trên số lượng, hạng ghế và trả về tổng tiền (bao gồm 5% phí dịch vụ).
    
    :param quantity: int
    :param ticket_class: int
    :return: float
    """
    if ticket_class == 1:
        price_per_ticket = BASE_PRICE
    else:
        price_per_ticket = BASE_PRICE * 1.5
        
    total_price = quantity * price_per_ticket
    service_fee = total_price * 0.05
    final_total = total_price + service_fee
    
    return final_total

def process_booking(quantity, ticket_class):
    """
    Xử lý logic đặt vé: kiểm tra ghế trống, trừ ghế, cộng doanh thu và in biên lai.
    """
    global available_seats, flight_revenue
    
    if quantity > available_seats:
        print(f"Rất tiếc, chuyến bay chỉ còn {available_seats} chỗ trống.")
        return
        
    final_total = calculate_ticket_price(quantity, ticket_class)
    
    available_seats -= quantity
    flight_revenue += final_total
    
    print("-> Xác nhận đặt chỗ:")
    if ticket_class == 1:
        class_name = "Economy"
        base_calc = BASE_PRICE
    else:
        class_name = "Business"
        base_calc = BASE_PRICE * 1.5
        
    print(f"Số lượng: {quantity} | Hạng: {class_name}")
    print(f"Tạm tính: ${quantity * base_calc}")
    print(f"Phí dịch vụ (5%): ${final_total - (quantity * base_calc)}")
    print(f"Tổng thanh toán: ${final_total}")
    print(f"Đặt vé thành công! Ghế trống còn lại: {available_seats}")

def process_refund(quantity):
    """
    kiểm tra số lượng hợp lệ, hoàn 80% tiền và thu hồi ghế.
    """
    global available_seats, flight_revenue
    
    if available_seats + quantity > 50:
        print("Lỗi: Số lượng vé hủy vượt quá số vé đã bán ra.")
        return
        
    refund_amount = quantity * (BASE_PRICE * 0.8)
    
    available_seats += quantity
    flight_revenue -= refund_amount
    
    print(f"Hủy vé thành công. Hệ thống đã hoàn lại: ${refund_amount} (80% giá cơ bản).")
    print(f"Ghế trống hiện tại: {available_seats}")

def display_flight_status():
    """
    Hiển thị báo cáo chi tiết về tình trạng ghế ngồi và tổng doanh thu hiện tại của chuyến bay.
    """
    booked_seats = 50 - available_seats
    print("--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---")
    print("Sức chứa tối đa: 50")
    print(f"Ghế đã đặt: {booked_seats}")
    print(f"Ghế trống: {available_seats}")
    print(f"Tổng doanh thu hiện tại: ${flight_revenue}")

