from sqlalchemy import Column, Integer, Float, String
from database import Base

class Metrics(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)
    cpu = Column(Float)
    ram = Column(Float)
    network = Column(Float)
    process_count = Column(Integer)
    ip = Column(String)
    timestamp = Column(Float)