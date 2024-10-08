from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas, crud
from ..database import get_db

router = APIRouter(
    prefix="/threats",
    tags=["threats"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Threat)
def create_threat(threat: schemas.ThreatCreate, db: Session = Depends(get_db)):
    return crud.create_threat(db=db, threat=threat)

@router.get("/", response_model=List[schemas.Threat])
def get_threats(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    threats = crud.get_threats(db, skip=skip, limit=limit)
    return threats

@router.get("/{threat_id}", response_model=schemas.Threat)
def get_threat(threat_id: int, db: Session = Depends(get_db)):
    threat = crud.get_threat(db, threat_id=threat_id)
    if threat is None:
        raise HTTPException(status_code=404, detail="Threat not found")
    return threat

# Оновлення інформації про загрозу
@router.put("/{threat_id}", response_model=schemas.Threat)
def update_threat(threat_id: int, updated_threat: schemas.ThreatUpdate, db: Session = Depends(get_db)):
    threat = crud.get_threat(db, threat_id=threat_id)
    if threat is None:
        raise HTTPException(status_code=404, detail="Threat not found")
    return crud.update_threat(db=db, threat=threat, updated_threat=updated_threat)

# Видалення загрози
@router.delete("/{threat_id}")
def delete_threat(threat_id: int, db: Session = Depends(get_db)):
    threat = crud.get_threat(db, threat_id=threat_id)
    if threat is None:
        raise HTTPException(status_code=404, detail="Threat not found")
    crud.delete_threat(db=db, threat=threat)
    return {"detail": "Threat deleted successfully"}
