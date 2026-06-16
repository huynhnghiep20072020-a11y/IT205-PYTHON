import random
from utils.player_utils import find_player

def open_treasure_chest(records):
    """Mở rương ngẫu nhiên để nhận vật phẩm hoặc vàng."""
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    player_id = input("Nhập mã người chơi mở rương: ")
    player = find_player(records, player_id)
    
    if player is None:
        print("Không tìm thấy người chơi!")
        return

    rewards = ["Potion", "Iron Sword", "Magic Scroll", "100 Gold", "Mana Stone"]
    reward = random.choice(rewards)
    
    print(f">> Người chơi {player['name']} đã mở rương!")
    print(f">> Phần thưởng nhận được: {reward}")
    
    if reward == "100 Gold":
        player["gold"] += 100
        print(">> Đã cộng 100 vàng vào tài khoản.")
    else:
        player["inventory"].append(reward)
        print(f">> Đã thêm {reward} vào túi đồ.")

def buy_item(records):
    """Xử lý giao dịch mua đồ trong cửa hàng nếu đủ điều kiện vàng."""
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    player_id = input("Nhập mã người chơi: ")
    player = find_player(records, player_id)
    
    if player is None:
        print("Không tìm thấy người chơi!")
        return

    shop_items = {
        "Potion": 50,
        "Iron Sword": 200,
        "Magic Book": 300,
        "Mana Stone": 150
    }
    
    item_name = input("Nhập tên vật phẩm muốn mua: ").strip().title()
    
    if item_name not in shop_items:
        print("Vật phẩm không tồn tại trong cửa hàng!")
        return
        
    price = shop_items[item_name]
    
    if player["gold"] >= price:
        player["gold"] -= price
        player["inventory"].append(item_name)
        print(f">> Mua thành công {item_name}!")
        print(f">> Số vàng còn lại: {player['gold']}")
    else:
        print("Không đủ vàng để mua vật phẩm này!")