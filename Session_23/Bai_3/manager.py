from datetime import datetime

def check_duplicate_id(flight_id, flight_list):
    """Kiểm tra mã chuyến bay đã tồn tại trong danh sách hay chưa."""
    for f in flight_list:
        if f["flight_id"] == flight_id:
            return True
    return False

def add_new_flight(flights):
    """Tiếp nhận thông tin chuyến bay mới và bẫy lỗi định dạng thời gian."""
    print("\n----- TIẾP NHẬN CHUYẾN BAY MỚI -----")
    flight_id = input("Nhập mã chuyến bay: ").strip().upper()
    
    if check_duplicate_id(flight_id, flights):
        print("Lỗi: Mã chuyến bay đã tồn tại!")
        return
        
    try:
        passengers = int(input("Nhập số lượng hành khách: "))
        depart_time = input("Nhập thời gian cất cánh (YYYY-MM-DD HH:MM:SS): ").strip()
        
        datetime.strptime(depart_time, "%Y-%m-%d %H:%M:%S")
        
        duration = int(input("Nhập số phút bay: "))
        
        new_flight = {
            "flight_id": flight_id,
            "passengers": passengers,
            "depart_time": depart_time,
            "duration_min": duration
        }
        flights.append(new_flight)
        print(f">> Thêm chuyến bay {flight_id} thành công!")
        
    except ValueError:
        print("Sai định dạng thời gian! Vui lòng nhập đúng chuẩn YYYY-MM-DD HH:MM:SS (hoặc lỗi nhập chữ vào ô số).")