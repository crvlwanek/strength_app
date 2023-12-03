from fastapi import FastAPI

from parsing import get_most_recent_workout

app = FastAPI()

@app.get("/")
async def get_most_recent_strength_workout():
    return get_most_recent_workout()