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
                sh 'python -m venv venv'   // use sh if Linux
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install .'
            }
        }
        stage('Lint') {
            steps {
                sh './venv/bin/flake8 app/'
            }
        }
        stage('Test') {
            steps {
                sh './venv/bin/pytest --cov=app --cov-report=xml'
            }
        }
        stage('Build') {
            steps {
                sh './venv/bin/python -m build'
            }
        }
        stage('Deploy') {
            steps {
                sh './venv/bin/python -m flask run --host=0.0.0.0 --port=8000'
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