from abc import ABC, abstractmethod

class BaseDevice(ABC):
    """Lớp trừu tượng đại diện cho thiết bị cơ sở trong nhà máy."""
    
    factory_name = "Rikkei Smart Factory"
    base_maintenance_cost = 1000000

    def __init__(self, device_code, device_name):
        self.device_code = device_code
        self._device_name = ""
        self.device_name = device_name
        self.__operating_hours = 0

    @property
    def operating_hours(self):
        """Getter cho số giờ vận hành."""
        return self.__operating_hours

    def _add_operating_hours(self, hours):
        """Cập nhật số giờ vận hành an toàn."""
        if hours <= 0:
            raise ValueError("[Lỗi] (ERR-IOT-03): Định dạng dữ liệu sai! Giá trị nhập vào phải là số lớn hơn 0.")
        self.__operating_hours += hours

    @property
    def device_name(self):
        """Getter cho tên thiết bị."""
        return self._device_name

    @device_name.setter
    def device_name(self, value):
        """Chuẩn hóa tên thiết bị."""
        self._device_name = value.strip().upper()

    @abstractmethod
    def track_performance(self, *args, **kwargs):
        """Phương thức trừu tượng theo dõi hiệu suất."""
        pass

    @abstractmethod
    def run_diagnostic(self):
        """Phương thức trừu tượng chạy chẩn đoán."""
        pass

    def __add__(self, other):
        """Nạp chồng toán tử cộng."""
        if not isinstance(other, BaseDevice):
            raise TypeError("[Lỗi] (ERR-IOT-04): Lỗi kiểu dữ liệu! Không thể thực hiện toán tử với đối tượng ngoài hệ thống.")
        return self.operating_hours + other.operating_hours

    def __lt__(self, other):
        """Nạp chồng toán tử nhỏ hơn."""
        if not isinstance(other, BaseDevice):
            raise TypeError("[Lỗi] (ERR-IOT-04): Lỗi kiểu dữ liệu! Không thể thực hiện toán tử với đối tượng ngoài hệ thống.")
        return self.operating_hours < other.operating_hours

    @staticmethod
    def validate_device_code(device_code):
        """Kiểm tra mã thiết bị hợp lệ."""
        if len(device_code) == 10 and device_code[0].isalpha():
            return True
        return False

    @classmethod
    def update_maintenance_cost(cls, new_cost):
        """Cập nhật chi phí bảo trì hệ thống."""
        cls.base_maintenance_cost = new_cost


class ProductionRobot(BaseDevice):
    """Lớp thiết bị Robot lắp ráp."""

    def __init__(self, device_code, device_name):
        super().__init__(device_code, device_name)
        self.completed_products = 0

    def track_performance(self, hours, products):
        """Ghi nhận hiệu suất cho Robot."""
        self._add_operating_hours(hours)
        if products <= 0:
            raise ValueError("[Lỗi] (ERR-IOT-03): Định dạng dữ liệu sai! Giá trị nhập vào phải là số lớn hơn 0.")
        self.completed_products += products
        oee = (self.completed_products / self.operating_hours) * 10 if self.operating_hours > 0 else 0
        print("[Thành công]: Đã cập nhật số liệu vận hành.")
        print(f"Tổng số giờ chạy tích lũy: {self.operating_hours} giờ.")
        print(f"Chỉ số hiệu suất thiết bị tổng thể (OEE): {oee:.1f}%")

    def run_diagnostic(self):
        """Quy trình chẩn đoán cho Robot."""
        print("--- QUY TRÌNH TỰ CHẨN ĐOÁN LỖI KỸ THUẬT ---")
        if self.completed_products > 10000:
            print("[Cảnh báo hệ thống]: Thiết bị phát hiện trạng thái bất thường!")
            print("Kết quả chẩn đoán: Vượt định mức sản lượng, cần bôi trơn hệ thống cơ khí.")
            print(f"Định mức chi phí bảo trì hệ thống dự kiến: {self.base_maintenance_cost:,.0f} VND")
        else:
            print("Hệ thống cơ khí hoạt động ổn định.")


class ThermalSensor(BaseDevice):
    """Lớp thiết bị Cảm biến nhiệt độ."""

    def __init__(self, device_code, device_name, safety_threshold=80.0):
        super().__init__(device_code, device_name)
        self.current_temperature = 25.0
        self.safety_threshold = safety_threshold

    def track_performance(self, hours, temperature):
        """Ghi nhận hiệu suất cho Cảm biến."""
        self._add_operating_hours(hours)
        if temperature <= 0:
            raise ValueError("[Lỗi] (ERR-IOT-03): Định dạng dữ liệu sai! Giá trị nhập vào phải là số lớn hơn 0.")
        self.current_temperature = temperature
        print("[Thành công]: Đã cập nhật số liệu vận hành.")
        print(f"Tổng số giờ chạy tích lũy: {self.operating_hours} giờ.")
        print(f"Nhiệt độ hiện tại ghi nhận: {self.current_temperature} độ C")

    def run_diagnostic(self):
        """Quy trình chẩn đoán cho Cảm biến."""
        print("--- QUY TRÌNH TỰ CHẨN ĐOÁN LỖI KỸ THUẬT ---")
        if self.current_temperature > self.safety_threshold:
            print("[Cảnh báo hệ thống]: Thiết bị phát hiện trạng thái bất thường!")
            print(f"Kết quả chẩn đoán: Nguy hiểm: Vượt ngưỡng nhiệt! (Nhiệt độ hiện tại: {self.current_temperature} độ C / Ngưỡng an toàn: {self.safety_threshold} độ C)")
            print(f"Định mức chi phí bảo trì hệ thống dự kiến: {self.base_maintenance_cost:,.0f} VND")
        else:
            print("Nhiệt độ hệ thống nằm trong ngưỡng an toàn.")


class HybridSmartActuator(ProductionRobot, ThermalSensor):
    """Lớp thiết bị truyền động lai kết hợp."""

    def __init__(self, device_code, device_name):
        BaseDevice.__init__(self, device_code, device_name)
        self.completed_products = 0
        self.current_temperature = 25.0
        self.safety_threshold = 80.0

    def track_performance(self, hours, products, temperature):
        """Ghi nhận hiệu suất thiết bị lai."""
        self._add_operating_hours(hours)
        
        if products <= 0 or temperature <= 0:
            raise ValueError("[Lỗi] (ERR-IOT-03): Định dạng dữ liệu sai! Giá trị nhập vào phải là số lớn hơn 0.")
        
        self.completed_products += products
        self.current_temperature = temperature
        oee = (self.completed_products / self.operating_hours) * 10
        
        print("[Thành công]: Đã cập nhật số liệu vận hành.")
        print(f"Tổng số giờ chạy tích lũy: {self.operating_hours} giờ.")
        print(f"Chỉ số hiệu suất OEE: {oee:.1f}%")
        print(f"Nhiệt độ hiện tại: {self.current_temperature} độ C")

    def run_diagnostic(self):
        """Quy trình chẩn đoán cho thiết bị lai."""
        ProductionRobot.run_diagnostic(self)
        if self.current_temperature > self.safety_threshold:
            print(f"[Cảnh báo hệ thống]: Vượt ngưỡng nhiệt! ({self.current_temperature} > {self.safety_threshold} độ C)")