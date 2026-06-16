from tabulate import tabulate

def display_records(records):
    """Hiển thị danh sách chấm công dưới dạng bảng sử dụng thư viện tabulate."""
    print("\n--- BẢNG CHẤM CÔNG ---")
    if not records:
        print("Hệ thống chưa có dữ liệu.")
        return

    table_data = []
    for r in records:
        in_time = r["times"][0]
        out_time = r["times"][1]
        
        if out_time is None:
            out_time_display = "[Đang làm việc]"
        else:
            out_time_display = out_time
            
        table_data.append([r["id"], r["name"], in_time, out_time_display])
        
    print(tabulate(table_data, headers=["Mã NV", "Tên Nhân Viên", "Giờ Vào", "Giờ Ra"], tablefmt="simple"))