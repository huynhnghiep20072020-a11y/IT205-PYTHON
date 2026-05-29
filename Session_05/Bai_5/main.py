branch_count = int(input("Nhập số lượng chi nhánh: "))

for branch in range(1, branch_count + 1):
    print(f"Chi nhánh {branch}:")

    for class_id in range(1, 3):
        # Ép người dùng nhập số >= 0
        while True:
            student_count = int(input(f"Nhập số học viên đi học của lớp {class_id}: "))
            if student_count < 0:
                print("Số học viên không hợp lệ. Vui lòng nhập lại.")
            else:
                break  
                
        if student_count == 0:
            print("Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.")
            continue  
            
        # Đánh giá lớp học
        if student_count >= 20:
            print(f"Chi nhánh {branch} - Lớp {class_id}: Lớp học ổn định")
        else:
            print(f"Chi nhánh {branch} - Lớp {class_id}: Lớp cần được nhắc nhở theo dõi")