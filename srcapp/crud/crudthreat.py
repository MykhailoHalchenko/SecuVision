from sqlalchemy.orm import Session
from models.threat import Threat

def create_threat(db: Session, name: str, severity: str, description: str = None, source: str = None):
    threat = Threat(
        name=name,
        severity=severity,
        description=description,
        source=source
    )
    db.add(threat)
    db.commit()
    db.refresh(threat)
    return threat
