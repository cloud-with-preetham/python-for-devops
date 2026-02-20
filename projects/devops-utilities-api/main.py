# Application entry point
from app.api import app
import uvicorn

if __name__ == "__main__":
    # ASGI
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True, log_level="info")
