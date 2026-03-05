from fastapi import APIRouter, UploadFile, HTTPException, Depends
from app.services.file_service import FileService
from app.dependencies.auth import get_current_user
from app.clients.supabase import supabase

router = APIRouter()

@router.post("/upload")
async def upload_file(
    file: UploadFile, 
    user = Depends(get_current_user)
):
    try:
        url = await FileService.upload(file, user.id)
        return {"message": "File uploaded", "url": url}
    except Exception :
        raise HTTPException(status_code=500)
    
@router.post("/signup")
async def signup(email: str, password: str):
    res = supabase.auth.sign_up({"email": email, "password": password})
    return res

@router.post("/login")
async def login(email: str, password: str):
    # This returns an 'access_token' (JWT) which the frontend must save
    res = supabase.auth.sign_in_with_password({"email": email, "password": password})
    return res