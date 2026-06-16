def calculate_average(scores):
    """Lọc các điểm hợp lệ và tính điểm trung bình. Trả về 0.0 nếu danh sách điểm rỗng."""
    valid_scores = []
    for s in scores:
        if type(s) in (int, float):
            valid_scores.append(s)
            
    if len(valid_scores) == 0:
        return 0.0
        
    total = sum(valid_scores)
    return total / len(valid_scores)

def classify_student(average):
    """Xếp loại học lực dựa trên điểm trung bình."""
    if average >= 8.0:
        return "Giỏi"
    elif average >= 6.5:
        return "Khá"
    elif average >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"