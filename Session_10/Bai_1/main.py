cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]

while True:
    print("\n===== SHOPEE CART MANAGEMENT SYSTEM =====")
    print("1. Xem chi tiết giỏ hàng & Tính tổng tiền")
    print("2. Thêm sản phẩm mới / Cộng dồn số lượng")
    print("3. Cập nhật số lượng của một sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")
    print("=========================================")
    
    choice = input("Mời bạn chọn chức năng (1-5): ").strip()
    
    if choice not in ["1", "2", "3", "4", "5"]:
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 5!")
        continue
        
    if choice == "1":
        tong_so_luong = 0
        tong_tien_thanh_toan = 0
        
        print(f"\n--- CHI TIẾT GIỎ HÀNG ---")
        print(f"{'STT':<4} | {'Mã SP':<6} | {'Tên Sản Phẩm':<22} | {'SL':<4} | {'Đơn Giá':<12} | {'Thành Tiền'}")
        print("-" * 75)
        
        for i in range(len(cart_items)):
            thanh_tien = cart_items[i][2] * cart_items[i][3]
            tong_so_luong += cart_items[i][2]
            tong_tien_thanh_toan += thanh_tien
            print(f"{i+1:<4} | {cart_items[i][0]:<6} | {cart_items[i][1]:<22} | {cart_items[i][2]:<4} | {cart_items[i][3]:<12} | {thanh_tien}")
            
        print("-" * 75)
        print(f"=> Tổng số lượng sản phẩm trong giỏ: {tong_so_luong}")
        print(f"=> TỔNG TIỀN THANH TOÁN: {tong_tien_thanh_toan}")
        
    elif choice == "2":
        ma_sp = input("Nhập mã sản phẩm: ").strip().upper()
        ten_sp = input("Nhập tên sản phẩm: ").strip()
        so_luong = int(input("Nhập số lượng: "))
        don_gia = int(input("Nhập đơn giá: "))
        
        if so_luong <= 0 or don_gia < 0:
            print("Lỗi: Số lượng phải > 0 và đơn giá không được âm!")
        else:
            found = False
            for i in range(len(cart_items)):
                if cart_items[i][0] == ma_sp:
                    cart_items[i][2] += so_luong
                    found = True
                    print("Đã cộng dồn số lượng cho sản phẩm có sẵn.")
                    break
                    
            if not found:
                cart_items.append([ma_sp, ten_sp, so_luong, don_gia])
                print("Đã thêm sản phẩm mới vào giỏ hàng.")
                
    elif choice == "3":
        ma_sp = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
        so_luong_moi = int(input("Nhập số lượng mới: "))
        
        if so_luong_moi <= 0:
            print("Lỗi: Số lượng cập nhật phải lớn hơn 0!")
        else:
            found = False
            for i in range(len(cart_items)):
                if cart_items[i][0] == ma_sp:
                    cart_items[i][2] = so_luong_moi
                    found = True
                    print("Đã cập nhật số lượng thành công.")
                    break
                    
            if not found:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")
                
    elif choice == "4":
        ma_sp = input("Nhập mã sản phẩm cần xóa: ").strip().upper()
        found = False
        
        for i in range(len(cart_items)):
            if cart_items[i][0] == ma_sp:
                cart_items.pop(i)
                found = True
                print("Đã xóa sản phẩm khỏi giỏ hàng.")
                break
                
        if not found:
            print("Mã sản phẩm không tồn tại trong giỏ hàng.")
            
    elif choice == "5":
        print("Thoát chương trình. Hẹn gặp lại!")
        break