# 1. Phân tích module/package

# main.py: Chứa menu điều hướng chính của game bằng vòng lặp while True và cấu trúc match-case.

# data/players.py: Chứa dữ liệu danh sách người chơi khởi tạo ban đầu.

# utils/player_utils.py: Chứa các hàm dùng chung để tìm kiếm, chuẩn hóa mã người chơi và lấy trạng thái HP.

# utils/item_utils.py: Xử lý logic mở rương báu ngẫu nhiên và giao dịch mua bán vật phẩm trong cửa hàng.

# utils/battle_utils.py: Xử lý logic tính toán sát thương, trừ HP và cộng vàng khi chiến đấu với quái vật.

# reports/dungeon_report.py: Xử lý logic hiển thị danh sách người chơi và tính toán bảng xếp hạng dựa trên nhiều tiêu chí (Level, Gold, HP).

# 2. Phân tích Input/Output của các hàm cốt lõi

# find_player(records, player_id)

# Input: Danh sách người chơi và mã người chơi nhập từ bàn phím.

# Output: Dictionary của người chơi nếu tìm thấy, ngược lại trả về None.

# Module: utils/player_utils.py

# display_players(records)

# Input: Danh sách người chơi.

# Output: Hiển thị danh sách ra màn hình kèm trạng thái sức khỏe hiện tại.

# Module: reports/dungeon_report.py

# buy_item(records)

# Input: Danh sách người chơi. Yêu cầu nhập mã người chơi và tên vật phẩm.

# Output: Cập nhật lại số vàng và túi đồ của người chơi.

# Module: utils/item_utils.py

# 3. Đề xuất giải pháp Modular Design
# Thay vì lặp lại đoạn code tìm kiếm người chơi bằng vòng lặp for ở chức năng mở rương,
# mua vật phẩm và chiến đấu, ta định nghĩa hàm find_player(records, player_id) tại player_utils.py.
# Các module khác chỉ cần import hàm này vào để dùng. Giải pháp này giúp loại bỏ code thừa,
# dễ dàng gỡ lỗi và tuân thủ nguyên tắc DRY (Don't Repeat Yourself).

# 4. Thiết kế thuật toán (Pseudocode)

# Chức năng Mua vật phẩm:

# Kiểm tra danh sách rỗng.

# Nhập mã người chơi -> Gọi hàm find_player(). Nếu trả về None, in lỗi và dừng.

# In danh sách đồ trong cửa hàng. Nhập tên đồ muốn mua.

# Kiểm tra tên đồ có trong cửa hàng không. Nếu không, báo lỗi.

# Kiểm tra vàng của người chơi >= giá đồ. Nếu đủ, trừ vàng và thêm tên đồ vào inventory. Nếu thiếu, báo lỗi.

# Chức năng Chiến đấu:

# Kiểm tra danh sách rỗng.

# Nhập mã người chơi -> Gọi hàm find_player(). Nếu trả về None, in lỗi và dừng.

# Kiểm tra hp <= 0. Nếu đúng, báo người chơi đã gục ngã và dừng.

# Random chọn 1 quái vật từ danh sách.

# Trừ HP người chơi theo damage của quái vật.

# Nếu HP > 0, báo chiến thắng và cộng vàng. Nếu HP <= 0, báo thua cuộc.


from data.players import player_records
from utils.item_utils import open_treasure_chest, buy_item
from utils.battle_utils import fight_monster
from reports.dungeon_report import display_players, show_leaderboard

def main():
    """Vòng lặp chính quản lý menu hệ thống của trò chơi."""
    while True:
        print("\n===== RIKKEI DUNGEON - PYTHON MODULE ADVENTURE =====")
        print(" 1. Hiển thị danh sách người chơi")
        print(" 2. Mở rương báu ngẫu nhiên")
        print(" 3. Mua vật phẩm trong cửa hàng")
        print(" 4. Chiến đấu với quái vật")
        print(" 5. Xem bảng xếp hạng người chơi")
        print(" 6. Thoát chương trình")
        print("====================================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()
        
        match choice:
            case "1":
                display_players(player_records)
            case "2":
                open_treasure_chest(player_records)
            case "3":
                buy_item(player_records)
            case "4":
                fight_monster(player_records)
            case "5":
                show_leaderboard(player_records)
            case "6":
                print("Cảm ơn bạn đã tham gia Rikkei Dungeon!")
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 6.")

if __name__ == "__main__":
    main()