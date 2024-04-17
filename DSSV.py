import pandas as pd

# Đọc dữ liệu từ tệp Excel
df = pd.read_excel(r'C:\Git\Test_2\DSSV.xlsx')

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
df.to_excel(r'C:\Git\Test_2\DSSV.xlsx', index=False)
print("Dữ liệu đã được ghi vào tệp Excel.")
