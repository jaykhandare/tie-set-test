pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                cd "workspace/test"
                sh pwd
                sh "sample_run.sh"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}

