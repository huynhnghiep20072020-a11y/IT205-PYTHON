# 1. Input / Output:
# Input: patient_name (Chuỗi ký tự từ bàn phím), patient_age (Số nguyên từ bàn phím).
# Output: Phiếu khám bệnh hợp lệ (Tên, Tuổi, Trạng thái) hoặc thông báo lỗi hệ thống và dừng chương trình.
# 2. Giải pháp và Thuật toán:Dùng .strip() để xóa khoảng trắng thừa ở hai đầu chuỗi tên nhằm chặn bẫy bỏ trống hoặc nhập toàn dấu cách.
# Kiểm tra bẫy dữ liệu: Nếu tên rỗng hoặc tuổi < 0 hoặc tuổi > 150 thì in thông báo lỗi và dùng sys.exit() ngắt chương trình lập tức.
# Phân luồng bằng if-elif-else: Tuổi < 6 là "Bệnh nhi", tuổi \ge 80 là "Người cao tuổi", còn lại là "Khám thường".

# viết code
import sys

raw_name = input("Nhập họ và tên bệnh nhân: ")
raw_age = input("Nhập tuổi bệnh nhân: ")

patient_name = raw_name.strip()

if not raw_age.isdigit() and not (raw_age.startswith('-') and raw_age[1:].isdigit()):
    print("\n[LỖI]: Tuổi nhập vào phải là một số nguyên hợp lệ!")
    sys.exit()

patient_age = int(raw_age)

if patient_name == "" or patient_age < 0 or patient_age > 150:
    print("\n[LỖI]: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
    sys.exit()

if patient_age < 6:
    classification = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
elif patient_age >= 80:
    classification = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
else:
    classification = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

print("       PHIẾU KHÁM BỆNH ĐIỆN TỬ            ")
print("==========================================")
print(" Họ và tên : {}".format(patient_name))
print(" Tuổi      : {} tuổi".format(patient_age))
print(" Trạng thái: {}".format(classification))
