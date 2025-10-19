# fix_excel.py
import os
from openpyxl import Workbook

os.makedirs("data", exist_ok=True)

wb = Workbook()
ws = wb.active
ws.title = "LoginTests"
ws.append(["TestCaseID", "Username", "Password", "ExpectedResult"])
ws.append(["TC001", "standard_user", "secret_sauce", "Success"])
ws.append(["TC002", "locked_out_user", "secret_sauce", "Error"])

wb.save("data/login_data.xlsx")
print("✅ Fixed: data/login_data.xlsx is now a valid Excel file.")