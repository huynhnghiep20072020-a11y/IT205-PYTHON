tong_so_hoa_don = 0
tong_doanh_thu = 0
so_hoa_don_lon = 0

while True:
    khach_hang_thu = tong_so_hoa_don + 1
    gia_tri = int(input(f"\nKhách hàng {khach_hang_thu} - Nhập giá trị hóa đơn: "))
    tong_so_hoa_don += 1
    tong_doanh_thu += gia_tri

    if gia_tri >= 1000000:
        so_hoa_don_lon += 1

    tiep_tuc = input("Có muốn nhập tiếp không? (C/K): ").strip().upper()
    if tiep_tuc == 'K':
        break

print("\n--- BÁO CÁO DOANH THU CUỐI NGÀY RIKKEI STORE ---")

if tong_so_hoa_don > 0:
    ty_le = (so_hoa_don_lon / tong_so_hoa_don) * 100
    print(f"Tổng số hóa đơn đã xử lý: {tong_so_hoa_don} hóa đơn.")
    print(f"Tổng doanh thu ngày hôm nay: {tong_doanh_thu:,} VNĐ.")
    print(f"Số hóa đơn lớn (>= 1,000,000 VND): {so_hoa_don_lon} hóa đơn.")
    print(f"Tỷ lệ hóa đơn lớn đạt: {ty_le:.1f}% trên tổng số đơn hàng.")
else:
    print("Hệ thống đóng cửa sớm. Hôm nay chưa có hóa đơn nào được xử lý.")