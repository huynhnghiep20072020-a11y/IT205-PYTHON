# (1) Phân tích và thiết kế giải pháp
#   + Input: Lựa chọn menu (String), branch_count, class_count, student_count (int).
#   + Output: Báo cáo tổng học viên, danh sách lớp vắng, chi nhánh đông nhất, thông báo lỗi.
# - Giải pháp & Thuật toán:
#   + Sử dụng vòng lặp while True vòng ngoài cùng để duy trì Menu. Kiểm tra choice hợp lệ (Bẫy 2).
#   + Chức năng 1: Khởi tạo biến max_students và best_branch để theo dõi chi nhánh đông nhất.
#   + Dùng vòng lặp for duyệt từng chi nhánh. Khởi tạo tổng học viên chi nhánh = 0 và một list để lưu lớp < 10 học viên.
#   + Dùng vòng lặp for duyệt từng lớp. Dùng while True để ép nhập student_count >= 0 (Bẫy 1).
#   + Cộng dồn học viên và kiểm tra nếu < 10 thì đưa vào list.
#   + Sau khi duyệt xong lớp của 1 chi nhánh: In tổng số, in list lớp vắng hoặc thông báo nếu list rỗng (Bẫy 3). Cập nhật best_branch.
#   + In kết quả chi nhánh đông nhất khi kết thúc vòng lặp chi nhánh.

# Triển khai code
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
                
                if student_count < 10:
                    low_student_classes.append(class_id)
            
            print(f"\n[Báo cáo Chi nhánh {branch}]")
            print(f"Tổng số học viên: {branch_total_students}")
            
            if len(low_student_classes) == 0:
                print("Không có lớp nào dưới 10 học viên.")
            else:
                classes_str = ", ".join(map(str, low_student_classes))
                print(f"Danh sách các lớp có sĩ số dưới 10 học viên: Lớp {classes_str}")
            
            if branch_total_students > max_students:
                max_students = branch_total_students
                best_branch = branch
                
        if branch_count > 0:
            print("\n[BÁO CÁO CHUNG]")
            print(f"Chi nhánh có tổng số học viên cao nhất là Chi nhánh {best_branch} ({max_students} học viên).")
            
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 3.")