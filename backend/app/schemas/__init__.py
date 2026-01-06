# # user schemas
# from .user import (
#     UserBase,
#     UserCreate,
#     LoginRequest,
#     UserUpdate,
#     UserOut,
#     Token,
#     TokenData,
#     TokenResponse
# )
# # employee schemas
# from .employee import (
#     Employee,
#     EmployeeCreate,
#     PaginatedEmployees,
#     EmployeeListResponse,
#     EmployeeUpdate
# )
# from .permission import (
#     PermissionBase,
#     PermissionCreate,
#     PermissionUpdate,
#     Permission,
#     PaginatedPermissions,
#     PermissionListResponse
# )
# from .role import (
#     RoleBase,
#     RoleCreate,
#     RoleUpdate,
#     Role,
#     PaginatedRoles,
#     RoleListResponse
# )
# from .image_category import (
#     ImageCategoryBase,
#     ImageCategoryCreate,
#     ImageCategoryUpdate,
#     PaginatedImageCategory,
#     ImageCategoryListResponse
# )       
# from .image import (
#     ImageBase,
#     ImageCreate,    
#     ImageUpdate,
#     ImageOut,
# )
# # define what will be exported on `from schemas import *`
# __all__ = [
#     'UserBase', 'UserCreate', 'LoginRequest', 'UserUpdate', 'UserOut',
#     'Token', 'TokenData', 'TokenResponse',
#     'Employee', 'EmployeeCreate','PaginatedEmployees','EmployeeListResponse','EmployeeUpdate',
#     'PermissionBase', 'PermissionCreate' ,'PermissionUpdate','Permission', 'PaginatedPermissions', 'PermissionListResponse',
#     'RoleBase', 'RoleCreate', 'RoleUpdate', 'Role', 'PaginatedRoles', 'RoleListResponse',
#     'ImageCategoryBase', 'ImageCategoryCreate', 'ImageCategoryUpdate', 'PaginatedImageCategory', 'ImageCategoryListResponse',
#     'ImageBase', 'ImageCreate', 'ImageUpdate', 'ImageOut'
# ]






# app/schemas/__init__.py
"""
Centralized schemas export
"""
from app.schemas.user import (
    UserCreate, UserUpdate, UserOut, UserWithRole,
    PaginatedUsers, UserListResponse,
    LoginRequest, TokenResponse, TokenData
)
from app.schemas.employee import (
    EmployeeCreate, EmployeeUpdate, EmployeeOut,
    PaginatedEmployees, EmployeeListResponse
)
from app.schemas.permission import (
    PermissionCreate, PermissionUpdate, PermissionOut,
    PaginatedPermissions, PermissionListResponse
)
from app.schemas.role import (
    RoleCreate, RoleUpdate, RoleOut, RoleWithPermissions,
    PaginatedRoles, RoleListResponse
)
from app.schemas.image_category import (
    ImageCategoryCreate, ImageCategoryUpdate, ImageCategoryOut,
    ImageCategoryWithImages, PaginatedImageCategories, ImageCategoryListResponse
)
from app.schemas.image import (
    ImageCreate, ImageUpdate, ImageOut, ImageWithCategory,
    PaginatedImages, ImageListResponse, ImageUploadResponse
)

__all__ = [
    # User
    "UserCreate", "UserUpdate", "UserOut", "UserWithRole",
    "PaginatedUsers", "UserListResponse",
    "LoginRequest", "TokenResponse", "TokenData",
    
    # Employee
    "EmployeeCreate", "EmployeeUpdate", "EmployeeOut",
    "PaginatedEmployees", "EmployeeListResponse",
    
    # Permission
    "PermissionCreate", "PermissionUpdate", "PermissionOut",
    "PaginatedPermissions", "PermissionListResponse",
    
    # Role
    "RoleCreate", "RoleUpdate", "RoleOut", "RoleWithPermissions",
    "PaginatedRoles", "RoleListResponse",
    
    # Image Category
    "ImageCategoryCreate", "ImageCategoryUpdate", "ImageCategoryOut",
    "ImageCategoryWithImages", "PaginatedImageCategories", "ImageCategoryListResponse",
    
    # Image
    "ImageCreate", "ImageUpdate", "ImageOut", "ImageWithCategory",
    "PaginatedImages", "ImageListResponse", "ImageUploadResponse",
]