
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pyagent.api.v1 import router as v1_router


app = FastAPI()

# Allow same-origin and localhost for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_router, prefix="/v1")

@app.get("/")
def read_root():
    return {"message": "Healthy"}
