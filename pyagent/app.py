
from fastapi import FastAPI
from pyagent.api.v1 import router as v1_router

app = FastAPI()

app.include_router(v1_router, prefix="/v1")

@app.get("/")
def read_root():
    return {"message": "Healthy"}
