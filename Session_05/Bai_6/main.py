while True:
    print("\n====== MENU ======")
    print("1. Nhập dữ liệu và xem báo cáo thống kê")
    print("2. Xem hướng dẫn sử dụng")
    print("3. Thoát chương trình")
    
    choice = input("Nhập lựa chọn của bạn: ")
    
    if choice == '3':
        print("Thoát chương trình")
        break
        
    elif choice == '2':
        print("\n--- Hướng dẫn sử dụng ---")
        print("Chọn chức năng 1 để bắt đầu thống kê.")
        print("Hệ thống sẽ yêu cầu nhập số chi nhánh, số lớp và số học viên từng lớp.")
        print("Vui lòng nhập số liệu nguyên dương.")
        
    elif choice == '1':
        branch_count = int(input("\nNhập số lượng chi nhánh: "))
        max_students = -1
        best_branch = 0
        
        for branch in range(1, branch_count + 1):
            print(f"\n--- Chi nhánh {branch} ---")
            class_count = int(input(f"Nhập số lớp học của chi nhánh {branch}: "))
            
            branch_total_students = 0
            low_student_classes = []
            
            for class_id in range(1, class_count + 1):
                while True:
                    student_count = int(input(f"Nhập số học viên của lớp {class_id}: "))
                    if student_count < 0:
                        print("Số học viên không hợp lệ. Vui lòng nhập lại.")
                    else:
                        break
                
                branch_total_students += student_count
                
                # Lưu lại id các lớp có ít học viên
                if student_count < 10:
                    low_student_classes.append(class_id)
            
            print(f"\n[Báo cáo Chi nhánh {branch}]")
            print(f"Tổng số học viên: {branch_total_students}")
            
            if len(low_student_classes) == 0:
                print("Không có lớp nào dưới 10 học viên.")
            else:
                classes_str = ", ".join(map(str, low_student_classes))
                print(f"Danh sách các lớp có sĩ số dưới 10 học viên: Lớp {classes_str}")
            
            # Kiểm tra chi nhánh đông nhất
            if branch_total_students > max_students:
                max_students = branch_total_students
                best_branch = branch
                
        if branch_count > 0:
            print("\n[BÁO CÁO CHUNG]")
            print(f"Chi nhánh có tổng số học viên cao nhất là Chi nhánh {best_branch} ({max_students} học viên).")
            
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 3.")