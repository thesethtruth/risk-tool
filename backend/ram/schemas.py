from pydantic import BaseModel
from typing import List, Optional
from datetime import date


class MeasureBase(BaseModel):
    name: str
    description: Optional[str] = None
    owner: Optional[str] = None  # Add owner field
    deadline: Optional[date] = None  # Add deadline field
    status: Optional[str] = None  # Add status field


class MeasureCreate(MeasureBase):
    pass


class Measure(MeasureBase):
    id: int
    risks: List[int] = []

    class Config:
        orm_mode: True


class MeasureUpdate(MeasureBase):
    risks: List[int] = []


class RiskBase(BaseModel):
    name: str
    description: Optional[str] = None
    cause: Optional[str] = None  # Add cause field
    consequence: Optional[str] = None  # Add consequence field
    phase: Optional[str] = None  # Add phase field
    theme: Optional[str] = None  # Add theme field
    allocation: Optional[str] = None  # Add allocation field
    responsible: Optional[str] = None  # Add responsible field
    status: Optional[str] = None  # Add status field


class RiskCreate(RiskBase):
    pass


class Risk(RiskBase):
    id: int
    measures: List[Measure] = []

    class Config:
        orm_mode: True


class RiskUpdate(RiskBase):
    measures: List[int] = []


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
    likelihood: Optional[int] = None  # Add likelihood field
    geld: Optional[int] = None  # Add geld field
    tijd: Optional[int] = None  # Add tijd field
    kwaliteit: Optional[int] = None  # Add kwaliteit field
    omgeving: Optional[int] = None  # Add omgeving field
    veiligheid: Optional[int] = None  # Add veiligheid field
    imago: Optional[int] = None  # Add imago field


class ScoringCreate(ScoringBase):
    pass


class Scoring(ScoringBase):
    id: int

    class Config:
        orm_mode: True


class RubricBase(BaseModel):
    name: str
    description: Optional[str] = None


class RubricCreate(RubricBase):
    pass


class RubricUpdate(RubricBase):
    pass


class Rubric(RubricBase):
    id: int

    class Config:
        orm_mode: True
