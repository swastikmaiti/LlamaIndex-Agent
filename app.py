import gradio as gr
from utils import get_agent

def create_agent(uploaded_pdf,user_state):
    agent = get_agent(uploaded_pdf)
    return {input_box: gr.Textbox(value="Ask a question", visible=True),
            state_var:[agent]}

def response_generator(text,user_state):
    print("Query: ",text)
    agent = user_state[0]
    response = agent.query(text)
    output = ""
    for text in response.response_gen:
        output+=text
        yield {output_box:output}

def submit():
    return {input_box: gr.Textbox(visible=True)}

with gr.Blocks() as demo:
    
    state_var = gr.State([])

    with gr.Row():
        upload_button = gr.UploadButton("📁 Upload PDF", file_types=[".pdf"])
    error_box = gr.Textbox(label="Error", visible=False)

    input_box = gr.Textbox(autoscroll=True,visible=False,label='User')
    output_box = gr.Textbox(autoscroll=True,max_lines=30,value="Output",label='Assistant')
    gr.Interface(fn=response_generator, inputs=[input_box,state_var], outputs=[output_box,state_var],delete_cache=(20,10))

    upload_button.upload(create_agent,inputs=[upload_button,state_var],outputs=[input_box,state_var],queue=False,show_progress=True,trigger_mode="once")
    upload_button.upload(submit,None,input_box)
    
demo.queue()
demo.launch(share=True)


