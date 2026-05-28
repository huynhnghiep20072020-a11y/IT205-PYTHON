# Kiosk phan luong tu phuc vu - Benh vien Suc Khoe Vang

print("Chao mung den voi Kiosk Kham Benh")
print("Vui long nhap thong tin de duoc phan luong")
print()

# Thu thap thong tin benh nhan
patient_name = input("Nhap ho va ten (VD: Nguyen Van An): ")
patient_age = int(input("Nhap tuoi (VD: 35): "))
spo2_level = float(input("Nhap nong do oxy SpO2 (VD: 96.5): "))
heart_rate = int(input("Nhap nhip tim - nhip/phut (VD: 80): "))
has_insurance = input("Ban co the Bao hiem Y te khong? (Vui long chi go 'yes' hoac 'no'): ")

# Phan luong y khoa
if spo2_level < 90 or heart_rate > 120:
    triage_level = "BAO DONG DO - CAP CUU KHAN"
elif (90 <= spo2_level <= 95) or (100 <= heart_rate <= 120):
    triage_level = "BAO DONG VANG - THEO DOI SAT"
else:
    triage_level = "XANH - KHAM THUONG"

# Tinh vien phi
if patient_age < 6 or patient_age >= 80:
    hospital_fee = 0
elif has_insurance == "yes":
    hospital_fee = 250000
else:
    hospital_fee = 500000

# In phieu kham benh
print()
print("====== PHIEU KHAM BENH DIEN TU ======")
print("Ho va ten     :", patient_name)
print("Tuoi          :", patient_age)
print("SpO2          :", spo2_level, "%")
print("Nhip tim      :", heart_rate, "nhip/phut")
print("Co BHYT       :", has_insurance)
print("Phan luong    :", triage_level)
print("Vien phi tam ung:", hospital_fee, "VND")
print("=====================================")

# Log he thong
print()
print("====== LOG HE THONG ======")
print("patient_name  =", patient_name, "| kieu:", type(patient_name))
print("patient_age   =", patient_age, "| kieu:", type(patient_age))
print("spo2_level    =", spo2_level, "| kieu:", type(spo2_level))
print("heart_rate    =", heart_rate, "| kieu:", type(heart_rate))
print("has_insurance =", has_insurance, "| kieu:", type(has_insurance))
print("triage_level  =", triage_level, "| kieu:", type(triage_level))
print("hospital_fee  =", hospital_fee, "| kieu:", type(hospital_fee))
print("==========================")