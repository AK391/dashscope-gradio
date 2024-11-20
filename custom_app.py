import gradio as gr
import dashscope_gradio

gr.load(
    name='qwen-turbo',
    src=dashscope_gradio.registry,
    title='DashScope-Gradio Integration',
    description="Chat with qwen-turbo model.",
    examples=["Explain quantum gravity to a 5-year old.", "How many R are there in the word Strawberry?"]
).launch()