import gradio as gr
import dashscope_gradio

with gr.Blocks() as demo:
    with gr.Tab("Qwen-turbo"):
        gr.load('qwen-turbo', src=dashscope_gradio.registry)
    with gr.Tab("GPT-3.5-turbo"):
        gr.load('gpt-3.5-turbo', src=dashscope_gradio.registry)

demo.launch()