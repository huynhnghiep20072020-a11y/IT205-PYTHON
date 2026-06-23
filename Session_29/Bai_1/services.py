class MQTTEngineGateway:
    """Cổng kết nối MQTT Engine."""

    def process_stream(self, device):
        """Xử lý luồng dữ liệu MQTT."""
        print("[Hệ thống MQTT Engine]: Đang khởi tạo băng thông kết nối dữ liệu IoT...")
        print(f"Dữ liệu của thiết bị {device.device_code} đã được đóng gói và xuất chuỗi luồng thành công.")

class ERPReportGateway:
    """Cổng kết nối hệ thống ERP."""

    def process_stream(self, device):
        """Xử lý luồng dữ liệu ERP."""
        print("[Hệ thống quản trị ERP]: Đang nhận luồng dữ liệu API...")
        print(f"Báo cáo của thiết bị {device.device_code} đã được đồng bộ vào Data Warehouse.")

def export_telemetry_data(data_gateway, device_object):
    """Hàm toàn cục thực thi giao thức ngoại vi qua Duck Typing."""
    try:
        data_gateway.process_stream(device_object)
        print("Xác thực cổng ngoại vi bằng Duck Typing thành công!")
    except AttributeError:
        print("[Lỗi] (ERR-IOT-05): Xung đột kiến trúc! Không thể xuất dữ liệu do cấu hình cổng ngoại vi không tương thích.")