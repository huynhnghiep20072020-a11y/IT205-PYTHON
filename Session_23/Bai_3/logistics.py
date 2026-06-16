from math import ceil

def display_flights(flights):
    """Hiển thị danh sách chuyến bay và tính toán số thùng nước dự phòng."""
    print("\n----- DANH SÁCH CHUYẾN BAY & HẬU CẦN -----")
    if not flights:
        print("Chưa có chuyến bay nào trong hệ thống.")
        return
        
    for i in range(len(flights)):
        f = flights[i]
        water_boxes = ceil(f["passengers"] / 10)
        print(f"{i + 1}. Mã: {f['flight_id']} | Khởi hành: {f['depart_time']} | Số khách: {f['passengers']} | Dự phòng: {water_boxes} thùng nước.")