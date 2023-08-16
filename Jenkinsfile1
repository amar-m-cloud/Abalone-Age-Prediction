pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                sh 'sudo pip3 install -r requirements.txt'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'sudo screen -m -d python3 app.py build'
            }
        }
    }   
}
