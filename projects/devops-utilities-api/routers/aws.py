from fastapi import APIRouter
from services.aws_services import get_bucket_info
from fastapi import HTTPException

router = APIRouter()


@router.get("/s3", status_code=200)
def get_buckets():

    try:
        metrics = get_bucket_info()
        return metrics
    except:
        raise HTTPException(
            status_code=500, detail="Error occured while fetching system metrics"
        )
