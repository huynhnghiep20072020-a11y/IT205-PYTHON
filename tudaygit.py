import os
import subprocess

# Duong link GitHub cua ban
repo_url = "https://github.com/huynhnghiep20072020-a11y/IT205-PYTHON.git"

print("1. Dang cau hinh Git va ket noi GitHub...")
subprocess.run(['git', 'init'])
# Xoa link cu (neu co bi loi) de cai lai cho chac chan
subprocess.run(['git', 'remote', 'remove', 'origin'], stderr=subprocess.DEVNULL)
# Them link GitHub chuan
subprocess.run(['git', 'remote', 'add', 'origin', repo_url])

print("2. Dang tao cac thu muc bai tap...")
for i in range(10):
    folder_name = f'BTVN_{i + 1}'
    # Neu chua co thu muc thi tao moi
    if not os.path.exists(folder_name):
        subprocess.run(['mkdir', folder_name])
    # Tao file main.py ben trong thu muc
    subprocess.run(['touch', f'{folder_name}/main.py'])

print("3. Dang day toan bo bai cua lop CNTT5 len GitHub...")
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'Cap nhat BTVN tu 1 den 10'])
# Day toan bo len nhanh master
subprocess.run(['git', 'push', '-u', 'origin', 'master'])

print("🎉 THANH CONG! Ban len trang GitHub kiem tra nhe!")