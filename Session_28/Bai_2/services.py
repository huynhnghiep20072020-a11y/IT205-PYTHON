class AWSS3StorageService:
    """Cổng dịch vụ lưu trữ đám mây AWS S3."""

    def upload_lesson(self, lesson):
        """Thực hiện upload dữ liệu lên AWS."""
        print("[Hệ thống AWS S3]: Đang khởi tạo luồng băng thông kết nối tới LMS...")
        print(f"Hệ thống lưu trữ đám mây đã upload toàn bộ tài nguyên của bài học {lesson.lesson_code} lên cụm máy chủ an toàn.")


class GoogleCloudStorageService:
    """Cổng dịch vụ lưu trữ đám mây Google Cloud."""

    def upload_lesson(self, lesson):
        """Thực hiện upload dữ liệu lên Google Cloud."""
        print("[Hệ thống Google Cloud]: Đang đồng bộ thư mục khóa học...")
        print(f"Hệ thống lưu trữ đám mây đã upload toàn bộ tài nguyên của bài học {lesson.lesson_code} lên cụm máy chủ an toàn.")


def sync_to_cloud(cloud_service, lesson):
    """Hàm toàn cục xử lý đồng bộ dữ liệu ứng dụng Duck Typing."""
    try:
        cloud_service.upload_lesson(lesson)
        print("Xác thực dịch vụ bằng Duck Typing thành công!")
    except AttributeError:
        print("Lỗi: Dịch vụ lưu trữ đám mây không hợp lệ hoặc chưa ký kết chứng chỉ API liên thông.")