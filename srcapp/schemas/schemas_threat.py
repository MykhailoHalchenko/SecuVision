from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ThreatBase(BaseModel):
    name: str
    description: Optional[str] = None
    severity: str
    source: Optional[str] = None
    status: Optional[str] = "open"  

class ThreatCreate(ThreatBase):
    pass  

class ThreatUpdate(ThreatBase):
    status: Optional[str] = None  

class ThreatInDBBase(ThreatBase):
    id: int
    reported_at: datetime

    class Config:
        orm_mode = True  

class Threat(ThreatInDBBase):
    pass  

class ThreatInDB(ThreatInDBBase):
    pass
