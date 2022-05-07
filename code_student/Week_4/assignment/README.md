
# Sentiment Containerized App


## Quick Easy Build and Run
`docker build -t sentiment_app . ` 
`docker run -it --rm --name sentiment_app sentiment_app`


## Navigate to the running Container in your browser
`http://0.0.0.0:8001/docs`

Then use the try it out button and enter a sentence.

```
{
  "query_string": "I like MLOps"
}
```

Curl:
```
curl -X 'POST' \
  'http://0.0.0.0:8001/sentiment/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "query_string": "I like MLOps"
}'
```

Response Body:
```
[
  {
    "label": "POSITIVE",
    "score": 0.9919929504394531
  }
]
```