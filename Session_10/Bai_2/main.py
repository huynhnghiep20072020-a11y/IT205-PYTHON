# Khởi tạo danh sách phát trống
playlist = []

while True:
    print("\n========== MENU QUẢN LÝ DANH SÁCH PHÁT ==========")
    print("1. Thêm bài hát vào danh sách phát")
    print("2. Xem danh sách phát")
    print("3. Xóa bài hát khỏi danh sách")
    print("4. Sắp xếp và trích xuất danh sách")
    print("5. Thoát chương trình")
    print("=================================================")
    
    choice = input("Nhập lựa chọn của bạn: ").strip()
    
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")
        continue
        
    if choice == "1":
        print("\n--- THÊM BÀI HÁT ---")
        print("1. Thêm vào cuối danh sách")
        print("2. Chèn vào vị trí cụ thể")
        sub_choice = input("Nhập lựa chọn: ").strip()
        
        if sub_choice == "1":
            ten_bai = input("Nhập tên bài hát: ").strip()
            playlist.append(ten_bai)
            print(f"Đã thêm bài hát '{ten_bai}' thành công!")
            
        elif sub_choice == "2":
            ten_bai = input("Nhập tên bài hát: ").strip()
            vi_tri = input("Nhập số thứ tự (index) muốn chèn: ").strip()
            
            if vi_tri.isdigit():
                vi_tri_int = int(vi_tri)
                if 0 <= vi_tri_int <= len(playlist):
                    playlist.insert(vi_tri_int, ten_bai)
                    print(f"Đã chèn bài hát '{ten_bai}' thành công!")
                    print(f"Số lượng bài hát hiện tại trong playlist: {len(playlist)}")
                else:
                    print("Vị trí không hợp lệ.")
            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")
            
    elif choice == "2":
        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống!")
        else:
            print("\n--- DANH SÁCH PHÁT ---")
            for i in range(len(playlist)):
                print(f"{i + 1}. {playlist[i]}")
            print(f"\nTổng số bài hát: {len(playlist)}")
            
    elif choice == "3":
        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống!")
            continue
            
        print("\n--- XÓA BÀI HÁT ---")
        print("1. Xóa theo tên bài hát")
        print("2. Xóa theo số thứ tự")
        sub_choice = input("Nhập lựa chọn: ").strip()
        
        if sub_choice == "1":
            ten_bai = input("Nhập tên bài hát cần xóa: ").strip()
            if ten_bai in playlist:
                playlist.remove(ten_bai)
                print(f"Đã xóa bài hát '{ten_bai}' khỏi danh sách.")
            else:
                print("Không tìm thấy bài hát trong danh sách phát.")
                
        elif sub_choice == "2":
            vi_tri = input("Nhập số thứ tự (index) cần xóa: ").strip()
            if vi_tri.isdigit():
                vi_tri_int = int(vi_tri)
                if 0 <= vi_tri_int < len(playlist):
                    ten_bai_xoa = playlist.pop(vi_tri_int)
                    print(f"Đã xóa bài hát '{ten_bai_xoa}' khỏi danh sách.")
                else:
                    print("Vị trí không hợp lệ.")
            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")
            
    elif choice == "4":
        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống!")
            continue
            
        print("\n--- SẮP XẾP VÀ TRÍCH XUẤT DANH SÁCH ---")
        print("1. Sắp xếp danh sách phát theo bảng chữ cái A-Z")
        print("2. Hiển thị 3 bài hát đầu tiên")
        sub_choice = input("Nhập lựa chọn: ").strip()
        
        if sub_choice == "1":
            playlist.sort()
            print("Đã sắp xếp danh sách phát thành công!")
            
        elif sub_choice == "2":
            top3 = playlist[:3]
            print("\n3 bài hát đầu tiên là:")
            for i in range(len(top3)):
                print(f"{i + 1}. {top3[i]}")
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")
            
    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
        break
        
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")