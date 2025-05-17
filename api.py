from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="API BERT - Démo")

class Tweet(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "API en ligne"}

@app.post("/predict")
def predict(tweet: Tweet):
    if "love" in tweet.text.lower():
        sentiment = "positif"
        confidence = 0.95
    else:
        sentiment = "négatif"
        confidence = 0.80

    return {
        "sentiment": sentiment,
        "confidence": confidence
    }
