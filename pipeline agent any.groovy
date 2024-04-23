pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
                sh 'kubectl get svc'
            }
        }
	stage('Update docker images') {
            steps {

                echo "COMMENTED"
                // sh 'rm -rf PES2UG21CS462_PES2UG21CS466_PES2UG21CS468_PES2UG21CS478_ProjectNo-6'
                // sh 'git clone https://github.com/samridh3215/PES2UG21CS462_PES2UG21CS466_PES2UG21CS468_PES2UG21CS478_ProjectNo-6'
                // sh 'ls'
                // dir('PES2UG21CS462_PES2UG21CS466_PES2UG21CS468_PES2UG21CS478_ProjectNo-6'){
                // 	dir('AuthenticationMicroservice'){
                // 		sh 'docker build -t samridh3215/auth-ms:0.2 .'
                // 	}
                // 	dir('Item_ManagementMicroservice'){
                // 		sh 'docker build -t samridh3215/microservices:item .'
                // 	}
                // 	dir('Order_ManagementMicroservice'){
                // 		sh 'docker build -t samridh3215/order-ms:0.3 .'
                // 	}
                // }
            }
        }
        stage('Push docker images') {
            steps {
                echo "COMMENTED"
                // dir('PES2UG21CS462_PES2UG21CS466_PES2UG21CS468_PES2UG21CS478_ProjectNo-6'){
                // 	dir('AuthenticationMicroservice'){
                // 		sh 'docker push samridh3215/auth-ms:0.2'
                // 	}
                // 	dir('Item_ManagementMicroservice'){
                // 		sh 'docker push samridh3215/microservices:item'
                // 	}
                // 	dir('Order_ManagementMicroservice'){
                // 		sh 'docker push samridh3215/order-ms:0.3'
                // 	}
                // }
            }
        }
        stage("Create kubernetes deployments and services"){
        steps{
       		sh 'kubectl delete deployments --all'
            sh 'kubectl delete svc --all'
            sh 'kubectl create deployment auth --image=samridh3215/auth-ms:0.2'
            sh 'kubectl create deployment order --image=samridh3215/order-ms:0.3'
            sh 'kubectl create deployment item --image=samridh3215/microservices:item'
            sh 'kubectl expose deployment auth --type=NodePort --port=6000'
            sh 'kubectl expose deployment item --type=NodePort --port=8000'
            sh 'kubectl expose deployment order --type=NodePort --port=3000'

        }
        }
    }
}

