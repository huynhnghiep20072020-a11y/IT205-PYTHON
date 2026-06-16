import random
import string

def generate_assignment_code():
    """Sinh mã bài tập ngẫu nhiên theo định dạng PY-[4 ký tự]."""
    characters = string.ascii_uppercase + string.digits
    random_chars = random.choices(characters, k=4)
    code_suffix = "".join(random_chars)
    
    print("--- SINH MÃ BÀI TẬP ---")
    print(f"Mã bài tập của bạn là: PY-{code_suffix}")