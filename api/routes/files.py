from fastapi import APIRouter, UploadFile, HTTPException
from app.services.file_service import FileService

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile, user_id: str):
    try:
        url = FileService.upload(file, user_id)
        return {"message": "File uploaded", "url": url}
    except Exception:
        raise HTTPException(status_code=500)