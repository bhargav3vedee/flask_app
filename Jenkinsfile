pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup Environment') {
            steps {
                bat 'python -m venv venv'
                bat '.\\venv\\Scripts\\pip install --upgrade pip'
                bat '.\\venv\\Scripts\\pip install .'
            }
        }
        stage('Lint') {
            steps {
                bat '.\\venv\\Scripts\\pylint .\\'
            }
        }
        stage('Test') {
            steps {
                bat '.\\venv\\Scripts\\pytest --cov=. --cov-report=term-missing'
            }
        }
        stage('Build') {
            steps {
                bat '.\\venv\\Scripts\\python -m build'
            }
        }
        stage('Deploy') {
            steps {
                bat '.\\venv\\Scripts\\python -m flask run --host=0.0.0.0 --port=8000'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'dist\\*', fingerprint: true
        }
    }
}
