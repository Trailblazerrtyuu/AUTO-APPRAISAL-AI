from fastapi import FastAPI

fastapi_app = FastAPI()

@fastapi_app.get("/")
def read_root():
    return {"Hello": "World"}
