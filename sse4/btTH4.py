ma_so_may_man = 79
chien_thang = False

for luot in range(1, 6):
    doan = int(input(f"Lượt đoán {luot} - Nhập số của bạn: "))
    if doan == ma_so_may_man:
        print("=> Chúc mừng! Bạn đã đoán chính xác mã số may mắn!")
        chien_thang = True
        break
    elif doan < ma_so_may_man:
        print("=> Gợi ý: Số của bạn nhỏ hơn mã số may mắn!")
    else:
        print("=> Gợi ý: Số của bạn lớn hơn mã số may mắn!")

if not chien_thang:
    print("=> Rất tiếc, bạn đã sử dụng hết 5 lượt đoán. Chúc bạn may mắn lần sau!")

print("--- TRÒ CHƠI KẾT THÚC ---")