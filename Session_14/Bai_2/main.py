# Lỗi UnboundLocalError xảy ra do chương trình hiểu nhầm total_points là
# một biến cục bộ mới nhưng lại bị đem ra tính toán trước khi được gán giá trị. 
# Thay vào đó, chúng ta truyền điểm hiện tại vào hàm thông qua tham số current_points, thực hiện phép cộng, 
# và dùng lệnh return để trả số điểm mới ra ngoài hệ thống.

total_points = 100

def add_reward_points(current_points, points_earned):
    """
    Cộng thêm điểm thưởng vào tổng điểm hiện tại của khách hàng.

    :param current_points: Số điểm hiện tại khách hàng đang có.
    :param points_earned: Số điểm thưởng mới nhận được.
    :return: Tổng điểm mới sau khi đã cộng thêm.
    """
    new_total = current_points + points_earned
    print("Đã cộng thêm", points_earned, "điểm.")
    return new_total

total_points = add_reward_points(total_points, 50)

print("Tổng điểm hiện tại của khách hàng:", total_points)