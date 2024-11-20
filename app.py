import gradio as gr
import dashscope_gradio

gr.load(
    name='qwen-turbo-latest',
    src=dashscope_gradio.registry,
).launch()