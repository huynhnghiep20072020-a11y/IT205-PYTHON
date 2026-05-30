# 1. Dữ liệu thô chứa nhiều khoảng trắng thừa ở các đầu chuỗi, cần dùng .strip() để làm sạch.
# 2. Các phần tử bị gộp chung, cần dùng .split('|') để tách nhân viên và .split(';') để tách thuộc tính.
# 3. Sai định dạng chữ: ID và Phòng ban cần .upper(), Họ tên cần .title() để viết hoa chữ cái đầu.
# 4. Số điện thoại chứa ký tự lạ, cần xóa dấu '-' bằng .replace() và kiểm tra .isdigit() trước khi che 6 số đầu.
# 5. Hệ thống tìm kiếm và menu dễ lỗi do nhập sai, cần ép kiểu .strip().upper() cho từ khóa và dùng vòng lặp while True.

raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")
    
    choice = input("Nhập lựa chọn của bạn: ").strip()
    
    if choice == '1':
        print("\n[Dữ liệu gốc]:")
        print(raw_data)
        
    elif choice == '2':
        print("\n[Báo cáo nhân sự]")
        print(f"{'ID':<10} | {'Họ tên':<20} | {'SĐT':<15} | {'Phòng ban':<10}")
        print("-" * 65)
        
        employees = raw_data.split('|')
        for emp in employees:
            fields = emp.split(';')
            if len(fields) == 4:
                emp_id = fields[0].strip().upper()
                name = fields[1].strip().title()
                phone = fields[2].strip().replace('-', '')
                dept = fields[3].strip().upper()
                
                # Xử lý số điện thoại
                if phone.isdigit():
                    # Che 6 số đầu
                    phone = "******" + phone[6:]
                else:
                    phone = "Invalid Format"
                    
                print(f"{emp_id:<10} | {name:<20} | {phone:<15} | {dept:<10}")
                
    elif choice == '3':
        search_input = input("Nhập mã nhân viên cần tìm: ")
        search_id = search_input.strip().upper()
        found = False
        
        employees = raw_data.split('|')
        for emp in employees:
            fields = emp.split(';')
            if len(fields) == 4:
                emp_id = fields[0].strip().upper()
                
                if emp_id == search_id:
                    name = fields[1].strip().title()
                    phone = fields[2].strip().replace('-', '')
                    dept = fields[3].strip().upper()
                    
                    if phone.isdigit():
                        phone = "******" + phone[6:]
                    else:
                        phone = "Invalid Format"
                        
                    print("\n[Thông tin nhân viên]")
                    print(f"ID: {emp_id}")
                    print(f"Họ tên: {name}")
                    print(f"SĐT: {phone}")
                    print(f"Phòng ban: {dept}")
                    found = True
                    break 
                    
        if not found:
            print("Không tìm thấy nhân viên")
            
    elif choice == '4':
        print("Thoát chương trình")
        break
        
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")