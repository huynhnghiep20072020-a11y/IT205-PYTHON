# Tác hại của from datetime import *: Cú pháp này nạp toàn bộ các class và hàm của thư viện datetime (như date, time, datetime, timedelta) trực tiếp vào không gian tên chung (Global Namespace).
# trong mã nguồn của bạn đang có sẵn một biến time = 120, câu lệnh import này sẽ lập tức ghi đè (overwrite) biến time thành class datetime.time.
# Điều này gây ra lỗi ngầm cực kỳ nguy hiểm và khó debug. Cách import an toàn và tường minh hơn là import datetime hoặc from datetime import datetime, timedelta.

# Tạo thư mục an toàn với thư viện os: Thay vì dùng os.mkdir(),
# tệp tin cấu trúc chuyên nghiệp nên dùng hàm os.makedirs(path, exist_ok=True).
# Cờ exist_ok=True giúp hệ thống tự động bỏ qua nếu thư mục đã tồn tại, ngăn chặn lỗi FileExistsError làm sập chương trình. 
# Hàm này còn hỗ trợ tạo nhiều cấp thư mục lồng nhau cùng lúc.

# Folder Tree
# Rikkei_Media/
# ├── main.py
# ├── analytics/
# │   ├── __init__.py
# │   └── time_validator.py
# └── storage/
#     ├── __init__.py
#     ├── disk_manager.py
#     └── io_helper.py



from storage.disk_manager import calculate_disk_blocks
from storage.io_helper import safe_create_dir
from analytics.time_validator import parse_and_inspect_date

def main():
    """Hàm điều phối trung tâm xử lý, phân loại và lưu trữ tệp tin."""
    raw_files = [
        {"filename": "pod_ep1.mp3", "size_bytes": 4500, "duration_sec": 180, "upload_at": "2026-06-10"},
        {"filename": "movie_trailer.mp4", "size_bytes": 105000, "duration_sec": 145, "upload_at": "2026-06-31"},
        {"filename": "clip_short.mp4", "size_bytes": 8200, "duration_sec": 15, "upload_at": "2026-05-15"}
    ]

    print("======== HỆ THỐNG QUẢN LÝ LƯU TRỮ RIKKEI MEDIA ======")
    
    safe_create_dir("media_vault")
    safe_create_dir("media_vault/audio")
    safe_create_dir("media_vault/video")
    
    print("[SYSTEM] Kiểm tra hạ tầng lưu trữ... Hoàn tất.")
    print("-" * 75)

    success_count = 0
    total_files = len(raw_files)

    for file_data in raw_files:
        filename = file_data["filename"]
        size_bytes = file_data["size_bytes"]
        upload_at = file_data["upload_at"]

        print(f"[TỆP TIN: {filename}]")
        
        valid_date = parse_and_inspect_date(upload_at)

        if valid_date is None:
            print(f" + Trạng thái phân loại: 🔴 THẤT BẠI (Lỗi: Định dạng ngày upload '{upload_at}' không tồn tại)\n")
        else:
            blocks = calculate_disk_blocks(size_bytes)
            print(f" + Dung lượng thực tế: {size_bytes:,} Bytes")
            print(f" + Số khối phân vùng (4KB Block): {blocks} Blocks")
            
            if filename.endswith(".mp3"):
                folder_dest = "audio"
            else:
                folder_dest = "video"
                
            print(f" + Trạng thái phân loại: 🟢 HỢP LỆ (Lưu trữ vào thư mục '{folder_dest}')\n")
            success_count += 1

    print("========================================================")
    print(f"TIẾN ĐỘ QUÉT: Hoàn thành xử lý {success_count}/{total_files} tệp tin thành công. Hệ thống ổn định.")

if __name__ == "__main__":
    main()