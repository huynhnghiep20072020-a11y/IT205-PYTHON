# Tính đa hình: Vòng lặp for thể hiện tính đa hình vì hệ thống không cần biết biến hero đang là Mage hay Assassin, 
# nó chỉ cần biết rằng đối tượng đó chắc chắn có hàm use_ultimate() để gọi ra chiêu thức tương ứng của từng hệ phái.

# Thời điểm văng lỗi của code cũ: Trong code cũ, việc tạo đối tượng Assassin diễn ra bình thường. 
# Lỗi NotImplementedError chỉ phát nổ vào lúc giao tranh, khi dòng lệnh hero.use_ultimate() được gọi.
# Đây là thảm họa vì người chơi đã phải đợi load xong game, đang đánh nhau thì bị văng ứng dụng.

# Thời điểm văng lỗi của code mới (dùng ABC): Khi dùng thư viện abc, nếu lớp Assassin quên ghi đè hàm use_ultimate(), 
# lỗi TypeError sẽ văng ra ngay từ lúc khởi tạo đối tượng (lúc loading game).

# Nguyên lý Fail Fast: Việc báo lỗi ngay lúc khởi tạo (Instantiation Time) chính là nguyên lý "Fail Fast".
# Lập trình viên sẽ phát hiện ra lỗi và sửa ngay lập tức, ngăn chặn việc tạo ra các đối tượng lỗi ("bom nổ chậm") tồn tại trong bộ nhớ và gây sập hệ thống sau đó.


from abc import ABC, abstractmethod

class Hero(ABC):
    """Lớp trừu tượng định nghĩa khuôn mẫu chung cho mọi tướng trong game."""
    
    @abstractmethod
    def use_ultimate(self):
        """Phương thức bắt buộc các lớp con phải tự định nghĩa chiêu cuối."""
        pass


class Mage(Hero):
    """Lớp đại diện cho hệ tướng Pháp Sư."""
    
    def use_ultimate(self):
        """Triển khai chiêu cuối Mưa Sao Băng cho Pháp Sư."""
        print("🔥 Pháp Sư tung chiêu: MƯA SAO BĂNG!")


class Assassin(Hero):
    """Lớp đại diện cho hệ tướng Sát Thủ."""
    
    def use_ultimate(self):
        """Triển khai chiêu cuối Ám Sát cho Sát Thủ."""
        print("🗡️ Sát Thủ tung chiêu: ÁM SÁT TỪ PHÍA SAU!")


def main():
    """Hàm chạy kịch bản trận đấu tự động của hệ thống."""
    print("--- LOADING TRẬN ĐẤU ---")
    team_heroes = [Mage(), Assassin()]
    print("Tải trận đấu thành công! Các tướng đã sẵn sàng...")

    print("\n--- GIAO TRANH TỔNG BẮT ĐẦU ---")
    for hero in team_heroes:
        hero.use_ultimate()


if __name__ == "__main__":
    main()