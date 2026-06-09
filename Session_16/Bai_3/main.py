# Sử dụng hàm phụ trợ  Để tránh việc viết lại vòng lặp tìm kiếm mã bệnh nhân ở cả chức năng thêm mới và cập nhật,
# chúng ta tách riêng một hàm find_patient_index. hàm validate_gender giúp làm sạch logic kiểm tra giới tính hợp lệ.

# Chuẩn hóa dữ liệu triệt để: Mọi dữ liệu do người dùng nhập vào thông qua input() đều được cắt bỏ khoảng trắng hai đầu bằng .strip(). 
# tùy vào yêu cầu của từng trường dữ liệu mà áp dụng .upper() (mã bệnh nhân), .title() (tên riêng) hoặc .capitalize() (chẩn đoán bệnh)
# trước khi đẩy vào danh sách. Việc chặn dữ liệu rỗng (chỉ toàn dấu cách) cũng được thực hiện bằng cách kiểm tra độ dài chuỗi ngay sau khi strip().


def main():
    patients = [
        ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
        ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
    ]

    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====")
        print("1. Hiển thị danh sách bệnh nhân")
        print("2. Tiếp nhận bệnh nhân mới")
        print("3. Cập nhật chẩn đoán bệnh theo mã BN")
        print("4. Tìm kiếm và thống kê theo tên bệnh")
        print("5. Thoát chương trình")
        print("=============================================")

        choice = input("Nhập lựa chọn của bạn: ").strip()

        if choice == "1":
            display_patients(patients)
        elif choice == "2":
            add_patient(patients)
        elif choice == "3":
            update_diagnosis(patients)
        elif choice == "4":
            search_by_disease(patients)
        elif choice == "5":
            print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại!")

if __name__ == "__main__":
    main()
def validate_gender(gender_input):
    """
    Kiểm tra giới tính nhập vào có hợp lệ hay không. Trả về True nếu là Nam/Nữ, ngược lại False.
    """
    gender = gender_input.strip().lower()
    if gender == "nam" or gender == "nu":
        return True
    return False

def find_patient_index(patient_list, patient_id):
    """
    Tìm kiếm và trả về vị trí (index) của bệnh nhân trong danh sách dựa vào mã bệnh nhân.
    Trả về -1 nếu không tìm thấy.
    """
    patient_id = patient_id.strip().upper()
    for i in range(len(patient_list)):
        if patient_list[i][0] == patient_id:
            return i
    return -1

def display_patients(patient_list):
    """
    Hiển thị danh sách toàn bộ bệnh nhân đang điều trị.
    """
    if len(patient_list) == 0:
        print("Hiện không có bệnh nhân nào đang điều trị.")
        return
        
    print("----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----")
    for i in range(len(patient_list)):
        p = patient_list[i]
        print(f"{i + 1}. Mã: {p[0]} | Tên: {p[1]} | Giới tính: {p[2]} | Bệnh: {p[3]}")

def add_patient(patient_list):
    """
    Thêm một hồ sơ bệnh nhân mới vào hệ thống với các bước chuẩn hóa và bắt lỗi nhập liệu.
    """
    print("----- TIẾP NHẬN BỆNH NHÂN MỚI -----")
    
    ma_bn = input("Nhập mã bệnh nhân: ").strip().upper()
    if len(ma_bn) == 0:
        print("Mã bệnh nhân không được để trống!")
        return
        
    if find_patient_index(patient_list, ma_bn) != -1:
        print("Mã bệnh nhân đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
        return

    ten_bn = input("Nhập tên bệnh nhân: ").strip().title()
    if len(ten_bn) == 0:
        print("Tên bệnh nhân không được để trống!")
        return

    gioi_tinh = input("Nhập giới tính Nam/Nu: ").strip()
    if not validate_gender(gioi_tinh):
        print("Giới tính không hợp lệ, vui lòng nhập lại!")
        return
    gioi_tinh = gioi_tinh.title()

    chan_doan = input("Nhập chẩn đoán bệnh: ").strip().capitalize()
    if len(chan_doan) == 0:
        print("Chẩn đoán bệnh không được để trống!")
        return

    patient_list.append([ma_bn, ten_bn, gioi_tinh, chan_doan])
    print("Tiếp nhận bệnh nhân thành công!")

def update_diagnosis(patient_list):
    """
    Cập nhật lại chẩn đoán bệnh cho một bệnh nhân hiện có dựa trên mã bệnh nhân.
    """
    print("----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")
    
    ma_bn = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()
    if len(ma_bn) == 0:
        print("Mã bệnh nhân không được để trống!")
        return

    index = find_patient_index(patient_list, ma_bn)
    if index == -1:
        print(f"Không tìm thấy hồ sơ mang mã [{ma_bn}]!")
        return

    print(f"Tìm thấy bệnh nhân: {patient_list[index][1]}")
    print(f"Chẩn đoán hiện tại: {patient_list[index][3]}")

    chan_doan_moi = input("Nhập chẩn đoán mới: ").strip().capitalize()
    if len(chan_doan_moi) == 0:
        print("Chẩn đoán bệnh không được để trống!")
        return

    patient_list[index][3] = chan_doan_moi
    print("Cập nhật chẩn đoán thành công!")

def search_by_disease(patient_list):
    """
    Tìm kiếm và thống kê số lượng bệnh nhân theo một từ khóa liên quan đến tên bệnh.
    """
    print("----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")
    
    keyword = input("Nhập từ khóa tên bệnh: ").strip()
    if len(keyword) == 0:
        print("Từ khóa tìm kiếm không được để trống!")
        return

    count = 0
    print("Kết quả tìm kiếm:")
    for p in patient_list:
        if keyword.lower() in p[3].lower():
            count += 1
            print(f"{count}. Mã: {p[0]} | Tên: {p[1]} | Giới tính: {p[2]} | Bệnh: {p[3]}")

    print(f"\nCó tổng cộng {count} bệnh nhân mắc bệnh liên quan đến '{keyword}'.")

