# Tại sao lại dùng combinations (Tổ hợp) thay vì permutations (Chỉnh hợp)?  trận đấu giữa "Đội A và Đội B" cũng chính là trận đấu giữa "Đội B và Đội A" (không phân biệt thứ tự). 
# Lệnh combinations giúp ta lấy ra các cặp đấu duy nhất mà không bị lặp lại ngược chiều, tránh việc xếp lịch dư thừa.
#  Để giải quyết việc sinh mã ID tự động (thêm số 0 ở đầu và điền chữ X nếu tên đội quá ngắn), Python cung cấp sẵn cú pháp định dạng trực tiếp vào F-String. 
#  Cú pháp {:02d} ép các số từ 1 đến 9 thành "01", "02". Cú pháp {team1:X<3} sẽ lấy giá trị biến, căn lề trái (<) trong phạm vi 3 ký tự, và tự động nhét chữ X vào các khoảng trống nếu tên đội bị thiếu độ dài.

# Bẫy dữ liệu (Edge Cases): Hàm nhập đội tuyển sử dụng một List tạm cùng câu lệnh kiểm tra not in để chặn đứng ngay lập tức người dùng cố tình nhập hai đội trùng tên 
# Các hàm tạo lịch và sinh mã ID đều dùng if len() == 0 chặn ngay ở dòng đầu tiên để báo lỗi nếu thao tác sai trình tự.

import itertools

teams_list = []
match_schedule = []

def input_teams():
    """Nhập danh sách đội tuyển, làm sạch khoảng trắng và loại bỏ các đội bị nhập trùng lặp."""
    global teams_list
    print("--- NHẬP DANH SÁCH ---")
    raw_input = input("Nhập các đội (cách nhau bởi dấu phẩy): ")
    
    temp_teams = [team.strip().upper() for team in raw_input.split(',')]
    teams_list = []
    
    for team in temp_teams:
        if len(team) > 0 and team not in teams_list:
            teams_list.append(team)
            
    print(f"Đã ghi nhận {len(teams_list)} đội: {teams_list}")

def generate_schedule():
    """Tạo lịch thi đấu vòng tròn một lượt sử dụng itertools.combinations và lưu vào danh sách."""
    global match_schedule
    if len(teams_list) < 2:
        print("Lỗi: Cần tối thiểu 2 đội để tạo lịch thi đấu.")
        return

    print("--- LỊCH THI ĐẤU VÒNG BẢNG ---")
    match_schedule = []
    matches = itertools.combinations(teams_list, 2)
    
    for team_a, team_b in matches:
        match_str = f"{team_a} vs {team_b}"
        match_schedule.append(match_str)
        
    for i in range(len(match_schedule)):
        print(f"{i + 1}. {match_schedule[i]}")
        
    print(f"Tổng số trận đấu: {len(match_schedule)} trận.")

def generate_match_ids():
    """Sinh mã ID duy nhất cho từng trận đấu bằng kỹ thuật cắt chuỗi và padding của F-String."""
    if len(match_schedule) == 0:
        print("Vui lòng tạo lịch thi đấu trước khi sinh mã ID.")
        return

    print("--- MÃ TRẬN ĐẤU (MATCH ID) ---")
    for i in range(len(match_schedule)):
        teams = match_schedule[i].split(" vs ")
        team1 = teams[0][:3]
        team2 = teams[1][:3]
        
        match_id = f"M{i + 1:02d}-{team1:X<3}-{team2:X<3}"
        print(f"Trận {i + 1} ({match_schedule[i]}) -> ID: {match_id}")

def main():
    while True:
        print("\n=============== ESPORTS MATCHMAKER ===============")
        print("1. Nhập danh sách Đội tuyển")
        print("2. Tạo lịch thi đấu (Combinations)")
        print("3. Tạo mã trận đấu tự động (F-String & Cắt chuỗi)")
        print("4. Đóng hệ thống")
        print("==================================================")
        
        choice = input("Chọn chức năng (1-4): ").strip()
        
        if choice == "1":
            input_teams()
        elif choice == "2":
            generate_schedule()
        elif choice == "3":
            generate_match_ids()
        elif choice == "4":
            print("Đóng hệ thống. Hẹn gặp lại tại giải đấu!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")

if __name__ == "__main__":
    main()