import gradio
import argparse
from typing import Dict, Any
from rich.console import Console
from transformers import pipeline, set_seed

logger = Console(record=True)

# set seed for reproducibility
set_seed(42)

# pre-load pipeline
gpt2 = pipeline('text-generation', model='gpt2')

# set of examples for users to try out
examples = [
    ["I like to play volleyball."],
    ["The capital of Texas is "]
    ]

def generate(prompt: str, max_tokens_to_generate: int) -> str:
    """ 
    Given a text prompt, generates (max_tokens_to_generate) tokens.
    """
    output = gpt2(
        prompt, 
        max_new_tokens=max_tokens_to_generate, 
        num_return_sequences=1
        )[0]['generated_text']
    
    return output

def main(args: Any) -> None:
    # create gui
    gui = gradio.Interface(
        fn = generate, 
        inputs = [
            gradio.components.Textbox(
                lines = 1, 
                label = "Prompt",
                placeholder = "Enter Text… "),
            gradio.Slider(1, 128, value=16, label="Tokens", info="Number of tokens to generate")
            ], 
        outputs = gradio.components.Textbox(label="Generated Text"), 
        allow_flagging = "auto", 
        theme = 'gradio/soft',
        title = "Text Generation using GPT-2",
        examples = examples)

    # requests will be sent over a websocket instead
    gui.queue(
        # This parameter is used to set the number of worker threads in the Gradio 
        # server that will be processing your requests in parallel
        concurrency_count = 8,
        # Maximum number of requests that the queue processes
        # If a request arrives when the queue is already of the maximum size, 
        # it will not be allowed to join the queue and instead, the user will
        # receive an error saying that the queue is full and to try again
        max_size = 8, 
        # restrict all traffic to happen through the user interface
        # prevents programmatic requests
        api_open = False)

    # launch the gui
    gui.launch(share=args.share)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--share", help="whether to create a public link for sharing", action="store_true")
    args = parser.parse_args()
    main(args)

