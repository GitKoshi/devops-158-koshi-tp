pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/GitKoshi/devops-158-koshi-tp'
            }
        }

        stage('Pull latest code') {
            steps {
                dir('/home/koshi/devops-158-koshi-tp') {
                    git branch: 'main', url: 'https://github.com/GitKoshi/devops-158-koshi-tp'
                }
            }
        }

        stage('Install dependencies') {
            steps {
                dir('/home/koshi/devops-158-koshi-tp') {
                    sh '''
                        . venv/bin/activate
                        pip install flask
                    '''
                }
            }
        }

        stage('Restart Flask app') {
            steps {
                script {
                    sh 'pkill -f "python app.py" || true'
                    sh '''
                        export JENKINS_NODE_COOKIE=dontKillMe
                        cd /home/koshi/devops-158-koshi-tp
                        . venv/bin/activate
                        nohup python app.py > flask.log 2>&1 &
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Déploiement automatique réussi ! BRAVO DAMN'
        }
        failure {
            echo 'Échec du pipeline. - AIE AIE AIE CA PUE'
        }
    }
}
