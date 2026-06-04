saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyen Van An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Tran Thi Binh",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách số tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán hoặc xóa sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")
    print("=========================================================")
    
    choice = input("Nhập lựa chọn của bạn (1-7): ").strip()
    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại")
        continue
        
    if choice == "1":
        print("\n--- DANH SÁCH SỔ TIẾT KIỆM ---")
        if len(saving_accounts) == 0:
            print("Danh sách số tiết kiệm hiện đang trống")
        else:
            for i in range(len(saving_accounts)):
                acc = saving_accounts[i]
                print(f"{i+1}. Mã số: {acc['account_id']} | Khách hàng: {acc['customer_name']} | Số tiền gửi: {acc['balance']} | Kỳ hạn: {acc['term_months']} tháng | Lãi suất: {acc['interest_rate']}%/năm | Trạng thái: {acc['status']}")
                
    elif choice == "2":
        ma_so = input("Nhập mã số tiết kiệm: ").strip().upper()
        is_duplicate = False
        for acc in saving_accounts:
            if acc["account_id"] == ma_so:
                is_duplicate = True
                break
        
        if is_duplicate:
            print("Mã số tiết kiệm đã tồn tại!")
            continue
            
        ten_kh = input("Nhập tên khách hàng: ").strip()
        if ten_kh == "":
            print("Tên khách hàng không được để trống")
            continue
            
        so_tien = input("Nhập số tiền gửi: ").strip()
        ky_han = input("Nhập kỳ hạn gửi theo tháng: ").strip()
        if not so_tien.isdigit() or not ky_han.isdigit() or int(so_tien) <= 0 or int(ky_han) <= 0:
            print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
            continue
            
        lai_suat_nhap = input("Nhập lãi suất năm: ").strip()
        try:
            lai_suat = float(lai_suat_nhap)
            if lai_suat <= 0:
                print("Lãi suất không hợp lệ!")
                continue
        except ValueError:
            print("Lãi suất không hợp lệ!")
            continue
            
        saving_accounts.append({
            "account_id": ma_so,
            "customer_name": ten_kh,
            "balance": int(so_tien),
            "term_months": int(ky_han),
            "interest_rate": lai_suat,
            "status": "active"
        })
        print("Mở sổ tiết kiệm thành công!")
        
    elif choice == "3":
        ma_so = input("Nhập mã số tiết kiệm cần cập nhật: ").strip().upper()
        found = False
        
        for acc in saving_accounts:
            if acc["account_id"] == ma_so:
                found = True
                if acc["status"] == "closed":
                    print("Không thể thao tác với số tiết kiệm đã tất toán!")
                else:
                    ten_kh_moi = input("Nhập tên khách hàng mới: ").strip()
                    if ten_kh_moi == "":
                        print("Tên khách hàng không được để trống")
                        continue
                        
                    so_tien_moi = input("Nhập số tiền gửi mới: ").strip()
                    ky_han_moi = input("Nhập kỳ hạn mới theo tháng: ").strip()
                    
                    if not so_tien_moi.isdigit() or not ky_han_moi.isdigit() or int(so_tien_moi) <= 0 or int(ky_han_moi) <= 0:
                        print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                        continue
                        
                    lai_suat_moi = input("Nhập lãi suất mới: ").strip()
                    try:
                        ls_moi_float = float(lai_suat_moi)
                        if ls_moi_float <= 0:
                            print("Lãi suất không hợp lệ!")
                            continue
                    except ValueError:
                        print("Lãi suất không hợp lệ!")
                        continue
                        
                    acc["customer_name"] = ten_kh_moi
                    acc["balance"] = int(so_tien_moi)
                    acc["term_months"] = int(ky_han_moi)
                    acc["interest_rate"] = ls_moi_float
                    print("Cập nhật thông tin thành công!")
                break
                
        if not found:
            print("Không tìm thấy mã số tiết kiệm")
            
    elif choice == "4":
        ma_so = input("Nhập mã số tiết kiệm cần tất toán/xóa: ").strip().upper()
        found = False
        
        for acc in saving_accounts:
            if acc["account_id"] == ma_so:
                found = True
                if acc["status"] == "closed":
                    print("Không thể thao tác với số tiết kiệm đã tất toán!")
                else:
                    acc["status"] = "closed"
                    print("Tất toán sổ tiết kiệm thành công!")
                break
                
        if not found:
            print("Không tìm thấy mã số tiết kiệm")
            
    elif choice == "5":
        ma_so = input("Nhập mã số tiết kiệm cần tính lãi: ").strip().upper()
        found = False
        
        for acc in saving_accounts:
            if acc["account_id"] == ma_so:
                found = True
                if acc["status"] == "closed":
                    print("Không thể thao tác với số tiết kiệm đã tất toán!")
                else:
                    tien_lai = acc["balance"] * acc["interest_rate"] / 100 * acc["term_months"] / 12
                    tong_nhan = acc["balance"] + tien_lai
                    print(f"Tiền lãi dự kiến: {int(tien_lai)} VNĐ")
                    print(f"Tổng tiền nhận khi đến hạn: {int(tong_nhan)} VNĐ")
                break
                
        if not found:
            print("Không tìm thấy mã số tiết kiệm")
            
    elif choice == "6":
        ma_so = input("Nhập mã số tiết kiệm cần kiểm tra: ").strip().upper()
        found = False
        
        for acc in saving_accounts:
            if acc["account_id"] == ma_so:
                found = True
                if acc["status"] == "closed":
                    print("Không thể thao tác với số tiết kiệm đã tất toán!")
                else:
                    so_thang_thuc = input("Nhập số tháng thực gửi: ").strip()
                    if not so_thang_thuc.isdigit() or int(so_thang_thuc) <= 0:
                        print("Số tháng thực gửi không hợp lệ!")
                    else:
                        thang_thuc = int(so_thang_thuc)
                        if thang_thuc < acc["term_months"]:
                            lai_suat_ap_dung = 0.5
                            print("Khách hàng rút trước hạn, áp dụng mức lãi suất 0.5%/năm.")
                        else:
                            lai_suat_ap_dung = acc["interest_rate"]
                            print(f"Khách hàng rút đúng hạn, áp dụng mức lãi suất {lai_suat_ap_dung}%/năm.")
                            
                        tien_lai = acc["balance"] * lai_suat_ap_dung / 100 * thang_thuc / 12
                        tong_nhan = acc["balance"] + tien_lai
                        
                        print(f"Tiền lãi thực nhận: {int(tien_lai)} VNĐ")
                        print(f"Tổng tiền thực nhận: {int(tong_nhan)} VNĐ")
                break
                
        if not found:
            print("Không tìm thấy mã số tiết kiệm")
            
    elif choice == "7":
        print("Cảm ơn bạn đã sử dụng hệ thống TechBank. Tạm biệt!")
        break