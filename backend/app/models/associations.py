# from sqlalchemy import Table, Column, Integer, ForeignKey
# from app.database import Base

# # Association between users and roles
# user_role = Table(
#     'user_role',
#     Base.metadata,
#     Column('user_id', Integer, ForeignKey('users.id')),
#     Column('role_id', Integer, ForeignKey('roles.id'))
# )




# app/models/associations.py
from sqlalchemy import Table, Column, Integer, ForeignKey
from app.database import Base

# Association between roles and permissions
role_permission = Table(
    'role_permission',
    Base.metadata,
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True),
    Column('permission_id', Integer, ForeignKey('permissions.id'), primary_key=True)
)

# Association between users and permissions (direct permissions)
user_permission = Table(
    "user_permission",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("permission_id", Integer, ForeignKey("permissions.id"), primary_key=True)
)

# Association between users and roles (if needed for many-to-many)
# user_role = Table(
#     'user_role',
#     Base.metadata,
#     Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
#     Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True)
# )