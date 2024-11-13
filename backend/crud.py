from sqlalchemy.orm import Session
from . import models, schemas

def get_risk(db: Session, risk_id: int):
    return db.query(models.Risk).filter(models.Risk.id == risk_id).first()

def get_risks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Risk).offset(skip).limit(limit).all()

def create_risk(db: Session, risk: schemas.RiskCreate):
    db_risk = models.Risk(name=risk.name, description=risk.description)
    db.add(db_risk)
    db.commit()
    db.refresh(db_risk)
    return db_risk

def update_risk(db: Session, risk_id: int, risk: schemas.RiskUpdate):
    db_risk = db.query(models.Risk).filter(models.Risk.id == risk_id).first()
    if db_risk:
        db_risk.name = risk.name
        db_risk.description = risk.description
        db.commit()
        db.refresh(db_risk)
    return db_risk

def delete_risk(db: Session, risk_id: int):
    db_risk = db.query(models.Risk).filter(models.Risk.id == risk_id).first()
    if db_risk:
        db.delete(db_risk)
        db.commit()
    return db_risk

def get_measure(db: Session, measure_id: int):
    return db.query(models.Measure).filter(models.Measure.id == measure_id).first()

def get_measures(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Measure).offset(skip).limit(limit).all()

def create_measure(db: Session, measure: schemas.MeasureCreate):
    db_measure = models.Measure(name=measure.name, description=measure.description)
    db.add(db_measure)
    db.commit()
    db.refresh(db_measure)
    return db_measure

def update_measure(db: Session, measure_id: int, measure: schemas.MeasureUpdate):
    db_measure = db.query(models.Measure).filter(models.Measure.id == measure_id).first()
    if db_measure:
        db_measure.name = measure.name
        db_measure.description = measure.description
        db.commit()
        db.refresh(db_measure)
    return db_measure

def delete_measure(db: Session, measure_id: int):
    db_measure = db.query(models.Measure).filter(models.Measure.id == measure_id).first()
    if db_measure:
        db.delete(db_measure)
        db.commit()
    return db_measure

def get_rubrix(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Rubrix).offset(skip).limit(limit).all()
