from abc import ABC, abstractmethod

class BaseProduct(ABC):
    """Lớp cơ sở trừu tượng làm khuôn mẫu cho hệ thống quản lý hàng hóa Amazon."""

    warehouse_name = "Amazon Logistics"
    base_storage_fee = 5000

    def __init__(self, product_code, name):
        self.product_code = product_code
        self._name = ""
        self.name = name
        self.__stock_quantity = 0

    @property
    def stock_quantity(self):
        """Đọc số lượng tồn kho hiện tại một cách an toàn."""
        return self.__stock_quantity

    def _update_stock(self, amount):
        """Hàm hỗ trợ nội bộ cho phép các lớp con thay đổi số lượng tồn kho."""
        self.__stock_quantity += amount

    @property
    def name(self):
        """Đọc tên sản phẩm."""
        return self._name

    @name.setter
    def name(self, value):
        """Chuẩn hóa tên sản phẩm thành in hoa và bỏ khoảng trắng thừa."""
        self._name = value.strip().upper()

    @abstractmethod
    def import_stock(self, quantity):
        """Phương thức trừu tượng quy định logic nhập kho."""
        pass

    @abstractmethod
    def export_stock(self, quantity):
        """Phương thức trừu tượng quy định logic xuất kho."""
        pass

    def __add__(self, other):
        """Nạp chồng toán tử cộng để tính tổng tồn kho của hai sản phẩm."""
        if not isinstance(other, BaseProduct):
            return NotImplemented
        return self.stock_quantity + other.stock_quantity

    def __lt__(self, other):
        """Nạp chồng toán tử nhỏ hơn để so sánh mức tồn kho."""
        if not isinstance(other, BaseProduct):
            return NotImplemented
        return self.stock_quantity < other.stock_quantity

    @staticmethod
    def validate_product_code(product_code):
        """Kiểm tra mã sản phẩm phải bắt đầu bằng chữ cái và dài đúng 10 ký tự."""
        if len(product_code) == 10 and product_code[0].isalpha():
            return True
        return False

    @classmethod
    def update_warehouse_name(cls, new_name):
        """Cập nhật tên chuỗi kho hàng áp dụng cho toàn hệ thống."""
        cls.warehouse_name = new_name


class ColdStorageProduct(BaseProduct):
    """Lớp quản lý hàng đông lạnh có tính toán hao hụt nhiệt độ."""

    def __init__(self, product_code, name, required_temperature):
        super().__init__(product_code, name)
        self.required_temperature = required_temperature

    def import_stock(self, quantity):
        """Nhập kho hàng đông lạnh bình thường."""
        if quantity > 0:
            self._update_stock(quantity)
            print("Nhập kho hàng đông lạnh thành công!")

    def export_stock(self, quantity):
        """Xuất kho hàng đông lạnh với 5% hao hụt."""
        if quantity > 0:
            loss = quantity * 0.05
            total_deduction = quantity + loss
            if self.stock_quantity >= total_deduction:
                self._update_stock(-total_deduction)
                print("Xuất kho thành công!")
                print(f"Số lượng yêu cầu: {quantity} đơn vị")
                print(f"Số lượng hao hụt bảo quản (5%): {loss} đơn vị")
                print(f"Tổng số lượng khấu trừ trong kho: {total_deduction} đơn vị")
            else:
                print("Giao dịch thất bại! Không đủ hàng tồn kho để xuất và bù hao hụt.")

    def apply_cooling_cost(self):
        """Tính toán chi phí vận hành máy lạnh."""
        cost = self.stock_quantity * 3000
        print("--- TÍNH PHÍ BẢO QUẢN ĐÔNG LẠNH ---")
        print(f"Số lượng tồn kho hiện tại: {self.stock_quantity} đơn vị")
        print(f"Nhiệt độ yêu cầu: {self.required_temperature} độ C")
        print(f"Chi phí làm lạnh phát sinh trong ngày: +{cost:,.0f} VND")


class HazardousProduct(BaseProduct):
    """Lớp quản lý hàng hóa nguy hiểm với hạn mức an toàn."""

    def __init__(self, product_code, name, max_safety_limit):
        super().__init__(product_code, name)
        self.max_safety_limit = max_safety_limit

    def import_stock(self, quantity):
        """Nhập kho có kiểm soát chặt chẽ hạn mức an toàn."""
        if quantity > 0:
            if self.stock_quantity + quantity <= self.max_safety_limit:
                self._update_stock(quantity)
                print("Nhập kho hàng nguy hiểm thành công!")
            else:
                print(f"Giao dịch thất bại! Số lượng nhập vào khiến tồn kho vượt quá hạn mức an toàn cho phép (Tối đa: {self.max_safety_limit}).")

    def export_stock(self, quantity):
        """Xuất kho hàng nguy hiểm bình thường."""
        if quantity > 0 and self.stock_quantity >= quantity:
            self._update_stock(-quantity)
            print("Xuất kho hàng nguy hiểm thành công!")
        else:
            print("Giao dịch thất bại! Số lượng tồn kho không đủ.")


class HybridPremiumProduct(ColdStorageProduct, HazardousProduct):
    """Lớp sản phẩm lai kết hợp cả tính năng đông lạnh và hóa chất nguy hiểm."""

    def __init__(self, product_code, name, required_temperature, max_safety_limit):
        BaseProduct.__init__(self, product_code, name)
        self.required_temperature = required_temperature
        self.max_safety_limit = max_safety_limit

    def import_stock(self, quantity):
        """Áp dụng logic kiểm tra hạn mức an toàn từ HazardousProduct."""
        HazardousProduct.import_stock(self, quantity)

    def export_stock(self, quantity):
        """Áp dụng logic hao hụt nhiệt độ từ ColdStorageProduct."""
        ColdStorageProduct.export_stock(self, quantity)