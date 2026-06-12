# Xử lý lỗi IndexError (Thiếu dữ liệu): Hồ sơ của tuyển thủ "SofM" bị khuyết dữ liệu nên mảng chỉ có 2 phần tử (vị trí 0 và 1). 
# Khi lệnh cũ cố tình truy cập vào p[2] để lấy MMR, hệ thống sẽ báo lỗi vượt quá giới hạn mảng. 
# Việc đặt thao tác lấy dữ liệu vào khối try kết hợp với except IndexError sẽ giúp bắt gọn sự cố này.

# Xử lý lỗi ValueError (Sai kiểu dữ liệu): Với trường hợp của "Optimus", điểm MMR bị ghi là chuỗi "N/A". 
# Phép toán ép kiểu int("N/A") sẽ làm sập chương trình vì không thể biến chữ thành số. Bẫy lỗi except ValueError được thêm vào để xử lý riêng tình huống này.

# Tái cấu trúc mã nguồn (Clean Code): Mọi biến số được đổi tên cho rõ ràng, dễ hiểu (record, name, matches, mmr, bonus). 
# Công thức tính tiền thưởng được tách riêng ra một hàm calculate_bonus độc lập để hệ thống linh hoạt và tuân thủ nguyên tắc lập trình cơ bản.



def calculate_bonus(matches, mmr):
    """
    Tính toán và trả về số lượng RP thưởng dựa trên công thức quy định.
    """
    return (matches * 10) + (int(mmr) * 0.5)

def process_rewards(player_records):
    """
    Duyệt qua danh sách hồ sơ, bẫy lỗi thiếu dữ liệu/lỗi ép kiểu và in kết quả.
    """
    print("--- BẢNG TÍNH THƯỞNG RP ---")
    
    for record in player_records:
        name = record[0]
        
        try:
            matches = record[1]
            mmr = record[2]
            
            bonus = calculate_bonus(matches, mmr)
            print(f"Tuyển thủ {name} nhận được {bonus} RP")
            
        except IndexError:
            print(f"Tuyển thủ {name}: Lỗi - Hồ sơ bị thiếu thông tin!")
            
        except ValueError:
            print(f"Tuyển thủ {name}: Lỗi - Dữ liệu MMR không hợp lệ!")

def main():
    """
    Khởi tạo dữ liệu giả lập từ API và tiến hành gọi hàm xử lý trao thưởng.
    """
    api_data = [
        ("Levi", 120, 2500),
        ("SofM", 150),
        ("Optimus", 100, "N/A")
    ]
    
    process_rewards(api_data)

if __name__ == "__main__":
    main()