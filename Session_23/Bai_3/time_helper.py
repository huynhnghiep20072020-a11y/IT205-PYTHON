from datetime import datetime, timedelta

def process_eta(flights):
    """Tìm chuyến bay và tính toán thời gian hạ cánh dự kiến."""
    print("\n----- TÍNH TOÁN THỜI GIAN HẠ CÁNH (ETA) -----")
    flight_id = input("Nhập mã chuyến bay cần tính: ").strip().upper()
    
    for f in flights:
        if f["flight_id"] == flight_id:
            depart_time = datetime.strptime(f["depart_time"], "%Y-%m-%d %H:%M:%S")
            eta = depart_time + timedelta(minutes=f["duration_min"])
            
            print(f"-> Chuyến bay {flight_id} cất cánh lúc: {f['depart_time']}")
            print(f"-> Thời gian hạ cánh dự kiến (ETA): {eta}")
            return
            
    print("Không tìm thấy mã chuyến bay này.")