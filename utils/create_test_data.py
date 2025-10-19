# utils/create_test_data.py
import os
import csv
import xml.etree.ElementTree as ET
from openpyxl import Workbook

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

# ==============================
# 1. Generate Excel: login_data.xlsx (for SauceDemo login tests)
# ==============================
def create_login_excel():
    wb = Workbook()
    ws = wb.active
    ws.title = "LoginTests"

    ws.append(['TestCaseID', 'Username', 'Password', 'ExpectedResult'])

    test_cases = [
        ('TC001', 'standard_user', 'secret_sauce', 'Success'),
        ('TC002', 'locked_out_user', 'secret_sauce', 'Error'),
        ('TC003', 'problem_user', 'secret_sauce', 'Success'),
        ('TC004', 'performance_glitch_user', 'secret_sauce', 'Success'),
        ('TC005', 'invalid_user', 'wrong_pass', 'Error'),
        ('TC006', '', 'secret_sauce', 'Error'),
        ('TC007', 'standard_user', '', 'Error')
    ]

    for case in test_cases:
        ws.append(case)

    wb.save("data/login_data.xlsx")
    print("✅ Created: data/login_data.xlsx")


# ==============================
# 2. Generate CSV: login_data.csv (for SauceDemo login tests)
# ==============================
def create_login_csv():
    with open("data/login_data.csv", mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['TestCaseID', 'Username', 'Password', 'ExpectedResult'])

        test_cases = [
            ('TC101', 'standard_user', 'secret_sauce', 'Success'),
            ('TC102', 'locked_out_user', 'secret_sauce', 'Error'),
            ('TC103', 'problem_user', 'secret_sauce', 'Success'),
            ('TC104', '', 'secret_sauce', 'Error'),
            ('TC105', 'standard_user', '', 'Error')
        ]

        writer.writerows(test_cases)

    print("✅ Created: data/login_data.csv")


# ==============================
# 3. Generate Excel: name_data.xlsx (for Blogspot name field)
# ==============================
def create_name_excel():
    wb = Workbook()
    ws = wb.active
    ws.title = "NameTests"

    ws.append(['TestCaseID', 'Name', 'ExpectedResult'])

    test_cases = [
        ('TC001', 'John Doe', 'Valid'),
        ('TC002', '', 'Invalid'),
        ('TC003', 'Jane Smith', 'Valid'),
        ('TC004', 'Test123', 'Invalid'),
        ('TC005', 'Alice', 'Valid')
    ]

    for case in test_cases:
        ws.append(case)

    wb.save("data/name_data.xlsx")
    print("✅ Created: data/name_data.xlsx")


# ==============================
# 4. Generate CSV: email_data.csv (for Blogspot email field)
# ==============================
def create_email_csv():
    with open("data/email_data.csv", mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['TestCaseID', 'Email', 'ExpectedResult'])

        test_cases = [
            ('TC001', 'test@example.com', 'Valid'),
            ('TC002', 'invalid-email', 'Invalid'),
            ('TC003', 'user@domain.org', 'Valid'),
            ('TC004', '', 'Invalid'),
            ('TC005', 'admin@test.co.uk', 'Valid')
        ]

        writer.writerows(test_cases)

    print("✅ Created: data/email_data.csv")


# ==============================
# 5. Generate XML: phone_data.xml (for Blogspot phone field)
# ==============================
def create_phone_xml():
    root = ET.Element("TestData")
    phone_section = ET.SubElement(root, "PhoneTests")

    test_cases = [
        {'id': 'TC001', 'phone': '1234567890', 'expected': 'Valid'},
        {'id': 'TC002', 'phone': '123', 'expected': 'Invalid'},
        {'id': 'TC003', 'phone': '9876543210', 'expected': 'Valid'},
        {'id': 'TC004', 'phone': 'abc123', 'expected': 'Invalid'},
        {'id': 'TC005', 'phone': '+1-555-123-4567', 'expected': 'Valid'}
    ]

    for tc in test_cases:
        test_case = ET.SubElement(phone_section, "TestCase")
        test_case.set("testCaseID", tc['id'])
        phone = ET.SubElement(test_case, "Phone")
        phone.text = tc['phone'] if tc['phone'] else ""
        expected = ET.SubElement(test_case, "ExpectedResult")
        expected.text = tc['expected'] if tc['expected'] else ""

    tree = ET.ElementTree(root)
    with open("data/phone_data.xml", "wb") as f:
        f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        tree.write(f, encoding='utf-8')

    print("✅ Created: data/phone_data.xml")


# ==============================
# Main Execution
# ==============================
if __name__ == "__main__":
    print("🔧 Generating test data files...\n")
    create_login_excel()
    create_login_csv()          # ← NEW: CSV for login
    create_name_excel()
    create_email_csv()
    create_phone_xml()
    print("\n🎉 All test data files created successfully in 'data/' folder!")