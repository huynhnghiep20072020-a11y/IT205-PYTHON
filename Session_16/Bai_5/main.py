# Băm chuỗi và Ép kiểu  Để so sánh được Nhịp tim (HR > 100) và Nhiệt độ (TEMP >= 39.0) ở chức năng Báo động đỏ 
# dùng replace() để lột bỏ chữ "HR:" và "TEMP:", lấy ra phần số nguyên thủy và ép kiểu sang int hoặc float thì toán học mới hiểu để tính toán.

# Xử lý tính bất biến  Ở chức năng số 3 (Cập nhật sinh hiệu) Bạn phải tách chuỗi ra thành List, cập nhật giá trị mới vào vị trí index 2 hoặc 3,
# sau đó dùng lệnh "|".join(parts) để đúc lại thành một chuỗi nguyên khối và gán đè lên dữ liệu cũ.
# Tái sử dụng lại hàm find_patient_index để lấy ra vị trí của bệnh nhân trong danh sách. Nếu tìm thấy (index khác -1),
# ta dùng split("|") để trích xuất lấy tên bệnh nhân phục vụ cho câu lệnh in thông báo, sau đó mới gọi phương thức .pop(index) để xóa triệt để hồ sơ đó khỏi mảng.
# Thay vì dùng khối try-except, dùng .replace(".", "").isdigit() đối với nhiệt độ. 
# Nó sẽ tạm thời tàng hình dấu chấm thập phân, sau đó kiểm tra xem phần còn lại có phải toàn là số hay không. 
# nếu nhập chữ như "chín mươi", hàm trả về False và báo lỗi yêu cầu nhập lại ngay lập tức mà không làm sập (crash) chương trình.

def main():
    """Hàm khởi tạo chương trình chứa dữ liệu mẫu và menu điều hướng vòng lặp while."""
    er_patients = [
        "ER01|Nguyen Van Quan|HR:115|TEMP:39.5",
        "ER02|Tran Thi Binh|HR:80|TEMP:37.0",
        "ER03|Le Van Cuong|HR:130|TEMP:38.2"
    ]

    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ CẤP CỨU RIKKEI ER =====")
        print("1. Bảng theo dõi bệnh nhân")
        print("2. Tiếp nhận ca cấp cứu mới")
        print("3. Cập nhật lại sinh hiệu")
        print("4. Báo động đỏ (Lọc bệnh nhân nguy kịch)")
        print("5. Xuất viện / Chuyển khoa")
        print("6. Thoát chương trình")
        print("==============================================")

        choice = input("Chọn chức năng (1-6): ").strip()

        if choice == "1":
            display_dashboard(er_patients)
        elif choice == "2":
            admit_patient(er_patients)
        elif choice == "3":
            update_vitals(er_patients)
        elif choice == "4":
            trigger_red_alert(er_patients)
        elif choice == "5":
            discharge_patient(er_patients)
        elif choice == "6":
            print("In thông báo kết thúc ca trực và thoát vòng lặp.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-6!")

if __name__ == "__main__":
    main()
def find_patient_index(patients, er_id):
    """Tìm vị trí của bệnh nhân trong danh sách dựa trên mã ER bằng hàm startswith."""
    search_key = er_id + "|"
    for i in range(len(patients)):
        if patients[i].startswith(search_key):
            return i
    return -1

def extract_vital_value(vital_string):
    """Trích xuất và trả về con số thực từ chuỗi sinh hiệu (ví dụ 'HR:115' thành 115.0)."""
    parts = vital_string.split(":")
    return float(parts[1])

def display_dashboard(patients):
    """Tách chuỗi dữ liệu và in ra bảng theo dõi tình trạng của tất cả ca cấp cứu."""
    if len(patients) == 0:
        print("Khoa cấp cứu hiện đang trống.")
        return

    print("--- BẢNG THEO DÕI CA CẤP CỨU ---")
    for i in range(len(patients)):
        parts = patients[i].split("|")
        hr = parts[2].replace("HR:", "")
        temp = parts[3].replace("TEMP:", "")
        print(f"{i + 1}. [{parts[0]}] {parts[1]} | Nhịp tim: {hr} bpm | Nhiệt độ: {temp} °C")

def admit_patient(patients):
    """Tiếp nhận ca mới, kiểm tra các bẫy lỗi về kiểu dữ liệu bằng isdigit và giới hạn an toàn."""
    print("--- TIẾP NHẬN CA CẤP CỨU MỚI ---")
    
    er_id = input("Nhập mã ER: ").strip().upper()
    if len(er_id) == 0:
        print("Mã ER không được để trống!")
        return
        
    if find_patient_index(patients, er_id) != -1:
        print("Mã ca cấp cứu đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ").strip().title()
    if len(name) == 0:
        print("Tên bệnh nhân không được để trống!")
        return

    hr_input = input("Nhập nhịp tim HR: ").strip()
    if not hr_input.isdigit() or int(hr_input) <= 0:
        print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!")
        return
    hr = int(hr_input)

    temp_input = input("Nhập nhiệt độ TEMP: ").strip()
    if not temp_input.replace(".", "").isdigit() or float(temp_input) < 36.5:
        print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn hoặc bằng 36.5!")
        return
    temp = float(temp_input)

    new_record = f"{er_id}|{name}|HR:{hr}|TEMP:{temp}"
    patients.append(new_record)
    print("Tiếp nhận ca cấp cứu mới thành công!")

def update_vitals(patients):
    """Tìm bệnh nhân theo mã, cho phép chọn sinh hiệu cần sửa và cập nhật đè lại chuỗi."""
    print("--- CẬP NHẬT LẠI SINH HIỆU ---")
    
    er_id = input("Nhập mã ER cần cập nhật: ").strip().upper()
    index = find_patient_index(patients, er_id)

    if index == -1:
        print("Không tìm thấy bệnh nhân. Vui lòng kiểm tra lại mã ER!")
        return

    parts = patients[index].split("|")
    print(f"Tìm thấy bệnh nhân: {parts[1]}")
    print(f"Sinh hiệu hiện tại: {parts[2]} | {parts[3]}")
    print("Bạn muốn cập nhật:")
    print("1. Nhịp tim HR")
    print("2. Nhiệt độ TEMP")

    choice = input("Chọn loại sinh hiệu: ").strip()

    if choice == "1":
        new_hr_input = input("Nhập nhịp tim mới: ").strip()
        if not new_hr_input.isdigit() or int(new_hr_input) <= 0:
            print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!")
            return
        parts[2] = f"HR:{new_hr_input}"
        patients[index] = "|".join(parts)
        print("Cập nhật nhịp tim thành công!")
        
    elif choice == "2":
        new_temp_input = input("Nhập nhiệt độ mới: ").strip()
        if not new_temp_input.replace(".", "").isdigit() or float(new_temp_input) <= 0:
            print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!")
            return
        parts[3] = f"TEMP:{new_temp_input}"
        patients[index] = "|".join(parts)
        print("Cập nhật nhiệt độ thành công!")
        
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2!")

def trigger_red_alert(patients):
    """Lọc ra các bệnh nhân có sinh hiệu vượt ngưỡng an toàn bằng hàm trích xuất phụ trợ."""
    print("!!! BÁO ĐỘNG ĐỎ - DANH SÁCH BỆNH NHÂN NGUY KỊCH !!!")
    count = 0
    
    for patient in patients:
        parts = patient.split("|")
        hr = extract_vital_value(parts[2])
        temp = extract_vital_value(parts[3])

        if hr > 100 or temp >= 39.0:
            count += 1
            print(f"{count}. [{parts[0]}] {parts[1]} | HR: {int(hr)} bpm | TEMP: {temp} °C | CẦN XỬ LÝ KHẨN CẤP")

    if count == 0:
        print("Không có bệnh nhân nguy kịch tại thời điểm hiện tại.")
    else:
        print("-" * 40)
        print(f"Tổng số ca nguy kịch: {count}")

def discharge_patient(patients):
    """Tìm kiếm vị trí của bệnh nhân và dùng pop() để xóa hồ sơ khỏi danh sách trực."""
    print("--- XUẤT VIỆN / CHUYỂN KHOA ---")
    
    if len(patients) == 0:
        print("Khoa cấp cứu hiện đang trống.")
        return

    er_id = input("Nhập mã ER cần xóa khỏi hệ thống: ").strip().upper()
    if len(er_id) == 0:
        print("Mã ER không được để trống!")
        return

    index = find_patient_index(patients, er_id)

    if index == -1:
        print("Không tìm thấy bệnh nhân. Vui lòng kiểm tra lại mã ER!")
        return

    parts = patients[index].split("|")
    patient_name = parts[1]
    
    patients.pop(index)
    print(f"Đã chuyển khoa thành công cho bệnh nhân {patient_name}!")

