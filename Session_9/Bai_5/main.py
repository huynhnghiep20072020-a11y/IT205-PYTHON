# Danh sách đơn hàng mẫu ban đầu
order_list = [
    "GE001 - PENDING",
    "GE002 - ASSIGNED",
    "GE003 - DELIVERING"
]

while True:
    print("\n===== HỆ THỐNG ĐIỀU PHỐI GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Gán tài xế cho đơn hàng")
    print("3. Cập nhật trạng thái giao hàng")
    print("4. Hủy đơn hàng")
    print("5. Thoát chương trình")
    
    choice = input("Mời bạn chọn chức năng (1-5): ").strip()
    
    if choice not in ["1", "2", "3", "4", "5"]:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue
        
    if choice == "1":
        if len(order_list) == 0:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")
            for i in range(len(order_list)):
                print(f"{i + 1}. {order_list[i]}")
                
    elif choice == "2":
        # 1. Dùng .strip().upper() để loại bỏ khoảng trắng thừa và tự động viết hoa, xử lý triệt để bẫy dữ liệu đầu vào.
        ma_nhap = input("Nhập mã đơn hàng cần gán tài xế: ").strip().upper()
        found = False
        
        # 2. Dùng vòng lặp quét qua từng phần tử, kết hợp .startswith() để tìm chính xác mã đơn hàng ở đầu chuỗi.
        for i in range(len(order_list)):
            if order_list[i].startswith(ma_nhap):
                found = True
                if "PENDING" in order_list[i]:
                    order_list[i] = f"{ma_nhap} - ASSIGNED"
                    print("Gán tài xế thành công!")
                else:
                    print("Chỉ có thể gán tài xế cho đơn hàng đang chờ xử lý.")
                break
                
        if not found:
            print("Không tìm thấy mã đơn hàng.")
            
    elif choice == "3":
        ma_nhap = input("Nhập mã đơn hàng cần cập nhật: ").strip().upper()
        found = False
        
        for i in range(len(order_list)):
            if order_list[i].startswith(ma_nhap):
                found = True
                # 3. Dùng chuỗi if/elif nối tiếp nhau để kiểm soát chặt chẽ luồng trạng thái, chặn các lỗi vượt cấp.
                if "ASSIGNED" in order_list[i]:
                    order_list[i] = f"{ma_nhap} - DELIVERING"
                    print("Đã cập nhật trạng thái thành DELIVERING.")
                elif "DELIVERING" in order_list[i]:
                    order_list[i] = f"{ma_nhap} - COMPLETED"
                    print("Đã cập nhật trạng thái thành COMPLETED.")
                elif "PENDING" in order_list[i]:
                    print("Đơn hàng chưa được gán tài xế, không thể chuyển sang trạng thái giao hàng.")
                elif "COMPLETED" in order_list[i]:
                    print("Đơn hàng đã hoàn tất, không thể cập nhật tiếp.")
                elif "CANCELLED" in order_list[i]:
                    print("Đơn hàng đã hủy, không thể cập nhật.")
                break
                
        if not found:
            print("Không tìm thấy mã đơn hàng.")
            
    elif choice == "4":
        ma_nhap = input("Nhập mã đơn hàng cần hủy: ").strip().upper()
        found = False
        
        for i in range(len(order_list)):
            if order_list[i].startswith(ma_nhap):
                found = True
                if "PENDING" in order_list[i] or "ASSIGNED" in order_list[i]:
                    order_list[i] = f"{ma_nhap} - CANCELLED"
                    print("Đã hủy đơn hàng thành công.")
                elif "DELIVERING" in order_list[i]:
                    print("Đơn hàng đang được giao, không thể hủy.")
                elif "COMPLETED" in order_list[i]:
                    print("Đơn hàng đã hoàn tất, không thể hủy.")
                elif "CANCELLED" in order_list[i]:
                    print("Đơn hàng đã được hủy trước đó.")
                break
                
        if not found:
            print("Không tìm thấy mã đơn hàng.")
            
    elif choice == "5":
        print("Thoát chương trình.")
        break