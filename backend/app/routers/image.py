# # app/routers/image.py

# from fastapi import APIRouter, Depends, UploadFile, File,Form, HTTPException, Request
# from sqlalchemy.orm import Session
# from app import database, schemas
# from app.database import get_db
# from app.schemas.image import ImageCreate, ImageOut, ImageUpdate, ImageListResponse
# from app.crud.image import create_image, get_all_images, get_image, update_image, delete_image
# from app import oauth2, models
# from app.utils import paginate_data, filter_images, filter_images_all
# from typing import List, Optional
# from app.schemas.image import ImageUpdate, ImageOut
# from app.crud.image import update_image , save_image_file
# from app.schemas.image import ImageCreate
# from app.crud.image import update_image
# from builtins import Exception
# from app.dependencies.permission import require

# router = APIRouter(prefix="/images", tags=["Images"])


# @router.post("/", response_model=ImageOut, dependencies=[require("read_image")])
# def upload_image(
#     file: UploadFile = File(...),
#     name: Optional[str] = Form(None),
#     description: Optional[str] = Form(None),
#     category_id: Optional[int] = Form(None),
#     db: Session = Depends(get_db),
#     current_user: models.User = Depends(oauth2.get_current_user)
# ):
#     try:
#         # 1. First save the file and get its path
#         file_info = save_image_file(file)
#         if not file_info or not file_info.get("image_path"):
#             raise HTTPException(
#                 status_code=400, 
#                 detail="Failed to save image file"
#             )

#         # 2. Prepare complete image data including the path
#         image_data = {
#             "name": name,
#             "description": description,
#             "category_id": category_id,
#             "image_path": file_info["image_path"],  # Include the saved path
#             "created_by_user_id": current_user.id,
#             "updated_by_user_id": None,
#         }

#         # 3. Create the image record
#         db_image = models.Image(**image_data)
#         db.add(db_image)
#         db.commit()
#         db.refresh(db_image)

#         return db_image

#     except HTTPException:
#         raise  # Re-raise HTTP exceptions
#     except Exception as e:
#         db.rollback()
#         # Clean up the saved file if database operation failed
#         if 'file_info' in locals() and file_info.get("image_path"):
#             try:
#                 Path(file_info["image_path"]).unlink(missing_ok=True)
#             except Exception:
#                 pass
#         raise HTTPException(
#             status_code=500, 
#             detail=f"Failed to upload image: {str(e)}"
#         )


# @router.get("/", response_model=ImageListResponse, dependencies=[require("read_image")])
# def get_images(
#     request: Request,
#     db: Session = Depends(database.get_db),
#     # current_user: models.User = Depends(oauth2.get_current_user),
# ):
#     try:
#         query = db.query(models.Image)

#         # Convert query params to dictionary and include current_user.id as a filter
#         query_params = dict(request.query_params)
#         # query_params["created_by_user_id"] = str(current_user.id)

#         query = filter_images_all(query_params, query)

#         data = query.all()
#         paginated_data, count = paginate_data(data, request)

#         serialized_data = [schemas.ImageOut.from_orm(item) for item in paginated_data]

#         return {
#             "status": "SUCCESSFUL",
#             "result": {
#                 "count": count,
#                 "data": serialized_data
#             }
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))



# from fastapi import APIRouter, Query, Depends, HTTPException, Request
# from sqlalchemy.orm import Session, joinedload
# from typing import List
# from app import models, oauth2
# from app.database import get_db
# from app.schemas.image import ImageListResponse, PaginatedImages, ImageOut
# from app.models.image_category import ImageCategory
# from app.utils import paginate_data  # adjust import as needed


# @router.get("/categorywise", response_model=ImageListResponse, dependencies=[require("read_image")])
# def get_images_by_category(
#     request: Request,
#     category: str = Query(..., description="Category of images to filter by"),
#     db: Session = Depends(get_db),
#     # current_user: models.User = Depends(oauth2.get_current_user)
# ):
#     try:
#         images = (
#             db.query(models.Image)
#             .join(ImageCategory)
#             .options(joinedload(models.Image.category))
#             .filter(ImageCategory.category == category)
#             .all()
#         )

#         if not images:
#             raise HTTPException(
#                 status_code=404,
#                 detail=f"No images found in category '{category}'"
#             )

#         paginated_data, count = paginate_data(images, request)

#         return ImageListResponse(
#             status="SUCCESSFUL",
#             result=PaginatedImages(
#                 count=count,
#                 data=paginated_data
#             )
#         )

#     except HTTPException:
#         raise
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))




# @router.get("/publiccategorywise", response_model=ImageListResponse, dependencies=[require("read_image")])
# def get_images_by_category(
#     request: Request,
#     category: str = Query(..., description="Category of images to filter by"),
#     db: Session = Depends(get_db),
#     # current_user: models.User = Depends(oauth2.get_current_user)
# ):
#     try:
#         images = (
#             db.query(models.Image)
#             .join(ImageCategory)
#             .options(joinedload(models.Image.category))
#             .filter(ImageCategory.category == category)
#             .all()
#         )

#         if not images:
#             raise HTTPException(
#                 status_code=404,
#                 detail=f"No images found in category '{category}'"
#             )

#         paginated_data, count = paginate_data(images, request)

#         return ImageListResponse(
#             status="SUCCESSFUL",
#             result=PaginatedImages(
#                 count=count,
#                 data=paginated_data
#             )
#         )

#     except HTTPException:
#         raise
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# @router.get("/{image_id}", response_model=ImageOut, dependencies=[require("read_image")])
# def read_image(
#     image_id: int, 
#     db: Session = Depends(get_db),
#     current_user: models.User = Depends(oauth2.get_current_user)
# ):
#     try:
#         image = get_image(db, image_id)
#         if not image:
#             raise HTTPException(status_code=404, detail="Image not found")
#         return image
#     except HTTPException:
#         raise
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))





# from fastapi import UploadFile, File, Form, HTTPException
# from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
# from sqlalchemy.orm import Session
# from typing import Optional
# from pathlib import Path
# import logging
# from datetime import datetime

# # Import your models and schemas
# from app import models, oauth2
# from app.database import get_db
# from app.schemas.image import ImageOut, ImageUpdate
# from app.crud.image import save_image_file

# logger = logging.getLogger(__name__)

# @router.patch("/{image_id}", response_model=ImageOut, dependencies=[require("update_image")])
# def update_image_route(
#     image_id: int,
#     file: Optional[UploadFile] = File(None),
#     name: Optional[str] = Form(None),
#     description: Optional[str] = Form(None),
#     category_id: Optional[int] = Form(None),
#     db: Session = Depends(get_db),
#     current_user: models.User = Depends(oauth2.get_current_user)
# ):
#     try:
#         db_image = db.query(models.Image).filter(models.Image.id == image_id).first()
#         if not db_image:
#             raise HTTPException(status_code=404, detail="Image not found")

#         # Always update these fields
#         db_image.updated_by_user_id = current_user.id
#         db_image.upload_date = datetime.utcnow()

#         # Update other fields if provided
#         if name is not None:
#             db_image.name = name
#         if description is not None:
#             db_image.description = description
#         if category_id is not None:
#             db_image.category_id = category_id

#         # Handle file upload
#         if file:
#             file_info = save_image_file(file)
#             # Clean up old file first
#             if db_image.image_path:
#                 try:
#                     Path(db_image.image_path).unlink(missing_ok=True)
#                 except Exception as e:
#                     logger.warning(f"Couldn't delete old image: {e}")
#             # Update file-related fields
#             db_image.image_path = file_info["image_path"]
#             db_image.original_filename = file_info.get("original_filename")
#             db_image.file_size = file_info.get("file_size")
#             db_image.mime_type = file_info.get("mime_type")

#         db.commit()
#         db.refresh(db_image)
#         return db_image

#     except Exception as e:
#         db.rollback()
#         raise HTTPException(status_code=500, detail=str(e))

# @router.delete("/{image_id}", dependencies=[require("delete_image")])
# def delete_existing_image(
#     image_id: int, 
#     db: Session = Depends(get_db),
#     current_user: models.User = Depends(oauth2.get_current_user)
# ):
#     try:
#         if delete_image(db, image_id):
#             return {"status": "SUCCESSFUL", "message": "Image deleted successfully"}
#         raise HTTPException(status_code=404, detail="Image not found")
#     except HTTPException:
#         raise
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))





# app/api/routers/image.py
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException, Request, Query
from sqlalchemy.orm import Session, joinedload
from typing import Optional
from pathlib import Path
import os
import shutil
from datetime import datetime
import uuid

from app import database, models, oauth2, schemas
from app.utils import paginate_data, filter_images
from app.dependencies.permission import require
from rest_framework import status


router = APIRouter(
    prefix="/images",
    tags=['Images']
)

# Configuration
UPLOAD_DIR = "static/images"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def save_image_file(file: UploadFile) -> dict:
    """Save uploaded image file and return file information"""
    try:
        # Generate unique filename
        file_extension = Path(file.filename).suffix
        unique_filename = f"{uuid.uuid4()}{file_extension}"
        save_path = os.path.join(UPLOAD_DIR, unique_filename)
        
        # Save file
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        return {
            "image_path": save_path,
            "original_filename": file.filename,
            "file_size": os.path.getsize(save_path),
            "mime_type": file.content_type
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error saving file: {str(e)}"
        )


@router.get("/", response_model=schemas.ImageListResponse, dependencies=[require("read_image")])
def get_images(
    request: Request,
    skip: int = 0,
    limit: int = 10,
    include_deleted: bool = False,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(oauth2.get_current_user),
):
    """Get all images with pagination and filtering"""
    try:
        # Query based on include_deleted flag
        if include_deleted:
            query = models.Image.get_all_including_deleted(db)
        else:
            query = models.Image.get_active(db)
        
        # Apply filters
        query = filter_images(request.query_params, query)
        
        total = query.count()
        images = query.offset(skip).limit(limit).all()

        # Convert ORM to Pydantic
        serialized_data = [schemas.ImageWithCategory.from_orm(img) for img in images]

        return {
            "status": "success",
            "result": {
                "count": total,
                "data": serialized_data
            }
        }

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.get("/by-category", response_model=schemas.ImageListResponse, dependencies=[require("read_image")])
def get_images_by_category(
    request: Request,
    category: str = Query(..., description="Category name to filter by"),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    """Get images filtered by category name"""
    try:
        # Query images with category filter (only active images and categories)
        images = (
            db.query(models.Image)
            .join(models.ImageCategory)
            .options(joinedload(models.Image.category))
            .filter(
                models.ImageCategory.category == category,
                models.Image.deleted == False,
                models.ImageCategory.deleted == False
            )
            .offset(skip)
            .limit(limit)
            .all()
        )

        total = (
            db.query(models.Image)
            .join(models.ImageCategory)
            .filter(
                models.ImageCategory.category == category,
                models.Image.deleted == False,
                models.ImageCategory.deleted == False
            )
            .count()
        )

        if not images:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No images found in category '{category}'"
            )

        # Convert to Pydantic
        serialized_data = [schemas.ImageWithCategory.from_orm(img) for img in images]

        return {
            "status": "success",
            "result": {
                "count": total,
                "data": serialized_data
            }
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.get("/{image_id}", response_model=schemas.ImageWithCategory, dependencies=[require("read_image")])
def get_image(
    image_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    """Get image by ID"""
    image = db.query(models.Image).filter(
        models.Image.id == image_id,
        models.Image.deleted == False
    ).first()
    
    if not image:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Image with id {image_id} not found"
        )
    
    return image


@router.post("/", 
            status_code=status.HTTP_201_CREATED, 
            response_model=schemas.ImageOut, 
            dependencies=[require("create_image")])
async def upload_image(
    file: UploadFile = File(...),
    name: Optional[str] = Form(None),
    description: Optional[str] = Form(None),
    category_id: Optional[int] = Form(None),
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    """Upload a new image"""
    try:
        # Validate file type
        allowed_types = ["image/jpeg", "image/png", "image/gif", "image/webp"]
        if file.content_type not in allowed_types:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"File type {file.content_type} not allowed. Allowed types: {', '.join(allowed_types)}"
            )
        
        # Validate category if provided
        if category_id:
            category = db.query(models.ImageCategory).filter(
                models.ImageCategory.id == category_id,
                models.ImageCategory.deleted == False
            ).first()
            
            if not category:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Image category with id {category_id} not found"
                )

        # Save file
        file_info = save_image_file(file)
        
        if not file_info or not file_info.get("image_path"):
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to save image file"
            )

        # Create image record with user tracking
        new_image = models.Image(
            name=name,
            description=description,
            category_id=category_id,
            image_path=file_info["image_path"],
            created_by_user_id=current_user.id,
            updated_by_user_id=current_user.id
        )
        
        db.add(new_image)
        db.commit()
        db.refresh(new_image)

        return new_image

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        # Clean up saved file on error
        if 'file_info' in locals() and file_info.get("image_path"):
            try:
                Path(file_info["image_path"]).unlink(missing_ok=True)
            except Exception:
                pass
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error uploading image: {str(e)}"
        )


@router.patch("/{image_id}", 
             response_model=schemas.ImageOut, 
             dependencies=[require("update_image")])
async def update_image(
    image_id: int,
    file: Optional[UploadFile] = File(None),
    name: Optional[str] = Form(None),
    description: Optional[str] = Form(None),
    category_id: Optional[int] = Form(None),
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    """Update image information and optionally replace the file"""
    try:
        image = db.query(models.Image).filter(
            models.Image.id == image_id,
            models.Image.deleted == False
        ).first()
        
        if not image:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Image with id {image_id} not found"
            )

        # Update text fields
        if name is not None:
            image.name = name
        if description is not None:
            image.description = description
        
        # Validate and update category if provided
        if category_id is not None:
            if category_id != image.category_id:
                category = db.query(models.ImageCategory).filter(
                    models.ImageCategory.id == category_id,
                    models.ImageCategory.deleted == False
                ).first()
                
                if not category:
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Image category with id {category_id} not found"
                    )
                
                image.category_id = category_id

        # Handle file replacement
        if file:
            # Validate file type
            allowed_types = ["image/jpeg", "image/png", "image/gif", "image/webp"]
            if file.content_type not in allowed_types:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"File type {file.content_type} not allowed"
                )
            
            # Save new file
            file_info = save_image_file(file)
            
            # Delete old file
            if image.image_path and os.path.exists(image.image_path):
                try:
                    Path(image.image_path).unlink(missing_ok=True)
                except Exception as e:
                    print(f"Warning: Couldn't delete old image: {e}")
            
            # Update file path
            image.image_path = file_info["image_path"]

        # Track who updated
        image.updated_by_user_id = current_user.id

        db.commit()
        db.refresh(image)

        return image

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating image: {str(e)}"
        )


@router.delete("/{image_id}", 
              status_code=status.HTTP_200_OK, 
              dependencies=[require("delete_image")])
def delete_image(
    image_id: int,
    permanent: bool = False,
    delete_file: bool = False,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    """Soft delete image (or permanent delete if superuser)"""
    image = db.query(models.Image).filter(
        models.Image.id == image_id
    ).first()

    if not image:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Image with id {image_id} not found"
        )

    if permanent and current_user.is_superuser:
        # Permanent delete (hard delete) - only for superusers
        # Optionally delete the physical file
        if delete_file and image.image_path and os.path.exists(image.image_path):
            try:
                Path(image.image_path).unlink(missing_ok=True)
            except Exception as e:
                print(f"Warning: Couldn't delete image file: {e}")
        
        db.delete(image)
        db.commit()
        return {"message": "Image permanently deleted"}
    else:
        # Soft delete with user tracking
        image.soft_delete(user_id=current_user.id)
        db.commit()
        return {"message": "Image soft deleted successfully"}


@router.post("/{image_id}/restore", 
            response_model=schemas.ImageOut, 
            dependencies=[require("update_image")])
def restore_image(
    image_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    """Restore a soft-deleted image"""
    image = db.query(models.Image).filter(
        models.Image.id == image_id,
        models.Image.deleted == True
    ).first()

    if not image:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Deleted image with id {image_id} not found"
        )
    
    # Check if the physical file still exists
    if not os.path.exists(image.image_path):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot restore image. Physical file no longer exists."
        )

    image.restore()
    image.updated_by_user_id = current_user.id
    db.commit()
    db.refresh(image)

    return image