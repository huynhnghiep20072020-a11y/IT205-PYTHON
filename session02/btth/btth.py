# Chuong trinh quan ly benh nhan phong kham

# 1. Nhap thong tin benh nhan
name = input("Nhap ten benh nhan: ")
birth_year = int(input("Nhap nam sinh: "))
sick_days = int(input("Nhap so ngay bi benh: "))
temperature = float(input("Nhap nhiet do co the (°C): "))
exam_cost = float(input("Nhap chi phi kham: "))

# 2. Kiem tra du lieu hop le
if name == "":
    print("Ten khong duoc de trong")
elif birth_year < 1900 or birth_year > 2025:
    print("Nam sinh khong hop le")
elif sick_days < 0:
    print("So ngay benh khong hop le")
elif temperature < 30 or temperature > 45:
    print("Nhiet do khong hop le")
elif exam_cost <= 0:
    print("Chi phi kham khong hop le")

else:
    # 3. Tinh toan thong tin
    age = 2026 - birth_year
    surcharge = exam_cost * 10 / 100
    total_cost = exam_cost + surcharge

    # 4. Phan loai tinh trang suc khoe
    if temperature > 38 and sick_days > 3:
        health_status = "Nguy hiem"
    elif temperature > 38:
        health_status = "Sot cao"
    elif temperature > 37.5:
        health_status = "Sot nhe"
    else:
        health_status = "Binh thuong"

    # 5. Danh gia muc do uu tien (nested if)
    if health_status == "Nguy hiem":
        if age > 60:
            priority = "Cap cuu"
        else:
            priority = "Uu tien cao"
    else:
        priority = "Binh thuong"

    # 6. Danh gia muc chi phi (toan tu 3 ngoi)
    cost_level = "Cao" if total_cost > 500000 else "Thap"

    # 7. Hien thi ket qua
    print()
    print("--- KET QUA ---")
    print("Ten:", name)
    print("Tuoi:", age)
    print("Nhiet do:", temperature, "°C")
    print("So ngay benh:", sick_days)
    print()
    print("Tinh trang:", health_status)
    print("Muc do uu tien:", priority)
    print()
    print("Tong chi phi:", total_cost, "VND")
    print("Muc chi phi:", cost_level)