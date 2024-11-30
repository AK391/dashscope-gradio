import gradio as gr
import dashscope_gradio

gr.load(
    name='qwq-32b-preview',
    src=dashscope_gradio.registry,
).launch()