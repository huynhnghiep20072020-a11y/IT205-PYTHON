# (1) Phân tích và thiết kế giải pháp
#   + Input: branch_count (int), student_count (int).
#   + Output: Thông báo trạng thái lớp học, cảnh báo lỗi (String).
# - Giải pháp & Thuật toán:
#   + Dùng vòng lặp for ngoài duyệt từng chi nhánh (từ 1 đến branch_count).
#   + Dùng vòng lặp for trong duyệt 2 lớp (range(1, 3)).
#   + (Bẫy 1): Dùng vòng lặp while True khi nhập student_count. Nếu < 0, báo lỗi và bắt nhập lại (không break). Nếu >= 0 thì break.
#   + (Bẫy 2): Dùng lệnh if kiểm tra student_count == 0. Nếu đúng, in thông báo và dùng lệnh 'continue' để bỏ qua các lệnh phía dưới.
#   + Dùng if/else đánh giá student_count >= 20 hoặc < 20 để in trạng thái.

# (2) Triển khai code
branch_count = int(input("Nhập số lượng chi nhánh: "))

for branch in range(1, branch_count + 1):
    print(f"Chi nhánh {branch}:")

    for class_id in range(1, 3):
        while True:
            student_count = int(input(f"Nhập số học viên đi học của lớp {class_id}: "))
            
            if student_count < 0:
                print("Số học viên không hợp lệ. Vui lòng nhập lại.")
            else:
                break  
        if student_count == 0:
            print("Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.")
            continue  
        if student_count >= 20:
            print(f"Chi nhánh {branch} - Lớp {class_id}: Lớp học ổn định")
        else:
            print(f"Chi nhánh {branch} - Lớp {class_id}: Lớp cần được nhắc nhở theo dõi")