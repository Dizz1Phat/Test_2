import pandas as pd
from collections import namedtuple

def read_student_data():
    # Đọc dữ liệu từ tệp Excel
    df = pd.read_excel("C:\Git\Test_2\DSSV.xlsx")

    # Tìm các hàng bị trùng lặp dựa trên cột 'Mã sinh viên'
    duplicate_rows = df[df.duplicated(subset=['Mã SV'], keep='first')]

    # Kiểm tra xem có hàng bị trùng lặp không
    if not duplicate_rows.empty:
        print("Lỗi: Có mã sinh viên bị trùng. Thông tin sinh viên này sẽ bị xóa.")
        # Loại bỏ các hàng bị trùng lặp
        print("Sinh vien bi trung lap")
        print(duplicate_rows)
        df = df.drop_duplicates(subset=['Mã SV'], keep='first')
    else:
        print("Không có mã sinh viên nào bị trùng lặp.")

    # Ghi dữ liệu đã chỉnh sửa vào tệp Excel
    df.to_excel("C:\Git\Test_2\DSSV.xlsx", index=False)
    print("Dữ liệu đã được ghi vào tệp Excel.")

    # Định nghĩa cấu trúc dữ liệu cho một sinh viên
    students = []
    Student = namedtuple('Student', ['Stt', 'Mã_SV', 'Họ_lót', 'Tên', 'Mã_lớp', 'Điểm'])

    # Chuyển đổi dữ liệu thành danh sách liên kết đơn
    for index, row in df.iterrows():
        student = Student(row['Stt'], row['Mã SV'], row['Họ lót'], row['Tên'], row['Mã lớp'], row['Điểm'])
        students.append(students)

    return students

def choose_storage_method():
    while True:
        print("Chọn cách thức lưu trữ danh sách sinh viên:")
        print("1. Mảng (list)")
        print("2. Danh sách liên kết đơn")
        print("3. Danh sách liên kết vòng")
        print("4. Danh sách liên kết kép")
        choice = input("Nhập lựa chọn của bạn (1-4): ")
        if choice in ['1', '2', '3', '4']:
            return int(choice)
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

def get_search_criteria():
    criteria = input("Nhập tiêu chí tìm kiếm (Mã_SV, Họ_lót, Tên, Mã_lớp, Điểm): ")
    keyword = input("Nhập từ khóa tìm kiếm: ")
    return criteria, keyword

def search_students(students, criteria, keyword):
    search_results = []
    for student in students:
        if getattr(student, criteria.lower(), None) and keyword.lower() in getattr(student, criteria.lower()).lower():
            search_results.append(student)
    return search_results

def main ():
    students = read_student_data()
    storage_method = choose_storage_method()

    if storage_method == 1:
        print("Danh sách sinh viên được lưu trong mảng (list):")
        from Mang import mang
    elif storage_method == 2:
        print("Danh sách sinh viên được lưu trong danh sách liên kết đơn:")
        from DSLK_don import dslk_don
        students_dslk_don = dslk_don()
        for student in students:
            students_dslk_don.append(student)
        criteria, keyword = get_search_criteria()
        search_results = students_dslk_don.search_students(criteria, keyword)
    elif storage_method == 3:
        print("Danh sách sinh viên được lưu trong danh sách liên kết vòng:")
        from DSLK_vong import dslk_vong
        students_dslk_vong = dslk_vong()
        criteria, keyword = get_search_criteria()
        search_results = students_dslk_don.search_students(criteria, keyword)
    elif storage_method == 4:
        print("Danh sách sinh viên được lưu trong danh sách liên kết kép:")
        from DSLK_kep import dslk_kep
        students_dslk_kep = dslk_kep()
        criteria, keyword = get_search_criteria()
        search_results = students_dslk_don.search_students(criteria, keyword)

    # Tìm kiếm sinh viên và in kết quả
    if search_results:
        print("Kết quả tìm kiếm:")
        for student in search_results:
            print(student)
    else:
        print("Không tìm thấy sinh viên nào phù hợp.")


if __name__ == "__main__":
    main()
