# ====================================================================
# PHẦN I: KHỞI TẠO HỆ THỐNG
# ====================================================================
# Khởi tạo các biến độc lập với kiểu số nguyên (int)
laptop = 0
phone = 0
tablet = 0

# ====================================================================
# PHẦN II: XÂY DỰNG MENU ĐIỀU HƯỚNG
# ====================================================================
while True:
    print("\n" + "="*40)
    print("   HỆ THỐNG QUẢN LÝ KHO TECH STORE")
    print("="*40)
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo hàng tồn kho thấp")
    print("5. Thoát chương trình")
    print("="*40)
    
    lua_chon = input("Nhập lựa chọn của bạn (1-5): ").strip()
    
    # ----------------------------------------------------------------
    # PHẦN V: XEM BÁO CÁO TỒN KHO
    # ----------------------------------------------------------------
    if lua_chon == '1':
        print("\n--- BÁO CÁO TỒN KHO ---")
        
        # Vẽ biểu đồ dấu sao bằng vòng lặp for
        print(f"Laptop ({laptop}): ", end="")
        for _ in range(laptop):
            print("*", end="")
        print() # Xuống dòng
        
        print(f"Phone  ({phone}): ", end="")
        for _ in range(phone):
            print("*", end="")
        print()
        
        print(f"Tablet ({tablet}): ", end="")
        for _ in range(tablet):
            print("*", end="")
        print()

    # ----------------------------------------------------------------
    # PHẦN III & IV: NHẬP KHO (Có Validation)
    # ----------------------------------------------------------------
    elif lua_chon == '2':
        print("\n--- NHẬP KHO ---")
        loai_hang = input("Chọn mặt hàng (1-Laptop, 2-Phone, 3-Tablet): ").strip()
        
        if loai_hang in ['1', '2', '3']:
            # Vòng lặp kiểm tra validation số lượng
            while True:
                try:
                    so_luong = int(input("Nhập số lượng cần thêm: "))
                    if so_luong >= 0:
                        break # Thoát vòng lặp nếu nhập đúng
                    else:
                        print("[!] Số lượng không hợp lệ (Không được âm). Vui lòng nhập lại!")
                except ValueError:
                    print("[!] LỖI: Vui lòng nhập một số nguyên!")
            
            # Xử lý nghiệp vụ cộng dồn
            if loai_hang == '1':
                laptop += so_luong
            elif loai_hang == '2':
                phone += so_luong
            elif loai_hang == '3':
                tablet += so_luong
            print("=> Cập nhật Nhập kho thành công!")
        else:
            print("[!] Lựa chọn mặt hàng không hợp lệ!")

    # ----------------------------------------------------------------
    # PHẦN III & IV: XUẤT KHO (Có Validation và Ràng buộc tồn kho)
    # ----------------------------------------------------------------
    elif lua_chon == '3':
        print("\n--- XUẤT KHO ---")
        loai_hang = input("Chọn mặt hàng (1-Laptop, 2-Phone, 3-Tablet): ").strip()
        
        if loai_hang in ['1', '2', '3']:
            # Vòng lặp kiểm tra validation số lượng
            while True:
                try:
                    so_luong = int(input("Nhập số lượng cần xuất: "))
                    if so_luong >= 0:
                        break
                    else:
                        print("[!] Số lượng không hợp lệ (Không được âm). Vui lòng nhập lại!")
                except ValueError:
                    print("[!] LỖI: Vui lòng nhập một số nguyên!")
            
            # Xử lý nghiệp vụ trừ đi (Kiểm tra kho đủ hàng không)
            if loai_hang == '1':
                if so_luong > laptop:
                    print("[!] LỖI: Không đủ hàng. Hủy giao dịch!")
                else:
                    laptop -= so_luong
                    print("=> Cập nhật Xuất kho thành công!")
                    
            elif loai_hang == '2':
                if so_luong > phone:
                    print("[!] LỖI: Không đủ hàng. Hủy giao dịch!")
                else:
                    phone -= so_luong
                    print("=> Cập nhật Xuất kho thành công!")
                    
            elif loai_hang == '3':
                if so_luong > tablet:
                    print("[!] LỖI: Không đủ hàng. Hủy giao dịch!")
                else:
                    tablet -= so_luong
                    print("=> Cập nhật Xuất kho thành công!")
        else:
            print("[!] Lựa chọn mặt hàng không hợp lệ!")

    # ----------------------------------------------------------------
    # PHẦN V: CẢNH BÁO TỒN KHO THẤP
    # ----------------------------------------------------------------
    elif lua_chon == '4':
        print("\n--- KIỂM TRA MỨC TỒN KHO ---")
        co_canh_bao = False
        
        # Dùng các lệnh if độc lập để kiểm tra TẤT CẢ mặt hàng
        if laptop < 10:
            print(f"[CẢNH BÁO] Mặt hàng Laptop sắp hết (Chỉ còn {laptop} sản phẩm)")
            co_canh_bao = True
        if phone < 10:
            print(f"[CẢNH BÁO] Mặt hàng Phone sắp hết (Chỉ còn {phone} sản phẩm)")
            co_canh_bao = True
        if tablet < 10:
            print(f"[CẢNH BÁO] Mặt hàng Tablet sắp hết (Chỉ còn {tablet} sản phẩm)")
            co_canh_bao = True
            
        if not co_canh_bao:
            print("=> Tất cả mặt hàng đều có số lượng tồn kho an toàn (>= 10).")

    # ----------------------------------------------------------------
    # THOÁT CHƯƠNG TRÌNH
    # ----------------------------------------------------------------
    elif lua_chon == '5':
        print("\nĐang đóng hệ thống... Tạm biệt!")
        break # Đập vỡ vòng lặp vô hạn
        
    else:
        print("[!] Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 5!")


"""
=========================================================================
GÓC ĐỀ XUẤT KIẾN TRÚC TỐI ƯU (DÀNH CHO ỨNG DỤNG THỰC TẾ)
=========================================================================
Việc sử dụng 3 biến độc lập (laptop, phone, tablet) là tốt để rèn luyện logic cơ 
bản. Tuy nhiên, khi hệ thống phình to ra (cửa hàng bán 1000 mặt hàng), code sẽ 
bị lặp lại rất nhiều (Spaghetti code). Dưới đây là 2 hướng nâng cấp:

GIẢI PHÁP 1: SỬ DỤNG CẤU TRÚC DỮ LIỆU DICTIONARY (BẢNG BĂM)
Thay vì tạo nhiều biến, ta gộp tất cả vào một Dictionary.
- Code khởi tạo: 
  kho_hang = {
      '1': {'ten': 'Laptop', 'soluong': 0},
      '2': {'ten': 'Phone', 'soluong': 0},
      '3': {'ten': 'Tablet', 'soluong': 0}
  }
- Lợi ích: Khi xử lý Nhập/Xuất, bạn KHÔNG cần dùng chuỗi if/elif dài dòng 
  cho từng mặt hàng nữa. Chỉ cần gọi: 
  kho_hang[loai_hang]['soluong'] += so_luong
  Điều này làm code ngắn đi 80% và dễ dàng thêm mặt hàng mới.

GIẢI PHÁP 2: KẾT HỢP LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG (OOP) VÀ LƯU TRỮ FILE
Trong thực tế, kho hàng không thể bị reset về 0 mỗi khi tắt phần mềm.
- Kiến trúc: 
  + Tạo một Class `Item` chứa các thuộc tính (id, name, stock) và phương thức.
  + Gắn thêm chức năng File I/O: Khi người dùng chọn "5. Thoát", hệ thống 
    tự động lưu toàn bộ kho hàng ra một file JSON (vd: database.json). 
  + Khi mở lại chương trình, nó sẽ đọc file JSON này để load lại số lượng.
- Lợi ích: Mang tính áp dụng thực tế cao, dữ liệu được bảo toàn (Persistent Data), 
  giúp bạn tiệm cận với việc làm backend có kết nối CSDL (Database) sau này.
=========================================================================
"""