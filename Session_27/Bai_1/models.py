from abc import ABC, abstractmethod

class Employee(ABC):
    """Lớp cơ sở đại diện cho nhân viên."""

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def display_info(self):
        """Hiển thị thông tin cơ bản của nhân viên."""
        pass

    @abstractmethod
    def calculate_salary(self):
        """Tính lương nhân viên."""
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