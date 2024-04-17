import pandas as pd
f1 =pd.read_excel(r'C:\Git\Test_2\DSSV_Test.xlsx')

duplicate_rows = pd.read_excel(r'C:\Git\Test_2\DSSV_Test.xlsx')

duplicate_rows = f1[f1.duplicated(['Mã sinh viên'])]

if not duplicate_rows.empty:
    print("Lỗi: Có mã sinh viên bị trùng lặp.")
    print(duplicate_rows)
else:
    print("Không có mã sinh viên nào bị trùng lặp.")
print (f1)