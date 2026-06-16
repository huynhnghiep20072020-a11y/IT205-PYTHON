import datetime as dt
import colorama as cr
from utils.score_utils import calculate_average, classify_student

cr.init(autoreset=True)

def display_student_scores(records):
    """Hiển thị danh sách điểm và học lực của sinh viên."""
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("--- DANH SÁCH ĐIỂM SINH VIÊN ---")
    for i, student in enumerate(records):
        avg = calculate_average(student["scores"])
        rank = classify_student(avg)
        print(f"{i + 1}. [{student['student_id']}] {student['name']} | Điểm: {student['scores']} | ĐTB: {avg:.2f} - {rank}")
    print("---------------------------------")

def export_learning_report(records):
    """Thống kê, xuất báo cáo ra file txt và in thông báo màu ra màn hình."""
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total_students = len(records)
    passed_count = 0
    failed_count = 0

    for student in records:
        avg = calculate_average(student["scores"])
        if avg >= 5.0:
            passed_count += 1
        else:
            failed_count += 1

    current_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("learning_report.txt", "w", encoding="utf-8") as file:
        file.write("BÁO CÁO HỌC TẬP RIKKEI ACADEMY\n")
        file.write(f"Thời gian tạo: {current_time}\n")
        file.write("-" * 30 + "\n")
        file.write(f"Tổng số sinh viên: {total_students}\n")
        file.write(f"Số sinh viên đạt yêu cầu: {passed_count}\n")
        file.write(f"Số sinh viên cần cải thiện: {failed_count}\n")

    print("--- XUẤT BÁO CÁO HỌC TẬP ---")
    print(f"Tổng số sinh viên: {total_students}")
    print(f"Số sinh viên đạt yêu cầu: {passed_count}")
    print(f"Số sinh viên cần cải thiện: {failed_count}")
    print(cr.Fore.GREEN + ">> Đã xuất báo cáo ra file learning_report.txt")