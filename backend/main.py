from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller import get_engine, obtain_inference
from models import UserInṕut

app = FastAPI()

origins = ["*", "http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Sistema de Recomendacion de Carne"}


@app.post("/results")
async def get_results(input: UserInṕut):
    motor = get_engine()
    results = obtain_inference(motor, input)
    return results
