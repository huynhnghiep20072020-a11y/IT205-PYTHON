ten_nguoi_gui = ""
sdt_nguoi_gui = ""
dia_chi_lay = ""
ten_nguoi_nhan = ""
sdt_nguoi_nhan = ""
dia_chi_giao = ""
ghi_chu = ""

while True:
    print("\n=======================================================")
    print("|   HỆ THỐNG QUẢN LÝ NỘI DUNG ĐƠN HÀNG GRAB EXPRESS   |")
    print("=======================================================")
    print("| 1. Nhập dữ liệu đơn hàng và xem báo cáo thống kê    |")
    print("| 2. Chuẩn hóa mã đơn hàng                            |")
    print("| 3. Ẩn số điện thoại khách hàng                      |")
    print("| 4. Tìm kiếm và thay thế từ khóa trong ghi chú       |")
    print("| 5. Thoát chương trình                               |")
    print("=======================================================")
    
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
        tng_input = input("- Tên người gửi: ")
        if tng_input.strip() == "":
            print("Tên người gửi không được bỏ trống")
            continue
            
        sdg_input = input("- Số điện thoại người gửi: ")
        if sdg_input.strip() == "":
            print("Số điện thoại người gửi không được bỏ trống")
            continue
        elif not sdg_input.isdigit():
            print("Số điện thoại không hợp lệ")
            continue
        elif len(sdg_input) != 10:
            print("Số điện thoại không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
            continue
            
        dcl_input = input("- Địa chỉ lấy hàng: ")
        if dcl_input.strip() == "":
            print("Địa chỉ lấy hàng không được bỏ trống")
            continue
            
        tnn_input = input("- Tên người nhận: ")
        if tnn_input.strip() == "":
            print("Tên người nhận không được bỏ trống")
            continue
            
        sdn_input = input("- Số điện thoại người nhận: ")
        if sdn_input.strip() == "":
            print("Số điện thoại người nhận không được bỏ trống")
            continue
        elif not sdn_input.isdigit():
            print("Số điện thoại không hợp lệ")
            continue
        elif len(sdn_input) != 10:
            print("Số điện thoại không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
            continue
            
        dcg_input = input("- Địa chỉ giao hàng: ")
        if dcg_input.strip() == "":
            print("Địa chỉ giao hàng không được bỏ trống")
            continue
            
        gc_input = input("- Ghi chú giao hàng: ")
        
        ten_nguoi_gui = tng_input.strip().title()
        sdt_nguoi_gui = sdg_input.strip()
        dia_chi_lay = dcl_input.strip()
        ten_nguoi_nhan = tnn_input.strip().title()
        sdt_nguoi_nhan = sdn_input.strip()
        dia_chi_giao = dcg_input.strip()
        ghi_chu = gc_input.strip()
        
        if ghi_chu == "":
            so_tu = 0
        else:
            so_tu = ghi_chu.count(" ") + 1
            
        print("\n--- BÁO CÁO THỐNG KÊ ---")
        print(f"- Tên người gửi: {ten_nguoi_gui}")
        print(f"- Tên người nhận: {ten_nguoi_nhan}")
        print(f"- Địa chỉ lấy hàng: {dia_chi_lay}")
        print(f"- Địa chỉ giao hàng: {dia_chi_giao}")
        print(f"- Ghi chú giao hàng: {ghi_chu}")
        print(f"- Độ dài ghi chú giao hàng: {len(ghi_chu)}")
        print(f"- Số lượng từ trong ghi chú giao hàng: {so_tu}")
        print(f"- Ghi chú giao hàng dạng chữ thường: {ghi_chu.lower()}")
        print(f"- Ghi chú giao hàng dạng chữ hoa: {ghi_chu.upper()}")
        
    elif choice == 2:
        ma_don = input("Nhập mã đơn hàng ban đầu: ").strip()
        if ma_don == "":
            print("Mã đơn hàng không được bỏ trống")
            continue
            
        clean_ma = ma_don.upper().replace(" ", "-")
        
        if not clean_ma.startswith("GRAB-"):
            clean_ma = "GRAB-" + clean_ma
            
        print(f"\nMã đơn hàng ban đầu: {ma_don}")
        print(f"Mã đơn hàng sau khi được chuẩn hóa: {clean_ma}")
        
    elif choice == 3:
        if sdt_nguoi_gui == "" or sdt_nguoi_nhan == "":
            print("Vui lòng nhập dữ liệu đơn hàng ở chức năng 1 trước!")
            continue
            
        sdt_gui_an = sdt_nguoi_gui[:3] + "*****" + sdt_nguoi_gui[-2:]
        sdt_nhan_an = sdt_nguoi_nhan[:3] + "*****" + sdt_nguoi_nhan[-2:]
        
        print("\n--- KẾT QUẢ ẨN SỐ ĐIỆN THOẠI ---")
        print(f"Output:")
        print(f"SĐT người gửi: {sdt_gui_an}")
        print(f"SĐT người nhận: {sdt_nhan_an}")
        
    elif choice == 4:
        if ghi_chu == "":
            print("Chưa có ghi chú giao hàng để tìm kiếm")
            continue
            
        tu_khoa = input("- Từ khóa cần tìm: ").strip()
        tu_thay_the = input("- Từ khóa thay thế: ").strip()
        
        if tu_khoa in ghi_chu:
            so_lan = ghi_chu.count(tu_khoa)
            ghi_chu_moi = ghi_chu.replace(tu_khoa, tu_thay_the)
            
            print(f"\nOutput:")
            print(f"Số lần xuất hiện của từ khóa: {so_lan}")
            print(f"Ghi chú đơn hàng sau khi thay thế:\n{ghi_chu_moi}")
            
            ghi_chu = ghi_chu_moi
        else:
            print("Không tìm thấy từ khóa cần tìm trong ghi chú giao hàng")