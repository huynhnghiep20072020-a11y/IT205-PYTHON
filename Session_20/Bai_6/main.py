import logging

logging.basicConfig(
    filename='arena_tickets.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def display_tickets(tickets):
    """Hiển thị danh sách vé dưới dạng bảng và bẫy lỗi KeyError nếu thiếu dữ liệu."""
    print("\n--- DANH SÁCH VÉ ---")
    if len(tickets) == 0:
        print("Hiện chưa có vé nào trong hệ thống.")
        return

    print(f"{'Mã Vé':<7} | {'Tên Khách Hàng':<15} | {'Giá Vé':<7} | {'Chỗ Ngồi':<10} | {'Trạng Thái'}")
    print("-" * 65)

    for ticket in tickets:
        try:
            seat_info = f"{ticket['seat'][0]}-{ticket['seat'][1]}"
            status_display = ticket['status']
            
            if status_display == "Cancelled":
                status_display += " [ĐÃ HỦY]"

            print(f"{ticket['ticket_id']:<7} | {ticket['buyer_name']:<15} | {ticket['price']:<7.1f} | {seat_info:<10} | {status_display}")
        except KeyError:
            print("Lỗi: Một vé đang bị thiếu dữ liệu, vui lòng kiểm tra lại.")
            print("-" * 65)
            logging.error("Missing key while displaying ticket: 'seat'")
            return

    print("-" * 65)
    logging.info("User viewed ticket list.")

def book_ticket(tickets):
    """Thêm vé mới vào hệ thống, kiểm tra mã trùng và bẫy lỗi nhập số."""
    print("\n--- ĐẶT VÉ MỚI ---")
    ticket_id = input("Nhập mã vé: ").strip().upper()

    for ticket in tickets:
        if ticket.get("ticket_id") == ticket_id:
            print(f"Lỗi: Mã vé {ticket_id} đã tồn tại.")
            logging.warning(f"Duplicate ticket ID entered: {ticket_id}")
            return

    buyer_name = input("Nhập tên khách hàng: ").strip().title()

    while True:
        try:
            price_input = input("Nhập giá vé: ").strip()
            price = float(price_input)
            if price <= 0:
                print("\nGiá vé phải lớn hơn 0. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("\nGiá vé phải là số. Vui lòng nhập lại.")
            logging.warning("Invalid price input while booking ticket")

    seat_row = input("Nhập khu vực ghế: ").strip().upper()

    while True:
        try:
            seat_num_input = input("Nhập số ghế: ").strip()
            seat_number = int(seat_num_input)
            break
        except ValueError:
            print("\nSố ghế phải là số nguyên. Vui lòng nhập lại.")

    new_ticket = {
        "ticket_id": ticket_id,
        "buyer_name": buyer_name,
        "price": price,
        "status": "Booked",
        "seat": (seat_row, seat_number)
    }

    tickets.append(new_ticket)
    print(f"\nThành công: Đã đặt vé {ticket_id} cho khách hàng {buyer_name}.")
    logging.info(f"Booked new ticket {ticket_id} for {buyer_name}")

def change_seat(tickets):
    """Tìm vé theo mã và cập nhật chỗ ngồi bằng cách ghi đè Tuple mới."""
    print("\n--- ĐỔI CHỖ NGỒI ---")
    ticket_id = input("Nhập mã vé cần đổi chỗ: ").strip().upper()

    target_ticket = None
    for ticket in tickets:
        if ticket.get("ticket_id") == ticket_id:
            target_ticket = ticket
            break

    if not target_ticket:
        print(f"\nKhông tìm thấy vé mang mã {ticket_id}.")
        logging.warning(f"Change seat failed - Ticket {ticket_id} not found")
        return

    new_row = input("Nhập khu vực ghế mới: ").strip().upper()

    while True:
        try:
            new_num_input = input("Nhập số ghế mới: ").strip()
            new_number = int(new_num_input)
            break
        except ValueError:
            print("\nSố ghế phải là số nguyên. Vui lòng nhập lại.")

    target_ticket["seat"] = (new_row, new_number)
    print(f"\nThành công: Đã đổi chỗ vé {ticket_id} sang {new_row}-{new_number}.")
    logging.info(f"Seat changed for ticket {ticket_id} to {new_row}-{new_number}")

def cancel_ticket(tickets):
    """Chuyển trạng thái của vé thành Cancelled dựa trên mã vé."""
    print("\n--- HỦY VÉ ---")
    ticket_id = input("Nhập mã vé cần hủy: ").strip().upper()

    target_ticket = None
    for ticket in tickets:
        if ticket.get("ticket_id") == ticket_id:
            target_ticket = ticket
            break

    if not target_ticket:
        print(f"\nKhông tìm thấy vé mang mã {ticket_id}.")
        logging.warning(f"Cancel ticket failed - Ticket {ticket_id} not found")
        return

    if target_ticket.get("status") == "Cancelled":
        print(f"\nVé {ticket_id} đã ở trạng thái Cancelled trước đó.")
        return

    target_ticket["status"] = "Cancelled"
    print(f"\nThành công: Vé {ticket_id} đã được hủy.")
    logging.warning(f"Ticket {ticket_id} has been cancelled.")

def calculate_total_revenue(ticket_list):
    """Hàm phụ trợ tính tổng doanh thu chỉ từ các vé có trạng thái Booked."""
    total = 0.0
    for ticket in ticket_list:
        if ticket.get("status") == "Booked":
            total += float(ticket["price"])
    return total

def calculate_revenue(tickets):
    """Báo cáo tổng doanh thu và xử lý lỗi thiếu dữ liệu thông qua KeyError."""
    print("\n--- BÁO CÁO DOANH THU ---")
    booked_count = 0
    cancelled_count = 0

    for ticket in tickets:
        if ticket.get("status") == "Booked":
            booked_count += 1
        elif ticket.get("status") == "Cancelled":
            cancelled_count += 1

    try:
        total_revenue = calculate_total_revenue(tickets)
        print(f"Tổng số vé đã đặt: {booked_count}")
        print(f"Tổng số vé đã hủy: {cancelled_count}")
        print(f"Tổng doanh thu hợp lệ: {total_revenue:,.1f}")
        logging.info(f"Revenue report generated. Total: {total_revenue}")
    except KeyError:
        print("Lỗi: Một vé đang bị thiếu dữ liệu doanh thu.")
        print("Tổng doanh thu hợp lệ: 0.0")
        logging.error("Missing key while calculating revenue: 'price'")

def main():
    """Hệ thống điều hướng menu chính bằng cấu trúc match-case."""
    ticket_db = [
        {"ticket_id": "T01", "buyer_name": "Nguyen Van A", "price": 500.0, "status": "Booked", "seat": ("A", 1)},
        {"ticket_id": "T02", "buyer_name": "Tran Thi B", "price": 300.0, "status": "Cancelled", "seat": ("B", 5)},
        {"ticket_id": "T03", "buyer_name": "Le Van C", "price": 500.0, "status": "Booked", "seat": ("A", 2)}
    ]

    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ VÉ RIKKEI ESPORTS ===")
        print("1. Xem danh sách vé đã bán")
        print("2. Đặt vé mới")
        print("3. Đổi chỗ ngồi (Cập nhật vé)")
        print("4. Hủy vé")
        print("5. Báo cáo doanh thu")
        print("6. Thoát chương trình")
        print("========================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()

        match choice:
            case "1":
                display_tickets(ticket_db)
            case "2":
                book_ticket(ticket_db)
            case "3":
                change_seat(ticket_db)
            case "4":
                cancel_ticket(ticket_db)
            case "5":
                calculate_revenue(ticket_db)
            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý vé Rikkei Esports.")
                logging.info("Ticket management system closed.")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 6.")

if __name__ == "__main__":
    main()