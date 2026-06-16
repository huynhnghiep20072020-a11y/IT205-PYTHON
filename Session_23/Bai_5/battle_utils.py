import random
from utils.player_utils import find_player

def fight_monster(records):
    """Mô phỏng trận chiến ngẫu nhiên, trừ máu và kiểm tra điều kiện chiến thắng."""
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    player_id = input("Nhập mã người chơi chiến đấu: ")
    player = find_player(records, player_id)
    
    if player is None:
        print("Không tìm thấy người chơi!")
        return

    if player["hp"] <= 0:
        print("Người chơi đã gục ngã, không thể tiếp tục chiến đấu!")
        return

    monsters = [
        {"name": "Bug Python", "damage": 20, "reward_gold": 100},
        {"name": "Import Error", "damage": 35, "reward_gold": 150},
        {"name": "Module Not Found", "damage": 50, "reward_gold": 250}
    ]
    
    monster = random.choice(monsters)
    print(f">> Quái vật xuất hiện: {monster['name']}")
    
    player["hp"] -= monster["damage"]
    print(f">> {player['name']} bị mất {monster['damage']} HP.")
    
    if player["hp"] > 0:
        player["gold"] += monster["reward_gold"]
        print(f">> Chiến thắng! Bạn nhận được {monster['reward_gold']} vàng.")
    else:
        player["hp"] = 0
        print(">> Bạn đã thua cuộc và gục ngã!")
        
    print(f">> HP còn lại: {player['hp']}")