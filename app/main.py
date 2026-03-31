from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="Smart Route AI",
    description="AI-powered dynamic route optimization system",
    version="1.0.0"
)

app.include_router(router)