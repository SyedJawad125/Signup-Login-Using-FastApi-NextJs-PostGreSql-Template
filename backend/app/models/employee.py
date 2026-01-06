# from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
# from sqlalchemy.orm import relationship
# from app.database import Base
# from app.models import User
# from sqlalchemy.ext.hybrid import hybrid_property

# class Employee(Base):
#     __tablename__ = "employees"

#     id = Column(Integer, primary_key=True, index=True)
#     first_name = Column(String(50), nullable=False)
#     last_name = Column(String(50), nullable=False)
#     email = Column(String(100), unique=True, index=True, nullable=False)
#     phone_number = Column(String(20))
#     hire_date = Column(Date, nullable=False)
#     job_title = Column(String(100), nullable=False)
#     salary = Column(Float, nullable=False)
    
#     @hybrid_property
#     def name(self) -> str:
#         return f"{self.first_name} {self.last_name}"
    
#     user = relationship("User", back_populates="employee", uselist=False)

    




# app/models/employee.py
from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from app.database import Base
from app.models.mixins import TimeUserStampMixin  # ✅ Added


class Employee(TimeUserStampMixin, Base):  # ✅ Added TimeUserStampMixin
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    phone_number = Column(String(20))
    hire_date = Column(Date, nullable=False)
    job_title = Column(String(100), nullable=False)
    salary = Column(Float, nullable=False)
    
    # ✅ created_at, updated_at, deleted, deleted_at come from mixin
    # ✅ created_by_user_id, updated_by_user_id, deleted_by_user_id come from mixin
    # ✅ creator, updater, deleter relationships come from mixin
    
    @hybrid_property
    def name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    # User relationship (one-to-one)
    user = relationship("User", back_populates="employee", uselist=False)