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

                        // Construir la imagen de la aplicación
                        sh 'gcloud builds submit --tag gcr.io/$PROJECT_ID/$SERVICE_NAME'
                    }
                }
            }
        }

        stage('Deploy to Cloud Run') {
            steps {
                script {
                    // Cambiar al directorio 'server'
                    dir('server') {
                        // Desplegar la imagen en Cloud Run
                        sh '''
                        gcloud run deploy $SERVICE_NAME \
                            --image gcr.io/$PROJECT_ID/$SERVICE_NAME \
                            --region $REGION \
                            --platform managed \
                            --allow-unauthenticated
                        '''
                    }
                }
            }
        }

        stage('Deploy to Firebase') {
            steps {
                script {
                    // Desplegar a Firebase
                    sh '''
                    env.GOOGLE_APPLICATION_CREDENTIALS = GOOGLE_APPLICATION_CREDENTIALS
                    firebase deploy --only hosting
                    '''
                }
            }
        }
    }
}