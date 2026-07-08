# AI Backend Deployment Assignment

## Project Overview

This project demonstrates the deployment and productionization of a FastAPI backend application using Docker and AWS EC2.

The application is containerized and deployed with Docker Compose, using PostgreSQL as the database, Redis as the cache, and NGINX as the reverse proxy. CI/CD is implemented using GitHub Actions for automatic deployment to AWS EC2.

---

# Tech Stack

- FastAPI
- Docker
- Docker Compose
- PostgreSQL
- Redis
- NGINX
- AWS EC2 (Ubuntu)
- GitHub Actions
- UFW Firewall
- Fail2Ban

---

# Project Structure

```
ai-backend-app/
│
├── app/
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── nginx/
│   └── default.conf
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

---

# Architecture

```
                Internet
                    │
                    ▼
            AWS EC2 (Ubuntu)
                    │
                    ▼
          NGINX Reverse Proxy
                    │
                    ▼
            FastAPI Container
             │             │
             ▼             ▼
      PostgreSQL       Redis
```

---

# Features

- FastAPI REST API
- Dockerized Application
- Docker Compose
- PostgreSQL Database
- Redis Cache
- NGINX Reverse Proxy
- GitHub Actions CI/CD
- AWS EC2 Deployment
- Health Check Endpoint
- Environment Variables
- UFW Firewall
- Fail2Ban Protection

---

# Running Locally

Clone the repository

```bash
git clone https://github.com/mohitkamboj0228-ops/ai-backend-app.git

cd ai-backend-app
```

Start the application

```bash
docker compose up -d --build
```

Stop containers

```bash
docker compose down
```

---

# Deployment

Application is deployed on

- AWS EC2 (Ubuntu)

Deployment is automated using GitHub Actions.

Whenever code is pushed to the **main** branch:

- GitHub Actions starts
- Connects to EC2 via SSH
- Pulls latest code
- Rebuilds Docker containers
- Restarts application automatically

---

# CI/CD Pipeline

GitHub Actions workflow

```
Push to GitHub
        │
        ▼
GitHub Actions
        │
        ▼
SSH into EC2
        │
        ▼
git pull
        │
        ▼
docker compose up -d --build
```

---

# Environment Variables

Example

```
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin123
POSTGRES_DB=fastapi

DB_HOST=postgres
REDIS_HOST=redis
```

---

# Health Check

Endpoint

```
GET /health
```

Response

```json
{
  "status": "healthy"
}
```

---

# Logging Strategy

Docker logging is used for application logs.

View logs

```bash
docker compose logs
```

Live logs

```bash
docker compose logs -f
```

FastAPI logs

```bash
docker compose logs app
```

---

# Backup Strategy

Create PostgreSQL backup

```bash
docker exec postgres_db pg_dump -U admin fastapi > backup.sql
```

Restore backup

```bash
cat backup.sql | docker exec -i postgres_db psql -U admin fastapi
```

---

# Security Measures

Implemented

- Docker container isolation
- Environment Variables
- UFW Firewall
- Fail2Ban
- NGINX Reverse Proxy
- GitHub Secrets for CI/CD

---

# SSL

The application is currently deployed using the AWS EC2 Public IP.

Since a custom domain is not available, HTTPS has not been configured.

For production deployment, SSL can be enabled using:

- Let's Encrypt
- Certbot
- NGINX Reverse Proxy

---

# Useful Docker Commands

Start

```bash
docker compose up -d
```

Stop

```bash
docker compose down
```

Restart

```bash
docker compose restart
```

View Containers

```bash
docker ps
```

View Logs

```bash
docker compose logs
```

---

# Future Improvements

- Cloudflare Integration
- HTTPS with Let's Encrypt
- Monitoring using Prometheus & Grafana
- Zero Downtime Deployment
- Automated Database Backups
- Load Balancer
- Kubernetes Deployment

---

# Author

Mohit Kamboj

GitHub

https://github.com/mohitkamboj0228-ops
