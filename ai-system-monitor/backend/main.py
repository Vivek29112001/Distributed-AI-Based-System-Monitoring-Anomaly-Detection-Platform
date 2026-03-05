from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Metrics, Machine, Base
# create table
Base.metadata.create_all(bind=engine)

app = FastAPI()


# -------- DB Dependency --------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------- Schema --------
class MetricData(BaseModel):
    cpu: float
    ram: float
    network: float
    process_count: int
    ip: str
    hostname: str
    timestamp: float


# -------- Store Metrics --------
@app.post("/metrics")
def receive_metrics(data: MetricData, db: Session = Depends(get_db)):

    # check machine by IP
    machine = db.query(Machine).filter(Machine.ip == data.ip).first()

    # if machine not exist create
    if not machine:
        machine = Machine(
            ip=data.ip,
            hostname=data.hostname
        )
        db.add(machine)
        db.commit()
        db.refresh(machine)

    # store metrics
    metric = Metrics(
        machine_id=machine.id,
        cpu=data.cpu,
        ram=data.ram,
        network=data.network,
        process_count=data.process_count,
        timestamp=data.timestamp
    )

    db.add(metric)
    db.commit()

    return {"status": "stored"}

# -------- Get Latest Metrics --------
@app.get("/metrics/latest")
def get_metrics(db: Session = Depends(get_db)):

    rows = db.query(Metrics).order_by(Metrics.id.desc()).limit(50).all()

    result = []

    for r in rows:
        result.append({
            "cpu": r.cpu,
            "ram": r.ram,
            "network": r.network,
            "process_count": r.process_count,
            "timestamp": r.timestamp
        })

    return result