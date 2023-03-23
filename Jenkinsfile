pipeline {
  agent any
  stages {
    stage('Initialize') {
      steps {
        sh '''sudo yum update -y
sudo yum install git -y
git clone https://github.com/amar-m-cloud/Abalone-Age-Prediction.git
cd Abalone-Age-Prediction
sudo amazon-linux-extras install nginx1 -y
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl status nginx
sudo cp -rf nginx.conf /etc/nginx/
sudo systemctl restart nginx
pip3 install -r requirements.txt
screen -m -d python3 app.py'''
      }
    }

  }
}