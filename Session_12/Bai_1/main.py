cart_items = [
    {
        "id": "P001",
        "name": "Dien thoai iPhone 15",
        "number": 1,
        "price": 25000000
    },
    {
        "id": "P002",
        "name": "Op lung Silicon",
        "number": 2,
        "price": 150000
    }
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
            sp = cart_items[i]
            thanh_tien = sp["number"] * sp["price"]
            tong_so_luong += sp["number"]
            tong_tien_thanh_toan += thanh_tien
            
            print(f"{i+1:<4} | {sp['id']:<6} | {sp['name']:<22} | {sp['number']:<4} | {sp['price']:<12} | {thanh_tien}")
            
        print("-" * 75)
        print(f"=> Tổng số lượng sản phẩm trong giỏ: {tong_so_luong}")
        print(f"=> TỔNG TIỀN THANH TOÁN: {tong_tien_thanh_toan}")
        
    elif choice == "2":
        ma_sp = input("Nhập mã sản phẩm: ").strip().upper()
        ten_sp = input("Nhập tên sản phẩm: ").strip()
        so_luong = input("Nhập số lượng: ").strip()
        don_gia = input("Nhập đơn giá: ").strip()
        if not so_luong.isdigit() or not don_gia.isdigit():
            print("Lỗi: Số lượng và đơn giá phải là số nguyên dương!")
            continue
            
        sl_nhap = int(so_luong)
        gia_nhap = int(don_gia)
        if sl_nhap <= 0 or gia_nhap < 0:
            print("Lỗi: Số lượng phải > 0 và đơn giá không được âm!")
        else:
            found = False
            for sp in cart_items:
                if sp["id"] == ma_sp:
                    sp["number"] += sl_nhap 
                    found = True
                    print("Đã cộng dồn số lượng cho sản phẩm có sẵn.")
                    break
                    
            if not found:
                cart_items.append({
                    "id": ma_sp,
                    "name": ten_sp,
                    "number": sl_nhap,
                    "price": gia_nhap
                })
                print("Đã thêm sản phẩm mới vào giỏ hàng.")
                
    elif choice == "3":
        ma_sp = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
        sl_nhap = input("Nhập số lượng mới: ").strip()
        
        if not sl_nhap.isdigit() or int(sl_nhap) <= 0:
            print("Lỗi: Số lượng cập nhật phải là số và lớn hơn 0!")
        else:
            sl_moi = int(sl_nhap)
            found = False
            for sp in cart_items:
                if sp["id"] == ma_sp:
                    sp["number"] = sl_moi 
                    found = True
                    print("Đã cập nhật số lượng thành công.")
                    break
            if not found:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")
                
    elif choice == "4":
        ma_sp = input("Nhập mã sản phẩm cần xóa: ").strip().upper()
        found = False
        
        for i in range(len(cart_items)):
            if cart_items[i]["id"] == ma_sp:
                cart_items.pop(i) 
                found = True
                print("Đã xóa sản phẩm khỏi giỏ hàng.")
                break
                
        if not found:
            print("Mã sản phẩm không tồn tại trong giỏ hàng.")
            
    elif choice == "5":
        print("Thoát chương trình. Hẹn gặp lại!")
        break