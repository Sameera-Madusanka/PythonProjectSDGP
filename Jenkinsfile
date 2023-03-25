pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Sameera-Madusanka/PythonProjectSDGP.git']])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/Sameera-Madusanka/PythonProjectSDGP.git'
                sh 'python3 test.py'
            }
        }

    }

}