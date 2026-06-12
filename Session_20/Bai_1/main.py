# Sửa lỗi sập hệ thống (Exception Handling): Khi số lần bị hạ gục của ShowMaker bằng 0, phép tính chia cho 0 trong toán học sẽ ném ra lỗi ZeroDivisionError. 
# nếu bỏ qua ShowMaker, hệ thống sẽ cố gắng ép kiểu chữ "ba" của Chovy thành số bằng hàm int(), điều này ném ra lỗi ValueError.
# Cấu trúc try...except được áp dụng để chủ động "đón đầu" các lỗi này, in ra thông báo tương ứng và cho phép vòng lặp tiếp tục chạy thay vì dừng đột ngột.

# Áp dụng Clean Code: Các biến tối nghĩa như ds, x, n, k, d, a được đổi tên hoàn toàn thành stats_list, player, name, kills, deaths, assists 
# giúp người đọc hiểu ngay biến đó đang chứa dữ liệu gì mà không cần phải suy luận.

# Tuân thủ nguyên tắc DRY (Don't Repeat Yourself): Logic tính toán KDA được rút ra thành một hàm riêng biệt calculate_kda. Điều này giúp việc bảo trì dễ dàng hơn;
#  nếu sau này công thức tính thay đổi, bạn chỉ cần sửa ở đúng một nơi duy nhất.



def calculate_kda(kills, deaths, assists):
    """
    Thực hiện công thức tính toán chỉ số KDA từ các con số đầu vào đã được làm sạch.
    """
    return (kills + assists) / deaths

def print_kda_ranking(stats_list):
    """
    Duyệt qua danh sách thống kê, thực hiện ép kiểu, bẫy lỗi và in ra màn hình.
    """
    print("--- BẢNG XẾP HẠNG KDA ---")
    
    for player in stats_list:
        name = player[0]
        
        try:
            kills = int(player[1])
            deaths = int(player[2])
            assists = int(player[3])
            
            kda = calculate_kda(kills, deaths, assists)
            print(f"Tuyển thủ {name} có chỉ số KDA là: {kda}")
            
        except ZeroDivisionError:
            print(f"Tuyển thủ {name}: KDA Hoàn hảo (Perfect KDA)!")
            
        except ValueError:
            print(f"Tuyển thủ {name}: Lỗi dữ liệu không hợp lệ!")

def main():
    """
    Khởi tạo dữ liệu từ API và tiến hành gọi hàm xử lý bảng xếp hạng.
    """
    api_data = [
        ("Faker", "10", "2", "8"),
        ("ShowMaker", "15", "0", "10"),
        ("Chovy", "12", "ba", "5")
    ]
    
    print_kda_ranking(api_data)

if __name__ == "__main__":
    main()