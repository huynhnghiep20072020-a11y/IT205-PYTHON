tong_tien = int(input("Nhập tổng tiền hóa đơn ban đầu: "))

if tong_tien >= 500000:
    tien_giam_gia = int(tong_tien * 0.1)
else:
    tien_giam_gia = 0

tien_phai_tra = tong_tien - tien_giam_gia

print("--- HÓA ĐƠN THANH TOÁN RIKKEI STORE ---")
print(f"Số tiền được giảm giá: {tien_giam_gia} VND")
print(f"Tổng tiền khách phải trả: {tien_phai_tra} VND")