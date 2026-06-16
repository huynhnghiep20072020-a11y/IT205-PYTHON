import os

def safe_create_dir(path):
    """Khởi tạo thư mục lưu trữ một cách an toàn, bỏ qua nếu đã tồn tại."""
    os.makedirs(path, exist_ok=True)