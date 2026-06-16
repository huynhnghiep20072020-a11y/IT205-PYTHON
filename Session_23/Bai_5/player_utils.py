def find_player(records, player_id):
    """Tìm kiếm và trả về thông tin người chơi dựa trên mã ID đã chuẩn hóa."""
    normalized_id = player_id.strip().upper()
    for player in records:
        if player["player_id"] == normalized_id:
            return player
    return None

def get_player_status(hp):
    """Đánh giá trạng thái người chơi dựa trên chỉ số máu hiện tại."""
    if hp <= 0:
        return "Đã gục ngã"
    elif hp < 50:
        return "Nguy hiểm"
    elif hp < 100:
        return "Ổn định"
    else:
        return "Sung sức"