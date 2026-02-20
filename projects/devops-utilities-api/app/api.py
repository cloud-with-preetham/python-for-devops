from fastapi import FastAPI  # Importing FastAPI Class
from routers import metrics, aws

app = FastAPI(
    title="Internal DevOps Utilities API",
    description="This is an internal Application Programming Interface Utilities application for Monitoring services, Amazon Web Services Usages & Log analysis",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)


@app.get("/")
def hello():
    """
    This is a hello API just for testing.
    """
    return {"message": "Hello Dosto, This is DevOps Utilities API"}


app.include_router(metrics.router)
app.include_router(aws.router, prefix="/aws")
