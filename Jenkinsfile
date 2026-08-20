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
                bat 'python -m venv venv'   // use bat if Linux
                bat './venv/bin/pip install --upgrade pip'
                bat './venv/bin/pip install .'
            }
        }
        stage('Lint') {
            steps {
                bat './venv/bin/flake8 app/'
            }
        }
        stage('Test') {
            steps {
                bat './venv/bin/pytest --cov=app --cov-report=xml'
            }
        }
        stage('Build') {
            steps {
                bat './venv/bin/python -m build'
            }
        }
        stage('Deploy') {
            steps {
                bat './venv/bin/python -m flask run --host=0.0.0.0 --port=8000'
            }
        }
    }
    post {
        always {
            junit 'tests/results.xml'
            archiveArtifacts artifacts: 'dist/*', fingerprint: true
        }
    }
}