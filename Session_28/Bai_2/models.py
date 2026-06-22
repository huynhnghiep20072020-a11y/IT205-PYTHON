from abc import ABC, abstractmethod

class BaseLesson(ABC):
    """Lớp cơ sở trừu tượng làm khuôn mẫu cho mọi bài học trên hệ thống LMS."""

    platform_name = "Rikkei Academy LMS"
    base_completion_points = 10

    def __init__(self, lesson_code, title):
        self.lesson_code = lesson_code
        self._title = ""
        self.title = title
        self.__duration_minutes = 0

    @property
    def duration_minutes(self):
        """Đọc thời lượng bài học hiện tại một cách an toàn."""
        return self.__duration_minutes

    def _set_duration(self, minutes):
        """Hàm hỗ trợ nội bộ cho phép cập nhật thời lượng với điều kiện chặt chẽ."""
        if minutes <= 0:
            raise ValueError("Thời lượng bài học và thông số kiểm thử không được nhỏ hơn hoặc bằng 0")
        self.__duration_minutes = minutes

    @property
    def title(self):
        """Đọc tiêu đề bài học."""
        return self._title

    @title.setter
    def title(self, value):
        """Chuẩn hóa tiêu đề bài học thành in hoa và bỏ khoảng trắng thừa."""
        self._title = value.strip().upper()

    @abstractmethod
    def calculate_completion_score(self):
        """Phương thức trừu tượng quy định logic tính điểm hoàn thành."""
        pass

    @abstractmethod
    def update_content(self, new_data):
        """Phương thức trừu tượng quy định logic cập nhật nội dung bài học."""
        pass

    def __add__(self, other):
        """Nạp chồng toán tử cộng để gộp thời lượng của hai bài học."""
        if not isinstance(other, BaseLesson):
            return NotImplemented
        return self.duration_minutes + other.duration_minutes

    def __lt__(self, other):
        """Nạp chồng toán tử nhỏ hơn để so sánh độ dài thời lượng hai bài học."""
        if not isinstance(other, BaseLesson):
            return NotImplemented
        return self.duration_minutes < other.duration_minutes

    @staticmethod
    def validate_lesson_code(lesson_code):
        """Kiểm tra mã bài học phải đúng 10 ký tự và bắt đầu bằng LMS."""
        if len(lesson_code) == 10 and lesson_code.startswith("LMS"):
            return True
        return False

    @classmethod
    def update_base_points(cls, new_points):
        """Cập nhật điểm kinh nghiệm cơ bản áp dụng cho toàn hệ thống."""
        cls.base_completion_points = new_points


class VideoLesson(BaseLesson):
    """Lớp quản lý các bài học dạng video lý thuyết."""

    def __init__(self, lesson_code, title):
        super().__init__(lesson_code, title)
        self.video_quality = "1080p"
        self.view_count = 0

    def calculate_completion_score(self):
        """Tính điểm dựa trên thời lượng video."""
        return self.base_completion_points + (self.duration_minutes * 0.5)

    def update_content(self, new_data):
        """Cập nhật thời lượng video."""
        if "duration" in new_data:
            self._set_duration(new_data["duration"])
            print("Cập nhật thông số thành công!")

    def play_video(self):
        """Giả lập lượt xem video của học viên."""
        self.view_count += 1
        print("Ghi nhận thành công! Học viên đã xem video bài học.")
        print(f"Tổng số lượt xem hiện tại: {self.view_count} lượt.")


class CodingChallenge(BaseLesson):
    """Lớp quản lý các bài tập thực hành lập trình."""

    def __init__(self, lesson_code, title):
        super().__init__(lesson_code, title)
        self.number_of_testcases = 0
        self.difficulty_multiplier = 1.5

    def calculate_completion_score(self):
        """Tính điểm dựa trên số lượng testcase và độ khó."""
        return self.base_completion_points * self.number_of_testcases * self.difficulty_multiplier

    def update_content(self, new_data):
        """Cập nhật số lượng testcase cho bài thực hành."""
        if "testcases" in new_data:
            if new_data["testcases"] <= 0:
                raise ValueError("Thời lượng bài học và thông số kiểm thử không được nhỏ hơn hoặc bằng 0")
            self.number_of_testcases = new_data["testcases"]
            print("Cập nhật thông số thành công!")
            print(f"Số lượng testcase hiện tại trên hệ thống: {self.number_of_testcases} testcases.")


class HybridAssessment(VideoLesson, CodingChallenge):
    """Lớp bài học kiểm tra lai đa năng ứng dụng đa kế thừa MRO."""

    def __init__(self, lesson_code, title):
        BaseLesson.__init__(self, lesson_code, title)
        self.video_quality = "1080p"
        self.view_count = 0
        self.number_of_testcases = 0
        self.difficulty_multiplier = 1.5

    def calculate_completion_score(self):
        """Gộp logic tính điểm từ cả phần Video và phần Code."""
        video_score = self.base_completion_points + (self.duration_minutes * 0.5)
        coding_score = self.base_completion_points * self.number_of_testcases * self.difficulty_multiplier
        return video_score + coding_score

    def update_content(self, new_data):
        """Cho phép cập nhật cả thời lượng video và số lượng testcase."""
        if "duration" in new_data:
            self._set_duration(new_data["duration"])
        if "testcases" in new_data:
            if new_data["testcases"] <= 0:
                raise ValueError("Thời lượng bài học và thông số kiểm thử không được nhỏ hơn hoặc bằng 0")
            self.number_of_testcases = new_data["testcases"]
        print("Cập nhật thông số thành công!")