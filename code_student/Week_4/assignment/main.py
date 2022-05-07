
from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


def get_sentiment(sentiment_query_sentence):
    sentiment_model = pipeline("sentiment-analysis")
    sentiment = sentiment_model(sentiment_query_sentence.query_string)
    return sentiment


app = FastAPI()


@app.get("/health")
def health():
    return "Service is online."


class SentimentRequest(BaseModel):
    query_string: str


@app.post("/sentiment/")
async def get_sentiment(sentiment_request: SentimentRequest):

    sentiment_model = pipeline("sentiment-analysis")
    sentiment_request = sentiment_model(sentiment_request.query_string)
    result = {"sentiment": sentiment_request, **sentiment_request.dict()}
    return result
