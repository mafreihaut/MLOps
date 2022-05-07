
# Sentiment Containerized App


## Quick Easy Build and Run
`docker build -t sentiment_app . ` 

`docker run -it --rm --name sentiment_app sentiment_app`


## Navigate to the running Container in your browser
`http://0.0.0.0:8001/docs`

Then use the try it out button and enter a sentence.

```
{
  "query_string": "Have you ever been Rick Rolled?"
}
```

Curl:
```
curl -X 'POST' \
  'http://0.0.0.0:8001/sentiment/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "query_string": "Have you ever been Rick Rolled?"
}'
```

Response Body:
```
[
  {
    "label": "NEGATIVE",
    "score": 0.9846113324165344
  }
]
```
### More Details
<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank">
 <img src="https://jalammar.github.io/images/word2vec/word2vec.png" alt="Watch the video" width="480" height="360" border="10" />
</a>