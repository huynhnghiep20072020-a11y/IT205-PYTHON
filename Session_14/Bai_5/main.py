# Thay vì phải viết đi viết lại vòng lặp tìm kiếm mã học viên ở tận 4 chức năng 
# (Đổi điểm, Phúc khảo, Nhân hệ số, Chấm bài), việc tách ra một hàm riêng trả về vị trí (index)
# giúp mã nguồn ngắn gọn và tối ưu hơn rất nhiều.

# Trong mỗi hàm chức năng, mã học viên được chuẩn hóa bằng .strip().upper().
# Các lỗi nhập liệu (nhập chữ thay vì số, nhập số âm, tiêu điểm vượt quá số dư)
# đều được kiểm soát chặt chẽ bằng khối try-except và các câu lệnh if kiểm tra điều kiện ngay từ đầu hàm.


def find_student(records, student_id):
    """Tìm kiếm học viên theo mã học viên và trả về vị trí index trong danh sách."""
    student_id = student_id.strip().upper()
    for i in range(len(records)):
        if records[i]["student_id"] == student_id:
            return i
    return -1

def display_statements(records):
    """Hiển thị sao kê điểm số và phân loại trạng thái của tất cả học viên."""
    print("--- SAO KÊ ĐIỂM SỐ ---")
    for i in range(len(records)):
        student = records[i]
        points = student["current_points"]
        
        if points < 500:
            status = "Cần tích lũy thêm"
        elif 500 <= points <= 1500:
            status = "Thành viên tiềm năng"
        else:
            status = "Thành viên ưu tú"
            
        print(f"{i + 1}. Mã: {student['student_id']} | Tên: {student['name']} | Hiện có: {student['current_points']} | Đã tiêu: {student['spent_points']} | Hoàn trả: {student['refunded_points']} | Hệ số: x{student['multiplier']} | Trạng thái: {status}")

def redeem_rewards(records):
    """Xử lý việc trừ điểm hiện có và cộng vào điểm đã tiêu khi sinh viên đổi quà."""
    student_id = input("Nhập mã học viên đổi quà: ")
    index = find_student(records, student_id)
    
    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return
        
    try:
        points_to_spend = int(input("Nhập số điểm cần tiêu: "))
        if points_to_spend <= 0:
            print("Số điểm tiêu phải là số nguyên dương.")
            return
            
        if points_to_spend > records[index]["current_points"]:
            print("Số dư điểm không đủ để thực hiện giao dịch!")
            return
            
        records[index]["current_points"] -= points_to_spend
        records[index]["spent_points"] += points_to_spend
        print(f">> Giao dịch thành công! '{records[index]['name']}' đã tiêu {points_to_spend} điểm. Số dư còn lại: {records[index]['current_points']} điểm.")
    except ValueError:
        print("Lỗi nhập liệu, vui lòng nhập số nguyên dương.")

def appeal_score(records):
    """Xử lý hoàn điểm khi phúc khảo thành công, giảm điểm đã tiêu và tăng điểm hiện có."""
    student_id = input("Nhập mã học viên cần phúc khảo: ")
    index = find_student(records, student_id)
    
    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return
        
    try:
        points_to_refund = int(input("Nhập số điểm hoàn lại: "))
        if points_to_refund <= 0:
            print("Số điểm hoàn phải là số nguyên dương.")
            return
            
        if points_to_refund > records[index]["spent_points"]:
            print("Không thể hoàn số điểm lớn hơn tổng điểm đã tiêu!")
            return
            
        records[index]["spent_points"] -= points_to_refund
        records[index]["current_points"] += points_to_refund
        records[index]["refunded_points"] += points_to_refund
        print(f">> Hoàn điểm thành công! '{records[index]['name']}' được cộng lại {points_to_refund} điểm.")
    except ValueError:
        print("Lỗi nhập liệu, vui lòng nhập số nguyên dương.")

def activate_multiplier(records):
    """Kiểm tra và cập nhật hệ số nhân điểm mới cho học viên."""
    student_id = input("Nhập mã học viên nhận hệ số: ")
    index = find_student(records, student_id)
    
    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return
        
    try:
        new_multiplier = float(input("Nhập hệ số nhân mới (1.0 - 3.0): "))
        if new_multiplier < 1.0 or new_multiplier > 3.0:
            print("Hệ số nhân không hợp lệ. Chỉ chấp nhận số từ 1.0 đến 3.0.")
            return
            
        records[index]["multiplier"] = new_multiplier
        print(f">> Đã kích hoạt hệ số x{new_multiplier} cho học viên '{records[index]['name']}'.")
    except ValueError:
        print("Hệ số nhân không hợp lệ. Chỉ chấp nhận số từ 1.0 đến 3.0.")

def grade_assignment(records):
    """Tính toán điểm thực nhận dựa trên điểm gốc và hệ số, sau đó cộng vào tài khoản."""
    student_id = input("Nhập mã học viên vừa nộp bài: ")
    index = find_student(records, student_id)
    
    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return
        
    try:
        base_points = int(input("Nhập số điểm gốc đạt được: "))
        if base_points <= 0:
            print("Số điểm gốc phải là số nguyên dương.")
            return
            
        actual_points = int(base_points * records[index]["multiplier"])
        records[index]["current_points"] += actual_points
        print(f">> Hệ số hiện tại của '{records[index]['name']}' là x{records[index]['multiplier']}. Điểm thực nhận: {actual_points}.")
        print(f">> Đã cộng {actual_points} điểm vào tài khoản!")
    except ValueError:
        print("Lỗi nhập liệu, vui lòng nhập số nguyên dương.")

def main():
    """Hàm khởi chạy chứa dữ liệu mẫu và vòng lặp menu chính."""
    student_records = [
        {
            "student_id": "RA01",
            "name": "Nguyễn Văn Code",
            "current_points": 1500,
            "spent_points": 500,
            "refunded_points": 0,
            "multiplier": 1.0
        },
        {
            "student_id": "RA02",
            "name": "Trần Thị Bug",
            "current_points": 800,
            "spent_points": 1200,
            "refunded_points": 100,
            "multiplier": 1.5
        },
        {
            "student_id": "RA03",
            "name": "Lê Văn Fix",
            "current_points": 300,
            "spent_points": 0,
            "refunded_points": 0,
            "multiplier": 2.0
        }
    ]
    
    while True:
        print("\n===== HỆ THỐNG NGÂN HÀNG ĐIỂM SỐ RIKKEI ACADEMY =====")
        print("1. Hiển thị sao kê điểm số")
        print("2. Đổi điểm lấy phần thưởng")
        print("3. Phúc khảo bài thi (Hoàn điểm)")
        print("4. Kích hoạt (Hệ số nhân điểm)")
        print("5. Chấm bài (thêm điểm)")
        print("6. Thoát chương trình")
        print("=====================================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()
        
        if choice == "1":
            display_statements(student_records)
        elif choice == "2":
            redeem_rewards(student_records)
        elif choice == "3":
            appeal_score(student_records)
        elif choice == "4":
            activate_multiplier(student_records)
        elif choice == "5":
            grade_assignment(student_records)
        elif choice == "6":
            print("Chào tạm biệt và kết thúc vòng lặp.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

if __name__ == "__main__":
    main()