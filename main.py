from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "error"}
    finally:
        file.file.close()

    return {"message": "success"}