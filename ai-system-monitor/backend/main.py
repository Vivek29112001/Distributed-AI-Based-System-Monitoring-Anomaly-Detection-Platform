from fastapi import FastAPI
from pydantic import BaseModel
from database import SessionLocal, engine
from models import Metrics, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

class MetricData(BaseModel):
    cpu: float
    ram: float
    network: float
    process_count: int
    ip: str
    timestamp: float


@app.post("/metrics")
def receive_metrics(data: MetricData):

    db = SessionLocal()

    metric = Metrics(
        cpu=data.cpu,
        ram=data.ram,
        network=data.network,
        process_count=data.process_count,
        ip=data.ip,
        timestamp=data.timestamp
    )

    db.add(metric)
    db.commit()

    return {"status": "stored"}


@app.get("/metrics-data")
def get_metrics():

    db = SessionLocal()

    rows = db.query(Metrics).order_by(Metrics.id.desc()).limit(50).all()

    result = []

    for r in rows:
        result.append({
            "cpu": r.cpu,
            "ram": r.ram,
            "timestamp": r.timestamp
        })

    return result