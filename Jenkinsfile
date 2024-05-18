pipeline {
    agent any

    environment {
        PROJECT_ID = 'flask-app-4cb7e'
        CLOUDSDK_CORE_PROJECT = 'flask-app-4cb7e'
        SERVICE_NAME = 'flask-fire'
        REGION = 'us-east1'
        GOOGLE_APPLICATION_CREDENTIALS = credentials('gcloud-creds')
    }

    stages {
        stage('Build') {
            steps {
                script {
                    // Cambiar al directorio 'server'
                    dir('server') {
                        // Configurar la autenticación con Google Cloud
                        sh 'gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS'

                        // Configurar el proyecto de Google Cloud
                        sh 'gcloud config set project $PROJECT_ID'

                    }
                }
            }
        }


        stage('Deploy to Firebase') {
            steps {
                script {
                    // Desplegar a Firebase
                    sh '''
                    firebase deploy --only hosting --token=$GOOGLE_APPLICATION_CREDENTIALS
                    '''
                }
            }
        }
    }
}