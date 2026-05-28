import random

def choi_keo_bua_bao():
    print("\n   KÉO BÚA BAO    ")
    lua_chon = ["Kéo", "Búa", "Bao"]
    while True:
        try:
            nguoi_dung = int(input("Chọn (1: Kéo, 2: Búa, 3: Bao, 0: Thoát game này): "))
        except ValueError:
            print("Lựa chọn không hợp lệ. Vui lòng nhập số.")
            continue
        if nguoi_dung == 0:
            print("Trở về menu chính.")
            break
        elif nguoi_dung not in [1, 2, 3]:
            print("Lựa chọn không hợp lệ. Vui lòng nhập 1, 2, 3 hoặc 0.")
            continue
        nguoi_dung -= 1
        may_tinh = random.randint(0, 2)
        print(f"Bạn chọn: {lua_chon[nguoi_dung]}")
        print(f"Máy tính chọn: {lua_chon[may_tinh]}")
        if nguoi_dung == may_tinh:
            print("Kết quả: HÒA!\n")
        elif (nguoi_dung == 0 and may_tinh == 2) or \
             (nguoi_dung == 1 and may_tinh == 0) or \
             (nguoi_dung == 2 and may_tinh == 1):
            print("Kết quả: BẠN THẮNG!\n")
        else:
            print("Kết quả: BẠN THUA!\n")

def choi_doan_so():
    print("\n    ĐOÁN SỐ    ")
    so_can_doan = random.randint(10, 99)
    while True:
        try:
            so_doan = input("Nhập số bạn đoán (có 2 chữ số, 0 để thoát game này): ")
            if so_doan == "0":
                print("Trở về menu chính.")
                break
            so_doan = int(so_doan)
        except ValueError:
            print("Lỗi: Vui lòng nhập một số hợp lệ.")
            continue
        if so_doan < 10 or so_doan > 99:
            print("Lỗi: Bạn phải nhập số có 2 chữ số.")
            continue
        if so_doan == so_can_doan:
            print("Chúc mừng bạn đã đoán đúng!")
            print("Trở về màn hình chính.\n")
            break
        else:
            print("Bạn đã đoán sai rồi!")
            if so_doan < so_can_doan:
                print("Gợi ý: Số bạn đoán nhỏ hơn số cần đoán.\n")
            else:
                print("Gợi ý: Số bạn đoán lớn hơn số cần đoán.\n")

while True:
    print("=" * 30)
    print("      MENU TRÒ CHƠI")
    print("=" * 30)
    print("1 > Đoán số")
    print("2 > Kéo búa bao")
    print("0 > Thoát trò chơi")
    try:
        lua_chon_menu = input("Lựa chọn của bạn: ")
        if lua_chon_menu == "0":
            print("Cảm ơn bạn đã chơi. Hẹn gặp lại!")
            break
        elif lua_chon_menu == "1":
            choi_doan_so()
        elif lua_chon_menu == "2":
            choi_keo_bua_bao()
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập 0, 1 hoặc 2.\n")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")