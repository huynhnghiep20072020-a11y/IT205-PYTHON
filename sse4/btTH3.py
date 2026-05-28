so_luong = int(input("Nhập số lượng hóa đơn trong ca: "))

hoa_don_max = 0
hoa_don_min = 0

for i in range(1, so_luong + 1):
    gia_tri = int(input(f"Nhập giá trị hóa đơn thứ {i}: "))
    if i == 1:
        hoa_don_max = gia_tri
        hoa_don_min = gia_tri
    else:
        if gia_tri > hoa_don_max:
            hoa_don_max = gia_tri
        if gia_tri < hoa_don_min:
            hoa_don_min = gia_tri

print("--- KẾT QUẢ KIỂM TOÁN CA RIKKEI STORE ---")
print(f"Hóa đơn có giá trị cao nhất: {hoa_don_max} VND")
print(f"Hóa đơn có giá trị thấp nhất: {hoa_don_min} VND")