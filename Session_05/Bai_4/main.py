# (1) Phân tích và thiết kế giải pháp
# - Input/Output: Nhập room_count, row_count, seat_count (int). Xuất thông báo lỗi hoặc sơ đồ '*' (String).
# - Giải pháp & Thuật toán: 
#   + Dùng if kiểm tra room_count <= 0 ngay từ đầu (Bẫy 1).
#   + Dùng vòng lặp for (Outer loop) duyệt từng phòng.
#   + Nếu row_count <= 0 hoặc seat_count <= 0: in lỗi và dùng 'continue' (Bẫy 2).
#   + Nếu row_count > 10 hoặc seat_count > 10: in lỗi và dùng 'break' (Bẫy 3).
#   + Nếu hợp lệ, dùng vòng lặp for lồng nhau (Nested loop) để in hàng và ghế.

# (2) Triển khai code
room_count = int(input("Nhập số lượng phòng học cần kiểm tra: "))

if room_count <= 0:
    print("Số lượng phòng học không hợp lệ")
else:
    for current_room in range(1, room_count + 1):
        print(f"\n--- Phòng học {current_room} ---")
        row_count = int(input("Nhập số hàng ghế của phòng: "))
        seat_count = int(input("Nhập số ghế trên mỗi hàng: "))

        if row_count <= 0 or seat_count <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue

        if row_count > 10 or seat_count > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break

        print("Sơ đồ chỗ ngồi:")
        for r in range(row_count):
            for s in range(seat_count):
                print("*", end="")
            print()