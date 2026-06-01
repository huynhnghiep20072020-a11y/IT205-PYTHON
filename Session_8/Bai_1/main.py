username = ""
video_title = ""
video_desc = ""
hashtags_input = ""

while True:
    print("\n======================================")
    print("|   HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK |")
    print("======================================")
    print("| 1. Nhập và phân tích thông tin video |")
    print("| 2. Chuẩn hóa tên tài khoản           |")
    print("| 3. Kiểm tra tính hợp lệ của hashtag  |")
    print("| 4. Tìm kiếm và thay thế từ khóa      |")
    print("| 5. Thoát chương trình                |")
    print("======================================")
    
    choice = input("> Mời bạn chọn chức năng (1-5): ").strip()
    
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập lại số!")
        continue
        
    choice = int(choice)
    
    if choice < 1 or choice > 5:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    if choice == 5:
        print("Thoát chương trình")
        break

    if choice == 1:
        username = input("- Tên tài khoản người đăng video: ").strip()
        if username == "":
            print("Tên tài khoản không được rỗng")
            continue
            
        video_title = input("- Tiêu đề video: ").strip()
        video_desc = input("- Mô tả video: ").strip()
        
        if video_desc == "":
            print("Mô tả video không được rỗng")
            continue
            
        hashtags_input = input("- Danh sách hashtag, cách nhau bởi dấu phẩy: ").strip()
        
        print("\n--- KẾT QUẢ PHÂN TÍCH ---")
        print(f"- Tên tài khoản: {username}")
        print(f"- Tiêu đề: {video_title.title()}")
        print(f"- Mô tả: {video_desc}")
        print(f"- Độ dài mô tả video: {len(video_desc)} ký tự")
        
        words = video_desc.split()
        print(f"- Số lượng từ trong mô tả video: {len(words)}")
        
        hashtag_list = hashtags_input.split(",")
        clean_hashtags = ""
        for tag in hashtag_list:
            clean_hashtags += tag.strip() + " "
            
        print(f"- Danh sách hashtag sau chuẩn hóa: {clean_hashtags.strip()}")
        print(f"- Số lượng hashtag: {len(hashtag_list)}")
        print(f"- Mô tả in thường: {video_desc.lower()}")
        print(f"- Mô tả in hoa: {video_desc.upper()}")

    elif choice == 2:
        if username == "":
            print("Vui lòng nhập dữ liệu ở chức năng 1 trước!")
            continue
            
        clean_username = "@" + username.lower().replace(" ", "")
        print("\n--- CHUẨN HÓA TÀI KHOẢN ---")
        print(f"- Tên tài khoản ban đầu: {username}")
        print(f"- Tên tài khoản chuẩn hóa: {clean_username}")

    elif choice == 3:
        tag_to_check = input("Nhập hashtag cần kiểm tra: ").strip()
        
        if tag_to_check == "":
            print("Hashtag không hợp lệ")
        elif not tag_to_check.startswith("#"):
            print("Hashtag không hợp lệ")
        elif " " in tag_to_check:
            print("Hashtag không hợp lệ")
        elif len(tag_to_check) < 2:
            print("Hashtag không hợp lệ")
        else:
            is_valid = True
            content = tag_to_check[1:] 
            
            for char in content:
                if not (char.isalnum() or char == "_"):
                    is_valid = False
                    break
                    
            if is_valid:
                print("Hashtag hợp lệ")
                hashtags_input += "," + tag_to_check
            else:
                print("Hashtag không hợp lệ")

    elif choice == 4:
        if video_desc == "":
            print("Vui lòng nhập dữ liệu ở chức năng 1 trước!")
            continue
            
        old_word = input("- Từ khóa cần tìm: ").strip()
        new_word = input("- Từ khóa thay thế: ").strip()
        
        if old_word in video_desc:
            count = video_desc.count(old_word)
            new_desc = video_desc.replace(old_word, new_word)
            print(f"\n- Mô tả sau khi thay thế:\n{new_desc}")
            print(f"- Từ khóa '{old_word}' xuất hiện {count} lần trong mô tả.")
        else:
            print(f"Không tìm thấy từ khóa '{old_word}' trong mô tả.")