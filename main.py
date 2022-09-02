from fastapi import FastAPI, File, UploadFile,  Depends
from fastapi.security.api_key import  APIKey
import auth

app = FastAPI()


@app.post("/api/v1/upload")
async def upload(
            file: UploadFile = File(...), api_key: APIKey = Depends(auth.get_api_key)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "error"}
    finally:
        file.file.close()

    return {"message": "success"}