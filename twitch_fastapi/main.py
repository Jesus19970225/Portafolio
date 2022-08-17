from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"twitch API": "Working!"}