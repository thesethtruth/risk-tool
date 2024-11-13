from sqlalchemy.orm import Session
from . import models, schemas


def get_risk(db: Session, risk_id: int):
    return db.query(models.Risk).filter(models.Risk.id == risk_id).first()


def get_risks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Risk).offset(skip).limit(limit).all()


def create_risk(db: Session, risk: schemas.RiskCreate):
    db_risk = models.Risk(
        name=risk.name,
        description=risk.description,
        cause=risk.cause,
        consequence=risk.consequence,
        phase=risk.phase,
        theme=risk.theme,
        allocation=risk.allocation,
        responsible=risk.responsible,
        status=risk.status,
    )
    db.add(db_risk)
    db.commit()
    db.refresh(db_risk)
    return db_risk


def update_risk(db: Session, risk_id: int, risk: schemas.RiskUpdate):
    db_risk = db.query(models.Risk).filter(models.Risk.id == risk_id).first()
    if db_risk:
        db_risk.name = risk.name
        db_risk.description = risk.description
        db_risk.cause = risk.cause
        db_risk.consequence = risk.consequence
        db_risk.phase = risk.phase
        db_risk.theme = risk.theme
        db_risk.allocation = risk.allocation
        db_risk.responsible = risk.responsible
        db_risk.status = risk.status
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
    db_measure = models.Measure(
        name=measure.name,
        description=measure.description,
        owner=measure.owner,
        deadline=measure.deadline,
        status=measure.status,
    )
    db.add(db_measure)
    db.commit()
    db.refresh(db_measure)
    return db_measure


def update_measure(db: Session, measure_id: int, measure: schemas.MeasureUpdate):
    db_measure = (
        db.query(models.Measure).filter(models.Measure.id == measure_id).first()
    )
    if db_measure:
        db_measure.name = measure.name
        db_measure.description = measure.description
        db_measure.owner = measure.owner
        db_measure.deadline = measure.deadline
        db_measure.status = measure.status
        db.commit()
        db.refresh(db_measure)
    return db_measure


def delete_measure(db: Session, measure_id: int):
    db_measure = (
        db.query(models.Measure).filter(models.Measure.id == measure_id).first()
    )
    if db_measure:
        db.delete(db_measure)
        db.commit()
    return db_measure


def get_rubric(db: Session, rubric_id: int):
    return db.query(models.Rubric).filter(models.Rubric.id == rubric_id).first()


def get_rubrics(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Rubric).offset(skip).limit(limit).all()


def create_rubric(db: Session, rubric: schemas.RubricCreate):
    db_rubric = models.Rubric(
        name=rubric.name,  # Add name field
        description=rubric.description,  # Add description field
        probability=rubric.probability,
        consequence_money=rubric.consequence_money,
        consequence_time=rubric.consequence_time,
        consequence_quality=rubric.consequence_quality,
    )
    db.add(db_rubric)
    db.commit()
    db.refresh(db_rubric)
    return db_rubric


def update_rubric(db: Session, rubric_id: int, rubric: schemas.RubricUpdate):
    db_rubric = db.query(models.Rubric).filter(models.Rubric.id == rubric_id).first()
    if db_rubric:
        db_rubric.name = rubric.name  # Add name field
        db_rubric.description = rubric.description  # Add description field
        db_rubric.probability = rubric.probability
        db_rubric.consequence_money = rubric.consequence_money
        db_rubric.consequence_time = rubric.consequence_time
        db_rubric.consequence_quality = rubric.consequence_quality
        db.commit()
        db.refresh(db_rubric)
    return db_rubric


def delete_rubric(db: Session, rubric_id: int):
    db_rubric = db.query(models.Rubric).filter(models.Rubric.id == rubric_id).first()
    if db_rubric:
        db.delete(db_rubric)
        db.commit()
    return db_rubric
