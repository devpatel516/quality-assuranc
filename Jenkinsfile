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
        }
    }

    stage('Show Project Files') {
        steps {
            bat 'dir'
        }
    }

    stage('Install Dependencies') {
        steps {
            bat '"C:\\Users\\Dev\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
        }
    }

    stage('Run Tests') {
        steps {
            bat '"C:\\Users\\Dev\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest -v test_bubble_sort.py'
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