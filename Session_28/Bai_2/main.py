from models import BaseLesson, VideoLesson, CodingChallenge, HybridAssessment
from services import AWSS3StorageService, GoogleCloudStorageService, sync_to_cloud

def get_lesson_by_code(lessons, lesson_code):
    """Hàm phụ trợ tìm kiếm bài học trong hệ thống."""
    for lesson in lessons:
        if lesson.lesson_code == lesson_code:
            return lesson
    return None

def main():
    """Hệ thống điều hướng Menu CLI quản lý LMS."""
    lessons = []
    current_lesson = None

    while True:
        print("\n===== RIKKEI ACADEMY LMS SIMULATOR PRO =====")
        print("1. Khởi tạo bài học mới (Chọn loại bài học nội dung)")
        print("2. Xem thông tin bài học & Kiểm tra thứ tự kế thừa (MRO)")
        print("3. Cập nhật thời lượng & Nội dung bài học (Tính đa hình)")
        print("4. Xem chi tiết điểm thưởng hoàn thành bài học")
        print("5. Kiểm tra gộp thời lượng & So sánh độ dài bài học (Overloading)")
        print("6. Đồng bộ bài giảng lên Nền tảng Đám mây (Duck Typing)")
        print("7. Thoát chương trình")
        print("============================================")
        
        choice = input("Chọn chức năng (1-7): ").strip()

        match choice:
            case "1":
                print("--- CHỌN LOẠI BÀI HỌC KHỞI TẠO ---")
                print("1. Video Lesson (Bài học Video Lý Thuyết)")
                print("2. Coding Challenge (Bài tập Thực Hành Code)")
                print("3. Hybrid Assessment (Bài Kiểm Tra Tổng Hợp)")
                lesson_type = input("Chọn loại bài học (1-3): ").strip()
                
                code = input("Nhập mã bài học 10 ký tự: ").strip().upper()
                if not BaseLesson.validate_lesson_code(code):
                    print("Mã bài học không hợp lệ! Phải gồm đúng 10 ký tự và bắt đầu bằng LMS.")
                    continue
                    
                title = input("Nhập tiêu đề bài học: ").strip()
                
                if lesson_type == "1":
                    new_lesson = VideoLesson(code, title)
                    type_name = "Video"
                elif lesson_type == "2":
                    new_lesson = CodingChallenge(code, title)
                    type_name = "Thực Hành Code"
                elif lesson_type == "3":
                    new_lesson = HybridAssessment(code, title)
                    type_name = "Kiểm Tra Hybrid"
                else:
                    print("Lựa chọn loại bài học không hợp lệ.")
                    continue

                lessons.append(new_lesson)
                current_lesson = new_lesson
                print(f"\nKhởi tạo bài học {type_name} thành công!")
                print(f"Tiêu đề bài học: {new_lesson.title}")

            case "2":
                if current_lesson is None:
                    print("Hệ thống chưa có thông tin bài học. Vui lòng khởi tạo trước.")
                    continue
                    
                print("--- THÔNG TIN BÀI HỌC HIỆN TẠI ---")
                print(f"Loại bài học: {current_lesson.__class__.__name__}")
                print(f"Nền tảng: {BaseLesson.platform_name}")
                print(f"Mã bài học: {current_lesson.lesson_code}")
                print(f"Tiêu đề bài học: {current_lesson.title}")
                print(f"Thời lượng bài học: {current_lesson.duration_minutes} phút")
                
                if isinstance(current_lesson, VideoLesson):
                    print(f"Chất lượng video: {current_lesson.video_quality}")
                if isinstance(current_lesson, CodingChallenge):
                    print(f"Số lượng testcase lập trình: {current_lesson.number_of_testcases} bài")
                    
                print("\n[Danh sách MRO của lớp hiện tại]:")
                for cls in current_lesson.__class__.__mro__:
                    print(f"- {cls.__name__}")

            case "3":
                if current_lesson is None:
                    print("Hệ thống chưa có thông tin bài học.")
                    continue
                    
                print("--- CẬP NHẬT NỘI DUNG & THỜI LƯỢNG ---")
                print("1. Giả lập học viên tăng lượt xem video (Chỉ dành cho Video/Hybrid)")
                print("2. Cập nhật thông số bài học (Thời lượng, testcase...)")
                action = input("Chọn tác vụ (1-2): ").strip()
                
                try:
                    if action == "1":
                        if isinstance(current_lesson, VideoLesson):
                            current_lesson.play_video()
                        else:
                            print("Lỗi: Bài học này không có chức năng xem video.")
                    elif action == "2":
                        if isinstance(current_lesson, CodingChallenge):
                            val = int(input("Nhập số lượng testcase kiểm thử mới bổ sung: "))
                            current_lesson.update_content({"testcases": val})
                        elif isinstance(current_lesson, VideoLesson):
                            val = int(input("Nhập thời lượng bài học (phút): "))
                            current_lesson.update_content({"duration": val})
                    else:
                        print("Lựa chọn tác vụ không hợp lệ.")
                except ValueError as e:
                    if "invalid literal" in str(e).lower():
                        print("Lỗi: Vui lòng nhập một số hợp lệ.")
                    else:
                        print(f"Lỗi: {e}")

            case "4":
                if current_lesson is None:
                    print("Hệ thống chưa có thông tin bài học.")
                    continue
                    
                print("--- CHI TIẾT ĐIỂM THƯỞNG HOÀN THÀNH ---")
                print(f"Bài học: {current_lesson.title} (Loại: {current_lesson.__class__.__name__})")
                print(f"Điểm cơ sở hệ thống: {BaseLesson.base_completion_points} XP")
                print(f"Thời lượng tích lũy: {current_lesson.duration_minutes} phút")
                if isinstance(current_lesson, CodingChallenge):
                    print(f"Số lượng testcase cấu hình: {current_lesson.number_of_testcases} bài")
                
                total_xp = current_lesson.calculate_completion_score()
                print(f"Tổng điểm kinh nghiệm (XP) nhận được khi hoàn thành: {total_xp} XP")

            case "5":
                if current_lesson is None:
                    print("Hệ thống chưa có thông tin bài học.")
                    continue
                    
                print("--- ĐỒNG BỘ & SO SÁNH THỜI LƯỢNG (OPERATOR OVERLOADING) ---")
                print(f"Bài học hiện tại (A): {current_lesson.title} (Thời lượng: {current_lesson.duration_minutes} phút)")
                target_code = input("Chọn mã bài học đối ứng (B) từ danh sách: ").strip().upper()
                target_lesson = get_lesson_by_code(lessons, target_code)
                
                if target_lesson:
                    print(f"Bài học đối ứng (B): {target_lesson.title} (Thời lượng: {target_lesson.duration_minutes} phút)")
                    try:
                        if current_lesson < target_lesson:
                            comp_res = "NGẮN HƠN"
                        elif target_lesson < current_lesson:
                            comp_res = "DÀI HƠN"
                        else:
                            comp_res = "BẰNG NHAU VỚI"
                        
                        print(f"[Kết quả So sánh (__lt__)]: Thời lượng bài học A {comp_res} thời lượng bài học B.")
                        
                        total_duration = current_lesson + target_lesson
                        print(f"[Kết quả Tổng hợp (__add__)]: Tổng thời lượng học tập của cả 2 bài học là: {total_duration} phút.")
                    except TypeError:
                        print("Lỗi: Không thể thực hiện tính toán do kiểu dữ liệu không tương thích.")
                else:
                    print("Không tìm thấy mã bài học đối ứng trong hệ thống.")

            case "6":
                if current_lesson is None:
                    print("Hệ thống chưa có thông tin bài học.")
                    continue
                    
                print("--- ĐỒNG BỘ BÀI GIẢNG LÊN NỀN TẢNG ĐÁM MÂY ---")
                print("1. Đồng bộ lên máy chủ AWS S3 Storage")
                print("2. Đồng bộ lên máy chủ Google Cloud Storage")
                print("3. Đồng bộ lên máy chủ Lỗi (Test Duck Typing)")
                cloud_choice = input("Chọn dịch vụ lưu trữ (1-3): ").strip()
                
                try:
                    if cloud_choice == "1":
                        service = AWSS3StorageService()
                    elif cloud_choice == "2":
                        service = GoogleCloudStorageService()
                    elif cloud_choice == "3":
                        class FakeCloud:
                            pass
                        service = FakeCloud()
                    else:
                        print("Lựa chọn không hợp lệ.")
                        continue
                        
                    sync_to_cloud(service, current_lesson)
                except Exception as e:
                    print(f"Lỗi hệ thống: {e}")

            case "7":
                print("Cảm ơn bạn đã trải nghiệm hệ thống Quản lý Bài học Rikkei Academy LMS Pro!")
                break

            case _:
                print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 7.")


if __name__ == "__main__":
    main()