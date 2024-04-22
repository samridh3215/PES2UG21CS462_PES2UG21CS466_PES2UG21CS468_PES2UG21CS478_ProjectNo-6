## Guidelines

- A microservice should be appeneded with "Microservice" 
- It should be created in the root directory of project and is independent of other modules 

## Steps to start 
- Make sure minikube and kubectl are installed
- Run the following commands to deploy pods

kubectl create deployment auth --image=samridh3215/auth-ms:0.2
kubectl create deployment item --image=samridh3215/microservices:item
kubectl create deployment order --image=samridh3215/order-ms:0.3

> You can also mention different images
- Run the following commands to expose these deployments

kubectl expose deployment auth --type=NodePort --port=6000
kubectl expose deployment item --type=NodePort --port=8000
kubectl expose deployment order --type=NodePort --port=3000


## Running jenkins
- Recommended to run it on a comtainer that has access to same network as minikube is running on
- Install jenkins
- Use ngrok to start port forwarding, by default need to forward port 8080
- Ensure docker commands can be run without sudo

## Steps to develop
- Create a python virtual env and name it "env" python3 -m venv env
- Activate the env source env/bin/activate
- Install dependencies pip install -r requirements.txt
- Start microservice project django-admin startproject <Service>Microservice

Refer Django Docs to get started

## Steps to create docker images and run docker containers
- Go inside the microservice dir where the dockerfile for that MS is present
- To create image -> docker build -t <TAG_FOR_IMAGE> .
- To run a container -> docker run -it -p <PORT>:<PORT> <TAG_FOR_IMAGE>
