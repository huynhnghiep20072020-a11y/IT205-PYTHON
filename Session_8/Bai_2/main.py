ten_shop = ""
ten_san_pham = ""
mo_ta = ""
danh_muc = ""
tu_khoa = ""

while True:
    print("\n==============================================")
    print("| HỆ THỐNG QUẢN LÝ NỘI DUNG SẢN PHẨM SHOPEE  |")
    print("==============================================")
    print("| 1. Nhập dữ liệu sản phẩm và xem báo cáo    |")
    print("| 2. Chuẩn hóa tên shop                      |")
    print("| 3. Kiểm tra mã giảm giá hợp lệ             |")
    print("| 4. Tìm kiếm và thay thế từ khóa trong mô tả|")
    print("| 5. Thoát chương trình                      |")
    print("==============================================")
    
    choice = input("> Mời bạn chọn chức năng (1-5): ").strip()
    
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue
        
    choice = int(choice)
    
    if choice < 1 or choice > 5:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue
        
    if choice == 5:
        print("Thoát chương trình")
        break
        
    if choice == 1:
        ten_shop_input = input("- Tên shop: ")
        if ten_shop_input.strip() == "":
            print("Tên shop không được bỏ trống")
            continue
            
        ten_san_pham_input = input("- Tên sản phẩm: ")
        
        mo_ta_input = input("- Mô tả sản phẩm: ")
        if mo_ta_input.strip() == "":
            print("Mô tả sản phẩm không được rỗng")
            continue
            
        danh_muc_input = input("- Danh mục sản phẩm: ")
        tu_khoa_input = input("- Danh sách từ khóa tìm kiếm (cách nhau bởi dấu phẩy): ")
        
        ten_shop = ten_shop_input.strip()
        mo_ta = mo_ta_input.strip()
        ten_san_pham = ten_san_pham_input.strip().title()
        danh_muc = danh_muc_input.strip().lower()
        tu_khoa = tu_khoa_input.replace(" ", "")
        
        if tu_khoa == "":
            so_luong_tu_khoa = 0
        else:
            so_luong_tu_khoa = tu_khoa.count(",") + 1
            
        print("\n--- BÁO CÁO THỐNG KÊ ---")
        print(f"- Tên shop: {ten_shop}")
        print(f"- Tên sản phẩm: {ten_san_pham}")
        print(f"- Mô tả sản phẩm: {mo_ta}")
        print(f"- Độ dài mô tả sản phẩm: {len(mo_ta)} ký tự")
        print(f"- Danh mục sản phẩm: {danh_muc}")
        print(f"- Danh sách từ khóa: {tu_khoa}")
        print(f"- Số lượng từ khóa tìm kiếm: {so_luong_tu_khoa}")
        print(f"- Mô tả in thường: {mo_ta.lower()}")
        print(f"- Mô tả in hoa: {mo_ta.upper()}")
        
    elif choice == 2:
        if ten_shop == "":
            print("Vui lòng nhập dữ liệu ở chức năng 1 trước!")
            continue
            
        clean_shop = ten_shop.lower().replace(" ", "-")
        
        if not clean_shop.startswith("shop-"):
            clean_shop = "shop-" + clean_shop
            
        print("\n--- CHUẨN HÓA TÊN SHOP ---")
        print(f"- Tên shop ban đầu: {ten_shop}")
        print(f"- Tên shop sau khi được chuẩn hóa: {clean_shop}")
        
    elif choice == 3:
        ma_giam_gia = input("Nhập mã giảm giá cần kiểm tra: ").strip()
        
        if ma_giam_gia == "":
            print("Mã giảm giá không hợp lệ (Mã không được rỗng)")
        elif " " in ma_giam_gia:
            print("Mã giảm giá không hợp lệ (Không được chứa khoảng trắng)")
        elif len(ma_giam_gia) < 6 or len(ma_giam_gia) > 12:
            print("Mã giảm giá không hợp lệ (Độ dài phải từ 6 đến 12 ký tự)")
        elif not ma_giam_gia.isupper():
            print("Mã giảm giá không hợp lệ (Phải được viết hoa toàn bộ)")
        elif not ma_giam_gia.isalnum():
            print("Mã giảm giá không hợp lệ (Chỉ được chứa chữ cái và chữ số)")
        elif not ma_giam_gia.startswith("SALE"):
            print("Mã giảm giá không hợp lệ (Phải bắt đầu bằng chuỗi SALE)")
        else:
            print("Mã giảm giá hợp lệ")
            
    elif choice == 4:
        if mo_ta == "":
            print("Vui lòng nhập dữ liệu ở chức năng 1 trước!")
            continue
            
        tu_can_tim = input("- Từ khóa cần tìm: ").strip()
        tu_thay_the = input("- Từ khóa thay thế: ").strip()
        
        if tu_can_tim in mo_ta:
            so_lan = mo_ta.count(tu_can_tim)
            mo_ta_moi = mo_ta.replace(tu_can_tim, tu_thay_the)
            print(f"\nSố lần xuất hiện của từ khóa: {so_lan}")
            print("Mô tả sau khi thay thế:")
            print(mo_ta_moi)
        else:
            print("Không tìm thấy từ khóa cần tìm trong mô tả sản phẩm")