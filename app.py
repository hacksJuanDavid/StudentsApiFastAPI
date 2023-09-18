from fastapi import FastAPI
from Routes.studentsRoute import router as StudentRouter

app = FastAPI()

app.include_router(StudentRouter, tags=["Students"], prefix="/api/v1")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}



