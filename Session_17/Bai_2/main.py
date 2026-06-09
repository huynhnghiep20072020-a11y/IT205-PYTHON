# Tham số key trong sort()  Khi hàm get_sort_key trả về một Tuple gồm 2 phần tử (-rating, price), Python sẽ dùng nó làm tiêu chí so sánh. 
# Nó xét phần tử đầu tiên trước: việc thêm dấu âm - vào trước rating sẽ "đánh lừa" Python, ép nó sắp xếp Đánh giá theo chiều giảm dần (từ cao xuống thấp).
# Nếu hai mặt hàng có Đánh giá bằng nhau, hệ thống tự động xét tiếp đến phần tử thứ hai (price) và sắp xếp theo chiều tăng dần tự nhiên.

# Cơ chế Accumulator của reduce(): Hàm reduce hoạt động như một cỗ máy cuốn chiếu. Nó lấy kết quả của phép tính trước đó (gọi là biến tích lũy total) 
# và đưa vào tính toán với phần tử tiếp theo trong danh sách (biến current_price), cứ thế lặp đi lặp lại cho đến khi "nghiền" toàn bộ mảng thành một con số tổng duy nhất.

# Thay vì dùng dằng nhằng các câu lệnh if-else kiểm tra độ dài chuỗi, mã nguồn tận dụng khối try-except để tóm gọn cả IndexError (khi chuỗi bị khuyết phần tử, ví dụ thiếu mất rating) 
# và ValueError (khi Giá hoặc Đánh giá bị nhập bằng chữ thay vì số).




import functools

product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5",
    "P04-Sạc Dự Phòng-300000",
    "P05-Cáp Sạc-HaiTrăm-4.0"
]

def display_labels(products):
    """Bóc tách chuỗi, map vào dictionary và in ra tem nhãn dạng bảng."""
    print("--- DANH SÁCH TEM NHÃN ---")
    for item in products:
        parts = item.split("-")
        try:
            product_dict = {
                "id": parts[0],
                "name": parts[1],
                "price": int(parts[2]),
                "rating": float(parts[3])
            }
            template = "Mã: {id:<10} | Tên: {name:<25} | Giá: {price:,} VND | Rating: {rating}*"
            print(template.format_map(product_dict))
        except IndexError:
            print(f"Bỏ qua sản phẩm [{parts[0]}] do sai cấu trúc dữ liệu.")
        except ValueError:
            print(f"Bỏ qua sản phẩm [{parts[0]}] do lỗi ép kiểu (không phải số).")

def get_sort_key(item):
    """Hàm phụ trợ tạo Tuple key sắp xếp: Ưu tiên Rating giảm dần, Giá tăng dần."""
    parts = item.split("-")
    try:
        rating = float(parts[3])
        price = int(parts[2])
        return (-rating, price)
    except (IndexError, ValueError):
        return (0, 0)

def sort_smart(products):
    """Sắp xếp lại danh sách sản phẩm bằng list.sort() và in kết quả ra màn hình."""
    print("--- SẮP XẾP SẢN PHẨM ---")
    products.sort(key=get_sort_key)
    print("Đã sắp xếp thành công! Cập nhật danh sách:")
    for i in range(len(products)):
        print(f"{i + 1}. {products[i]}")

def sum_accumulator(total, current_price):
    """Hàm phụ trợ định nghĩa phép cộng dồn cho functools.reduce."""
    return total + current_price

def calculate_total(products):
    """Trích xuất danh sách giá tiền hợp lệ và dùng reduce để tính tổng giá trị kho."""
    print("--- TỔNG GIÁ TRỊ KHO ---")
    valid_prices = []
    
    for item in products:
        parts = item.split("-")
        try:
            price = int(parts[2])
            valid_prices.append(price)
        except (IndexError, ValueError):
            pass
            
    if len(valid_prices) == 0:
        print("Không có mặt hàng nào hợp lệ để tính toán.")
        return

    total_value = functools.reduce(sum_accumulator, valid_prices)
    print(f"Tổng giá trị các mặt hàng hiện tại là: {total_value:,} VND.")

def main():
    while True:
        print("\n=============== E-COMMERCE ANALYTICS ===============")
        print("1. Hiển thị tem nhãn sản phẩm (format_map & F-String)")
        print("2. Sắp xếp sản phẩm thông minh (sort key)")
        print("3. Tính tổng giá trị kho hàng (reduce)")
        print("4. Đóng hệ thống")
        print("====================================================")
        
        choice = input("Chọn chức năng (1-4): ").strip()
        
        if choice == "1":
            display_labels(product_list)
        elif choice == "2":
            sort_smart(product_list)
        elif choice == "3":
            calculate_total(product_list)
        elif choice == "4":
            print("Cảm ơn bạn đã sử dụng hệ thống. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1-4!")

if __name__ == "__main__":
    main()