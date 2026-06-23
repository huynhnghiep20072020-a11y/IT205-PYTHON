from models import BaseDevice, ProductionRobot, ThermalSensor, HybridSmartActuator
from services import MQTTEngineGateway, ERPReportGateway, export_telemetry_data

def get_device_by_code(devices, code):
    """Tìm kiếm thiết bị theo mã."""
    for d in devices:
        if d.device_code == code:
            return d
    return None

def main():
    """Hàm chạy chương trình chính."""
    devices_list = []
    current_device = None

    while True:
        print("\n===== RIKKEI SMART FACTORY IOT SIMULATOR =====")
        print("1. Đăng ký & Khởi tạo thiết bị IoT mới")
        print("2. Xem thông tin thiết bị & Thứ tự kế thừa (MRO)")
        print("3. Check-in giờ vận hành & Cập nhật chỉ số hiệu suất (Đa hình)")
        print("4. Thực thi quy trình tự chẩn đoán kỹ thuật (Diagnostic)")
        print("5. Cộng gộp thời gian tải & So sánh hao mòn (Operator Overloading)")
        print("6. Xuất dữ liệu vận hành ra Cổng ngoại vi (Duck Typing)")
        print("7. Thoát chương trình")
        print("==============================================")
        
        choice = input("Chọn chức năng (1-7): ").strip()

        match choice:
            case "1":
                print("--- ĐĂNG KÝ THIẾT BỊ IOT MỚI ---")
                print("1. Production Robot (Robot sản xuất lắp ráp)")
                print("2. Thermal Sensor (Cảm biến nhiệt độ)")
                print("3. Hybrid Smart Actuator (Thiết bị truyền động lai)")
                dev_type = input("Chọn phân loại thiết bị (1-3): ").strip()
                
                code = input("Nhập mã thiết bị 10 ký tự: ").strip().upper()
                if not BaseDevice.validate_device_code(code):
                    print("[Lỗi] (ERR-IOT-01): Mã thiết bị không hợp lệ! Phải gồm đúng 10 ký tự và bắt đầu bằng tiền tố quy định.")
                    continue
                    
                name = input("Nhập tên thiết bị: ").strip()
                
                if dev_type == "1":
                    new_dev = ProductionRobot(code, name)
                    type_str = "Robot sản xuất"
                elif dev_type == "2":
                    new_dev = ThermalSensor(code, name)
                    type_str = "Cảm biến nhiệt độ"
                elif dev_type == "3":
                    new_dev = HybridSmartActuator(code, name)
                    type_str = "Thiết bị truyền động lai"
                else:
                    print("[Lỗi] (ERR-IOT-06): Lựa chọn không hợp lệ! Vui lòng nhập đúng số thứ tự chức năng từ 1 đến 7.")
                    continue
                
                devices_list.append(new_dev)
                current_device = new_dev
                print(f"[Thành công]: Đăng ký {type_str} thành công!")
                print(f"Tên thiết bị: {current_device.device_name}")

            case "2":
                if current_device is None:
                    print("[Lỗi] (ERR-IOT-02): Thao tác bị từ chối! Hệ thống chưa có thông tin thiết bị hoạt động.")
                    continue
                    
                print("--- THÔNG TIN THIẾT BỊ HIỆN TẠI ---")
                print(f"Loại thiết bị: {current_device.__class__.__name__}")
                print(f"Nhà máy: {BaseDevice.factory_name}")
                print(f"Mã thiết bị: {current_device.device_code}")
                print(f"Tên thiết bị: {current_device.device_name}")
                print(f"Số giờ vận hành: {current_device.operating_hours} giờ")
                
                if isinstance(current_device, ProductionRobot):
                    print(f"Sản phẩm hoàn thành: {current_device.completed_products} sản phẩm")
                if isinstance(current_device, ThermalSensor):
                    print(f"Nhiệt độ hiện tại: {current_device.current_temperature} độ C")
                    
                mro_path = " -> ".join([cls.__name__ for cls in current_device.__class__.__mro__])
                print(f"[Hệ thống MRO]: {mro_path}")

            case "3":
                if current_device is None:
                    print("[Lỗi] (ERR-IOT-02): Thao tác bị từ chối! Hệ thống chưa có thông tin thiết bị hoạt động.")
                    continue
                
                print("--- GHI NHẬN SỐ LIỆU VẬN HÀNH ---")
                try:
                    hrs = float(input("Nhập số giờ chạy mới phát sinh: "))
                    if type(current_device) is ProductionRobot:
                        prods = int(input("Nhập số lượng sản phẩm hoàn thành mới bổ sung: "))
                        current_device.track_performance(hrs, prods)
                    elif type(current_device) is ThermalSensor:
                        temp = float(input("Nhập nhiệt độ môi trường hiện tại: "))
                        current_device.track_performance(hrs, temp)
                    elif type(current_device) is HybridSmartActuator:
                        prods = int(input("Nhập số lượng sản phẩm hoàn thành mới bổ sung: "))
                        temp = float(input("Nhập nhiệt độ môi trường hiện tại: "))
                        current_device.track_performance(hrs, prods, temp)
                except ValueError:
                    print("[Lỗi] (ERR-IOT-03): Định dạng dữ liệu sai! Giá trị nhập vào phải là số lớn hơn 0.")

            case "4":
                if current_device is None:
                    print("[Lỗi] (ERR-IOT-02): Thao tác bị từ chối! Hệ thống chưa có thông tin thiết bị hoạt động.")
                    continue
                current_device.run_diagnostic()

            case "5":
                if current_device is None:
                    print("[Lỗi] (ERR-IOT-02): Thao tác bị từ chối! Hệ thống chưa có thông tin thiết bị hoạt động.")
                    continue
                    
                print("--- KIỂM KÊ & SO SÁNH TẢI (OPERATOR OVERLOADING) ---")
                print(f"Thiết bị hiện tại (A): {current_device.device_code} (Số giờ chạy: {current_device.operating_hours} giờ)")
                target_code = input("Chọn mã thiết bị đối ứng (B) từ danh sách: ").strip().upper()
                target_dev = get_device_by_code(devices_list, target_code)
                
                if target_dev:
                    try:
                        if current_device < target_dev:
                            comp = "ÍT HƠN"
                        elif target_dev < current_device:
                            comp = "NHIỀU HƠN"
                        else:
                            comp = "BẰNG NHAU VỚI"
                            
                        print(f"[Kết quả So sánh (__lt__)]: Hao mòn (số giờ chạy) của thiết bị A {comp} thiết bị B.")
                        total_hrs = current_device + target_dev
                        print(f"[Kết quả Tổng hợp (__add__)]: Tổng thời gian tải vận hành của cả 2 thiết bị là: {total_hrs} giờ.")
                    except TypeError as e:
                        print(e)
                else:
                    print("Không tìm thấy mã thiết bị đối ứng trong hệ thống.")

            case "6":
                if current_device is None:
                    print("[Lỗi] (ERR-IOT-02): Thao tác bị từ chối! Hệ thống chưa có thông tin thiết bị hoạt động.")
                    continue
                    
                print("--- XUẤT DỮ LIỆU VẬN HÀNH RA CỔNG NGOẠI VI ---")
                print("1. Xuất dữ liệu qua cổng MQTT (Cloud Stream)")
                print("2. Đồng bộ số liệu vào hệ thống quản trị ERP")
                print("3. Kiểm tra cổng lỗi (Test Duck Typing Error)")
                gate_choice = input("Chọn cổng kết nối ngoại vi (1-3): ").strip()
                
                if gate_choice == "1":
                    gateway = MQTTEngineGateway()
                elif gate_choice == "2":
                    gateway = ERPReportGateway()
                elif gate_choice == "3":
                    class FakeGateway:
                        pass
                    gateway = FakeGateway()
                else:
                    print("[Lỗi] (ERR-IOT-06): Lựa chọn không hợp lệ! Vui lòng nhập đúng số thứ tự chức năng từ 1 đến 7.")
                    continue
                    
                export_telemetry_data(gateway, current_device)

            case "7":
                print("Cảm ơn bạn đã sử dụng hệ thống Quản lý Thiết bị Rikkei Smart Factory IoT Pro!")
                break

            case _:
                print("[Lỗi] (ERR-IOT-06): Lựa chọn không hợp lệ! Vui lòng nhập đúng số thứ tự chức năng từ 1 đến 7.")

if __name__ == "__main__":
    main()