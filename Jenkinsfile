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
                bat '.\\venv\\Scripts\\pytest'
            }
        }
        stage('Build') {
            steps {
                bat '.\\venv\\Scripts\\python -m build'
            }
        }
        stage('Deploy and Test') {
            steps {
                bat '.\\venv\\Scripts\\python main.py'
                bat 'curl http://localhost:8000/health || exit 1'
                bat 'for /F %p in (flask.pid) do taskkill /F /PID %p'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'dist\\*', fingerprint: true
        }
    }
}
