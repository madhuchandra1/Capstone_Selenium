# run_all_tests.py
import subprocess
import sys
import os

if __name__ == "__main__":
    # Create reports directory if not exists
    reports_dir = "reports"
    allure_results_dir = os.path.join(reports_dir, "allure-results")
    allure_report_dir = os.path.join(reports_dir, "allure-report")

    os.makedirs(allure_results_dir, exist_ok=True)

    print("🚀 Running all tests with Allure + HTML report generation...\n")

    # Run pytest with both Allure and HTML reporting
    result = subprocess.run([
        sys.executable, "-m", "pytest",
        "tests/",
        "-v",
        "-s",
        f"--alluredir={allure_results_dir}",              # Allure results
        f"--html={reports_dir}/report.html",              # HTML report
        "--self-contained-html"                           # Single-file HTML report
    ])

    # Check result
    if result.returncode == 0:
        print("\n✅ All tests passed successfully!")
    else:
        print(f"\n❌ Some tests failed! (Exit code: {result.returncode})")

    # Generate Allure Report
    print("\n📊 Generating Allure report...")
    subprocess.run([
        "allure", "generate", allure_results_dir,
        "--clean", "-o", allure_report_dir
    ])

    print(f"✅ Allure Report generated at: {allure_report_dir}")
    print(f"✅ HTML Report generated at: {reports_dir}/report.html")

    # Optional: Auto-open Allure report in browser
    # subprocess.run(["allure", "open", allure_report_dir])
