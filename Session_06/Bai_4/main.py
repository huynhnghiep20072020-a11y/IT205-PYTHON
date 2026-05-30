# 1. Bẫy 1: Cần dùng if để chặn đứng chương trình ngay từ đầu nếu số lượng phiếu <= 0.
# 2. Bẫy 2: Dùng hàm .split('|') để tách chuỗi và kiểm tra độ dài mảng (len) phải bằng chính xác 4.
# 3. Bẫy 3 & 4: Dùng từ khóa 'in' để tìm ký tự '@' trong email và hàm len() để đo chiều dài mã học viên.
# 4. Chuẩn hóa: Dùng .strip() xóa khoảng trắng, .title() cho Họ tên/Khóa học, .upper() cho Mã HV và .lower() cho Email.
# 5. Mã xác nhận: Cần lấy Mã HV nối với '_' và tên Khóa học (đã được .upper() và .replace() khoảng trắng thành dấu '-').

num_forms = int(input("Nhập số lượng phiếu đăng ký cần xử lý: "))

if num_forms <= 0:
    print("Số lượng phiếu đăng ký không hợp lệ")
else:
    for i in range(num_forms):
        raw_data = input(f"\nNhập chuỗi dữ liệu phiếu {i+1}: ")
        

        parts = raw_data.split('|')
        

        if len(parts) != 4:
            print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
            continue
            
        name = parts[0].strip().title()
        course = parts[1].strip().title() 
        student_code = parts[2].strip().upper()
        email = parts[3].strip().lower()
        

        if "@" not in email:
            print("Email không hợp lệ. Bỏ qua phiếu này")
            continue
            
        if len(student_code) < 5:
            print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
            continue
            

        course_formatted = course.upper().replace(" ", "-")
        confirmation_code = f"{student_code}_{course_formatted}"
        
        print("\n===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
        print(f"Học viên: {name}")
        print(f"Khóa học: {course}")
        print(f"Mã học viên: {student_code}")
        print(f"Email: {email}")
        print(f"Mã xác nhận: {confirmation_code}")