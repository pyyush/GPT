# Text Generation GPT-2
This repository contains code for a text generation demo using GPT-2 with Gradio/FastAPI. The GPT-2 model is a language model developed by OpenAI that generates text based on the input text prompt.

## Setup
Before running the code, please ensure that you have installed the required dependencies mentioned in the requirements.txt file. You can do this by running the following command in your terminal:
```bash
pip3 install -r requirements.txt
```

# FastAPI
To run the FastAPI web server, you can use the following command in your terminal:
``` bash
uvicorn fastAPI:app 
```
Once the server is up and running, you can access the Swagger documentation for the API at <ins>http://127.0.0.1:8000/docs</ins> \
Alternatively, you can use the curl command to generate text as shown below:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/generate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "promt": "I love playing volleyball",
  "max_tokens_to_generate": 50
}'
```

# Gradio
To run the Gradio web application, you can use the following command in your terminal:
``` bash
python3 Gradio.py
```
Once the server is up and running, you can access the web application at <ins>http://127.0.0.1:7860</ins> \
The web application allows you to enter a text prompt and generate text using the GPT-2 model. You can also select the maximum number of tokens to generate.