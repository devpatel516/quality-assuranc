pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat 'python --version'
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest -v'
            }
        }
    }

    post {
        always {
            echo 'Build completed.'
        }

        success {
            echo 'All tests passed.'
        }

        failure {
            echo 'Tests failed. Check the Jenkins console output.'
        }
    }
}