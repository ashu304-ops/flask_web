Mechanical Domain Chatbot: A DevOps-Driven flask Microservices Project

A Mechanical Domain Chatbot that answers mechanical engineering questions (e.g., “What is Young’s modulus?”) using a microservice architecture, orchestrated with modern DevOps tools. This project leverages Docker for containerization, Kubernetes for deployment, Jenkins for CI/CD automation, and GitHub for version control, showcasing a robust DevOps pipeline for building, testing, and deploying microservices.

Table of Contents

Project Overview
DevOps Tools Implemented
Microservice Architecture
Project Structure
Prerequisites
Setup Instructions
CI/CD Pipeline with Jenkins
Kubernetes Deployment
Testing the Application
Troubleshooting
Contributing
License

Project Overview
The Mechanical Domain Chatbot is a web-based application that processes queries about mechanical engineering concepts using natural language processing (NLP). Built with a microservice architecture (Flask, spaCy, React), it’s deployed using a DevOps pipeline that emphasizes automation, scalability, and reliability. The project integrates Docker for containerized environments, Kubernetes for orchestration, Jenkins for CI/CD, and GitHub for source control, making it a showcase of modern DevOps practices.
DevOps Tools Implemented
This project demonstrates a full DevOps lifecycle with the following tools:

GitHub: Hosts the source code, enabling version control and collaboration. Webhooks trigger Jenkins builds on code pushes.
Docker: Containerizes each microservice (api_gateway, user_service, nlp_service, dialogue_service, frontend) for consistent development, testing, and deployment environments.
Jenkins: Automates the CI/CD pipeline, handling code checkout, dependency installation, unit testing, Docker image building, and Kubernetes deployment.
Kubernetes: Orchestrates microservices as Deployments and Services, with a PersistentVolumeClaim (PVC) for SQLite database persistence. A NodePort Service exposes the frontend for external access.


Microservice Architecture
The chatbot comprises five microservices, each running in a Docker container and deployed on Kubernetes:

API Gateway (Port 5000):
Role: Routes user requests to appropriate services.
Tech: Flask, HTTP REST APIs.


User Service (Port 5001):
Role: Manages user data (ID, name, preferences).
Tech: Flask, SQLite (users.db).


NLP Service (Port 5002):
Role: Detects intents using spaCy’s en_core_web_sm model.
Tech: Flask, spaCy.


Dialogue Service (Port 5003):
Role: Generates responses from a knowledge base (mechanical_knowledge.json).
Tech: Flask, SQLite (conversations.db), FuzzyWuzzy.


Frontend (Port 8000, NodePort 30080):
Role: Provides a web-based chat interface.
Tech: React.



Project Structure
mechanical-chatbot/
├── data/
│   ├── users.db
│   └── conversations.db
├── kubernetes/
│   ├── manifests.yaml
├── images/
│   ├── architecture_illustration.png
│   ├── frontend_screenshot.png
│   ├── docker_setup.png
├── api_gateway/
│   ├── Dockerfile
│   ├── api_gateway.py
│   ├── requirements.txt
│   ├── Jenkinsfile
├── user_service/
│   ├── Dockerfile
│   ├── user_service.py
│   ├── requirements.txt
│   ├── Jenkinsfile
├── nlp_service/
│   ├── Dockerfile
│   ├── nlp_service.py
│   ├── requirements.txt
│   ├── en_core_web_sm/
│   ├── Jenkinsfile
├── dialogue_service/
│   ├── Dockerfile
│   ├── dialogue_service.py
│   ├── requirements.txt
│   ├── mechanical_knowledge.json
│   ├── Jenkinsfile
├── frontend/
│   ├── Dockerfile
│   ├── src/
│   ├── public/
│   ├── Jenkinsfile
├── docker-compose.yml
├── .gitignore
├── LICENSE
└── README.md

Prerequisites

Docker: For containerization.
Linux: sudo apt-get update && sudo apt-get install docker.io docker-compose
Windows/Mac: Docker Desktop


Kubernetes: Minikube for local testing or AWS EKS for production.
kubectl: Kubernetes CLI.
Jenkins: For CI/CD (preferably in Docker).
Git: For cloning the repository.
Docker Hub Account: For pushing images.
Python 3.9, Node.js: Optional for local development.

Setup Instructions

Clone the Repository:
git clone https://github.com/<your-username>/mechanical-chatbot.git
cd mechanical-chatbot


Create Data Directory:Ensure SQLite database permissions:
mkdir -p data
chmod 777 data
touch data/users.db
touch data/conversations.db
chmod 666 data/users.db
chmod 666 data/conversations.db


Set Up spaCy Model:Verify nlp_service/en_core_web_sm/:
ls -R nlp_service/en_core_web_sm

If missing:
python3 -m venv env
source env/bin/activate
pip install spacy==3.8.0
python -m spacy download en_core_web_sm
cp -r env/lib/python3.9/site-packages/en_core_web_sm nlp_service/
deactivate


Verify Configuration Files:

requirements.txt (per service):flask==2.3.2
flask-cors==4.0.1
spacy==3.8.0
fuzzywuzzy==0.18.0
python-Levenshtein==0.25.1


mechanical_knowledge.json (in dialogue_service):[
    {
        "question": "What is Young’s modulus?",
        "answer": "Young’s modulus (E) is a measure of a material’s stiffness, defined as the ratio of stress to strain in the linear elastic region. It’s given by E = σ/ε, where σ is stress and ε is strain.",
        "intents": ["material_query"]
    }
]





CI/CD Pipeline with Jenkins
The Jenkins CI/CD pipeline automates the DevOps workflow for each microservice:

Checkout: Clones the GitHub repository.
Build: Installs dependencies and verifies configurations (e.g., spaCy model).
Test: Runs unit tests for Flask services and React components.
Docker Build & Push: Builds Docker images and pushes to Docker Hub.
Deploy: Applies Kubernetes manifests for deployment.

Jenkins Setup

Run Jenkins in Docker:
docker run -d -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --name jenkins \
  jenkins/jenkins:lts

Access at http://localhost:8080.

Install Plugins:

Go to Manage Jenkins > Manage Plugins > Available.
Install: Docker Pipeline, Git, Pipeline, Kubernetes CLI.


Configure Docker and Kubernetes:

Add Docker cloud: unix:///var/run/docker.sock.
Add Kubernetes cloud: Set URL to Minikube (https://kubernetes.default) or EKS API server.


Add Credentials:

Docker Hub: ID dockerhub-credentials (username and access token).
Kubernetes: Service account token if required.


Create Multibranch Pipeline:

Name: mechanical-chatbot-pipeline.
Git URL: https://github.com/<your-username>/mechanical-chatbot.git.
Enable periodic scanning (e.g., every 5 minutes).


GitHub Webhook:

In GitHub: Settings > Webhooks > Add webhook.
Payload URL: http://<jenkins-host>:8080/github-webhook/.
Content type: application/json.
Events: “Just the push event.”



Jenkinsfile Example (nlp_service)
pipeline:
  agent:
    docker:
      image: python:3.9-slim
      args: -v $HOME/.cache:/root/.cache
  environment:
    DOCKERHUB_CREDENTIALS: credentials('dockerhub-credentials')
    DOCKER_IMAGE: yourusername/mechanical-chatbot-nlp:${BUILD_ID}
  stages:
    - stage: Checkout
      steps:
        - git:
            url: https://github.com/<your-username>/mechanical-chatbot.git
            branch: ${BRANCH_NAME}
        - sh: cd nlp_service
    - stage: Build
      steps:
        - sh: |
            pip install --no-cache-dir -r requirements.txt
            cp -r en_core_web_sm /usr/local/lib/python3.9/site-packages/
            python -c "import spacy; nlp = spacy.load('en_core_web_sm'); print('Model loaded successfully')"
    - stage: Test
      steps:
        - sh: python -m unittest discover tests
    - stage: Docker Build & Push
      when:
        branch: main
      steps:
        - script:
            sh: docker build -t ${DOCKER_IMAGE} -f Dockerfile .
            sh: echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
            sh: docker push ${DOCKER_IMAGE}
            sh: docker tag ${DOCKER_IMAGE} yourusername/mechanical-chatbot-nlp:latest
            sh: docker push yourusername/mechanical-chatbot-nlp:latest
    - stage: Deploy to Kubernetes
      when:
        branch: main
      steps:
        - sh: kubectl apply -f ../kubernetes/manifests.yaml
  post:
    always:
      - sh: kubectl delete -f ../kubernetes/manifests.yaml || true


Create similar Jenkinsfiles for other services, adjusting paths and agent images (e.g., node:18 for frontend).

Kubernetes Deployment
Kubernetes orchestrates the microservices as Deployments and Services, with a PersistentVolumeClaim (PVC) for SQLite databases.
Setup Kubernetes

Local (Minikube):
minikube start --driver=docker


Cloud (AWS EKS):
aws eks update-kubeconfig --name your-cluster-name --region your-region



Deploy to Kubernetes
kubectl apply -f kubernetes/manifests.yaml


Access Frontend:
Minikube: minikube service frontend --url (e.g., http://<minikube-ip>:30080).
EKS: Use node’s external IP (e.g., http://<node-ip>:30080).



Kubernetes Manifests
The kubernetes/manifests.yaml defines:

PVC: chatbot-data-pvc for users.db and conversations.db.
Deployments: One per microservice with resource limits.
Services: ClusterIP for internal services, NodePort (30080) for frontend.

Testing the Application

API Test:
curl -X POST -H "Content-Type: application/json" -d '{"user_id":"user1","message":"What is Young’s modulus?"}' http://<node-ip>:30080/chat

Expected:
{"response":"Young’s modulus (E) is a measure of a material’s stiffness, defined as the ratio of stress to strain in the linear elastic region. It’s given by E = σ/ε, where σ is stress and ε is strain."}


Frontend Test:

Open http://<node-ip>:30080.
Enter “What is Young’s modulus?” and verify the response.



Individual Services:

Requires kubectl port-forward for internal ClusterIP services:kubectl port-forward svc/nlp-service 5002:5002
curl -X POST -H "Content-Type: application/json" -d '{"message":"What is Young’s modulus?"}' http://localhost:5002/process





Troubleshooting

spaCy Error: OSError: [E050]:
Verify nlp_service/en_core_web_sm/.
Rebuild: docker build -t yourusername/mechanical-chatbot-nlp nlp_service.


Database Error: sqlite3.OperationalError:
Check PVC: kubectl get pvc.
Ensure data/ permissions: chmod 777 data.


Jenkins Issues:
Check logs: docker logs jenkins.
Clear Docker cache: docker builder prune.


Kubernetes Issues:
Check pods: kubectl describe pod <pod-name>.
Verify services: kubectl get services.



