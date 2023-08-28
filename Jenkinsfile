pipeline {
    agent any
    stages{
        stage("Clone Code"){
            steps{
                git url: "https://github.com/hiijitesh/Result_Scrapper.git", branch: "main"
            }
        }
        stage("Build and Test"){
            steps{
                date=$(date +%Y.%m.%d)
                sh "docker build . -t result-bot:$date"
            }
        }
        stage("Push to Docker Hub"){
            steps{
                date=$(date +%Y.%m.%d)
                withCredentials([usernamePassword(credentialsId:"dockerHub",passwordVariable:"dockerHubPass",usernameVariable:"dockerHubUser")]){
                sh "docker tag note-app-test-new ${env.dockerHubUser}/result-bot:$date"
                sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                sh "docker push ${env.dockerHubUser}/result-bot:$date"
                }
            }
        }
        stage("Deploy"){
            steps{
                sh "docker-compose down && docker-compose up -d"
            }
        }
    }
}
