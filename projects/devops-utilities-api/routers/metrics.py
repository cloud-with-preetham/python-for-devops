from fastapi import APIRouter
from services.metrics_services import get_system_metrics
from fastapi import HTTPException

router = APIRouter()


@router.get("/metrics", status_code=200)
def get_metrics():

    try:
        metrics = get_system_metrics()
        return metrics
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error occured while fetching system metrics: {str(e)}"
        )
