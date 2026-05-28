# 1. Phân tích lỗi 
# - Biến 'total_students' đang được khởi tạo bằng 0 ở NGOÀI CÙNG vòng lặp (trước khi bắt đầu duyệt chi nhánh).
# - Chi nhánh 1: Lúc này 'total_students' = 0. Hệ thống cộng dồn 3 lớp (30 + 25 + 28) = 83. Kết quả in ra đúng là 83.
# - Chi nhánh 2: Lẽ ra 'total_students' phải được reset về 0 để tính lại từ đầu. Nhưng vì biến này đặt ngoài vòng lặp, nó vẫn đang giữ giá trị 83 của Chi nhánh 1. Hệ thống tiếp tục cộng dồn (83 + 20 + 22 + 18) = 143. Kết quả sai.
# - Chi nhánh 3: Tương tự, biến tổng đang giữ giá trị 143. Hệ thống tiếp tục cộng dồn (143 + 35 + 32 + 30) = 240. Kết quả sai.
# => Kết luận: Lỗi do không reset biến tích lũy (accumulator variable) khi bắt đầu một chu kỳ lặp mới ở vòng ngoài.

# 2. Sửa lỗi 
branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = int(input("Nhập số lớp học của mỗi chi nhánh: "))

for branch in range(1, branch_count + 1):
    print(f"\nChi nhánh {branch}")
    
    total_students = 0 
    
    for classroom in range(1, class_count + 1):
        student_count = int(input(f"Nhập số học viên lớp {classroom}: "))
        total_students += student_count
        
    print(f"Chi nhánh {branch}: {total_students} học viên")