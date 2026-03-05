from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Metrics(BaseModel):
    cpu:float
    ram:float
    network:float
    process_count:int
    ip:str
    timtstamp:float
    
@app.post("/metrics")
def receive_metrics(data: Metrics):
    print("Recieved Data")
    print(data)
    
    return {
        "status": "success",
        "message" : "Metrics received"
    }