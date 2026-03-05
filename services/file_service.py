from fastapi import HTTPException
from app.clients.r2 import s3
from app.clients.supabase import supabase
from app.core.config import settings

ALLOWED_TYPES = {
    "image/png",
    "text/plain",
    "video/mp4"
}

class FileService:

    @staticmethod
    async def upload(file, user_id):
        if file.content_type not in ALLOWED_TYPES:
            raise HTTPException(status_code=400, detail="Invalid file type")

        contents = await file.read()
        file_size = len(contents)
        await file.seek(0)
        
        file_key = f"{user_id}/{file.filename}"

        s3.upload_fileobj(
            file.file,
            settings.BUCKET_NAME,
            file_key,
            ExtraArgs={"ContentType": file.content_type},
        )

        file_url = f"{settings.FILE_BASE_URL}/{file_key}"

        supabase.table("files").insert({
            "user_id": user_id,
            "filename": file.filename,
            "file_key": file_key,
            "file_url": file_url,
            "content_type": file.content_type,
            "size": file.size,
        }).execute()

        return file_url