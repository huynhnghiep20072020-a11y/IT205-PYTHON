import datetime  # Dùng cho CÁCH TỐI ƯU (Tự động hóa thời gian)
import math      # Dùng cho CÁCH TỐI ƯU (Làm tròn giờ)

# =================================================================
# 1. KHỞI TẠO DỮ LIỆU
# =================================================================
# [CÁCH CŨ ĐÃ COMMENT]: Dùng List (Tốn thời gian quét vòng lặp)
# parking_lot = []  

# [CÁCH TỐI ƯU ĐANG CHẠY]: Dùng Dictionary (Tìm kiếm ngay lập tức O(1))
parking_lot = {} 

DON_GIA_XE_MAY = 5000
DON_GIA_OTO = 10000

while True:
    print("\n===== HỆ THỐNG SMART PARKING =====")
    print("1. Quản lý vào bãi (Check-in)")
    print("2. Quản lý ra bãi (Check-out)")
    print("3. Hiển thị danh sách bãi xe")
    print("4. Tìm kiếm phương tiện")
    print("5. Thoát chương trình")
    
    choice = input("Mời bạn chọn chức năng (1-5): ").strip()
    
    if choice not in ["1", "2", "3", "4", "5"]:
        print("[Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập từ 1-5!")
        continue
        
    if choice == "1":
        print("\n--- NHẬN XE VÀO BÃI ---")
        plate = input("Nhập biển số xe: ").strip().upper()
        if not plate:
            print("[Lỗi]: Biển số không được để trống!")
            continue
            
        # =================================================================
        # 2. KIỂM TRA BIỂN SỐ TRÙNG LẶP KHI VÀO BÃI
        # =================================================================
        # [CÁCH CŨ ĐÃ COMMENT]: Quét for qua toàn bộ bãi xe
        # is_duplicate = False
        # for i in range(len(parking_lot)):
        #     if parking_lot[i]["plate"] == plate:
        #         is_duplicate = True
        #         break
        # if is_duplicate:
        #     print("[Lỗi]: Xe đã tồn tại!")
        #     continue

        # [CÁCH TỐI ƯU ĐANG CHẠY]: Dùng 'in' kiểm tra thẳng vào Key của Dict cực nhanh
        if plate in parking_lot:
            print("[Lỗi]: Xe với biển số này đã tồn tại trong bãi!")
            continue
            
        while True:
            v_type = input("Nhập loại xe (1: Xe máy, 2: Ô tô): ").strip()
            if v_type in ["1", "2"]:
                v_type = int(v_type)
                break
            print("[Lỗi]: Loại xe không hợp lệ (1: Xe máy, 2: Ô tô)!")
                
        # =================================================================
        # 3. NHẬP THỜI GIAN VÀ LƯU DỮ LIỆU
        # =================================================================
        # [CÁCH CŨ ĐANG COMMENT]: Bắt người dùng tự gõ tay giờ vào
        # while True:
        #     entry_time = input("Nhập giờ vào (0-24): ").strip()
        #     if entry_time.isdigit() and 0 <= int(entry_time) <= 24:
        #         entry_time = int(entry_time)
        #         break
        # parking_lot.append({"plate": plate, "type": v_type, "entry_time": entry_time})

        # [CÁCH TỐI ƯU ĐANG CHẠY]: Tự động lấy giờ hệ thống và lưu bằng Dict
        current_time = datetime.datetime.now()
        parking_lot[plate] = {
            "type": v_type,
            "entry_time": current_time
        }
        
        print(f"[Thành công]: Đã nhận xe {plate} lúc {current_time.strftime('%H:%M:%S')}.")
        
    elif choice == "2":
        print("\n--- TRẢ XE VÀ TÍNH PHÍ ---")
        plate = input("Nhập biển số xe ra bãi: ").strip().upper()
        
        # =================================================================
        # 4. TÌM XE ĐỂ THANH TOÁN & XÓA KHỎI BÃI
        # =================================================================
        # [CÁCH CŨ ĐÃ COMMENT]: Chạy vòng lặp tìm index, nhập giờ thủ công và xóa bằng pop(index)
        # found_idx = -1
        # for i in range(len(parking_lot)):
        #     if parking_lot[i]["plate"] == plate:
        #         found_idx = i
        #         break
        # if found_idx == -1:
        #     print("[Lỗi]: Không tìm thấy xe!")
        # else:
        #     v = parking_lot[found_idx]
        #     exit_time = int(input("Nhập giờ ra: "))
        #     so_gio = exit_time - v["entry_time"]
        #     parking_lot.pop(found_idx) # Xóa bằng index

        # [CÁCH TỐI ƯU ĐANG CHẠY]: Truy vấn trực tiếp bằng Key, tính giờ tự động và xóa bằng pop(Key)
        if plate not in parking_lot:
            print(f"[Lỗi]: Không tìm thấy biển số {plate} trong hệ thống!")
        else:
            v = parking_lot[plate] # Rút thông tin xe ra ngay lập tức
            
            exit_time = datetime.datetime.now() # Lấy giờ ra tự động
            time_diff = exit_time - v["entry_time"]
            
            # Tính toán block thời gian đỗ
            hours_parked = math.ceil(time_diff.total_seconds() / 3600)
            hours_parked = max(1, hours_parked) # Thu tối thiểu 1 block
            
            don_gia = DON_GIA_XE_MAY if v["type"] == 1 else DON_GIA_OTO
            tong_tien = hours_parked * don_gia
            
            print(f"-> Giờ vào: {v['entry_time'].strftime('%H:%M:%S')}")
            print(f"-> Giờ ra:  {exit_time.strftime('%H:%M:%S')}")
            print(f"-> Thời gian tính phí: {hours_parked} block.")
            print(f"-> TỔNG TIỀN: {tong_tien:,} VNĐ.")
            
            # Xóa xe cực nhanh gọn bằng cách gọi pop() trực tiếp với biển số
            parking_lot.pop(plate)
            print(f"[Thành công]: Đã thanh toán và xóa xe {plate} khỏi bãi.")
                    
    elif choice == "3":
        print("\n--- DANH SÁCH BÃI XE HIỆN TẠI ---")
        if len(parking_lot) == 0:
            print("[Danh sách bãi xe hiện đang trống]")
        else:
            print(f"{'Biển số':<15} | {'Loại xe':<10} | {'Giờ vào'}")
            print("-" * 45)
            
            # =================================================================
            # 5. DUYỆT ĐỂ IN DANH SÁCH
            # =================================================================
            # [CÁCH CŨ ĐÃ COMMENT]: Duyệt List bình thường
            # for i in range(len(parking_lot)):
            #     v = parking_lot[i]
            #     print(f"{v['plate']} - {v['type']} - {v['entry_time']}")

            # [CÁCH TỐI ƯU ĐANG CHẠY]: Duyệt Dictionary bằng .items()
            for bien_so, v in parking_lot.items():
                ten_loai = "Xe máy" if v["type"] == 1 else "Ô tô"
                thoi_gian_dep = v['entry_time'].strftime('%H:%M:%S')
                print(f"{bien_so:<15} | {ten_loai:<10} | {thoi_gian_dep}")
                
    elif choice == "4":
        print("\n--- TÌM KIẾM PHƯƠNG TIỆN ---")
        plate = input("Nhập biển số cần tìm: ").strip().upper()
        
        # [CÁCH CŨ ĐÃ COMMENT]: Dùng vòng lặp for và biến cờ
        # found = False
        # for v in parking_lot:
        #     if v["plate"] == plate:
        #         print("Tìm thấy xe!")
        #         found = True
        #         break
        # if not found: print("Không tìm thấy!")

        # [CÁCH TỐI ƯU ĐANG CHẠY]: Tra cứu bằng 1 dòng if
        if plate in parking_lot:
            v = parking_lot[plate]
            thoi_gian_dep = v['entry_time'].strftime('%H:%M:%S %d/%m/%Y')
            print(f"[Thành công]: Tìm thấy xe {plate}. Vào bãi lúc: {thoi_gian_dep}.")
        else:
            print(f"[Lỗi]: Không tìm thấy biển số {plate}!")
            
    elif choice == "5":
        print("Đóng hệ thống Smart Parking. Cảm ơn bạn!")
        break