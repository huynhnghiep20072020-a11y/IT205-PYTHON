# Danh sách đơn hàng mẫu ban đầu
order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Cập nhật danh sách đơn hàng")
    print("3. Thống kê đơn hàng theo trạng thái")
    print("4. Thoát chương trình")
    
    choice = input("Mời bạn chọn chức năng (1-4): ").strip()
    
    if choice == "1":
        if len(order_list) == 0:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")
            for i in range(len(order_list)):
                print(f"{i + 1}. {order_list[i]}")
                
    elif choice == "2":
        while True:
            print("\n----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----")
            print("1. Thêm đơn hàng mới")
            print("2. Sửa đơn hàng theo vị trí")
            print("3. Xóa đơn hàng theo vị trí")
            print("4. Quay lại menu chính")
            
            sub_choice = input("Chọn chức năng con (1-4): ").strip()
            
            if sub_choice == "1":
                ma = input("Nhập mã đơn hàng: ")
                tt = input("Nhập trạng thái: ")
                # 1. Dùng .strip().upper() để bẫy lỗi người dùng nhập dư khoảng trắng hoặc chữ thường, tự động chuẩn hóa dữ liệu.
                order_list.append(f"{ma.strip().upper()} - {tt.strip().upper()}")
                
            elif sub_choice == "2" or sub_choice == "3":
                vi_tri_nhap = input("Nhập vị trí: ").strip()
                # 2. Dùng hàm .isdigit() để kiểm tra người dùng có nhập đúng SỐ hay không, giúp bẫy lỗi nhập chữ cái (abc) gây sập chương trình.
                if not vi_tri_nhap.isdigit():
                    print("Vị trí không hợp lệ!")
                else:
                    vi_tri = int(vi_tri_nhap)
                    if vi_tri < 1 or vi_tri > len(order_list):
                        print("Không tồn tại đơn hàng ở vị trí này!")
                    else:
                        index_thuc_te = vi_tri - 1
                        if sub_choice == "2":
                            ma_moi = input("Nhập mã đơn hàng mới: ")
                            tt_moi = input("Nhập trạng thái mới: ")
                            order_list[index_thuc_te] = f"{ma_moi.strip().upper()} - {tt_moi.strip().upper()}"
                        elif sub_choice == "3":
                            order_list.pop(index_thuc_te)
                            
            elif sub_choice == "4":
                break
            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
                
    elif choice == "3":
        pending = 0
        delivering = 0
        completed = 0
        cancelled = 0
        
        # 3. Dùng vòng lặp for kết hợp toán tử 'in' để tìm từ khóa trạng thái nằm lẩn bên trong mỗi chuỗi đơn hàng để đếm số lượng.
        for order in order_list:
            if "PENDING" in order:
                pending += 1
            elif "DELIVERING" in order:
                delivering += 1
            elif "COMPLETED" in order:
                completed += 1
            elif "CANCELLED" in order:
                cancelled += 1
                
        print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
        print(f"PENDING: {pending}")
        print(f"DELIVERING: {delivering}")
        print(f"COMPLETED: {completed}")
        print(f"CANCELLED: {cancelled}")
        print(f"Tổng số đơn hàng: {len(order_list)}")
        
    elif choice == "4":
        print("Thoát chương trình.")
        break
        
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")