from fastapi import FastAPI

app = FastAPI(title="AI Backend Assignment")

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Backend Assignment"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
