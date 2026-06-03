# 1. Dùng .strip().upper() để chuẩn hóa mã sản phẩm và .isdigit() để kiểm tra số nguyên nhằm tránh lỗi văng app.
# 2. Dùng biến cờ (found = False) để theo dõi và báo lỗi "Không tìm thấy sản phẩm" khi Bán/Đổi trả/Giảm giá/Nhập kho.
# 3. Khi Bán và Đổi trả, tính giá sau giảm bằng công thức: price * (100 - discount) / 100 để tính ra số tiền chính xác.
# 4. Khi Đổi trả, chặn lỗi logic bằng cách kiểm tra số lượng trả không được lớn hơn số lượng đã bán (key "sold").
# 5. Khống chế phần trăm giảm giá chỉ được phép nằm trong khoảng từ 0 đến 70 để bảo vệ doanh thu cửa hàng.

product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5,
        "returned": 1,
        "discount": 0
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3,
        "returned": 0,
        "discount": 10
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7,
        "returned": 1,
        "discount": 15
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ GIAO DỊCH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Xử lý đổi trả hàng")
    print("4. Áp dụng giảm giá cho sản phẩm")
    print("5. Nhập thêm hàng vào kho cửa hàng")
    print("6. Thoát chương trình")
    
    choice = input("Mời bạn chọn chức năng (1-6): ").strip()
    
    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue
        
    if choice == "1":
        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            for i in range(len(product_list)):
                sp = product_list[i]
                
                # Logic xác định trạng thái tồn kho
                if sp["quantity"] == 0:
                    trang_thai = "Hết hàng"
                elif sp["quantity"] <= 5:
                    trang_thai = "Sắp hết hàng"
                else:
                    trang_thai = "Còn hàng"
                    
                print(f"{i+1}. Mã SP: {sp['product_id']} | Tên: {sp['product_name']} | Giá: {sp['price']} | Tồn kho: {sp['quantity']} | Đã bán: {sp['sold']} | Đã trả: {sp['returned']} | Giảm giá: {sp['discount']}% | Trạng thái: {trang_thai}")
                
    elif choice == "2":
        ma_sp = input("Nhập mã sản phẩm khách muốn mua: ").strip().upper()
        sl_nhap = input("Nhập số lượng khách mua: ").strip()
        
        if not sl_nhap.isdigit() or int(sl_nhap) <= 0:
            print("Số/Số lượng không hợp lệ")
        else:
            sl_mua = int(sl_nhap)
            found = False
            
            for i in range(len(product_list)):
                if product_list[i]["product_id"] == ma_sp:
                    found = True
                    if sl_mua > product_list[i]["quantity"]:
                        print("Số lượng trong kho không đủ để bán")
                    else:
                        product_list[i]["quantity"] -= sl_mua
                        product_list[i]["sold"] += sl_mua
                        
                        # Tính tiền dựa trên giá đã giảm
                        gia_sau_giam = product_list[i]["price"] * (100 - product_list[i]["discount"]) / 100
                        tong_tien = gia_sau_giam * sl_mua
                        
                        print(f"Bán thành công! Tổng tiền khách cần thanh toán: {int(tong_tien)} VNĐ")
                    break
                    
            if not found:
                print("Không tìm thấy sản phẩm cần bán")
                
    elif choice == "3":
        ma_sp = input("Nhập mã sản phẩm khách muốn đổi/trả: ").strip().upper()
        sl_nhap = input("Nhập số lượng đổi/trả: ").strip()
        
        if not sl_nhap.isdigit() or int(sl_nhap) <= 0:
            print("Số lượng đổi/trả không hợp lệ")
        else:
            sl_tra = int(sl_nhap)
            found = False
            
            for i in range(len(product_list)):
                if product_list[i]["product_id"] == ma_sp:
                    found = True
                    # Bẫy 5: Không thể trả số lượng lớn hơn số lượng đã mua (đã bán)
                    if sl_tra > product_list[i]["sold"]:
                        print("Số lượng đổi/trả không được vượt quá số lượng đã bán")
                    else:
                        product_list[i]["sold"] -= sl_tra
                        product_list[i]["quantity"] += sl_tra
                        product_list[i]["returned"] += sl_tra
                        
                        # Tính số tiền hoàn lại
                        gia_sau_giam = product_list[i]["price"] * (100 - product_list[i]["discount"]) / 100
                        tien_hoan_lai = gia_sau_giam * sl_tra
                        
                        print(f"Đổi trả thành công! Số tiền hoàn lại cho khách: {int(tien_hoan_lai)} VNĐ")
                    break
                    
            if not found:
                print("Không tìm thấy sản phẩm cần đổi/trả")
                
    elif choice == "4":
        ma_sp = input("Nhập mã sản phẩm cần áp dụng giảm giá: ").strip().upper()
        giam_gia_nhap = input("Nhập phần trăm giảm giá (0-70): ").strip()
        
        # Bẫy 6: Khống chế phần trăm giảm giá từ 0 -> 70
        if not giam_gia_nhap.isdigit() or int(giam_gia_nhap) < 0 or int(giam_gia_nhap) > 70:
            print("Phần trăm giảm giá không hợp lệ")
        else:
            phan_tram_giam = int(giam_gia_nhap)
            found = False
            
            for i in range(len(product_list)):
                if product_list[i]["product_id"] == ma_sp:
                    found = True
                    product_list[i]["discount"] = phan_tram_giam
                    print("Cập nhật phần trăm giảm giá thành công!")
                    break
                    
            if not found:
                print("Không tìm thấy sản phẩm cần giảm giá")
                
    elif choice == "5":
        ma_sp = input("Nhập mã sản phẩm cần nhập thêm: ").strip().upper()
        sl_nhap = input("Nhập số lượng nhập thêm: ").strip()
        
        if not sl_nhap.isdigit() or int(sl_nhap) <= 0:
            print("Số lượng nhập kho không hợp lệ")
        else:
            sl_them = int(sl_nhap)
            found = False
            
            for i in range(len(product_list)):
                if product_list[i]["product_id"] == ma_sp:
                    found = True
                    product_list[i]["quantity"] += sl_them
                    print("Nhập kho thành công!")
                    break
                    
            if not found:
                print("Không tìm thấy sản phẩm cần nhập kho")
                
    elif choice == "6":
        print("Thoát chương trình. Hẹn gặp lại!")
        break