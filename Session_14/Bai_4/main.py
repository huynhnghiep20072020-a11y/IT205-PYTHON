#  Hàm phụ trợ calculate_average được tạo ra để gom nhóm logic dùng chung, triệt tiêu việc phải viết lại một công thức nhiều lần ở các chức năng khác nhau.
# Hệ thống phân định ranh giới rõ ràng: hàm nào làm nhiệm vụ tính toán thì trả về số liệu (Return float), hàm nào điều hướng giao diện hoặc cập nhật thì không trả gì cả (Return None).
#  Hàm update_student_score đóng vai trò như một màng lọc bảo mật, tự động chuẩn hóa chuỗi và chặn đứng dữ liệu rác (chữ cái, số âm) bằng try-except và ràng kiện toán học 
# Việc kiểm tra độ dài danh sách ngay dòng đầu tiên của các hàm báo cáo là cách tối ưu nhất để "chặn đứng" lỗi sập bộ nhớ (Crash) trước khi thuật toán kịp chạy.


def calculate_average(student):
    """Tính và trả về điểm trung bình của một sinh viên."""
    return (student["math"] + student["physics"] + student["chemistry"]) / 3

def display_grades(records):
    """Tính điểm trung bình, phân loại học lực và in ra bảng điểm."""
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
        
    print("--- BẢNG ĐIỂM SINH VIÊN ---")
    for i in range(len(records)):
        student = records[i]
        dtb = calculate_average(student)
        
        if dtb >= 8.0:
            rank = "Giỏi"
        elif dtb >= 6.5:
            rank = "Khá"
        elif dtb >= 5.0:
            rank = "Trung bình"
        else:
            rank = "Yếu"
            
        print(f"{i + 1}. [{student['student_id']}] {student['name']} | Toán: {student['math']} | Lý: {student['physics']} | Hóa: {student['chemistry']} | ĐTB: {dtb:.2f} - {rank}")

def update_student_score(records):
    """Cập nhật điểm thi cho sinh viên theo mã sinh viên và môn học."""
    student_id = input("Nhập mã sinh viên cần cập nhật: ").strip().upper()
    found_student = None
    
    for student in records:
        if student["student_id"] == student_id:
            found_student = student
            break
            
    if found_student is None:
        print(f"Không tìm thấy sinh viên mang mã {student_id} trong hệ thống!")
        return

    choice = input("Chọn môn học (1-Toán, 2-Lý, 3-Hóa): ").strip()
    if choice not in ["1", "2", "3"]:
        print("Lựa chọn môn học không hợp lệ.")
        return

    try:
        new_score = float(input("Nhập điểm mới: "))
        if new_score < 0 or new_score > 10:
            print("Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!")
            return
    except ValueError:
        print("Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!")
        return

    if choice == "1":
        found_student["math"] = new_score
        subject_name = "Toán"
    elif choice == "2":
        found_student["physics"] = new_score
        subject_name = "Lý"
    else:
        found_student["chemistry"] = new_score
        subject_name = "Hóa"
        
    print(f">> Đã cập nhật điểm {subject_name} của sinh viên '{found_student['name']}' thành {new_score}.")

def generate_report(records):
    """Thống kê số lượng và tỷ lệ sinh viên đỗ/trượt dựa trên điểm trung bình."""
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
        
    total_students = len(records)
    pass_count = 0
    
    for student in records:
        if calculate_average(student) >= 5.0:
            pass_count += 1
            
    fail_count = total_students - pass_count
    pass_rate = (pass_count / total_students) * 100
    fail_rate = (fail_count / total_students) * 100
    
    print("--- BÁO CÁO HỌC VỤ ---")
    print(f"Tổng số sinh viên: {total_students}")
    print(f"Số lượng qua môn (ĐTB >= 5.0): {pass_count} sinh viên (Chiếm {pass_rate:.2f}%)")
    print(f"Số lượng trượt (ĐTB < 5.0): {fail_count} sinh viên (Chiếm {fail_rate:.2f}%)")

def find_valedictorian(records):
    """Tìm và vinh danh sinh viên có điểm trung bình cao nhất (Thủ khoa)."""
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
        
    max_dtb = -1
    valedictorian = None
    
    for student in records:
        dtb = calculate_average(student)
        if dtb > max_dtb:
            max_dtb = dtb
            valedictorian = student
            
    print("--- VINH DANH THỦ KHOA ---")
    print(f"Sinh viên: {valedictorian['name']} (Mã: {valedictorian['student_id']})")
    print(f"Điểm Trung Bình: {max_dtb:.2f}")
    print("Chúc mừng sinh viên đã đạt thành tích xuất sắc nhất khóa!")

def main():
    #dữ liệu mẫu ban đầu cho hệ thống quản lý điểm thi
    """Vòng lặp chính để chạy menu điều hướng của chương trình."""
    student_records = [
        {"student_id": "SV001", "name": "Nguyễn Văn A", "math": 8.5, "physics": 7.0, "chemistry": 9.0},
        {"student_id": "SV002", "name": "Trần Thị B", "math": 4.0, "physics": 5.5, "chemistry": 5.0},
        {"student_id": "SV003", "name": "Lê Văn C", "math": 9.5, "physics": 9.0, "chemistry": 8.5}
    ]
    
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====")
        print("1. Xem bảng điểm và học lực")
        print("2. Cập nhật điểm thi sinh viên")
        print("3. Báo cáo thống kê (Đỗ/Trượt)")
        print("4. Tìm sinh viên Thủ khoa")
        print("5. Thoát chương trình")
        print("=========================================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        if choice == "1":
            display_grades(student_records)
        elif choice == "2":
            update_student_score(student_records)
        elif choice == "3":
            generate_report(student_records)
        elif choice == "4":
            find_valedictorian(student_records)
        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

main()