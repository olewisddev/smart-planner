from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


from routers.campaign_router import campaign_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5000", "http://127.0.0.1:5000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(campaign_router)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}


def main():
    """App entrypoint"""
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
