# Tách và Ghép chuỗi: Trong tính năng Cập nhật chẩn đoán, vì bạn không thể sửa trực tiếp một phần của chuỗi ban đầu,
# hệ thống phải dùng lệnh split("-") để băm chuỗi thành một danh sách (List) các thành phần rời rạc. 
# Sau khi thay đổi thành phần chẩn đoán ở vị trí số 3, ta dùng "-".join() để dán chúng lại thành một chuỗi mới hoàn chỉnh và ghi đè vào danh sách gốc.

# Xử lý ký tự phân tách: Nếu bệnh nhân nhập chẩn đoán có chứa dấu - , nó sẽ làm hỏng cấu trúc 4 phần của hệ thống. 
# hàm replace("-", " ") được dùng để dọn dẹp trước khi ghép chuỗi.

# Tìm kiếm chính xác: Thay vì dùng toán tử in dễ gây nhầm lẫn , ta sử dụng phương thức startswith(patient_id + "-") 
# để đảm bảo hệ thống tra cứu đúng mã hồ sơ ở ngay đầu chuỗi.

def main():
    patient_records = [
        "BN001-Nguyen Van A-1985-Viem Phoi",
        "BN002-Tran Thi B-1990-Sot Xuat Huyet",
        "BN003-Le Van C-2015-Viem Phe Quan"
    ]

    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====")
        print("1. Xem danh sách hồ sơ bệnh án")
        print("2. Thêm hồ sơ bệnh nhân mới")
        print("3. Cập nhật chẩn đoán theo Mã BN")
        print("4. Báo cáo phân loại theo độ tuổi")
        print("5. Thoát chương trình")
        print("====================================================")

        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == "1":
            display_records(patient_records)
        elif choice == "2":
            add_patient(patient_records)
        elif choice == "3":
            update_diagnosis(patient_records)
        elif choice == "4":
            generate_age_report(patient_records)
        elif choice == "5":
            print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
def find_patient_index(records, patient_id):
    """
    Tìm vị trí của bệnh nhân trong danh sách dựa trên mã bệnh nhân nằm ở đầu chuỗi.
    Trả về chỉ mục (index) nếu tìm thấy, ngược lại trả về -1.
    """
    search_key = patient_id + "-"
    for i in range(len(records)):
        if records[i].startswith(search_key):
            return i
    return -1

def display_records(records):
    """
    Tách chuỗi dữ liệu của từng hồ sơ và hiển thị dưới dạng bảng được căn lề.
    """
    if len(records) == 0:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return

    print("--- DANH SÁCH BỆNH NHÂN ---")
    for i in range(len(records)):
        parts = records[i].split("-")
        print(f"{i + 1}. [{parts[0]}] {parts[1]} | Năm sinh: {parts[2]} | Chẩn đoán: {parts[3]}")

def add_patient(records):
    """
    Tiếp nhận hồ sơ mới, chuẩn hóa chuỗi, bắt lỗi năm sinh và định dạng lại thành chuỗi tổng hợp.
    """
    print("--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")
    
    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()
    if find_patient_index(records, patient_id) != -1:
        print("Mã bệnh nhân đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ").strip().title()
    
    year_input = input("Nhập năm sinh: ").strip()
    if not year_input.isdigit():
        print("Năm sinh không hợp lệ, vui lòng nhập lại!")
        return
        
    year = int(year_input)
    if year < 1900 or year > 2026:
        print("Năm sinh không hợp lệ, vui lòng nhập lại!")
        return

    diagnosis = input("Nhập chẩn đoán: ").strip()
    diagnosis = diagnosis.replace("-", " ").capitalize()

    new_record = f"{patient_id}-{name}-{year}-{diagnosis}"
    records.append(new_record)
    print("Thêm hồ sơ bệnh nhân thành công!")

def update_diagnosis(records):
    """
    Tìm kiếm hồ sơ theo mã, tách chuỗi để thay đổi thông tin chẩn đoán, sau đó nối lại.
    """
    print("--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")
    
    patient_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()
    index = find_patient_index(records, patient_id)
    
    if index == -1:
        print(f"Không tìm thấy bệnh nhân mang mã {patient_id}!")
        return

    parts = records[index].split("-")
    print(f"Tìm thấy bệnh nhân: {parts[1]}")
    print(f"Chẩn đoán hiện tại: {parts[3]}")

    new_diagnosis = input("Nhập chẩn đoán mới: ").strip()
    new_diagnosis = new_diagnosis.replace("-", " ").capitalize()

    parts[3] = new_diagnosis
    records[index] = "-".join(parts)
    print("Cập nhật chẩn đoán thành công!")

def generate_age_report(records):
    """
    Tính toán tuổi của từng bệnh nhân và phân loại vào các nhóm tương ứng để thống kê.
    """
    print("--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")
    
    tre_em = 0
    truong_thanh = 0
    nguoi_cao_tuoi = 0
    current_year = 2026

    for record in records:
        parts = record.split("-")
        age = current_year - int(parts[2])
        
        if age < 16:
            tre_em += 1
        elif age <= 60:
            truong_thanh += 1
        else:
            nguoi_cao_tuoi += 1

    print(f"Trẻ em: {tre_em} bệnh nhân")
    print(f"Trưởng thành: {truong_thanh} bệnh nhân")
    print(f"Người cao tuổi: {nguoi_cao_tuoi} bệnh nhân")

