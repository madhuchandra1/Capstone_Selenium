# run_all_tests.py
import subprocess
import sys
import os

if __name__ == "__main__":
    reports_dir = "reports"
    allure_results = os.path.join(reports_dir, "allure-results")

    # Create reports directory
    os.makedirs(allure_results, exist_ok=True)

    print(" Running tests with HTML + Allure reporting...")

    # Run pytest with BOTH HTML and Allure
    result = subprocess.run([
        sys.executable, "-m", "pytest",
        "tests/",
        "-v",
        "-s",
        f"--html={reports_dir}/report.html",
        "--self-contained-html",
        f"--alluredir={allure_results}"
    ])

    if result.returncode == 0:
        print(" All tests passed!")
    else:
        print(f" {result.returncode} test(s) failed!")

    print(" Reports generated:")
    print(f"   HTML: {reports_dir}/report.html")
    print(f"   Allure: {allure_results}/")