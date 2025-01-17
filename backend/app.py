from typing import List
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from ram.database import SessionLocal, engine
from ram import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/risks/", response_model=schemas.Risk)
def create_risk(risk: schemas.RiskCreate, db: Session = Depends(get_db)):
    return crud.create_risk(db=db, risk=risk)


@app.get("/risks/", response_model=List[schemas.Risk])
def read_risks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    risks = crud.get_risks(db, skip=skip, limit=limit)
    return risks


@app.get("/risks/{risk_id}", response_model=schemas.Risk)
def read_risk(risk_id: int, db: Session = Depends(get_db)):
    db_risk = crud.get_risk(db, risk_id=risk_id)
    if db_risk is None:
        raise HTTPException(status_code=404, detail="Risk not found")
    return db_risk


@app.put("/risks/{risk_id}", response_model=schemas.Risk)
def update_risk(risk_id: int, risk: schemas.RiskUpdate, db: Session = Depends(get_db)):
    db_risk = crud.get_risk(db, risk_id=risk_id)
    if db_risk is None:
        raise HTTPException(status_code=404, detail="Risk not found")
    return crud.update_risk(db=db, risk=risk, risk_id=risk_id)


@app.delete("/risks/{risk_id}", response_model=schemas.Risk)
def delete_risk(risk_id: int, db: Session = Depends(get_db)):
    db_risk = crud.get_risk(db, risk_id=risk_id)
    if db_risk is None:
        raise HTTPException(status_code=404, detail="Risk not found")
    return crud.delete_risk(db=db, risk_id=risk_id)


@app.get("/rubrics/", response_model=List[schemas.Rubric])
def read_rubrics(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    rubrics = crud.get_rubrics(db, skip=skip, limit=limit)
    return rubrics


@app.post("/measures/", response_model=schemas.Measure)
def create_measure(measure: schemas.MeasureCreate, db: Session = Depends(get_db)):
    return crud.create_measure(db=db, measure=measure)


@app.get("/measures/", response_model=List[schemas.Measure])
def read_measures(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    measures = crud.get_measures(db, skip=skip, limit=limit)
    return measures


@app.get("/measures/{measure_id}", response_model=schemas.Measure)
def read_measure(measure_id: int, db: Session = Depends(get_db)):
    db_measure = crud.get_measure(db, measure_id=measure_id)
    if db_measure is None:
        raise HTTPException(status_code=404, detail="Measure not found")
    return db_measure


@app.put("/measures/{measure_id}", response_model=schemas.Measure)
def update_measure(
    measure_id: int, measure: schemas.MeasureUpdate, db: Session = Depends(get_db)
):
    db_measure = crud.get_measure(db, measure_id=measure_id)
    if db_measure is None:
        raise HTTPException(status_code=404, detail="Measure not found")
    return crud.update_measure(db=db, measure=measure, measure_id=measure_id)


@app.delete("/measures/{measure_id}", response_model=schemas.Measure)
def delete_measure(measure_id: int, db: Session = Depends(get_db)):
    db_measure = crud.get_measure(db, measure_id=measure_id)
    if db_measure is None:
        raise HTTPException(status_code=404, detail="Measure not found")
    return crud.delete_measure(db=db, measure_id=measure_id)


@app.post("/projects/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db=db, project=project)


@app.get("/projects/", response_model=List[schemas.Project])
def read_projects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    projects = crud.get_projects(db, skip=skip, limit=limit)
    return projects


@app.get("/projects/{project_id}", response_model=schemas.Project)
def read_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project(db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project


@app.put("/projects/{project_id}", response_model=schemas.Project)
def update_project(
    project_id: int, project: schemas.ProjectUpdate, db: Session = Depends(get_db)
):
    db_project = crud.get_project(db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return crud.update_project(db=db, project=project, project_id=project_id)


@app.delete("/projects/{project_id}", response_model=schemas.Project)
def delete_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project(db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return crud.delete_project(db=db, project_id=project_id)
