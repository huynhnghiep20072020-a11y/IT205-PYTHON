import os
import subprocess

# --- BAN CHI CAN DOI THONG TIN O DAY MOI NGAY HOC ---
ten_session = "ss7"   # Doi thanh buoi hoc hom nay
so_bai_tap = 7               # So luong bai tap
# ---------------------------------------------------

print(f"1. Dang tao thu muc {ten_session} voi {so_bai_tap} bai tap...")

if not os.path.exists(ten_session):
    subprocess.run(['mkdir', ten_session])

for i in range(so_bai_tap):
    thu_muc_con = f'{ten_session}/Bai_{i + 1}'
    
    if not os.path.exists(thu_muc_con):
        subprocess.run(['mkdir', thu_muc_con])
        
    subprocess.run(['touch', f'{thu_muc_con}/main.py'])

print(f"2. Dang CHI gom rieng {ten_session} va day len GitHub...")

# Chi add dung thu muc ten_session, bo qua cac thu muc khac
subprocess.run(['git', 'add', ten_session])

subprocess.run(['git', 'commit', '-m', f'Cap nhat bai tap rieng cho {ten_session}'])
subprocess.run(['git', 'push', '-u', 'origin', 'master'])

print(f"THANH CONG! Chi rieng {ten_session} duoc day len GitHub!")