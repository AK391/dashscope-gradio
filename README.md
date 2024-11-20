# `dashscope-gradio`

is a Python package that makes it very easy for developers to create machine learning apps that are powered by DashScope's API.

# Installation 

You can install `dashscope-gradio` directly using pip:

```bash
pip install dashscope-gradio
```

That's it! 

# Basic Usage

Just like if you were to use the `dashscope` API, you should first save your DashScope API key to this environment variable:

```
export DASHSCOPE_API_KEY=<your token>
```

Then in a Python file, write:

```python
import gradio as gr
import dashscope_gradio

gr.load(
    name='qwen-turbo',
    src=dashscope_gradio.registry,
).launch()
```

Run the Python file, and you should see a Gradio Interface connected to the model on DashScope!

![ChatInterface](chatinterface.png)

# Customization 

Once you can create a Gradio UI from a DashScope endpoint, you can customize it by setting your own input and output components, or any other arguments to `gr.Interface`. For example, the screenshot below was generated with:

```py
import gradio as gr
import dashscope_gradio

gr.load(
    name='qwen-turbo',
    src=dashscope_gradio.registry,
    title='DashScope-Gradio Integration',
    description="Chat with Qwen-turbo model.",
    examples=["Explain quantum gravity to a 5-year old.", "How many R are there in the word Strawberry?"]
).launch()
```
![ChatInterface with customizations](chatinterface_with_customization.png)

# Composition

Or use your loaded Interface within larger Gradio Web UIs, e.g.

```python
import gradio as gr
import dashscope_gradio

with gr.Blocks() as demo:
    with gr.Tab("Qwen-turbo"):
        gr.load('qwen-turbo', src=dashscope_gradio.registry)
    with gr.Tab("Qwen-plus"):
        gr.load('qwen-plus', src=dashscope_gradio.registry)

demo.launch()
```

# Under the Hood

The `dashscope-gradio` Python library has two dependencies: `dashscope` and `gradio`. It defines a "registry" function `dashscope_gradio.registry`, which takes in a model name and returns a Gradio app.

# Supported Models in DashScope

All chat API models supported by DashScope are compatible with this integration. For a comprehensive list of available models and their specifications, please refer to the [DashScope Models documentation](https://help.aliyun.com/zh/dashscope/developer-reference/model-overview).

-------

Note: if you are getting a 401 authentication error, then the DashScope API Client is not able to get the API token from the environment variable. This happened to me as well, in which case save it in your Python session, like this:

```python
import os

os.environ["DASHSCOPE_API_KEY"] = ...
```