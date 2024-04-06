## Guidelines

- A microservice should be appeneded with "Microservice" 
- It should be created in the root directory of project and is independent of other modules 

## Steps to set up
- Create a python virtual env and name it "env" `python3 -m venv env`
- Activate the env `source env/bin/activate`
- Install dependencies `pip install -r requirements.txt`
- Start microservice project `django-admin startproject <Service>Microservice`

Refer Django Docs to get started

## Steps to create docker images and run docker containers
- Go inside the microservice dir where the dockerfile for that MS is present
- To create image -> docker build -t <TAG_FOR_IMAGE> .
- To run a container -> docker run -it -p <PORT>:<PORT> <TAG_FOR_IMAGE>


