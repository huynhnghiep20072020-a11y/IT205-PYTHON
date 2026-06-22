from models import BaseEmployee, Lecturer, AdmissionStaff, HybridManager
from services import VietcombankCorporateService, TechcombankCorporateService, execute_payroll

def get_employee_by_code(employees, emp_code):
    """Hàm phụ trợ tìm kiếm nhân sự theo mã."""
    for emp in employees:
        if emp.emp_code == emp_code:
            return emp
    return None

def main():
    """Hệ thống điều hướng Menu CLI quản lý nhân sự."""
    employees = []
    current_employee = None

    while True:
        print("\n===== RIKKEI EDUCATION HR SIMULATOR PRO =====")
        print("1. Tuyển dụng nhân sự mới (Chọn loại hợp đồng nhân sự)")
        print("2. Xem thông tin & Kiểm tra thứ tự kế thừa (MRO)")
        print("3. Ghi nhận công nhật & Cập nhật KPI (Tính đa hình)")
        print("4. Tổng hợp quỹ lương và ngân sách chi trả")
        print("5. Kiểm tra gộp giờ làm việc & So sánh hiệu suất (Overloading)")
        print("6. Giải ngân lương qua Cổng thanh toán đối tác (Duck Typing)")
        print("7. Thoát chương trình")
        print("==============================================")
        
        choice = input("Chọn chức năng (1-7): ").strip()

        match choice:
            case "1":
                print("--- CHỌN LOẠI NHÂN SỰ KHỞI TẠO ---")
                print("1. Lecturer (Giảng viên chuyên trách)")
                print("2. Admission Staff (Nhân viên Tuyển sinh)")
                print("3. Hybrid Manager (Quản lý kiêm Giảng dạy)")
                emp_type = input("Chọn loại nhân sự (1-3): ").strip()
                
                code = input("Nhập mã nhân sự 10 ký tự: ").strip().upper()
                if not BaseEmployee.validate_employee_code(code):
                    print("Mã nhân sự không hợp lệ! Phải gồm đúng 10 ký tự và bắt đầu bằng RKE.")
                    continue
                    
                name = input("Nhập họ và tên: ").strip()
                
                try:
                    if emp_type == "1":
                        new_emp = Lecturer(code, name)
                        type_name = "Giảng viên"
                    elif emp_type == "2":
                        target = float(input("Nhập chỉ tiêu doanh số: "))
                        new_emp = AdmissionStaff(code, name, target)
                        type_name = "Nhân viên Tuyển sinh"
                    elif emp_type == "3":
                        target = float(input("Nhập chỉ tiêu doanh số: "))
                        new_emp = HybridManager(code, name, target)
                        type_name = "Quản lý Hybrid"
                    else:
                        print("Lựa chọn loại nhân sự không hợp lệ.")
                        continue

                    employees.append(new_emp)
                    current_employee = new_emp
                    print(f"\nTuyển dụng {type_name} thành công!")
                    print(f"Tên nhân sự: {new_emp.full_name}")
                except ValueError:
                    print("Lỗi: Dữ liệu nhập vào không hợp lệ.")

            case "2":
                if current_employee is None:
                    print("Hệ thống chưa có thông tin nhân sự. Vui lòng tuyển dụng trước.")
                    continue
                    
                print("--- THÔNG TIN NHÂN SỰ HIỆN TẠI ---")
                print(f"Loại nhân sự: {current_employee.__class__.__name__}")
                print(f"Tổ chức: {BaseEmployee.company_name}")
                print(f"Mã nhân sự: {current_employee.emp_code}")
                print(f"Họ và tên: {current_employee.full_name}")
                print(f"Số giờ làm việc: {current_employee.working_hours} giờ")
                
                if isinstance(current_employee, Lecturer):
                    print(f"Số ca đã dạy: {current_employee.teaching_slots} ca")
                if isinstance(current_employee, AdmissionStaff):
                    print(f"Doanh số mang về: {current_employee.revenue_generated:,.0f} VND")
                    
                print("\n[Danh sách MRO của lớp hiện tại]:")
                for cls in current_employee.__class__.__mro__:
                    print(f"- {cls.__name__}")

            case "3":
                if current_employee is None:
                    print("Hệ thống chưa có thông tin nhân sự.")
                    continue
                    
                print("--- GHI NHẬN CÔNG NHẬT & HIỆU SUẤT ---")
                print("1. Ghi nhận tham gia đứng lớp (Chỉ dành cho Giảng viên/Hybrid)")
                print("2. Cập nhật tiến độ KPI / Doanh số")
                action = input("Chọn tác vụ (1-2): ").strip()
                
                try:
                    if action == "1":
                        if isinstance(current_employee, Lecturer):
                            current_employee.conduct_class()
                        else:
                            print("Lỗi: Nhân sự này không có chức năng đứng lớp.")
                    elif action == "2":
                        val = float(input("Nhập chỉ số KPI/Doanh số mới cập nhật: "))
                        current_employee.update_kpi(val)
                    else:
                        print("Lựa chọn tác vụ không hợp lệ.")
                except ValueError as e:
                    if "could not convert string" in str(e).lower():
                        print("Lỗi: Số liệu phải là chữ số hợp lệ.")
                    else:
                        print(f"Lỗi: {e}")

            case "4":
                if current_employee is None:
                    print("Hệ thống chưa có thông tin nhân sự.")
                    continue
                    
                print("--- CHI TIẾT QUỸ LƯƠNG NHÂN SỰ ---")
                print(f"Nhân sự: {current_employee.full_name} (Loại: {current_employee.__class__.__name__})")
                print(f"Mức lương cơ sở hệ thống: {BaseEmployee.base_salary_rate:,.0f} VND")
                print(f"Số giờ làm việc tích lũy: {current_employee.working_hours} giờ")
                total_salary = current_employee.calculate_salary()
                print(f"Tổng lương thực nhận tháng này: {total_salary:,.0f} VND")

            case "5":
                if current_employee is None:
                    print("Hệ thống chưa có thông tin nhân sự.")
                    continue
                    
                print("--- ĐỒNG BỘ & SO SÁNH GIỜ CÔNG (OPERATOR OVERLOADING) ---")
                print(f"Nhân sự hiện tại (A): {current_employee.full_name} (Giờ công: {current_employee.working_hours} giờ)")
                target_code = input("Chọn mã nhân sự đối ứng (B) từ danh sách: ").strip().upper()
                target_emp = get_employee_by_code(employees, target_code)
                
                if target_emp:
                    print(f"Nhân sự đối ứng (B): {target_emp.full_name} (Giờ công: {target_emp.working_hours} giờ)")
                    try:
                        if current_employee < target_emp:
                            comp_res = "ÍT HƠN"
                        elif target_emp < current_employee:
                            comp_res = "NHIỀU HƠN"
                        else:
                            comp_res = "BẰNG"
                        
                        print(f"[Kết quả So sánh (__lt__)]: Giờ công cống hiến của nhân sự A {comp_res} nhân sự B.")
                        
                        total_sum = current_employee + target_emp
                        print(f"[Kết quả Tổng hợp (__add__)]: Tổng số giờ làm việc của cả 2 nhân sự là: {total_sum} giờ.")
                    except TypeError:
                        print("Lỗi: Không thể thực hiện tính toán do kiểu dữ liệu không tương thích.")
                else:
                    print("Không tìm thấy nhân sự đối ứng trong hệ thống.")

            case "6":
                if current_employee is None:
                    print("Hệ thống chưa có thông tin nhân sự.")
                    continue
                    
                print("--- CHI TRẢ LƯƠNG QUA CỔNG ĐỐI TÁC TRUNG GIAN ---")
                print("1. Chi trả qua tài khoản Doanh nghiệp Vietcombank")
                print("2. Chi trả qua tài khoản Doanh nghiệp Techcombank")
                print("3. Chi trả qua Cổng Lỗi (Test Duck Typing)")
                bank_choice = input("Chọn cổng ngân hàng (1-3): ").strip()
                
                try:
                    amount = current_employee.calculate_salary()
                    
                    if bank_choice == "1":
                        service = VietcombankCorporateService()
                    elif bank_choice == "2":
                        service = TechcombankCorporateService()
                    elif bank_choice == "3":
                        class FakeBank:
                            pass
                        service = FakeBank()
                    else:
                        print("Lựa chọn không hợp lệ.")
                        continue
                        
                    execute_payroll(service, current_employee, amount)
                except Exception as e:
                    print(f"Lỗi hệ thống: {e}")

            case "7":
                print("Cảm ơn đã sử dụng hệ thống Quản lý Nhân sự Rikkei Education Pro!")
                break

            case _:
                print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 7.")


if __name__ == "__main__":
    main()