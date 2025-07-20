# salary_structure_schema.py

from pydantic import BaseModel
from typing import Optional, List, Any
from datetime import date, datetime
from enum import Enum


class PaymentFrequency(str, Enum):
    MONTHLY = "monthly"
    BIWEEKLY = "biweekly"
    WEEKLY = "weekly"


# Base payload used for Create and Update
class SalaryStructureBase(BaseModel):
    base_salary: float
    allowances: float = 0.0
    bonuses: float = 0.0
    deductions: float = 0.0
    payment_frequency: PaymentFrequency = PaymentFrequency.MONTHLY
    effective_date: date
    end_date: Optional[date] = None
    employee_id: int
    rank_id: int
    department_id: int


# For POST request
class SalaryStructureCreate(SalaryStructureBase):
    pass


# For PATCH/PUT request
class SalaryStructureUpdate(BaseModel):
    base_salary: Optional[float]
    allowances: Optional[float]
    bonuses: Optional[float]
    deductions: Optional[float]
    payment_frequency: Optional[PaymentFrequency]
    effective_date: Optional[date]
    end_date: Optional[date]
    rank_id: Optional[int]
    department_id: Optional[int]


# For Response
class SalaryStructureOut(SalaryStructureBase):
    id: int
    created_by_user_id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
        from_attributes = True



class SalaryStructureListResponse(BaseModel):
    status: str
    result: dict[str, Any]

    class Config:
        orm_mode = True
        from_attributes = True

