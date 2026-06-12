# Refactoring Plan (Kế hoạch tái cấu trúc):

# Quy tắc đặt tên (Naming Conventions - PEP 8): Tất cả các biến và hàm đều sử dụng định dạng snake_case để rõ nghĩa (ví dụ: player_id, calculate_actual_pay).

# Đơn trách nhiệm (Single Responsibility): Mỗi chức năng của Menu được bóc tách thành một hàm riêng biệt. 
# Việc tính toán lương thực nhận cũng được tách riêng thành một hàm phụ trợ calculate_actual_pay giúp dễ dàng kiểm thử (Unit Test).

# Mã nguồn tự giải thích (Docstrings): Bổ sung tài liệu chuẩn (Docstrings) dưới mỗi hàm thay vì dùng các dòng comment lộn xộn trong code, giúp mã nguồn luôn sạch.

# Logging Strategy (Chiến lược ghi Log):

# Hệ thống cấu hình thư viện logging ghi trực tiếp vào file roster_app.log.

# Format chuẩn: [Thời gian] - [Cấp độ Log] - [Tin nhắn].

# Cấp độ INFO dùng để ghi nhận các thao tác thành công (như xem danh sách, cập nhật lương).

# Cấp độ WARNING hoặc ERROR dùng khi người dùng nhập sai kiểu dữ liệu hoặc hệ thống bắt gặp dữ liệu lỗi.

# Phân tích Input/Output & Luồng xử lý cho hàm update_player_status:

# Input: Danh sách đội hình hiện tại (roster_list).

# Output: Không trả về (None). Cập nhật trực tiếp vào danh sách.

# Exceptions: ValueError khi người dùng nhập lương mới là chữ thay vì số.

# Pseudocode (Mã giả):

# Yêu cầu người dùng nhập mã tuyển thủ.

# Tìm mã tuyển thủ trong danh sách. Nếu không có, in lỗi và thoát hàm.

# Nếu tìm thấy, in thông tin hiện tại và hiển thị sub-menu (1. Đổi lương, 2. Đổi trạng thái).

# Nếu chọn đổi lương: Mở vòng lặp while, dùng try-except nhận số thực. Nếu số <= 0, bắt nhập lại. Cập nhật thành công thì thoát vòng lặp.

# Nếu chọn đổi trạng thái: Cho phép chọn 1 (Active) hoặc 2 (Benched).

# Ghi log INFO cho từng cập nhật thành công.


import logging

logging.basicConfig(
    filename='roster_app.log',
    level=logging.INFO,
    format='[%(asctime)s] - [%(levelname)s] - %(message)s'
)

def display_roster(roster_list):
    """
    Hiển thị danh sách đội hình tuyển thủ. 
    Bẫy lỗi KeyError nếu dữ liệu bị thiếu key 'status'.
    """
    if len(roster_list) == 0:
        print("Đội hình hiện đang trống.")
        logging.info("Coach viewed the team roster.")
        return

    print("\n--- ĐỘI HÌNH RIKKEI ESPORTS ---")
    print(f"{'ID':<8} | {'Tên tuyển thủ':<20} | {'Vị trí':<15} | {'Lương':<12} | {'Trạng thái'}")
    print("-" * 80)
    
    for player in roster_list:
        try:
            status = player["status"]
        except KeyError:
            status = "Unknown"
            
        if status == "Benched":
            display_name = f"{player['name']} [DỰ BỊ]"
        else:
            display_name = player['name']
            
        print(f"{player['player_id']:<8} | {display_name:<20} | {player.get('role', 'N/A'):<15} | {player.get('salary', 0):<12,.1f} | {status}")
        
    logging.info("Coach viewed the team roster.")

def sign_player(roster_list):
    """
    Chiêu mộ tuyển thủ mới.
    Bẫy lỗi ValueError để ép buộc lương phải là số dương.
    """
    print("\n--- CHIÊU MỘ TUYỂN THỦ MỚI ---")
    player_id = input("Nhập mã tuyển thủ: ").strip().upper()
    
    for p in roster_list:
        if p.get("player_id") == player_id:
            print(f"\nLỗi: Mã tuyển thủ {player_id} đã tồn tại.")
            logging.warning(f"Failed to sign player - Duplicate player ID {player_id}")
            return
            
    name = input("Nhập tên tuyển thủ: ").strip().title()
    role = input("Nhập vị trí thi đấu: ").strip().title()
    
    while True:
        raw_salary = input("Nhập mức lương hàng tháng: ").strip()
        try:
            salary = float(raw_salary)
            if salary <= 0:
                print("\nLương phải là số dương. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("\nLương phải là số. Vui lòng nhập lại.")
            logging.warning("Failed to sign player - Invalid salary input")
            
    new_player = {
        "player_id": player_id,
        "name": name,
        "role": role,
        "salary": salary,
        "status": "Active"
    }
    roster_list.append(new_player)
    
    print(f"\nThành công: Đã chiêu mộ tuyển thủ {name}.")
    logging.info(f"Signed new player {name} with salary {salary}")

def update_player_status(roster_list):
    """
    Cập nhật lương hoặc trạng thái thi đấu của một tuyển thủ cụ thể.
    """
    print("\n--- CẬP NHẬT LƯƠNG & TRẠNG THÁI THI ĐẤU ---")
    player_id = input("Nhập mã tuyển thủ cần cập nhật: ").strip().upper()
    
    target_player = None
    for p in roster_list:
        if p.get("player_id") == player_id:
            target_player = p
            break
            
    if not target_player:
        print(f"\nKhông tìm thấy tuyển thủ mang mã {player_id}.")
        logging.warning(f"Failed to update player - Player ID {player_id} not found")
        return
        
    print(f"\nTuyển thủ: {target_player['name']}")
    print(f"Vị trí: {target_player['role']}")
    print(f"Lương hiện tại: {target_player['salary']:,.1f}")
    print(f"Trạng thái hiện tại: {target_player.get('status', 'Unknown')}")
    
    print("\nBạn muốn cập nhật:")
    print("1. Cập nhật lương")
    print("2. Cập nhật trạng thái thi đấu")
    choice = input("Chọn chức năng cập nhật (1-2): ").strip()
    
    if choice == "1":
        while True:
            raw_salary = input("Nhập mức lương mới: ").strip()
            try:
                new_salary = float(raw_salary)
                if new_salary <= 0:
                    print("\nLương phải là số dương. Vui lòng nhập lại.")
                    continue
                old_salary = target_player['salary']
                target_player['salary'] = new_salary
                print(f"\nThành công: Đã cập nhật lương cho tuyển thủ {player_id}.")
                logging.info(f"Updated player {player_id} salary from {old_salary} to {new_salary}")
                break
            except ValueError:
                print("\nLương phải là số. Vui lòng nhập lại.")
    elif choice == "2":
        print("\nChọn trạng thái mới:")
        print("1. Active")
        print("2. Benched")
        status_choice = input("Nhập lựa chọn trạng thái (1-2): ").strip()
        
        if status_choice == "1":
            target_player['status'] = "Active"
            print(f"\nThành công: Đã cập nhật trạng thái cho tuyển thủ {player_id}.")
            logging.info(f"Updated player {player_id} status to Active")
        elif status_choice == "2":
            target_player['status'] = "Benched"
            print(f"\nThành công: Đã cập nhật trạng thái cho tuyển thủ {player_id}.")
            logging.info(f"Updated player {player_id} status to Benched")
        else:
            print("Lựa chọn không hợp lệ.")
    else:
        print("Lựa chọn không hợp lệ.")

def calculate_actual_pay(player_dict):
    """
    Hàm phụ trợ tính toán mức lương thực nhận. Tuyển thủ dự bị nhận 50%.
    """
    salary = player_dict["salary"]
    status = player_dict.get("status", "Unknown")
    
    if status == "Benched":
        return salary * 0.5
    return salary

def generate_payroll_report(roster_list):
    """
    Tạo báo cáo tổng quỹ lương hàng tháng.
    Bẫy lỗi KeyError nếu thiếu trường dữ liệu quan trọng như salary.
    """
    print("\n--- BÁO CÁO QUỸ LƯƠNG HÀNG THÁNG ---")
    
    if len(roster_list) == 0:
        print("Đội hình hiện đang trống. Tổng quỹ lương: 0.0")
        logging.info("Generated monthly payroll report. Total: 0.0")
        return

    print(f"{'ID':<8} | {'Tên tuyển thủ':<15} | {'Trạng thái':<10} | {'Lương gốc':<12} | {'Lương thực nhận'}")
    print("-" * 80)
    
    total_payroll = 0.0
    has_error = False
    
    for player in roster_list:
        try:
            actual_pay = calculate_actual_pay(player)
            total_payroll += actual_pay
            status = player.get("status", "Unknown")
            print(f"{player['player_id']:<8} | {player['name']:<15} | {status:<10} | {player['salary']:<12,.1f} | {actual_pay:,.1f}")
        except KeyError as e:
            print(f"Lỗi: Một tuyển thủ đang bị thiếu dữ liệu.")
            logging.error(f"Missing key while generating payroll report: {e.args[0]}")
            has_error = True
            
    print("-" * 80)
    print(f"Tổng quỹ lương hàng tháng: {total_payroll:,.1f}")
    
    if not has_error:
        logging.info(f"Generated monthly payroll report. Total: {total_payroll}")

def main():
    """
    Hàm điều khiển menu chính với vòng lặp vô hạn.
    """
    roster = [
        {
            "player_id": "P01",
            "name": "Faker",
            "role": "Mid Lane",
            "salary": 5000.0,
            "status": "Active"
        },
        {
            "player_id": "P02",
            "name": "Oner",
            "role": "Jungle",
            "salary": 3500.0,
            "status": "Active"
        },
        {
            "player_id": "P03",
            "name": "Ruler",
            "role": "ADC",
            "salary": 6000.0,
            "status": "Benched"
        }
    ]

    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ ĐỘI HÌNH RIKKEI ESPORTS =====")
        print("1. Xem đội hình thi đấu hiện tại")
        print("2. Chiêu mộ tuyển thủ mới")
        print("3. Cập nhật lương & Trạng thái thi đấu")
        print("4. Báo cáo quỹ lương hàng tháng")
        print("5. Thoát hệ thống")
        print("==================================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        match choice:
            case "1":
                display_roster(roster)
            case "2":
                sign_player(roster)
            case "3":
                update_player_status(roster)
            case "4":
                generate_payroll_report(roster)
            case "5":
                print("Hệ thống kết thúc. Hẹn gặp lại!")
                logging.info("System closed by user.")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại.")

if __name__ == "__main__":
    main()