from pydantic import BaseModel
from typing import List, Optional

class MeasureBase(BaseModel):
    name: str
    description: Optional[str] = None

class MeasureCreate(MeasureBase):
    pass

class Measure(MeasureBase):
    id: int
    risks: List[int] = []

    class Config:
        orm_mode: True

class RiskBase(BaseModel):
    name: str
    description: Optional[str] = None

class RiskCreate(RiskBase):
    pass

class Risk(RiskBase):
    id: int
    measures: List[Measure] = []

    class Config:
        orm_mode: True

class MappingBase(BaseModel):
    risk_id: int
    measure_id: int

class MappingCreate(MappingBase):
    pass

class Mapping(MappingBase):
    id: int

    class Config:
        orm_mode: True

class ScoringBase(BaseModel):
    risk_id: int
    score: int

class ScoringCreate(ScoringBase):
    pass

class Scoring(ScoringBase):
    id: int

    class Config:
        orm_mode: True
