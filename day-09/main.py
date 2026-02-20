from fastapi import FastAPI
from log_analyzer import analyze_logs
from aws_utilities import get_ec2_summary

app = FastAPI(title="DevOps Automation API")


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "devops-api"}


@app.get("/logs")
def get_log_summary():
    summary = analyze_logs("Zookeeper_2k.log")
    return {"message": "Log analysis completed", "data": summary}


@app.get("/aws")
def aws_summary():
    data = get_ec2_summary()
    return {"message": "AWS EC2 summary fetched successfully", "data": data}
