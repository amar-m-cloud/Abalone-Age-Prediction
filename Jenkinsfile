pipeline{ 
  agent any 
  stages{ 
    stage{ 
	     steps{ 
	      git branch: 'main', url: 'https://github.com/amar-m-cloud/Abalone-Age-Prediction.git' 
	     } 
	   } 
	stage{ 
    steps{ 
	    echo "Testing" 
	  } 
  } 
  stage{ 
    steps{ 
      script{ 
		  sh "docker build --no-cache -t abp ." 
		  } 
    } 
  } 
  stage{ 
    steps{ 
      script{ 
	      sh "docker run -p 80:80 -d abp" 
	  	} 
    } 
  } 
 } 
} 
