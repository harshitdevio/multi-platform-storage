from fastapi import APIRouter, UploadFile, HTTPException, Depends
from app.services.file_service import FileService
from app.dependencies.auth import get_current_user

router = APIRouter()

@router.post("/upload")
async def upload_file(
    file: UploadFile, 
    user = Depends(get_current_user)
):
    try:
        url = FileService.upload(file, user.id)
        return {"message": "File uploaded", "url": url}
    except Exception :
        raise HTTPException(status_code=500)
    