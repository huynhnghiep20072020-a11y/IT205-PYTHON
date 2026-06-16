import datetime as dt
import colorama as cr
from utils.player_utils import get_player_status

cr.init(autoreset=True)

def display_players(records):
    """In danh sách người chơi cùng các chỉ số và trạng thái hiện tại."""
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    print("--- DANH SÁCH NGƯỜI CHƠI ---")
    for i in range(len(records)):
        p = records[i]
        status = get_player_status(p["hp"])
        print(f"{i + 1}. Mã: {p['player_id']} | Tên: {p['name']} | HP: {p['hp']} | Mana: {p['mana']} | Gold: {p['gold']} | Level: {p['level']} | Trạng thái: {status}")
    print("------------------------------")

def show_leaderboard(records):
    """Sắp xếp và hiển thị bảng xếp hạng theo Level, Gold, HP và in kèm thời gian."""
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    sorted_players = sorted(records, key=lambda x: (x["level"], x["gold"], x["hp"]), reverse=True)
    current_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("--- BẢNG XẾP HẠNG NGƯỜI CHƠI ---")
    for i in range(len(sorted_players)):
        p = sorted_players[i]
        print(cr.Fore.YELLOW + f"{i + 1}. {p['name']} | Level: {p['level']} | Gold: {p['gold']} | HP: {p['hp']}")
    
    print(cr.Fore.CYAN + f"Cập nhật lúc: {current_time}")
    print("--------------------------------")