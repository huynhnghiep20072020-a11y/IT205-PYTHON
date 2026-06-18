from abc import ABC, abstractmethod

class Employee(ABC):
    """Lớp cơ sở trừu tượng đại diện cho khuôn mẫu nhân viên chung."""

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def display_info(self):
        """Phương thức hiển thị thông tin cơ bản của nhân viên."""
        pass

    @abstractmethod
    def calculate_salary(self):
        """Phương thức trừu tượng bắt buộc các lớp con phải tự định nghĩa công thức tính lương."""
        pass


class FullTimeEmployee(Employee):
    """Lớp đại diện cho nhân viên toàn thời gian."""

    def __init__(self, employee_id, name, base_salary, bonus):
        super().__init__(employee_id, name)
        self.base_salary = base_salary
        self.bonus = bonus

    def display_info(self):
        print(f"Mã NV: {self.employee_id} | Họ tên: {self.name} | Loại: Full-time")

    def calculate_salary(self):
        return self.base_salary + self.bonus


class PartTimeEmployee(Employee):
    """Lớp đại diện cho nhân viên bán thời gian."""

    def __init__(self, employee_id, name, working_hours, hourly_rate):
        super().__init__(employee_id, name)
        self.working_hours = working_hours
        self.hourly_rate = hourly_rate

    def display_info(self):
        print(f"Mã NV: {self.employee_id} | Họ tên: {self.name} | Loại: Part-time")

    def calculate_salary(self):
        return self.working_hours * self.hourly_rate


class InternEmployee(Employee):
    """Lớp đại diện cho thực tập sinh."""

    def __init__(self, employee_id, name, allowance):
        super().__init__(employee_id, name)
        self.allowance = allowance

    def display_info(self):
        print(f"Mã NV: {self.employee_id} | Họ tên: {self.name} | Loại: Intern")

    def calculate_salary(self):
        return self.allowance


def display_employees(employees):
    """Duyệt và hiển thị danh sách thông tin cơ bản của tất cả nhân viên."""
    print("\n--- DANH SÁCH NHÂN VIÊN ---")
    for emp in employees:
        emp.display_info()


def display_salaries(employees):
    """Duyệt danh sách và tính toán lương cho toàn bộ nhân viên bằng tính Đa hình."""
    print("\n--- BẢNG LƯƠNG NHÂN VIÊN ---")
    for emp in employees:
        print(f"{emp.employee_id} | {emp.name:<12} | Lương: {emp.calculate_salary():,.0f} VND")


def main():
    """Hàm điều phối luồng chạy chính và giao diện Menu tương tác."""
    employees = [
        FullTimeEmployee("E001", "Nguyen Van A", 15000000, 3000000),
        PartTimeEmployee("E002", "Tran Thi B", 80, 50000),
        InternEmployee("E003", "Le Van C", 3000000)
    ]

    while True:
        print("\n=== EMPLOYEE SALARY MANAGER ===")
        print("1. Xem danh sách nhân viên")
        print("2. Tính lương toàn bộ nhân viên")
        print("3. Thoát chương trình")
        print("================================")
        
        choice = input("Chọn chức năng (1-3): ").strip()

        if choice == "1":
            display_employees(employees)
        elif choice == "2":
            display_salaries(employees)
        elif choice == "3":
            print("Cảm ơn bạn đã sử dụng Employee Salary Manager!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


if __name__ == "__main__":
    main()