def main():
    blood_inventory = [
        "BL001-Nguyen Van A-O+-250-31/12/2026",
        "BL002-Tran Thi B-A--350-15/11/2026",
        "BL003-Le Van C-AB+-250-20/10/2026"
    ]

    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ KHO MÁU RIKKEI ===")
        print("1. Xem danh sách túi máu trong kho")
        print("2. Nhập túi máu mới")
        print("3. Gia hạn / Sửa ngày hết hạn")
        print("4. Xuất / Hủy túi máu")
        print("5. Thoát chương trình")
        print("=======================================")

        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == "1":
            display_inventory(blood_inventory)
        elif choice == "2":
            add_blood_bag(blood_inventory)
        elif choice == "3":
            update_expiry(blood_inventory)
        elif choice == "4":
            remove_blood_bag(blood_inventory)
        elif choice == "5":
            print("Cảm ơn bác sĩ đã sử dụng hệ thống. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")

if __name__ == "__main__":
    main()
def find_blood_bag(inventory, bag_id):
    """Tìm kiếm vị trí của túi máu trong danh sách dựa trên mã túi."""
    search_key = bag_id + "-"
    for i in range(len(inventory)):
        if inventory[i].startswith(search_key):
            return i
    return -1

def display_inventory(inventory):
    """Hiển thị danh sách túi máu và tính tổng thể tích máu đang có trong kho."""
    if len(inventory) == 0:
        print("Kho máu hiện chưa có túi máu nào.")
        return
        
    print("--- DANH SÁCH KHO MÁU ---")
    print("Mã Túi | Người Hiến | Nhóm Máu | Thể Tích | Ngày Hết Hạn")
    
    total_volume = 0
    for bag in inventory:
        parts = bag.split("-")
        total_volume += int(parts[3])
        print(f"{parts[0]} | {parts[1]} | {parts[2]} | {parts[3]} ml | {parts[4]}")
        
    print(f"\nTổng thể tích máu trong kho: {total_volume} ml.")

def add_blood_bag(inventory):
    """Tiếp nhận túi máu mới, chuẩn hóa dữ liệu và kiểm tra các bẫy lỗi nhập liệu."""
    print("--- NHẬP TÚI MÁU MỚI ---")
    
    bag_id = input("Nhập mã túi máu mới: ").strip().upper()
    if len(bag_id) == 0:
        print("Lỗi: Mã túi máu không được để trống!")
        return
        
    if find_blood_bag(inventory, bag_id) != -1:
        print(f"Lỗi: Mã túi máu {bag_id} đã tồn tại! Vui lòng nhập mã khác.")
        return

    name = input("Nhập tên người hiến: ").strip().title()
    if len(name) == 0:
        print("Lỗi: Tên người hiến không được để trống!")
        return

    blood_type = input("Nhập nhóm máu: ").strip().upper().replace(" ", "")

    volume_input = input("Nhập thể tích (ml): ").strip()
    if not volume_input.isdigit() or int(volume_input) <= 0:
        print("Lỗi: Thể tích phải là số nguyên lớn hơn 0!")
        return
    volume = int(volume_input)

    expiry_date = input("Nhập ngày hết hạn (DD/MM/YYYY): ").strip()

    new_bag = f"{bag_id}-{name}-{blood_type}-{volume}-{expiry_date}"
    inventory.append(new_bag)
    print(f"Thành công: Đã nhập túi máu {bag_id} vào kho!")

def update_expiry(inventory):
    """Cập nhật ngày hết hạn cho một túi máu bằng cách tách và ghép lại chuỗi."""
    print("--- GIA HẠN / SỬA NGÀY HẾT HẠN ---")
    
    bag_id = input("Nhập mã túi máu cần cập nhật: ").strip().upper()
    if len(bag_id) == 0:
        print("Lỗi: Mã túi máu không được để trống!")
        return

    index = find_blood_bag(inventory, bag_id)
    if index == -1:
        print(f"Lỗi: Không tìm thấy túi máu {bag_id} trong kho!")
        return

    new_date = input("Nhập ngày hết hạn mới: ").strip()
    
    parts = inventory[index].split("-")
    parts[4] = new_date
    inventory[index] = "-".join(parts)
    
    print(f"Thành công: Đã cập nhật ngày hết hạn cho túi máu {bag_id}!")

def remove_blood_bag(inventory):
    """Xóa hồ sơ túi máu khỏi hệ thống khi xuất kho hoặc hủy bỏ."""
    print("--- XUẤT / HỦY TÚI MÁU ---")
    
    bag_id = input("Nhập mã túi máu cần xuất/hủy: ").strip().upper()
    if len(bag_id) == 0:
        print("Lỗi: Mã túi máu không được để trống!")
        return

    index = find_blood_bag(inventory, bag_id)
    if index == -1:
        print(f"Lỗi: Không tìm thấy túi máu {bag_id} trong kho!")
        return

    inventory.pop(index)
    print(f"Thành công: Đã xuất túi máu {bag_id} khỏi kho!")
