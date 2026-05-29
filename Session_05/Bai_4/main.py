room_count = int(input("Nhập số lượng phòng học cần kiểm tra: "))

if room_count <= 0:
    print("Số lượng phòng học không hợp lệ")
else:
    for current_room in range(1, room_count + 1):
        print(f"\n--- Phòng học {current_room} ---")
        row_count = int(input("Nhập số hàng ghế của phòng: "))
        seat_count = int(input("Nhập số ghế trên mỗi hàng: "))

        # Bỏ qua phòng nếu dữ liệu âm
        if row_count <= 0 or seat_count <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue

        # Dừng hẳn chương trình nếu phòng quá lớn
        if row_count > 10 or seat_count > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break

        print("Sơ đồ chỗ ngồi:")
        for r in range(row_count):
            for s in range(seat_count):
                print("*", end="")
            print()