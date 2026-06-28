# 🛒 ShopSphere – Enterprise E-Commerce Platform

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![ASP.NET](https://img.shields.io/badge/ASP.NET_Core-512BD4?style=for-the-badge&logo=dotnet&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-In_Progress-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)

---

## 📌 Overview

**ShopSphere** is an enterprise-style **microservices-inspired E-Commerce platform** built to demonstrate modern **DevOps practices**.

The project uses:

- **ASP.NET Core MVC** for the frontend
- **Python FastAPI** for the backend REST API
- **PostgreSQL** as the primary relational database
- **Redis** for caching
- **Docker** for containerization
- **Docker Compose** for local multi-container orchestration
- **Kubernetes** (currently in progress) for production orchestration

This repository is part of my DevOps learning journey, focusing on containerization, orchestration, automation, and cloud-native deployment.

---

# 🏗️ Architecture

```
                    Browser
                        │
                        ▼
              ASP.NET Core Frontend
                        │
                HTTP REST API
                        │
                        ▼
                 FastAPI Backend
                  │           │
                  ▼           ▼
            PostgreSQL      Redis
```

---

# 🚀 Tech Stack

| Layer | Technology |
|--------|------------|
| Frontend | ASP.NET Core MVC |
| Backend | FastAPI |
| Database | PostgreSQL 17 |
| Cache | Redis 8 |
| Containerization | Docker |
| Multi-container | Docker Compose |
| Orchestration | Kubernetes (In Progress) |
| API Documentation | Swagger / OpenAPI |
| ORM | SQLAlchemy |
| Serialization | Pydantic |
| Cache Serialization | ORJSON |

---

# 📂 Project Structure

```
ShopSphere/
│
├── backend-python/
│   ├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env
│
├── frontend-dotnet/
│   └── ShopSphere.Web/
│       ├── Controllers/
│       ├── Views/
│       ├── Dockerfile
│       └── Program.cs
│
├── k8s/
│   ├── namespace.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── deployments/
│   ├── services/
│   └── ingress.yaml
│
├── docker-compose.yml
│
└── README.md
```

---

# ✨ Features

## Backend

- RESTful API
- Product CRUD
- PostgreSQL Integration
- Redis Caching
- Swagger Documentation
- Health Check Endpoint
- Environment Variables
- SQLAlchemy ORM
- Pydantic Validation

---

## Frontend

- ASP.NET Core MVC
- Product Listing
- Product Details
- Category View
- API Integration
- Responsive Layout

---

# 🐳 Docker

This project uses **multi-stage Docker builds**.

### Containers

- Frontend
- Backend
- PostgreSQL
- Redis

Start the project

```bash
docker compose up -d
```

Stop

```bash
docker compose down
```

---

# ☸ Kubernetes (In Progress)

Current Kubernetes resources:

- Namespace
- ConfigMap
- Secret
- Persistent Volume Claim
- PostgreSQL Deployment
- PostgreSQL Service

Upcoming:

- Redis Deployment
- Backend Deployment
- Frontend Deployment
- Ingress
- Horizontal Pod Autoscaler
- Prometheus
- Grafana

---

# 🔐 Security

This project follows several container security best practices.

✅ Multi-stage Docker builds

✅ Non-root containers

✅ Docker Scout vulnerability scanning

✅ Environment variables

✅ Health Checks

✅ Persistent storage

---

# 📊 Docker Scout

Image security scanning performed using Docker Scout.

Example commands:

```bash
docker scout quickview <image>

docker scout cves <image>

docker scout recommendations <image>
```

---

# 📈 Future Enhancements

- Kubernetes Deployment
- Prometheus Monitoring
- Grafana Dashboards
- GitHub Actions CI/CD
- Helm Charts
- ArgoCD GitOps
- AWS EKS Deployment
- NGINX Ingress Controller

---

# 📷 Screenshots

Coming Soon

---

# 🎯 Learning Objectives

This project demonstrates practical knowledge of:

- Docker
- Docker Compose
- Multi-stage Dockerfiles
- FastAPI
- ASP.NET Core
- PostgreSQL
- Redis
- Kubernetes
- Container Networking
- Persistent Volumes
- Environment Management
- DevSecOps
- Docker Scout

---

# 🧑‍💻 Author

**Muhammad Zaid**

Future DevOps Engineer 🚀

- GitHub: https://github.com/MuhammadZaid11
- LinkedIn: https://www.linkedin.com/in/muhammad-zaid-9363bb377/

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!