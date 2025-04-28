from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import models.common

app = FastAPI(
    title="Calendar App Backend",
    description="Backend for Calendar App",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"root":"Calendar App Backend"}

@app.post("/")
async def root():
    return {"root":"Calendar App Backend"}

if __name__ == "__main__":
    uvicorn.run("app:app",host="0.0.0.0",port=8173,reload=True)