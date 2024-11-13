# Enumeration for the status of the risk file
from enum import Enum


class RiskFileStatus(Enum):
    CONCEPT = "concept"
    ACTIEF = "actief"
    DEFINITIEF = "definitief"
    ARCHIEF = "archief"
