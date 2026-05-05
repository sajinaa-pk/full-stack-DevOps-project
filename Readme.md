# 🚀 DevOps Dummy Project

A full-stack microservices application built to learn and demonstrate DevOps practices.

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vue.js&logoColor=4FC08D)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)

---

## 📌 Project Overview

A full-stack Todo application built with microservices architecture to demonstrate real-world DevOps practices including containerisation, orchestration, and automated deployment pipelines.
Developer pushes code
↓
GitHub Actions triggers automatically
↓
Docker images built
↓
Deployed to server
↓
App live! 🎉

---

## 🏗 Architecture
┌─────────────────────────────────────┐
│           USER BROWSER              │
│         localhost:3000              │
└──────────────┬──────────────────────┘
│
▼
┌─────────────────────────────────────┐
│         FRONTEND SERVICE            │
│      Vue.js 3 + Nginx + Docker      │
│           port: 3000                │
└──────────────┬──────────────────────┘
│ HTTP requests
▼
┌─────────────────────────────────────┐
│          BACKEND SERVICE            │
│     FastAPI + Python + Docker       │
│           port: 8000                │
└─────────────────────────────────────┘

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Vue.js 3 |
| Backend | FastAPI (Python) |
| Containerisation | Docker |
| Orchestration | Kubernetes (minikube) |
| CI/CD | GitHub Actions |
| Web Server | Nginx |

---

## 📁 Project Structure
devops-dummy-project/
├── backend/
│   ├── main.py             ← FastAPI app
│   ├── requirements.txt    ← Python dependencies
│   └── Dockerfile          ← Backend container
│
├── frontend/
│   ├── src/
│   │   └── App.vue         ← Vue todo app
│   ├── package.json
│   └── Dockerfile          ← Frontend container
│
└── README.md

---

## 🚀 Quick Start

### Prerequisites
- Docker installed
- Git

### Run with Docker

**Backend:**
```bash
cd backend
docker build -t backend:v1 .
docker run -d -p 8000:8000 --name todo-backend backend:v1
```

**Frontend:**
```bash
cd frontend
docker build -t frontend:v1 .
docker run -d -p 3000:80 --name todo-frontend frontend:v1
```

**Open browser:**
Frontend  → http://localhost:3000
Backend   → http://localhost:8000
API Docs  → http://localhost:8000/docs

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/todos` | Get all todos |
| POST | `/todos` | Add new todo |

---

## 🔄 CI/CD Pipeline
Push to main branch
↓
GitHub Actions triggers
↓
✅ Build Vue app
✅ Build Docker image
✅ Deploy to server
↓
Live in 5 minutes!

---

## ☸️ Kubernetes

```bash
# Start minikube
minikube start

# Deploy app
kubectl create deployment myapp --image=frontend:v1

# Scale to 3 replicas
kubectl scale deployment myapp --replicas=3

# Check pods
kubectl get pods

# Watch self healing — delete a pod and watch it recover!
kubectl delete pod <pod-name>
kubectl get pods
```

---

## 📚 What I Learned

- ✅ How containers work (namespaces + cgroups)
- ✅ Docker — images, containers, Dockerfile, multi-stage builds
- ✅ Microservices architecture vs monolithic
- ✅ Kubernetes — pods, deployments, services, autoscaling
- ✅ CI/CD pipelines with GitHub Actions
- ✅ Production DevOps practices

---

## 🗺 Roadmap

- [x] FastAPI backend
- [x] Vue.js frontend
- [x] Docker containerisation
- [ ] Docker Compose
- [ ] GitHub Actions pipeline
- [ ] Kubernetes deployment files
- [ ] Auto deploy to VM

---

## 👩‍💻 Author

**Sajina PK**
- Learning DevOps from scratch
- Built this in one evening! 🌙

---

## 📄 License
MIT
