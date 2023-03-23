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
                sh 'sudo pip3 install -r requirements.txt'
            }
        }
        
        stage('Build') {
            steps {
                sh 'screen -m -d python3 app.py build'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
