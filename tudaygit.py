import os
import subprocess

# --- BẠN CÓ THỂ THAY ĐỔI 2 DÒNG NÀY CHO MỖI BUỔI HỌC ---
ten_session = "Session_03"   # Đặt tên thư mục của buổi học (VD: Session_03, sse5...)
so_bai_tap = 7               # Số lượng bài tập thầy giao trong buổi đó
# -------------------------------------------------------

print(f"1. Dang tao thu muc {ten_session} voi {so_bai_tap} bai tap ben trong...")

# 1. Tạo thư mục Session ở ngoài cùng (nếu chưa có)
if not os.path.exists(ten_session):
    subprocess.run(['mkdir', ten_session])

# 2. Tạo các thư mục Bai_1, Bai_2... nằm lồng bên trong Session
for i in range(so_bai_tap):
    # Đường dẫn bây giờ sẽ có dạng: Session_03/Bai_1
    thu_muc_con = f'{ten_session}/Bai_{i + 1}'
    
    # Tạo thư mục con
    if not os.path.exists(thu_muc_con):
        subprocess.run(['mkdir', thu_muc_con])
        
    # Tạo file main.py trống nằm trong thư mục con đó
    subprocess.run(['touch', f'{thu_muc_con}/main.py'])

print("2. Dang gom cac thay doi va day len GitHub...")
# Tự động add, commit và push lên GitHub
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', f'Cap nhat bai tap cho {ten_session}'])
subprocess.run(['git', 'push', '-u', 'origin', 'master'])

print("THANH CONG! Code da len git!")