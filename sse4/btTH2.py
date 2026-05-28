tong_doanh_thu = 0
so_ngay_dat_muc_tieu = 0

for i in range(1, 8):
    doanh_thu_ngay = int(input(f"Nhập doanh thu Ngày {i}: "))
    tong_doanh_thu += doanh_thu_ngay
    if doanh_thu_ngay >= 5000000:
        so_ngay_dat_muc_tieu += 1

doanh_thu_trung_binh = int(tong_doanh_thu / 7)

print("\n--- BÁO CÁO DOANH THU TUẦN RIKKEI STORE ---")
print(f"Tổng doanh thu cả tuần: {tong_doanh_thu} VND")
print(f"Doanh thu trung bình mỗi ngày: {doanh_thu_trung_binh} VND")
print(f"Số ngày đạt doanh thu mục tiêu (>= 5,000,000 VND): {so_ngay_dat_muc_tieu} ngày")