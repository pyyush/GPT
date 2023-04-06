import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, set_seed

# set seed for reproducibility
set_seed(42)

# pre-load pipeline
gpt2 = pipeline('text-generation', model='gpt2')

class Request(BaseModel):
    prompt: str
    max_tokens_to_generate: int
    
class Response(BaseModel):
    prompt: str
    max_tokens_to_generate: int
    generated_text: str

# declaring FastAPI instance
app = FastAPI()

@app.get("/")
def status():
    return {"api_status": "OK"}

@app.get("/models")
def list_models():
    return {"models": ["GPT-2"]}
 
@app.post('/generate', response_model=Response)
def generate(request: Request) -> Response:
    output = gpt2(
        request.prompt, 
        max_new_tokens=request.max_tokens_to_generate, 
        num_return_sequences=1
        )[0]['generated_text']

    return Response(
        prompt = request.prompt,
        max_tokens_to_generate = request.max_tokens_to_generate,
        generated_text = output
        )

