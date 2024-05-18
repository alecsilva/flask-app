pipeline {
    agent any

pipeline {
    agent any

    environment {
        PROJECT_ID = 'flask-app-4cb7e'
        SERVICE_NAME = 'flask-fire'
        REGION = 'us-east1'
        GOOGLE_APPLICATION_CREDENTIALS = credentials('991b2ea2-3a9f-432a-ba09-5e301ac5423b')
    }

    stages {
        stage('Deploy to Cloud Run') {
            steps {
                script {
                    // Configurar la autenticación con Google Cloud
                    sh 'gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS'

                    // Configurar el proyecto de Google Cloud
                    sh 'gcloud config set project $PROJECT_ID'

                    // Construir y desplegar la aplicación en Cloud Run
                    sh '''
                    gcloud run deploy $SERVICE_NAME \
                        --source . \
                        --region $REGION \
                        --platform managed \
                        --allow-unauthenticated
                    '''
                }
            }
        }
    }
}


    stages {
        stage('Deploy to Cloud Run') {
            steps {
                script {
                    // Configurar la autenticación con Google Cloud
                    sh 'gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS'

                    // Configurar el proyecto de Google Cloud
                    sh 'gcloud config set project $PROJECT_ID'

                    // Construir y desplegar la aplicación en Cloud Run
                    sh '''
                    gcloud run deploy $SERVICE_NAME \
                        --source . \
                        --region $REGION \
                        --platform managed \
                        --allow-unauthenticated
                    '''
                }
            }
        }
    }
}
