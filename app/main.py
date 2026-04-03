from fastapi import FastAPI
from app.etl import run_etl

app = FastAPI()


@app.get("/")
def root():
    return {"message": "ETL API is running"}


@app.get("/stats")
def get_stats():
    return run_etl()