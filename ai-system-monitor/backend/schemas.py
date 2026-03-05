from pydantic import BaseModel

class MetricsSchema(BaseModel):
    cpu:float
    ram:float
    network:int
    process_count:int
    ip:str
    timestamp:float