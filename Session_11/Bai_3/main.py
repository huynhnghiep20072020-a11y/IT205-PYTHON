# 1. Bẫy 1 & 2: Luôn dùng .strip().upper() để chuẩn hóa mã SP và duyệt list để chặn thêm mã bị trùng lặp.
# 2. Bẫy 4: Sử dụng phương thức .isdigit() để kiểm tra giá tiền và số lượng nhập vào phải là số nguyên.
# 3. Quản lý dữ liệu bằng danh sách các Dictionary (List of Dicts), truy cập và sửa đổi giá trị thông qua Key.
# 4. Bẫy 3: Dùng biến cờ (found = False) để theo dõi và báo lỗi nếu mã sản phẩm không tồn tại khi Sửa/Xóa.
# 5. Bẫy 5: Chặn lỗi crash khi nhập sai Menu bằng cách kiểm tra choice có nằm trong danh sách ["1", "2", "3", "4", "5"].

# Dữ liệu ban đầu
product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm theo mã")
    print("5. Thoát chương trình")
    
    choice = input("Mời bạn chọn chức năng (1-5): ").strip()
    
    # Bẫy 5: Kiểm tra lựa chọn menu
    if choice not in ["1", "2", "3", "4", "5"]:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue
        
    if choice == "1":
        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("Danh sách sản phẩm hiện tại:")
            for i in range(len(product_list)):
                sp = product_list[i]
                print(f"{i + 1}. Mã SP: {sp['product_id']} | Tên: {sp['product_name']} | Giá: {sp['price']} | Số lượng: {sp['quantity']}")
                
    elif choice == "2":
        ma_sp = input("Nhập mã sản phẩm: ").strip().upper()
        
        # Bẫy 2: Kiểm tra mã trùng
        is_duplicate = False
        for sp in product_list:
            if sp["product_id"] == ma_sp:
                is_duplicate = True
                break
                
        if is_duplicate:
            print("Mã sản phẩm bị trùng")
        else:
            ten_sp = input("Nhập tên sản phẩm: ").strip()
            gia_nhap = input("Nhập giá sản phẩm: ").strip()
            sl_nhap = input("Nhập số lượng sản phẩm: ").strip()
            
            # Bẫy 4: Kiểm tra giá và số lượng phải là số và lớn hơn 0
            if not gia_nhap.isdigit() or int(gia_nhap) <= 0 or not sl_nhap.isdigit() or int(sl_nhap) <= 0:
                print("Giá/Số lượng không hợp lệ")
            else:
                product_list.append({
                    "product_id": ma_sp,
                    "product_name": ten_sp,
                    "price": int(gia_nhap),
                    "quantity": int(sl_nhap)
                })
                print("Thêm sản phẩm thành công")
                
    elif choice == "3":
        ma_sp = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
        found = False
        
        for i in range(len(product_list)):
            if product_list[i]["product_id"] == ma_sp:
                found = True
                ten_moi = input("Nhập tên sản phẩm mới: ").strip()
                gia_moi = input("Nhập giá sản phẩm mới: ").strip()
                sl_moi = input("Nhập số lượng sản phẩm mới: ").strip()
                
                if not gia_moi.isdigit() or int(gia_moi) <= 0 or not sl_moi.isdigit() or int(sl_moi) <= 0:
                    print("Giá/Số lượng không hợp lệ")
                else:
                    # Truy cập thông qua index và key để cập nhật dictionary
                    product_list[i]["product_name"] = ten_moi
                    product_list[i]["price"] = int(gia_moi)
                    product_list[i]["quantity"] = int(sl_moi)
                    print("Cập nhật thông tin thành công!")
                break
                
        # Bẫy 3: Không tìm thấy sản phẩm để cập nhật
        if not found:
            print("Không tìm thấy mã sản phẩm cần cập nhật!")
            
    elif choice == "4":
        ma_sp = input("Nhập mã sản phẩm cần xóa: ").strip().upper()
        found = False
        
        for i in range(len(product_list)):
            if product_list[i]["product_id"] == ma_sp:
                found = True
                product_list.pop(i)
                print("Xóa sản phẩm thành công!")
                break
                
        # Bẫy 3: Không tìm thấy sản phẩm để xóa
        if not found:
            print("Không tìm thấy mã sản phẩm cần xóa!")
            
    elif choice == "5":
        print("Thoát chương trình. Sau đó dừng chương trình.")
        break