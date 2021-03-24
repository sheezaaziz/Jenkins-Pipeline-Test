pipeline {
    agent { docker { image 'python:3.7.2'} }
    stages {
        stage('Set Up') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python -m venv venv'
                    sh '. venv/bin/activate'
                    sh 'pip install pytest --user'
                    sh 'pip install pytest-html --user'
                    sh 'pip install ansi2html --user'
                    sh 'pip list'
                }
            }
        }
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/sheezaaziz/Jenkins-Pipeline-Test.git']]])
            }
        }
        stage('Build') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    git branch: 'main', url: 'https://github.com/sheezaaziz/Jenkins-Pipeline-Test.git'
                    sh label: '', script: 'python -m pytest --html=report.html --self-contained-html'
                }
            }
        }
        stage('Close') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python -m deactivate'
                }
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'report.html'
        }
    }
}
