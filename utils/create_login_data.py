# utils/create_login_data.py
import os
from openpyxl import Workbook

def create_login_excel():
    # Create 'data' folder if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Create a new workbook and select active sheet
    wb = Workbook()

    ws = wb.active
    ws.title = "LoginTests"

    # Write headers
    ws.append(["TestCaseID", "Username", "Password", "ExpectedResult"])

    # Add test cases (for https://www.saucedemo.com/)
    test_cases = [
        ("TC001", "standard_user", "secret_sauce", "Success"),
        ("TC002", "locked_out_user", "secret_sauce", "Error"),
        ("TC003", "problem_user", "secret_sauce", "Success"),
        ("TC004", "performance_glitch_user", "secret_sauce", "Success"),
                           # Both empty
    ]

    # Write test cases to Excel
    for case in test_cases:
        ws.append(case)

    # Save the file
    file_path = "data/login_data.xlsx"
    wb.save(file_path)
    print(f"✅ Excel test data created successfully at: {os.path.abspath(file_path)}")

if __name__ == "__main__":
    create_login_excel()