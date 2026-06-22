from abc import ABC, abstractmethod

class BaseEmployee(ABC):
    """Lớp cơ sở trừu tượng làm khuôn mẫu cho hệ thống nhân sự Rikkei Education."""

    company_name = "Rikkei Education"
    base_salary_rate = 3000000

    def __init__(self, emp_code, full_name):
        self.emp_code = emp_code
        self._full_name = ""
        self.full_name = full_name
        self.__working_hours = 0

    @property
    def working_hours(self):
        """Đọc số giờ làm việc hiện tại một cách an toàn."""
        return self.__working_hours

    def _add_working_hours(self, hours):
        """Hàm hỗ trợ nội bộ cho phép cộng thêm giờ làm việc."""
        self.__working_hours += hours

    @property
    def full_name(self):
        """Đọc họ tên nhân sự."""
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        """Chuẩn hóa họ tên thành in hoa và bỏ khoảng trắng thừa."""
        self._full_name = value.strip().upper()

    @abstractmethod
    def calculate_salary(self):
        """Phương thức trừu tượng quy định logic tính lương."""
        pass

    @abstractmethod
    def update_kpi(self, progress):
        """Phương thức trừu tượng quy định logic cập nhật KPI."""
        pass

    def __add__(self, other):
        """Nạp chồng toán tử cộng để tính tổng số giờ làm việc của hai nhân sự."""
        if not isinstance(other, BaseEmployee):
            return NotImplemented
        return self.working_hours + other.working_hours

    def __lt__(self, other):
        """Nạp chồng toán tử nhỏ hơn để so sánh cống hiến giờ làm."""
        if not isinstance(other, BaseEmployee):
            return NotImplemented
        return self.working_hours < other.working_hours

    @staticmethod
    def validate_employee_code(emp_code):
        """Kiểm tra mã nhân sự phải đúng 10 ký tự và bắt đầu bằng RKE."""
        if len(emp_code) == 10 and emp_code.startswith("RKE"):
            return True
        return False

    @classmethod
    def update_base_salary_rate(cls, new_rate):
        """Cập nhật mức lương cơ sở áp dụng cho toàn hệ thống."""
        cls.base_salary_rate = new_rate


class Lecturer(BaseEmployee):
    """Lớp quản lý Giảng viên chuyên trách."""

    def __init__(self, emp_code, full_name):
        super().__init__(emp_code, full_name)
        self.teaching_slots = 0

    def calculate_salary(self):
        """Tính lương: Lương cứng theo giờ + Tiền ca dạy."""
        return (self.working_hours * self.base_salary_rate) + (self.teaching_slots * 500000)

    def update_kpi(self, progress):
        """Cập nhật tiến độ hoàn thành giáo án giảng dạy."""
        if progress <= 0:
            raise ValueError("Số liệu cập nhật hiệu suất không được nhỏ hơn hoặc bằng 0")
        print(f"Giảng viên {self.full_name} đã đạt {progress}% tiến độ khung chương trình.")

    def conduct_class(self):
        """Ghi nhận việc đứng lớp, tự động tăng ca dạy và giờ công."""
        self.teaching_slots += 1
        self._add_working_hours(2)
        print("Ghi nhận thành công! Thầy/Cô đã hoàn thành thêm 1 ca dạy.")
        print(f"Số ca dạy hiện tại: {self.teaching_slots} ca.")
        print("Số giờ làm việc tích lũy: +2 giờ.")


class AdmissionStaff(BaseEmployee):
    """Lớp quản lý Nhân viên Tuyển sinh."""

    def __init__(self, emp_code, full_name, kpi_target):
        super().__init__(emp_code, full_name)
        self.kpi_target = kpi_target
        self.revenue_generated = 0

    def calculate_salary(self):
        """Tính lương: Lương cứng theo giờ + 5% Hoa hồng doanh số."""
        return (self.working_hours * self.base_salary_rate) + (self.revenue_generated * 0.05)

    def update_kpi(self, progress):
        """Cộng dồn doanh số mang về vào tổng doanh số cá nhân."""
        if progress <= 0:
            raise ValueError("Số liệu cập nhật hiệu suất không được nhỏ hơn hoặc bằng 0")
        self.revenue_generated += progress
        print("Cập nhật KPI thành công!")
        print(f"Doanh số tích lũy mới: {self.revenue_generated:,.0f} VND.")


class HybridManager(Lecturer, AdmissionStaff):
    """Lớp quản lý cấp cao đa năng: Giảng dạy kiêm Tuyển sinh."""

    def __init__(self, emp_code, full_name, kpi_target):
        BaseEmployee.__init__(self, emp_code, full_name)
        self.teaching_slots = 0
        self.kpi_target = kpi_target
        self.revenue_generated = 0

    def calculate_salary(self):
        """Tính lương tổng hợp đảm bảo không bị nhân đôi lương cứng cơ sở."""
        base_pay = self.working_hours * self.base_salary_rate
        teaching_pay = self.teaching_slots * 500000
        commission_pay = self.revenue_generated * 0.05
        return base_pay + teaching_pay + commission_pay

    def update_kpi(self, progress):
        """Ưu tiên dùng logic cập nhật doanh số của AdmissionStaff."""
        AdmissionStaff.update_kpi(self, progress)