# Khởi tạo danh sách đơn hàng ban đầu
order_list = ["GE001", "GE002", "GE003"]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Thêm đơn hàng mới")
    print("3. Xóa đơn hàng theo mã")
    print("4. Thoát chương trình")
    
    choice = input("Mời bạn chọn chức năng (1-4): ").strip()
    
    # Xử lý Edge Case: Nhập sai lựa chọn menu
    if choice not in ["1", "2", "3", "4"]:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue
        
    if choice == "1":
        if len(order_list) == 0:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")
            # 1. Dùng enumerate(danh_sach, 1) để tự động đánh số thứ tự bắt đầu từ 1 khi in
            for index, order in enumerate(order_list, 1):
                print(f"{index}. {order}")
                
    elif choice == "2":
        ma_moi = input("Nhập mã đơn hàng mới: ")
        # 2. Dùng strip() để cắt khoảng trắng 2 đầu và upper() để in hoa toàn bộ chữ cái
        ma_chuan_hoa = ma_moi.strip().upper()
        order_list.append(ma_chuan_hoa)
        
        print("Sau khi xử lý, danh sách trở thành:")
        print(order_list)
        
    elif choice == "3":
        ma_xoa = input("Nhập mã đơn hàng cần xóa: ").strip().upper()
        # 3. Dùng toán tử 'in' để kiểm tra xem mã có tồn tại trong List không trước khi xóa
        if ma_xoa in order_list:
            order_list.remove(ma_xoa)
        else:
            print("Không tìm thấy mã đơn hàng cần xóa.")
            
    elif choice == "4":
        print("Thoát chương trình.")
        break