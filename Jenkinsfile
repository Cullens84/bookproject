pipeline {
    agent any

    stages {
        stage ('build') {
            steps{
                sh 'docker-compose -f /var/lib/jenkins/workspace/book/docker-compose.yml up --build -d'
                echo 'Build Stage Completed'
            }
        }

        stage ('test') {
            steps{
                echo 'Test stage executed.'
                
            }
        }

        stage ('deploy') {
            steps{
                echo 'Deploy stage executed.'

            }
        }
    }
}