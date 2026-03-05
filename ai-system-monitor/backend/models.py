from sqlalchemy import Column, Integer, Float, String, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Machine(Base):
    __tablename__ = "machines"

    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String, unique=True)
    hostname = Column(String)

    metrics = relationship("Metrics", back_populates="machine")


class Metrics(Base):
    __tablename__ = "system_metrics"

    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(Integer, ForeignKey("machines.id"))

    cpu = Column(Float)
    ram = Column(Float)
    network = Column(BigInteger)
    process_count = Column(Integer)
    timestamp = Column(BigInteger)

    machine = relationship("Machine", back_populates="metrics")