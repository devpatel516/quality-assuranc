```groovy
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat '"C:\\Users\\Dev\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" --version'
                bat '"C:\\Users\\Dev\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\Dev\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\Dev\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest -v
'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All tests passed!'
        }

        failure {
            echo 'FAILURE: Check the console output for errors.'
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}
```