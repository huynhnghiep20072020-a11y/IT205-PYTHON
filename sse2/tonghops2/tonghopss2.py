NAM_HIEN_TAI = 2026

ten_benh_nhan = input ("nhập tên bệnh nhân :")
nam_sinh = int(input("nhập năm sinh :"))
so_ngay_benh_ = int(input("nhập số ngày bị bệnh :"))
nhiet_do=float(input("nhập nhiệt độ cơ thể :"))
chi_phi_kham = float(input("nhập chi phí khám :"))

if len(ten_benh_nhan.strip()) ==0:
    print("tên bệnh nhân không hợp lệ !")
elif not (1900 <= nam_sinh <= NAM_HIEN_TAI):
    print("Năm sinh không hợp lệ !")
elif so_ngay_benh_ < 0:
    print("Số ngày bị bệnh không hợp lệ !")
elif not (30 <= nhiet_do <= 45):
    print("Nhiệt độ không hợp lệ !")
elif chi_phi_kham <= 0:
    print("Chi phí khám không hợp lệ !")
else:
    tuoi = NAM_HIEN_TAI - nam_sinh
    thu_phi = chi_phi_kham * 0.1
    tong_chi_phi = chi_phi_kham + thu_phi

    if nhiet_do > 38 and so_ngay_benh_ > 3:
        tinh_trang = "Nguy hiểm"
    elif nhiet_do > 38:
        tinh_trang = "Sốt cao"
    elif nhiet_do > 37.5:
        tinh_trang = "Sốt nhẹ"
    else:
        tinh_trang = "Bình thường"

    muc_chi_phi = "Cao" if tong_chi_phi > 500000 else "Thấp"
    print("\n  KẾT QUẢ   ")
    print(f"Tên: {ten_benh_nhan}")
    print(f"Tuổi: {tuoi}")
    print(f"Nhiệt độ : {nhiet_do} °C")
    print(f"Số ngày bệnh : {so_ngay_benh_}\n")
    print(f"Tình trạng : {tinh_trang}")
    print(f"Tổng chi phí : {tong_chi_phi} VND")
    print(f"Mức chi phí : {muc_chi_phi}")
