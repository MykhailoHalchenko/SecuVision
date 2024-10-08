from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()
# class to represent the threat model
class Threat(Base):
    __tablename__ = "threats"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    severity = Column(String(50), nullable=False)
    source = Column(String(255), nullable=True)
    reported_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String(50), default="open")
    def __repr__(self):
        return f"<Threat(name={self.name}, severity={self.severity}, status={self.status})>"