pipeline {
    agent any

    stages {
        stage('Verify Docker Accessibility') {
            steps {
                echo "Current Branch: ${env.BRANCH_NAME}"
                bat 'docker --version'
            }
        }

        stage('Build Cipher Image') {
            steps {
                echo "Building the Caesar Cipher Docker executor..."
                bat "docker build -t caesar-cipher:latest ."
            }
        }

        stage('Encryption Stage') {
            steps {
                echo "Original Text: DevOps with Jenkins, Docker Desktop, and WSL!"
                echo "Encrypting..."
                script {
                    def output = bat(
                        script: "docker run --rm caesar-cipher:latest encrypt \"DevOps with Jenkins, Docker Desktop, and WSL!\" 7", 
                        returnStdout: true
                    ).trim()
                    def lines = output.split(/\r?\n/)
                    env.ENCRYPTED_TEXT = lines[-1]
                }
                echo "Encrypted Output: ${env.ENCRYPTED_TEXT}"
            }
        }

        stage('Decryption Stage') {
            steps {
                echo "Passing Encrypted Text to Decryption Stage..."
                script {
                    def output = bat(
                        script: "docker run --rm caesar-cipher:latest decrypt \"${env.ENCRYPTED_TEXT}\" 7", 
                        returnStdout: true
                    ).trim()
                    def lines = output.split(/\r?\n/)
                    def decrypted_text = lines[-1]
                    echo "Decrypted Output: ${decrypted_text}"
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up local Docker images..."
            bat "docker rmi caesar-cipher:latest --force"
        }
    }
}