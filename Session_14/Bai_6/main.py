def display_grades(book):
    """
    Hiển thị toàn bộ danh sách học sinh dưới dạng bảng và tự động tính điểm trung bình.
    """
    print("\n--- BẢNG ĐIỂM HỌC SINH ---")
    print("Mã SV | Tên Học Sinh       | Điểm Toán | Điểm Anh | ĐTB")
    print("-" * 55)
    
    for student in book:
        toan = student["info"][0]
        anh = student["info"][1]
        dtb = (toan + anh) / 2
        print(f"{student['id']:5} | {student['name']:18} | {toan:<9} | {anh:<8} | {dtb:.2f}")
    
    print("-" * 55)

def add_student(book):
    """
    Thêm một hồ sơ học sinh mới vào hệ thống. Bao gồm kiểm tra trùng lặp mã ID.
    """
    student_id = input("Nhập mã học sinh mới: ").strip()
    
    for student in book:
        if student["id"] == student_id:
            print(f"Lỗi: Mã học sinh {student_id} đã tồn tại! Vui lòng nhập mã khác.")
            return

    name = input("Nhập tên học sinh: ").strip()
    math_score = float(input("Nhập điểm Toán: "))
    english_score = float(input("Nhập điểm Anh: "))
    
    new_student = {
        "id": student_id,
        "name": name,
        "info": (math_score, english_score)
    }
    book.append(new_student)
    print(f"Thành công: Đã thêm học sinh {student_id} vào hệ thống!")

def update_scores(book):
    """
    Cập nhật điểm số cho học sinh. Thực hiện ghi đè Tuple cũ bằng một Tuple mới.
    """
    student_id = input("Nhập mã học sinh cần cập nhật: ").strip()
    
    for student in book:
        if student["id"] == student_id:
            new_math = float(input("Nhập điểm Toán mới: "))
            new_english = float(input("Nhập điểm Anh mới: "))
            
            student["info"] = (new_math, new_english)
            print(f"Thành công: Đã cập nhật điểm cho học sinh {student_id}!")
            return
            
    print("Lỗi: Không tìm thấy mã học sinh này trong hệ thống!")

def delete_student(book):
    """
    Tìm kiếm và xóa hồ sơ của học sinh khỏi danh sách dựa trên mã ID.
    """
    student_id = input("Nhập mã học sinh cần xóa: ").strip()
    
    for i in range(len(book)):
        if book[i]["id"] == student_id:
            del book[i]
            print(f"Thành công: Đã xóa hồ sơ học sinh {student_id} khỏi hệ thống!")
            return
            
    print("Lỗi: Không tìm thấy mã học sinh này trong hệ thống!")

def main():
    """
    Hàm khởi chạy chương trình, chứa dữ liệu mẫu và vòng lặp menu tương tác.
    """
    grade_book = [
        {"id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
        {"id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)}
    ]
    
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===")
        print("1. Xem bảng điểm học sinh")
        print("2. Thêm hồ sơ học sinh mới")
        print("3. Cập nhật điểm số")
        print("4. Xóa hồ sơ học sinh")
        print("5. Thoát chương trình")
        print("================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        if choice == "1":
            display_grades(grade_book)
        elif choice == "2":
            add_student(grade_book)
        elif choice == "3":
            update_scores(grade_book)
        elif choice == "4":
            delete_student(grade_book)
        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng hệ thống. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

if __name__ == "__main__":
    main()