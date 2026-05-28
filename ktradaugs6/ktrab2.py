print("\n--- THỐNG KÊ HÀNG LỖI THU HỒI ---")
total_defective_items = 0
while True:
    defective_quantity = int(input("Nhập số lượng hàng lỗi từ quầy (nhập -1 để kết thúc): "))
    if defective_quantity == -1:
        break
    if defective_quantity >= 0:
        total_defective_items += defective_quantity
    else:
        print("Số lượng không hợp lệ, vui lòng nhập lại số dương hoặc -1 để thoát.")
print(f"Tổng số hàng lỗi thu hồi trong ngày là: {total_defective_items}")
