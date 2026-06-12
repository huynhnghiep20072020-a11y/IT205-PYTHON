# Bẫy lỗi bằng try-except ValueError: Các tính năng yêu cầu nhập số (Đầu tư, Rút vốn, Cập nhật phong độ) đều được bọc trong vòng lặp while True.
# Nếu người dùng vô tình nhập chữ cái, hệ thống bắt gọn lỗi, yêu cầu nhập lại thay vì thoát đột ngột.

# Kỹ thuật DRY (Don't Repeat Yourself) qua Helper Functions: Việc lặp đi lặp lại thuật toán tìm vị trí tuyển thủ được gộp thành một hàm duy nhất là find_player_by_id. 
#  logic tính phí rút tiền được đẩy ra hàm calc_actual_withdrawal để phục vụ cho công tác kiểm thử (Unit Test) tự động.

# An toàn dữ liệu với phương thức .get(): Mọi quá trình trích xuất thông tin từ Dictionary đều dùng hàm .get() kèm theo giá trị mặc định. Bằng cách này,
# kể cả khi dữ liệu từ API bị khuyết thiếu (như mất trường fan_tokens), ứng dụng vẫn lấy số 0 để chạy tiếp thay vì ném ra lỗi KeyError.

import logging

logging.basicConfig(
    filename='fantasy_league.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def find_player_by_id(players: list, player_id: str) -> int:
    """
    Tìm kiếm vị trí của tuyển thủ trong mảng bằng mã ID.
    Trả về chỉ mục (index) nếu tìm thấy, ngược lại trả về -1.
    """
    player_id = player_id.strip().upper()
    for i in range(len(players)):
        if players[i].get("player_id", "").upper() == player_id:
            return i
    return -1

def calc_actual_withdrawal(withdraw_amount: float) -> float:
    """
    Tính số token thực nhận sau khi trừ 10% phí giao dịch.
    """
    if withdraw_amount < 0:
        raise ValueError("Số lượng rút không được là số âm.")
    return float(withdraw_amount * 0.9)

def display_market(players: list) -> None:
    """
    Hiển thị sàn giao dịch tuyển thủ và phân loại trạng thái đầu tư.
    """
    if len(players) == 0:
        print("\nSàn giao dịch hiện chưa có tuyển thủ nào.")
        logging.info("User viewed the player market (empty).")
        return

    print("\n--- SÀN GIAO DỊCH TUYỂN THỦ ---")
    print(f"{'ID':<8} | {'Tên tuyển thủ':<15} | {'Giá trị thị trường':<20} | {'Fan Token':<10} | {'Điểm trận':<10} | {'Hệ số':<6} | {'Trạng thái đầu tư'}")
    print("-" * 105)

    for p in players:
        p_id = p.get("player_id", "Unknown")
        name = p.get("name", "Unknown")
        market_value = p.get("market_value", 0)
        fan_tokens = p.get("fan_tokens", 0)
        match_points = p.get("match_points", 0)
        form = p.get("form_multiplier", 1.0)

        if fan_tokens == 0:
            status = "Chưa có người đầu tư"
        elif fan_tokens <= 1000:
            status = "Đang thu hút"
        else:
            status = "Tuyển thủ Hot"

        print(f"{p_id:<8} | {name:<15} | {market_value:<20,} | {fan_tokens:<10,} | {match_points:<10,} | {form:<6} | {status}")
    
    logging.info("User viewed the player market.")

def invest_tokens(players: list) -> None:
    """
    Đầu tư Fan Token vào tuyển thủ với cơ chế bẫy lỗi nhập số và cập nhật biến đổi.
    """
    print("\n--- ĐẦU TƯ FAN TOKEN ---")
    player_id = input("Nhập mã tuyển thủ: ")
    index = find_player_by_id(players, player_id)

    if index == -1:
        print("\nKhông tìm thấy tuyển thủ!")
        logging.warning(f"Invest failed - Player {player_id.strip().upper()} not found")
        return

    while True:
        raw_token = input("Nhập số token muốn đầu tư: ").strip()
        try:
            tokens = int(raw_token)
            if tokens <= 0:
                print("\nSố token phải là số nguyên dương. Vui lòng nhập lại.")
                continue
            
            players[index]["fan_tokens"] = players[index].get("fan_tokens", 0) + tokens
            name = players[index].get("name", "Unknown")
            p_id = players[index].get("player_id", "Unknown")
            
            print(f"\nThành công: Đã đầu tư {tokens} token vào tuyển thủ {p_id}.")
            print(f"Số Fan Token hiện tại của {name}: {players[index]['fan_tokens']:,}")
            
            logging.info(f"Invested {tokens} tokens into {p_id}")
            break
        except ValueError:
            print("\nSố token phải là số nguyên dương. Vui lòng nhập lại.")
            logging.warning("Invalid token input while investing")

def withdraw_tokens(players: list) -> None:
    """
    Rút vốn Fan Token, tính toán 10% phí giao dịch tự động thông qua helper function.
    """
    print("\n--- RÚT VỐN FAN TOKEN ---")
    player_id = input("Nhập mã tuyển thủ: ")
    index = find_player_by_id(players, player_id)

    if index == -1:
        print("\nKhông tìm thấy tuyển thủ!")
        logging.warning(f"Withdraw failed - Player {player_id.strip().upper()} not found")
        return

    current_tokens = players[index].get("fan_tokens", 0)
    name = players[index].get("name", "Unknown")
    p_id = players[index].get("player_id", "Unknown")

    while True:
        raw_token = input("Nhập số token muốn rút: ").strip()
        try:
            tokens_to_withdraw = int(raw_token)
            if tokens_to_withdraw <= 0:
                print("\nSố token phải là số nguyên dương. Vui lòng nhập lại.")
                continue
            
            if tokens_to_withdraw > current_tokens:
                print("\nKhông thể rút. Số token muốn rút vượt quá số Fan Token hiện có.")
                print(f"Fan Token hiện có của {name}: {current_tokens:,}")
                logging.warning("Withdraw failed - Amount exceeds current fan tokens")
                return
            
            actual_received = calc_actual_withdrawal(float(tokens_to_withdraw))
            fee = float(tokens_to_withdraw) - actual_received
            
            players[index]["fan_tokens"] = current_tokens - tokens_to_withdraw
            
            print(f"\nThành công: Đã rút {tokens_to_withdraw} token khỏi tuyển thủ {p_id}.")
            print(f"Phí giao dịch 10%: {fee} token")
            print(f"Số token thực nhận về ví: {actual_received} token")
            print(f"Fan Token còn lại của {name}: {players[index]['fan_tokens']:,}")
            
            logging.info(f"Withdrawn {tokens_to_withdraw} tokens from {p_id}. Actual received: {actual_received}")
            break
        except ValueError:
            print("\nSố token phải là số nguyên. Vui lòng nhập lại.")
            logging.warning("Invalid token input while withdrawing")

def update_form(players: list) -> None:
    """
    Cập nhật hệ số phong độ cho tuyển thủ với điều kiện giới hạn an toàn tử 0.5 đến 2.5.
    """
    print("\n--- CẬP NHẬT HỆ SỐ PHONG ĐỘ ---")
    player_id = input("Nhập mã tuyển thủ: ")
    index = find_player_by_id(players, player_id)

    if index == -1:
        print("\nKhông tìm thấy tuyển thủ!")
        logging.warning(f"Update form failed - Player {player_id.strip().upper()} not found")
        return

    name = players[index].get("name", "Unknown")
    p_id = players[index].get("player_id", "Unknown")

    while True:
        raw_form = input("Nhập hệ số phong độ mới (0.5 - 2.5): ").strip()
        try:
            form_multiplier = float(raw_form)
            if form_multiplier < 0.5 or form_multiplier > 2.5:
                print("\nHệ số phong độ chỉ được nằm trong khoảng 0.5 đến 2.5.")
                continue
            
            players[index]["form_multiplier"] = form_multiplier
            
            print(f"\nThành công: Đã cập nhật hệ số phong độ cho {name}.")
            print(f"Hệ số mới: x{form_multiplier}")
            
            logging.info(f"Updated form multiplier for {p_id} to {form_multiplier}")
            break
        except ValueError:
            print("\nHệ số phong độ phải là số thực. Vui lòng nhập lại.")

def calculate_match_points(players: list) -> None:
    """
    Tính điểm thưởng sau trận đấu dựa trên điểm gốc và hệ số phong độ của người chơi.
    """
    print("\n--- CHẤM ĐIỂM SAU TRẬN ĐẤU ---")
    player_id = input("Nhập mã tuyển thủ: ")
    index = find_player_by_id(players, player_id)

    if index == -1:
        print("\nKhông tìm thấy tuyển thủ!")
        logging.warning(f"Calculate points failed - Player {player_id.strip().upper()} not found")
        return

    name = players[index].get("name", "Unknown")
    p_id = players[index].get("player_id", "Unknown")
    form_multiplier = players[index].get("form_multiplier", 1.0)

    while True:
        raw_points = input("Nhập điểm gốc của trận đấu: ").strip()
        try:
            base_points = float(raw_points)
            if base_points < 0:
                print("\nĐiểm gốc phải lớn hơn hoặc bằng 0. Vui lòng nhập lại.")
                continue
            
            earned_points = base_points * form_multiplier
            players[index]["match_points"] = players[index].get("match_points", 0) + int(earned_points)
            
            print(f"\n>> Tuyển thủ {name} nhận được {earned_points} điểm (Hệ số x{form_multiplier}).")
            print(f"Tổng điểm: {players[index]['match_points']:,}")
            
            logging.info(f"Added {earned_points} match points to {p_id}")
            break
        except ValueError:
            print("\nĐiểm gốc phải là số. Vui lòng nhập lại.")

def main() -> None:
    """
    Hàm chính điều khiển luồng menu và khởi tạo dữ liệu giả lập hệ thống Fantasy League.
    """
    players_data = [
        {
            "player_id": "T101",
            "name": "Faker",
            "market_value": 5000,
            "fan_tokens": 1500,
            "match_points": 0,
            "form_multiplier": 1.0
        },
        {
            "player_id": "GEN01",
            "name": "Chovy",
            "market_value": 4800,
            "fan_tokens": 800,
            "match_points": 500,
            "form_multiplier": 1.2
        },
        {
            "player_id": "DRX01",
            "name": "Deft",
            "market_value": 3000,
            "fan_tokens": 0,
            "match_points": 0,
            "form_multiplier": 0.8
        }
    ]

    while True:
        print("\n===== HỆ THỐNG RIKKEI ESPORTS FANTASY =====")
        print("1. Xem Sàn Giao Dịch Tuyển Thủ")
        print("2. Đầu tư Fan Token")
        print("3. Rút vốn (Hoàn trả Token)")
        print("4. Biến động phong độ (Cập nhật hệ số)")
        print("5. Chấm điểm sau trận đấu")
        print("6. Thoát hệ thống")
        print("==================================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()

        match choice:
            case "1":
                display_market(players_data)
            case "2":
                invest_tokens(players_data)
            case "3":
                withdraw_tokens(players_data)
            case "4":
                update_form(players_data)
            case "5":
                calculate_match_points(players_data)
            case "6":
                print("\nĐóng hệ thống Rikkei Esports Fantasy.")
                logging.info("System closed by user.")
                break
            case _:
                print("\nLựa chọn không hợp lệ, vui lòng chọn từ 1 đến 6.")

if __name__ == "__main__":
    main()