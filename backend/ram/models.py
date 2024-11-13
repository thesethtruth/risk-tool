from sqlalchemy import Column, Integer, String, ForeignKey, Table, Date
from sqlalchemy.orm import relationship
from .database import Base

# Association table for many-to-many relationship between Risk and Measures
risk_measures = Table(
    "risk_measures",
    Base.metadata,
    Column("risk_id", Integer, ForeignKey("risks.id"), primary_key=True),
    Column("measure_id", Integer, ForeignKey("measures.id"), primary_key=True),
)


class Risk(Base):
    __tablename__ = "risks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)  # Specify length for String
    description = Column(String(255))  # Specify length for String
    cause = Column(String(255))  # Add cause field
    consequence = Column(String(255))  # Add consequence field
    phase = Column(String(255))  # Add phase field
    theme = Column(String(255))  # Add theme field
    allocation = Column(String(255))  # Add allocation field
    responsible = Column(String(255))  # Add responsible field
    status = Column(String(255))  # Add status field
    measures = relationship("Measure", secondary=risk_measures, back_populates="risks")


class Measure(Base):
    __tablename__ = "measures"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)  # Specify length for String
    owner = Column(String(255))  # Add owner field
    deadline = Column(Date)  # Add deadline field
    status = Column(String(255))  # Add status field
    risks = relationship("Risk", secondary=risk_measures, back_populates="measures")


class Mapping(Base):
    __tablename__ = "mappings"

    id = Column(Integer, primary_key=True, index=True)
    risk_id = Column(Integer, ForeignKey("risks.id"))
    measure_id = Column(Integer, ForeignKey("measures.id"))


class Scoring(Base):
    __tablename__ = "scorings"

    id = Column(Integer, primary_key=True, index=True)
    risk_id = Column(Integer, ForeignKey("risks.id"))
    score = Column(Integer)
    likelihood = Column(Integer)  # Add likelihood field
    geld = Column(Integer)  # Add geld field
    tijd = Column(Integer)  # Add tijd field
    kwaliteit = Column(Integer)  # Add kwaliteit field
    omgeving = Column(Integer)  # Add omgeving field
    veiligheid = Column(Integer)  # Add veiligheid field
    imago = Column(Integer)  # Add imago field


class Rubric(Base):
    __tablename__ = "rubrics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)  # Add name field
    description = Column(String(255))  # Add description field
    probability = Column(String(255))
    consequence_money = Column(String(255))
    consequence_time = Column(String(255))
    consequence_quality = Column(String(255))
