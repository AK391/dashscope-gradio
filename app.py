import gradio as gr
import dashscope_gradio

gr.load(
    name='qvq-72b-preview',
    src=dashscope_gradio.registry,
).launch()
