# Ứng dụng Logging: Thay vì dùng print() thông thường, thư viện logging được cấu hình để tự động ghi lại toàn bộ lịch sử thao tác của người dùng,
# bao gồm cả các cảnh báo (WARNING) và lỗi nghiêm trọng (ERROR) vào file tournament_app.log. Điều này giúp ban tổ chức dễ dàng truy vết nguyên nhân khi phần mềm gặp sự cố.

# Bẫy lỗi nhập liệu & KeyError: Khi trọng tài nhập tỷ số, chương trình bắt buộc phải nhận vào dữ liệu tạm thời (raw input),
# sau đó đưa qua khối try...except ValueError để kiểm tra. Nếu trọng tài lỡ gõ chữ thay vì số, hệ thống lập tức chặn lại và bắt nhập lại chứ không làm sập chương trình. 
# khối try...except KeyError ở hàm tìm người chiến thắng sẽ phòng hờ việc API trả về dữ liệu thiếu các khóa như score_a hay status.

# Mô hình hóa và Unit Test: Logic quan trọng nhất là tìm ra đội chiến thắng được tách thành một hàm riêng biệt (determine_winner).
# Sự tách biệt này cho phép chúng ta viết một file kiểm thử độc lập (test_matches.py) để giả lập các kịch bản (đội A thắng, hòa, chưa đá)
# tự động xác nhận tính chính xác của thuật toán mà không cần phải mở giao diện phần mềm lên gõ thủ công.


import logging

logging.basicConfig(
    filename='tournament_app.log',
    level=logging.INFO,
    format='[%(asctime)s] - [%(levelname)s] - %(message)s'
)

def display_matches(match_list):
    """
    Hiển thị danh sách các trận đấu dưới dạng bảng và ghi log xác nhận thao tác.
    """
    if len(match_list) == 0:
        print("Hiện chưa có trận đấu nào trong hệ thống.")
        logging.info("User viewed the match list (empty).")
        return

    print("\n--- LỊCH THI ĐẤU & KẾT QUẢ ---")
    print(f"{'Mã trận':<10} | {'Đội A':<15} | {'Đội B':<15} | {'Tỷ số':<7} | {'Trạng thái'}")
    print("-" * 70)
    
    for match in match_list:
        try:
            score_str = f"{match['score_a']}-{match['score_b']}"
            print(f"{match['match_id']:<10} | {match['team_a']:<15} | {match['team_b']:<15} | {score_str:<7} | {match['status']}")
        except KeyError:
            print("Phát hiện dữ liệu trận đấu bị lỗi cấu trúc.")
            
    logging.info("User viewed the match list.")

def add_match(match_list):
    """
    Thêm một trận đấu mới vào hệ thống, kiểm tra tính hợp lệ của mã trận và tên đội.
    """
    print("\n--- THÊM TRẬN ĐẤU MỚI ---")
    
    match_id = input("Nhập mã trận đấu: ").strip()
    if len(match_id) == 0:
        print("Mã trận đấu không được để trống.")
        logging.warning("User tried to add a match with empty match ID.")
        return

    for match in match_list:
        if match.get("match_id") == match_id:
            print(f"\nLỗi: Mã trận đấu {match_id} đã tồn tại.")
            logging.warning(f"Match ID {match_id} already exists.")
            return

    team_a = input("Nhập tên Đội A: ").strip()
    team_b = input("Nhập tên Đội B: ").strip()

    if len(team_a) == 0 or len(team_b) == 0:
        print("\nTên đội không được để trống.")
        logging.warning("User tried to add a match with empty team name.")
        return

    new_match = {
        "match_id": match_id,
        "team_a": team_a,
        "team_b": team_b,
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }
    
    match_list.append(new_match)
    print(f"\nThành công: Đã thêm trận đấu {match_id}.")
    logging.info(f"Match {match_id} added successfully")

def update_score(match_list):
    """
    Cập nhật tỷ số, bẫy lỗi ValueError khi ép kiểu và xử lý logic xác nhận trạng thái.
    """
    print("\n--- CẬP NHẬT TỶ SỐ TRẬN ĐẤU ---")
    match_id = input("Nhập mã trận đấu cần cập nhật: ").strip()

    target_match = None
    for match in match_list:
        if match.get("match_id") == match_id:
            target_match = match
            break

    if not target_match:
        print(f"\nKhông tìm thấy trận đấu mang mã {match_id}.")
        logging.warning(f"User tried to update non-existing match {match_id}")
        return

    print(f"\nTrận đấu: {target_match['team_a']} vs {target_match['team_b']} ({target_match['status']})")

    while True:
        raw_a = input("Nhập điểm Đội A: ")
        try:
            score_a = int(raw_a)
            if score_a < 0:
                print("\nĐiểm số phải lớn hơn hoặc bằng 0.")
                logging.error(f"Negative score input detected: {score_a}")
                continue
            break
        except ValueError:
            print("\nĐiểm số phải là số nguyên. Vui lòng nhập lại.")
            logging.error(f"Invalid score input. Error: invalid literal for int() with base 10: '{raw_a}'")

    while True:
        raw_b = input("Nhập điểm Đội B: ")
        try:
            score_b = int(raw_b)
            if score_b < 0:
                print("\nĐiểm số phải lớn hơn hoặc bằng 0.")
                logging.error(f"Negative score input detected: {score_b}")
                continue
            break
        except ValueError:
            print("\nĐiểm số phải là số nguyên. Vui lòng nhập lại.")
            logging.error(f"Invalid score input. Error: invalid literal for int() with base 10: '{raw_b}'")

    if score_a == 0 and score_b == 0:
        confirm = input("\nTỷ số đang là 0-0. Trọng tài có xác nhận trận đã hoàn thành không? (y/n): ").strip().lower()
        if confirm == 'y':
            target_match['status'] = "Completed"
        else:
            target_match['status'] = "Pending"
    else:
        target_match['status'] = "Completed"

    target_match['score_a'] = score_a
    target_match['score_b'] = score_b

    print(f"\nThành công: Đã cập nhật tỷ số trận đấu {match_id}.")
    logging.info(f"Match {match_id} score updated successfully")

def determine_winner(match):
    """
    Hàm phụ trợ phân tích dữ liệu trận đấu và trả về kết quả chiến thắng.
    """
    try:
        if match["status"] == "Pending":
            return "Not Started"
            
        if match["score_a"] > match["score_b"]:
            return match["team_a"]
        elif match["score_b"] > match["score_a"]:
            return match["team_b"]
        else:
            return "Draw"
    except KeyError:
        return "Data Error"

def generate_report(match_list):
    """
    Duyệt danh sách giải đấu, in báo cáo thống kê và gọi hàm phụ trợ xác định người thắng.
    """
    print("\n--- BÁO CÁO THỐNG KÊ GIẢI ĐẤU ---")
    completed_count = 0

    for match in match_list:
        if match.get("status") == "Completed":
            completed_count += 1
            winner = determine_winner(match)
            score_str = f"{match['score_a']}-{match['score_b']}"
            print(f"{match['match_id']}: {match['team_a']} {score_str} {match['team_b']} | Kết quả: {winner}")

    if completed_count == 0:
        print("Chưa có trận đấu nào hoàn thành.")
        
    print(f"\nTổng số trận đã hoàn thành: {completed_count}")
    logging.info("User generated tournament report.")

def main():
    """
    Hệ thống menu điều phối chính với vòng lặp vô hạn.
    """
    matches = [
        {
            "match_id": "M01",
            "team_a": "T1",
            "team_b": "GenG",
            "score_a": 2,
            "score_b": 1,
            "status": "Completed"
        },
        {
            "match_id": "M02",
            "team_a": "JDG",
            "team_b": "BLG",
            "score_a": 0,
            "score_b": 0,
            "status": "Pending"
        }
    ]

    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ GIẢI ĐẤU RIKKEI ESPORTS =====")
        print("1. Hiển thị lịch thi đấu & Kết quả")
        print("2. Thêm trận đấu mới")
        print("3. Cập nhật tỷ số trận đấu")
        print("4. Báo cáo thống kê")
        print("5. Thoát chương trình")
        print("==================================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()

        match choice:
            case "1":
                display_matches(matches)
            case "2":
                add_match(matches)
            case "3":
                update_score(matches)
            case "4":
                generate_report(matches)
            case "5":
                print("Đóng hệ thống. Hẹn gặp lại!")
                logging.info("System closed by user.")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 5.")
                logging.warning("Invalid menu choice selected")

if __name__ == "__main__":
    main()