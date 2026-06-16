from datetime import datetime as dt

def evaluate_flex_time(records):
    """Tính toán và đánh giá vi phạm giờ giấc dựa trên luật Flex-time."""
    print("\n--- ĐÁNH GIÁ VI PHẠM ---")
    limit_time_str = "10:00"
    limit_dt = dt.strptime(limit_time_str, "%H:%M")

    for r in records:
        in_str = r["times"][0]
        out_str = r["times"][1]

        if out_str is None:
            continue

        in_dt = dt.strptime(in_str, "%H:%M")
        out_dt = dt.strptime(out_str, "%H:%M")

        if in_dt > limit_dt:
            print(f"{r['id']} - Vi phạm: Đến muộn quá 90 phút.")
        else:
            time_diff = out_dt - in_dt
            hours_worked = time_diff.total_seconds() / 3600
            
            if hours_worked < 9:
                print(f"{r['id']} - Vi phạm: Về sớm, chưa hoàn thành đủ 9 tiếng bù giờ.")
            else:
                print(f"{r['id']} - Hợp lệ: Hoàn thành ca làm việc.")