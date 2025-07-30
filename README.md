<img width="1536" height="1024" alt="file_00000000bb5061f783e74d0fb614ec32 (1)" src="https://github.com/user-attachments/assets/825634d2-8940-463d-804b-6fc76a67c8e2" />



---


```markdown
# 🤖 Mechanical Domain Chatbot

Welcome to the Mechanical Domain Chatbot — a Flask-based application that answers basic mechanical engineering questions. This project is containerized with Docker, automated with Jenkins, and deployed using Kubernetes.

---

##  What This Project Does

This chatbot helps answer common mechanical engineering questions, like:

> "What is Bernoulli's principle?"  
> "Explain Carnot cycle."  
> "What is the difference between stress and strain?"

It’s a simple web interface backed by Python logic, fully automated and cloud-ready.

---

## 📁 Project Structure

```

mechanical-chatbot/
├── app.py               # Main Flask server
├── chatbot.py           # Core mechanical domain logic
├── templates/
│   └── index.html       # Chat interface (HTML)
├── styles/
│   └── style.css        # Chat styling
├── Dockerfile           # Docker image instructions
├── Jenkinsfile          # CI/CD automation script
└── k8s/
├── deployment.yaml  # K8s deployment config
└── service.yaml     # K8s service (exposes app)

```

---

##  How It Works – Step by Step

### 1. User Opens the Web Interface

The user visits a web page with a simple chat window. This is rendered by `index.html`, styled with `style.css`.

### 2. Flask Handles User Input

`app.py` receives the question, sends it to `chatbot.py`, and returns a response.

### 3. Bot Replies

`chatbot.py` uses keyword-based logic to answer questions from the mechanical domain.

---

##  Docker Support – Why?

Docker allows the app to run consistently on any machine by packaging everything it needs.

- ✅ No setup struggles
- ✅ Runs the same on dev, test, or production machines

---

## Jenkins – What It Automates

The `Jenkinsfile` defines a pipeline that:

1. Pulls the latest code
2. Builds a Docker image
3. Pushes it to DockerHub (or any registry)
4. Deploys it to Kubernetes using `kubectl`

This means every time you push code to GitHub, Jenkins can do all the heavy lifting.

---

##  Kubernetes – What It Manages

Kubernetes ensures:

- The app runs on a container cluster
- It scales when needed
- It auto-restarts if a pod fails

YAML files (`deployment.yaml`, `service.yaml`) define how Kubernetes runs the app.

---

## How To Test It Locally (Overview)

1. Run the chatbot using Flask (Python).
2. Or, use Docker to run it in a container.
3. Optionally, set up Jenkins to automate the pipeline.
4. Deploy to Kubernetes cluster (like Minikube or GKE).

---

## 🖼️ Visual Overview (Architecture)

```

\[ User ] → \[ Web Interface (index.html) ]
↓
\[ Flask App (app.py) ]
↓
\[ Chatbot Logic (chatbot.py) ]
↓
\[ Docker Container ]
↓
\[ Jenkins Pipeline ]
↓
\[ Kubernetes Cluster ]

---

## 📦 Requirements

- Python 3.8+
- Flask
- Docker
- Jenkins (for CI/CD)
- Kubernetes CLI (`kubectl`) and a cluster (Minikube or GKE)

---

`
