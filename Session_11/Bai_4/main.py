# 1. Dùng .strip().upper() để chuẩn hóa mã sản phẩm đầu vào, tránh lỗi do dư khoảng trắng hoặc chữ thường.
# 2. Dùng hàm .isdigit() để bắt lỗi nhập số lượng là chữ cái hoặc số âm, đảm bảo tính toán không bị lỗi.
# 3. Dùng cờ báo (found = False) để kiểm tra sản phẩm có tồn tại hay không trước khi thực hiện bán hoặc nhập kho.
# 4. Sử dụng if/elif/else để kiểm tra logic tồn kho: ==0, <=5, và >5 nhằm hiển thị cảnh báo tương ứng.
# 5. Dùng thuật toán tìm max() cơ bản trong vòng lặp for để xác định Sản phẩm bán chạy nhất ở bảng báo cáo.

product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]

while True:
    print("\n===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Nhập thêm hàng vào kho")
    print("4. Xem báo cáo doanh thu")
    print("5. Thoát chương trình")
    
    choice = input("Mời bạn chọn chức năng (1-5): ").strip()
    
    # Bẫy 5: Lựa chọn menu không hợp lệ
    if choice not in ["1", "2", "3", "4", "5"]:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue
        
    if choice == "1":
        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            for i in range(len(product_list)):
                sp = product_list[i]
                
                # Logic xác định trạng thái cảnh báo tồn kho
                if sp["quantity"] == 0:
                    trang_thai = "Hết hàng"
                elif sp["quantity"] <= 5:
                    trang_thai = "Sắp hết hàng"
                else:
                    trang_thai = "Còn hàng"
                    
                print(f"{i+1}. Mã SP: {sp['product_id']} | Tên: {sp['product_name']} | Giá: {sp['price']} | Tồn kho: {sp['quantity']} | Đã bán: {sp['sold']} | Trạng thái: {trang_thai}")
                
    elif choice == "2":
        ma_sp = input("Nhập mã sản phẩm khách muốn mua: ").strip().upper()
        sl_nhap = input("Nhập số lượng khách mua: ").strip()
        
        # Bẫy 3: Kiểm tra nhập số lượng phải là số nguyên dương
        if not sl_nhap.isdigit() or int(sl_nhap) <= 0:
            print("Số lượng mua/Nhập kho không hợp lệ")
        else:
            sl_mua = int(sl_nhap)
            found = False
            
            for i in range(len(product_list)):
                if product_list[i]["product_id"] == ma_sp:
                    found = True
                    # Bẫy 4: Kiểm tra số lượng mua vượt quá số lượng tồn kho
                    if sl_mua > product_list[i]["quantity"]:
                        print("Số lượng trong kho không đủ để bán")
                    else:
                        product_list[i]["quantity"] -= sl_mua
                        product_list[i]["sold"] += sl_mua
                        thanh_tien = sl_mua * product_list[i]["price"]
                        print(f"Bán thành công! Thành tiền: {thanh_tien}")
                    break
                    
            # Bẫy 2: Bán sản phẩm không tồn tại
            if not found:
                print("Không tìm thấy sản phẩm cần bán/Nhập kho")
                
    elif choice == "3":
        ma_sp = input("Nhập mã sản phẩm cần nhập thêm: ").strip().upper()
        sl_nhap = input("Nhập số lượng nhập thêm: ").strip()
        
        # Bẫy 3: Kiểm tra số lượng nhập kho
        if not sl_nhap.isdigit() or int(sl_nhap) <= 0:
            print("Số lượng mua/Nhập kho không hợp lệ")
        else:
            sl_them = int(sl_nhap)
            found = False
            
            for i in range(len(product_list)):
                if product_list[i]["product_id"] == ma_sp:
                    found = True
                    product_list[i]["quantity"] += sl_them
                    print("Nhập kho thành công!")
                    break
                    
            # Bẫy 2: Nhập kho sản phẩm không tồn tại
            if not found:
                print("Không tìm thấy sản phẩm cần bán/Nhập kho")
                
    elif choice == "4":
        # Kiểm tra xem đã có bất kỳ sản phẩm nào được bán ra chưa
        tong_so_luong_ban_ra = 0
        for sp in product_list:
            tong_so_luong_ban_ra += sp["sold"]
            
        if tong_so_luong_ban_ra == 0:
            print("Chưa có doanh thu phát sinh.")
        else:
            print("\n===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====")
            tong_doanh_thu = 0
            max_sold = 0
            best_seller = ""
            
            for i in range(len(product_list)):
                sp = product_list[i]
                doanh_thu_sp = sp["sold"] * sp["price"]
                tong_doanh_thu += doanh_thu_sp
                
                print(f"{i+1}. {sp['product_name']} | Đã bán: {sp['sold']} | Doanh thu: {doanh_thu_sp}")
                
                # Thuật toán tìm sản phẩm bán chạy nhất
                if sp["sold"] > max_sold:
                    max_sold = sp["sold"]
                    best_seller = sp["product_name"]
                    
            print(f"\nTổng doanh thu: {tong_doanh_thu}")
            print(f"Sản phẩm bán chạy nhất: {best_seller}")
            
    elif choice == "5":
        print("Thoát chương trình.")
        break