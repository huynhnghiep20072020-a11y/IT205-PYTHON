def normalize_student_names(records):
    """Chuẩn hóa tên sinh viên: xóa khoảng trắng thừa và viết hoa chữ cái đầu."""
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("--- CHUẨN HÓA TÊN SINH VIÊN ---")
    for student in records:
        raw_name = student["name"]
        words = raw_name.split()
        normalized_name = " ".join(words).title()
        student["name"] = normalized_name
        print(f"{student['student_id']}: {student['name']}")
        
    print(">> Đã chuẩn hóa toàn bộ tên sinh viên.")