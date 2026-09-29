from fastapi import FastAPI
from datetime import datetime
import socket

app = FastAPI(
    title="ABTalks Day-50 Kubernetes App",
    description="Dockerized application deployed on Kubernetes",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "ABTalks Day-50 Kubernetes Deployment Successful!",
        "application": "AI Engineering Application",
        "status": "running",
        "hostname": socket.gethostname(),
        "timestamp": datetime.now().isoformat()
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/info")
def info():
    return {
        "project": "ABTalks Season-3 Day-50",
        "focus": "Docker",
        "technology": "Kubernetes",
        "deployment": "Dockerized FastAPI Application",
        "replicas": 3
    }