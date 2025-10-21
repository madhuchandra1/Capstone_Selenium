pipeline {
    agent any

    environment {
        REPORTS_DIR = 'reports'
        ALLURE_RESULTS = 'reports/allure-results'
        HTML_REPORT = 'reports/report.html'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests & Generate Reports') {
            steps {
                bat """
                    python -m pytest tests/ ^
                        --html=%HTML_REPORT% ^
                        --self-contained-html ^
                        --alluredir=%ALLURE_RESULTS% ^
                        -v -s
                """
            }
        }
    }

    post {
        always {
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: "${REPORTS_DIR}",
                reportFiles: 'report.html',
                reportName: 'HTML Report'
            ])

            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: "${ALLURE_RESULTS}"]]
            ])
        }
    }
}