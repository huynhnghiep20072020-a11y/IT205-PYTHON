import math

def calculate_disk_blocks(size_bytes, block_size=4096):
    """Tính toán số block ổ đĩa tiêu tốn bằng cách làm tròn lên."""
    return math.ceil(size_bytes / block_size)