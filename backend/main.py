from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from controller import get_engine, obtain_inference
from models import UserInṕut
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi.templating import Jinja2Templates

app = FastAPI()

origins = ["*", "http://localhost:5173","http://0.0.0.0"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="build")

# Monta la carpeta 'build' como una carpeta estática
app.mount("/assets", StaticFiles(directory=Path("build/"), html=True), name="assets")

@app.get("/",response_class=HTMLResponse)
async def root():
    return FileResponse("build/index.html", media_type="text/html")

@app.post("/results")
async def get_results(input: UserInṕut):
    print("input")
    print(input)
    motor = get_engine()
    results = obtain_inference(motor, input)
    return results
