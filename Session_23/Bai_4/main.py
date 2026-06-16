# 1. Package utils

# Module score_utils.py

# Vai trò: Xử lý các logic liên quan đến điểm số.

# Hàm calculate_average(scores): * Input: List các điểm số.

# Output: Điểm trung bình (float).



# Hàm classify_student(average):

# Input: Điểm trung bình (float).

# Output: Chuỗi xếp loại (Giỏi, Khá, Trung bình, Yếu).

# Luồng xử lý: Dùng cấu trúc if/elif/else để trả về xếp loại tương ứng.

# Module string_utils.py

# Vai trò: Xử lý và chuẩn hóa chuỗi dữ liệu.

# Hàm normalize_student_names(records):

# Input: Danh sách dictionary sinh viên.

# Output: Không có (Cập nhật trực tiếp vào danh sách).


# Module random_utils.py

# Vai trò: Xử lý các tác vụ sinh dữ liệu ngẫu nhiên.

# Hàm generate_assignment_code():

# Input: Không có.

# Output: Chuỗi mã bài tập.


# 2. Package reports

# Module report_generator.py

# Vai trò: Xử lý việc in ấn và xuất báo cáo.

# Hàm display_student_scores(records):

# Input: Danh sách sinh viên.

# Output: In kết quả ra terminal.

# Luồng xử lý: Nếu danh sách rỗng, in cảnh báo. Nếu có, gọi hàm tính điểm, xếp loại và in theo format.

# Hàm export_learning_report(records):

# Input: Danh sách sinh viên.

# Output: File learning_report.txt và in thông báo màu.


from data.students import student_records
from utils.string_utils import normalize_student_names
from utils.random_utils import generate_assignment_code
from reports.report_generator import display_student_scores, export_learning_report

def main():
    """Vòng lặp chính điều hướng hệ thống bằng match-case."""
    while True:
        print("\n===== HỆ THỐNG TIỆN ÍCH HỌC TẬP RIKKEI ACADEMY =====")
        print("1. Xem danh sách sinh viên và điểm trung bình")
        print("2. Chuẩn hóa tên sinh viên")
        print("3. Sinh mã bài tập ngẫu nhiên")
        print("4. Xuất báo cáo học tập")
        print("5. Thoát chương trình")
        print("====================================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        match choice:
            case "1":
                display_student_scores(student_records)
            case "2":
                normalize_student_names(student_records)
            case "3":
                generate_assignment_code()
            case "4":
                export_learning_report(student_records)
            case "5":
                print("Cảm ơn bạn đã sử dụng hệ thống!")
                break
            case _:
                print("Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 5.")

if __name__ == "__main__":
    main()