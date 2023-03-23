pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        
        stage('Build') {
            steps {
                sh 'python3 app.py build'
            }
        }
        
        stage('Test') {
            steps {
                sh 'python3 app.py test'
            }
        }
        
        stage('Package') {
            steps {
                sh 'python3 app.py sdist bdist_wheel'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
