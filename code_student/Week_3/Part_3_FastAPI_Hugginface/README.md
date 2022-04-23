<p align = "center" draggable=”false” ><img src="https://user-images.githubusercontent.com/37101144/161836199-fdb0219d-0361-4988-bf26-48b0fad160a3.png"
     width="200px"
     height="auto"/>
</p>



# <h1 align="center" id="heading">Part 3: FastAPI HuggingFace</h1>

For this assignment, our goal will be to run a health check endpoint in FastAPI, push the code to our repo, pull onto EC2, and launch our server and hit the docs endpoint.

## HuggingFace && FastAPI
* Look at Part III from last session's live assignment (HuggingFace sentiment analysis)
* You are going to need to implement something very similar here within your endpoint to return to the user (based off the query they provide) if the sentiment of the query is positive or negative

1. First off pip install the needed libraries: `pip install transformers torch torchvision torchaudio`
2. Your code from last time could look something like this:

```python
from transformers import pipeline
sentiment_model = pipeline("sentiment-analysis")

sentiment_query_sentence = get_random_comment(top_comments)
sentiment = sentiment_model(sentiment_query_sentence)
print(f"Sentiment test: {sentiment_query_sentence} == {sentiment})
```
But now you need to modify this in a way that can take in the query sentence and format a response to the user and return through FastAPI. It can be very close to this though!

3. FastAPI requires you to set a `Pydantic` model to make sure the request comes in formatted correctly. Let's make that:

```python
from pydantic import BaseModel

class PredictionRequest(BaseModel):
  query_string: str
```

4. Create a `post` endpoint with whatever name you like similar to this:

```python
@app.post("my-endpoint")
def my_endpoint(request: PredictionRequest):
  # YOUR CODE GOES HERE
```

5. Put your HuggingFace code into `main.py` and the logic within your `my_endpoint` function
6. Test that this works locally by running your server: `uvicorn main:app --port 8000` and navigate to your browser `localhost:8000/docs` to test it out.
7. If it works, commit to your repo and pull onto your EC2 instance.
8. From there, follow the same pip install commands from before and run your application by doing `uvicorn main:app --host 0.0.0.0 --port 8000`
9. Try hitting your endpoint by doing `{my-ip}:8000/docs`

## Bonus
* Try adding error handling to your endpoint.
* See if you can read through the [documentation](https://fastapi.tiangolo.com/tutorial/handling-errors/) and add a `500` error if any server error occurs.

## Resources
* https://fastapi.tiangolo.com/tutorial/first-steps/
* https://fastapi.tiangolo.com/tutorial/body/

