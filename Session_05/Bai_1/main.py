while True:
    so_luong = int(input("Nhập số lượng nhân viên: "))
    if so_luong > 0:
        break

print()

for i in range(so_luong):
    ten = input("Nhập tên nhân viên: ")
    ngay_lam = int(input("Nhập số ngày làm: "))

    if ngay_lam < 0 or ngay_lam > 22:
        print("Dữ liệu không hợp lệ\n")
        continue

    if ngay_lam == 0:
        print("Nhân viên nghỉ toàn bộ tháng\n")
        continue

    print(f"{ten}: ", end="")
    for j in range(ngay_lam):
        print("*", end="")
    print()

    if ngay_lam >= 18:
        print("Làm việc chăm chỉ\n")
    elif ngay_lam < 10:
        print("Làm việc ít\n")
    else:
        print("Làm việc bình thường\n")