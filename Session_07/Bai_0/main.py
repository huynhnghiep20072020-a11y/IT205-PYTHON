raw_input = "  nGuYen vAn aN ; 2004  "

parts = raw_input.split(";")
name_part = parts[0].strip().title()
year_part = parts[1].strip()

current_year = 2026
age = current_year - int(year_part)

name_parts = name_part.split()
ho = name_parts[0]
ten_dem = name_parts[1]
ten_chinh = name_parts[2]

email = (ho[0] + ten_dem[0] + ten_chinh).lower() + "@company.com"
ma_id = ten_chinh.upper() + year_part[-2:]

while True:
    print("\n===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa Họ tên và tính Tuổi")
    print("3. Tạo Mã ID và Email tự động")
    print("4. Thoát chương trình")
    print("=====================================")
    
    choice = input("Nhập lựa chọn của bạn (1-4): ")
    
    if choice == '1':
        print("\nChuỗi dữ liệu gốc hiện tại:")
        print(f"'{raw_input}'")
        
    elif choice == '2':
        print("\n[KẾT QUẢ CHUẨN HÓA DỮ LIỆU]:")
        print(f"- Họ và tên: {name_part}")
        print(f"- Tuổi hiện tại: {age} tuổi")
        
    elif choice == '3':
        print("\n------------------------------")
        print(f"| THẺ THÀNH VIÊN MỚI         |")
        print("------------------------------")
        print(f"| Mã ID  : {ma_id:<18}|")
        print(f"| Họ tên : {name_part:<18}|")
        print(f"| Email  : {email:<18}|")
        print("------------------------------")
        
    elif choice == '4':
        print("\nChương trình đã dừng!")
        break
        
    else:
        print("\nLựa chọn không hợp lệ, vui lòng nhập lại!")