pipeline {

  agent any

  stages {

    stage("checkout") {
            steps {
              checkout scm
            }
        }

    stage("build") {
      steps {
        sh 'python3 app.py &'
      }
    }

    stage("test") {
      steps {
        sh 'curl -X POST -H "Content-Type: application/json" -d \'{"a": 7, "b": 3}\' http://0.0.0.0:5000/plus'
        sh 'curl -X POST -H "Content-Type: application/json" -d \'{"a": 7, "b": 3}\' http://0.0.0.0:5000/minus'
        sh 'curl -X POST -H "Content-Type: application/json" -d \'{"a": 7, "b": 3}\' http://0.0.0.0:5000/multiply'
        sh 'curl -X POST -H "Content-Type: application/json" -d \'{"a": 7, "b": 3}\' http://0.0.0.0:5000/divide'
      }
    }

    stage("deploy") {
      steps {
        echo 'Deploying the application...'
      }
    }
  }
}
