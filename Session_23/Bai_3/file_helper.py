import os

def create_folder():
    """Kiểm tra và tạo thư mục lưu trữ log an toàn."""
    print("\n----- KHỞI TẠO THƯ MỤC HỆ THỐNG -----")
    folder_name = "aviation_logs"
    
    if os.path.exists(folder_name):
        print("Thư mục đã tồn tại, bỏ qua bước khởi tạo.")
    else:
        print(f"[SYSTEM] Thư mục '{folder_name}' chưa tồn tại. Đang tiến hành khởi tạo...")
        os.mkdir(folder_name)
        print("[SYSTEM] Tạo thư mục thành công!")