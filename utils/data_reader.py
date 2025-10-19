# utils/data_reader.py
import os
import openpyxl
import csv
import xml.etree.ElementTree as ET


def read_excel(file_path, sheet_name):
    """Read test data from Excel file"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Excel file not found: {os.path.abspath(file_path)}")

    wb = openpyxl.load_workbook(file_path)
    sheet = wb[sheet_name]
    data = []

    # Read headers (skip empty columns)
    headers = [cell.value for cell in sheet[1] if cell.value is not None]

    # Read data rows
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if row and row[0] is not None:  # Skip empty rows
            # Convert None to empty string and align with headers
            row_clean = []
            for i, cell in enumerate(row):
                if i < len(headers):
                    row_clean.append("" if cell is None else str(cell))
                else:
                    break
            # Pad row if shorter than headers
            while len(row_clean) < len(headers):
                row_clean.append("")
            data.append(dict(zip(headers, row_clean)))

    wb.close()
    return data


def read_csv(file_path):
    """Read test data from CSV file"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found: {os.path.abspath(file_path)}")

    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert None-like values to empty strings
            clean_row = {k: (v if v is not None else "") for k, v in row.items()}
            data.append(clean_row)
    return data


def read_xml(file_path):
    """Read test data from XML file (compatible with create_test_data.py)"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"XML file not found: {os.path.abspath(file_path)}")

    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []

    # Handle structure from create_test_data.py: <PhoneTests><TestCase testCaseID="..."><Phone>...</Phone><ExpectedResult>...</ExpectedResult></TestCase>
    for item in root.findall(".//TestCase"):
        test_id = item.get('testCaseID') or item.get('id', '')
        phone_elem = item.find('Phone')
        expected_elem = item.find('ExpectedResult')

        data.append({
            'TestCaseID': test_id,
            'Value': phone_elem.text if phone_elem is not None and phone_elem.text else '',
            'ExpectedResult': expected_elem.text if expected_elem is not None and expected_elem.text else ''
        })
    return data