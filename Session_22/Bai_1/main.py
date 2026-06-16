import logging

def show_devices(devices):
    """Duyệt và in danh sách thiết bị dưới dạng bảng. Thông báo nếu danh sách trống."""
    print("\n--- DANH SÁCH THIẾT BỊ GIÁM SÁT ---")
    if not devices:
        print("Hệ thống hiện tại chưa có dữ liệu thiết bị.")
        return

    print(f"{'Mã TB':<8} | {'Vị trí (Location)':<20} | {'CS Cũ':<8} | {'CS Mới':<8} | {'Trạng thái'}")
    print("-" * 65)
    for d in devices:
        print(f"{d['id']:<8} | {d['location']:<20} | {d['old_index']:<8} | {d['new_index']:<8} | {d['status']}")
    print("-" * 65)

def update_indices(devices):
    """Tìm thiết bị theo mã, kiểm tra tính hợp lệ của dữ liệu đầu vào và cập nhật chỉ số điện."""
    print("\n--- CẬP NHẬT CHỈ SỐ ĐIỆN TIÊU THỤ ---")
    device_id = input("Nhập mã thiết bị cần cập nhật: ").strip().upper()
    
    target_device = None
    for d in devices:
        if d['id'] == device_id:
            target_device = d
            break
            
    if target_device is None:
        print("Lỗi [ERR-E01]: Không tìm thấy mã thiết bị trong hệ thống!")
        return

    while True:
        try:
            old_index = int(input("Nhập chỉ số cũ: "))
            if old_index < 0:
                print("Lỗi: Chỉ số điện không được nhỏ hơn 0.")
                continue
            break
        except ValueError:
            print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")

    while True:
        try:
            new_index = int(input("Nhập chỉ số mới: "))
            if new_index < 0:
                print("Lỗi: Chỉ số điện không được nhỏ hơn 0.")
                continue
            if new_index < old_index:
                print("Lỗi [ERR-E02]: Chỉ số mới không được nhỏ hơn chỉ số cũ. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")

    target_device['old_index'] = old_index
    target_device['new_index'] = new_index
    print(f"Thành công: Đã cập nhật chỉ số cho thiết bị {device_id}!")

def trigger_overload_warning(devices):
    """Kiểm tra lượng điện tiêu thụ của thiết bị, đổi trạng thái thành Overload và ghi log nếu vượt mức 5000 kWh."""
    print("\n--- KÍCH HOẠT CẢNH BÁO QUÁ TẢI ---")
    device_id = input("Nhập mã thiết bị cần kiểm tra: ").strip().upper()
    
    target_device = None
    for d in devices:
        if d['id'] == device_id:
            target_device = d
            break
            
    if target_device is None:
        print("Lỗi [ERR-E01]: Không tìm thấy mã thiết bị trong hệ thống!")
        return

    if target_device['status'] == 'Overload':
        print("Lỗi [ERR-E04]: Thiết bị này đã ở trạng thái quá tải từ trước!")
        return

    consumed_energy = target_device['new_index'] - target_device['old_index']
    
    if consumed_energy > 5000:
        target_device['status'] = 'Overload'
        logging.warning(f"Thiết bị {device_id} tại {target_device['location']} tiêu thụ {consumed_energy} kWh - VƯỢT MỨC CHO PHÉP!")
        print("Thành công: Đã chuyển trạng thái thiết bị sang Overload.")
    else:
        print(f"Thiết bị hoạt động bình thường (Tiêu thụ: {consumed_energy} kWh).")

def calculate_energy_financials(devices):
    """Tính toán tổng điện năng tiêu thụ, phần trăm chiết khấu và tổng chi phí. Trả về cấu trúc Tuple."""
    total_kwh = 0
    for d in devices:
        total_kwh += (d['new_index'] - d['old_index'])
        
    base_cost = total_kwh * 3000
    
    if total_kwh >= 50000:
        discount_pct = 0.03
    else:
        discount_pct = 0.0
        
    final_cost = base_cost * (1 - discount_pct)
    
    return total_kwh, discount_pct, final_cost

def main():
    """Hàm điều phối trung tâm, thiết lập logging, quản lý dữ liệu gốc và chạy vòng lặp menu."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    devices = [
        {'id': 'M01', 'location': 'Mechanical Shop A', 'old_index': 1200, 'new_index': 4500, 'status': 'Normal'},
        {'id': 'M02', 'location': 'Assembly Line B', 'old_index': 2300, 'new_index': 8500, 'status': 'Overload'}
    ]

    while True:
        print("\n===== SMART ENERGY MONITOR =====")
        print("1. Xem danh sách thiết bị")
        print("2. Cập nhật chỉ số điện")
        print("3. Kích hoạt cảnh báo quá tải")
        print("4. Tính tổng lượng điện & Chi phí")
        print("5. Thoát chương trình")
        print("================================")
        
        try:
            choice = int(input("Chọn chức năng (1-5): "))
        except ValueError:
            print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5.")
            continue

        if choice == 1:
            show_devices(devices)
        elif choice == 2:
            update_indices(devices)
        elif choice == 3:
            trigger_overload_warning(devices)
        elif choice == 4:
            total_kwh, discount_pct, final_cost = calculate_energy_financials(devices)
            print("\n--- BÁO CÁO CHI PHÍ NĂNG LƯỢNG ---")
            print(f"Tổng lượng điện tiêu thụ: {total_kwh:,} kWh")
            print(f"Phần trăm chiết khấu: {int(discount_pct * 100)}%")
            print(f"Tổng tiền thanh toán: {final_cost:,.0f} VND")
            print("----------------------------------")
        elif choice == 5:
            print("Đã thoát hệ thống Smart Energy Monitor. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5.")

if __name__ == "__main__":
    main()