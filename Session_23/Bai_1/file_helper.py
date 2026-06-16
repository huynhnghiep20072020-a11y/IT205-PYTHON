import os

def create_log_dir(dir_name):
    """Kiểm tra sự tồn tại của thư mục trước khi tạo để tránh sập chương trình."""
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)