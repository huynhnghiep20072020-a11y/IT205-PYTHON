def clock_in(records):
    """Ghi nhận giờ vào làm của nhân viên mới và thiết lập tuple thời gian."""
    emp_id = input("Nhập mã nhân viên: ").strip().upper()
    
    for r in records:
        if r["id"] == emp_id:
            print("Lỗi: Mã nhân viên đã tồn tại trong ngày!")
            return
            
    name = input("Nhập tên nhân viên: ").strip().title()
    in_time = input("Nhập giờ vào (HH:MM): ").strip()
    
    records.append({
        "id": emp_id,
        "name": name,
        "times": (in_time, None)
    })
    print(f"Thành công: Đã ghi nhận {emp_id} chấm công vào lúc {in_time}!")

def clock_out(records):
    """Tìm nhân viên và cập nhật giờ ra bằng cách ghi đè hoàn toàn Tuple cũ."""
    emp_id = input("Nhập mã nhân viên: ").strip().upper()
    
    for r in records:
        if r["id"] == emp_id:
            if r["times"][1] is not None:
                print("Nhân viên này đã chấm công ra rồi!")
                return
                
            out_time = input("Nhập giờ ra (HH:MM): ").strip()
            in_time = r["times"][0]
            r["times"] = (in_time, out_time)
            
            print(f"Thành công: Đã ghi nhận {emp_id} chấm công ra lúc {out_time}!")
            return
            
    print("Lỗi: Không tìm thấy nhân viên này!")