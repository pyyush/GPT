# Text Generation GPT-2
Text Generation demo using GPT-2 + Gradio/FastAPI

## Setup
### 1. Install Miniconda 
#### Linux users
``` bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

#### Mac (Intel based) users
``` bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh
```

### 2. Create environment
``` bash
bash setup.sh
```

### 3. Activate environment
``` bash
conda activate GPT
```

# FastAPI

``` bash
uvicorn fastAPI:app 
```
#### You could either try the API at <ins>http://127.0.0.1:8000/docs</ins> or use the curl command as shown below -
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

``` bash
python Gradio.py
```
#### You could try the web application at <ins>http://127.0.0.1:7860</ins>