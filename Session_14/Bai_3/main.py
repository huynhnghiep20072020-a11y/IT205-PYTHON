#  validate_score hoặc find_student_by_id nhận đầu vào là các giá trị đơn lẻ (như chuỗi điểm số, mã học viên)
#  và return về kết quả logic (True/False hoặc vị trí Index). Các hàm chức năng chính thì nhận đầu vào
#  là toàn bộ mảng student_list để thực hiện thao tác in ấn hoặc thêm/sửa dữ liệu.


students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]

def validate_score(score_input):
    """
    Kiểm tra dữ liệu điểm số nhập vào có phải là số hợp lệ từ 0 đến 10 hay không.
    """
    try:
        score = float(score_input)
        if 0 <= score <= 10:
            return True
        return False
    except ValueError:
        return False

def find_student_by_id(student_list, student_id):
    """
    Tìm kiếm học viên theo mã. Trả về index nếu tìm thấy, ngược lại trả về -1.
    """
    for i in range(len(student_list)):
        if student_list[i]["student_id"] == student_id:
            return i
    return -1

def get_rank(average_score):
    """
    Xếp loại học lực dựa trên điểm trung bình.
    """
    if average_score >= 8.0:
        return "Giỏi"
    elif average_score >= 6.5:
        return "Khá"
    elif average_score >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

def display_students(student_list):
    """
    Hiển thị danh sách toàn bộ học viên hiện có.
    """
    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống.")
    else:
        for i in range(len(student_list)):
            s = student_list[i]
            print(f"{i + 1}. Mã: {s['student_id']} | Tên: {s['name']} | Toán: {s['math_score']} | Anh: {s['english_score']}")

def add_student(student_list):
    """
    Thêm một học viên mới vào hệ thống cùng với các điều kiện kiểm tra dữ liệu đầu vào.
    """
    student_id = input("Mã Học Viên: ").strip().upper()
    if find_student_by_id(student_list, student_id) != -1:
        print("Mã học viên đã tồn tại, vui lòng nhập mã khác!")
        return

    name = input("Tên Học Viên: ").strip().title()
    if name == "":
        print("Tên không được để trống!")
        return

    math_input = input("Nhập Điểm Toán: ")
    if not validate_score(math_input):
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")
        return
    
    english_input = input("Nhập Điểm Anh: ")
    if not validate_score(english_input):
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")
        return

    student_list.append({
        "student_id": student_id,
        "name": name,
        "math_score": float(math_input),
        "english_score": float(english_input)
    })
    print("Thêm học viên thành công!")

def update_score(student_list):
    """
    Cập nhật điểm Toán và điểm Anh cho học viên dựa trên mã học viên.
    """
    student_id = input("Nhập mã học viên cần cập nhật: ").strip().upper()
    index = find_student_by_id(student_list, student_id)
    
    if index == -1:
        print(f"Không tìm thấy học viên mang mã {student_id}!")
        return
        
    math_input = input("Nhập Điểm Toán mới: ")
    if not validate_score(math_input):
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")
        return
        
    english_input = input("Nhập Điểm Anh mới: ")
    if not validate_score(english_input):
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")
        return
        
    student_list[index]["math_score"] = float(math_input)
    student_list[index]["english_score"] = float(english_input)
    print("Cập nhật điểm thành công!")

def evaluate_students(student_list):
    """
    Duyệt danh sách, tính điểm trung bình và in ra kết quả xếp loại của từng học viên.
    """
    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống.")
        return
        
    for s in student_list:
        avg = (s["math_score"] + s["english_score"]) / 2
        rank = get_rank(avg)
        print(f"Mã: {s['student_id']} | Tên: {s['name']} | ĐTB: {avg} | Xếp loại: {rank}")

def main():
    """
    Vòng lặp chính điều hướng menu của hệ thống.
    """
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====")
        print("1. Hiển thị danh sách học viên")
        print("2. Thêm học viên mới")
        print("3. Cập nhật điểm thi theo mã học viên")
        print("4. Đánh giá học lực của toàn bộ học viên")
        print("5. Thoát chương trình")
        
        choice = input("Vui lòng chọn chức năng (1-5): ")
        
        if choice == "1":
            display_students(students)
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            update_score(students)
        elif choice == "4":
            evaluate_students(students)
        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

main()