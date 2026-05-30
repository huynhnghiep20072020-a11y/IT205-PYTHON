# 1. Dùng .split(';') để tách chuỗi lô hàng và .strip().upper() để làm sạch, đồng nhất thành chữ hoa.
# 2. Dùng .split('-') để tách từng mã thành 4 phần và định dạng lại Năm SX bằng cách cộng chuỗi "20".
# 3. (Bẫy 1) Dùng hàm .isdigit() kiểm tra phần Serial: nếu chứa chữ cái thì Reject, nếu toàn số thì Pass.
# 4. (Bẫy 2) Khi tìm kiếm, dùng .strip() để xóa khoảng trắng thừa của từ khóa trước khi so sánh.
# 5. Dùng kỹ thuật cắt chuỗi serial[-2:] để lấy chính xác 2 ký tự cuối cùng phục vụ đối chiếu.
# 6. (Bẫy 3) Dùng cấu trúc while True và if/elif/else để khóa menu, ép người dùng nhập đúng từ 1 đến 4.

raw_batch = " LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOn-vn-24-099 "

while True:
    print("\n===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====")
    print("1. Hiển thị chuỗi mã vạch gốc")
    print("2. Giải mã, làm sạch và in báo cáo kiểm kê")
    print("3. Tra cứu nhanh theo đuôi Serial")
    print("4. Thoát chương trình")
    
    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()
    
    if choice == '1':
        print(f"\n[Dữ liệu gốc]:\n{raw_batch}")
        
    elif choice == '2':
        print("\n[BÁO CÁO KIỂM KÊ]")
        print(f"{'MÃ SP':<10} | {'XUẤT XỨ':<10} | {'NĂM SX':<10} | {'SERIAL':<10} | {'TRẠNG THÁI'}")
        print("-" * 65)
        
        products = raw_batch.split(';')
        total_products = 0
        valid_products = 0
        
        for p in products:
            clean_p = p.strip().upper()
            if not clean_p:
                continue
                
            total_products += 1
            parts = clean_p.split('-')
            
            if len(parts) == 4:
                prod_type = parts[0]
                country = parts[1]
                year = "20" + parts[2]
                serial = parts[3]
                
                # Bẫy 1: Serial sai định dạng
                if serial.isdigit():
                    status = "Pass"
                    valid_products += 1
                else:
                    status = "Lỗi Serial - Reject"
                    
                print(f"{prod_type:<10} | {country:<10} | {year:<10} | {serial:<10} | {status}")
                
        print("-" * 65)
        print(f"Đã giải mã thành công {valid_products} sản phẩm hợp lệ / Tổng số {total_products} sản phẩm.")
        
    elif choice == '3':
        # Bẫy 2: Nhập dư khoảng trắng khi tra cứu
        search_suffix = input("Nhập 2 số cuối của Serial cần tìm: ").strip()
        print(f"\n[KẾT QUẢ TÌM KIẾM CHO ĐUÔI '{search_suffix}']")
        
        products = raw_batch.split(';')
        found = False
        
        for p in products:
            clean_p = p.strip().upper()
            if not clean_p:
                continue
            
            parts = clean_p.split('-')
            if len(parts) == 4:
                serial = parts[3]
                # Cắt 2 ký tự cuối của serial để đối chiếu
                if serial[-2:] == search_suffix:
                    print(f"Tìm thấy: {clean_p}")
                    found = True
                    
        if not found:
            print("Không tìm thấy sản phẩm phù hợp.")
            
    elif choice == '4':
        print("\nĐóng ca kiểm kho. Chào tạm biệt!")
        break
        
    else:
        # Bẫy 3: Nhập sai lựa chọn menu
        print("\nChức năng không tồn tại, vui lòng nhập số từ 1-4!")