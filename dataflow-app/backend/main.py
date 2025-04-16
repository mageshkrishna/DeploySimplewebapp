from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Serve React static files
app.mount("/static", StaticFiles(directory="frontend/build/static"), name="static")

@app.get("/")
def serve_react():
    return FileResponse("frontend/build/index.html")

@app.get("/api")
def read_root():
    return {"message": "Welcome to DataFlow API"}
