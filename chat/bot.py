import gradio as gr


def create_chatbot():

    with gr.Blocks() as app:
        chatbot = gr.Chatbot(label="三月七")
        msg = gr.Textbox(label="聊天真君")
        clear = gr.ClearButton([msg, chatbot], value="清空会话")
        gr.Image(r"static/image/三月七.png", label="三月七")

        def respond(message, history):

            bot_message = bot_ask(message)
            history.append((message, bot_message))
            return "", history

        msg.submit(respond, [msg, chatbot], [msg, chatbot],)

    return app


def bot_ask(message):
    # TODO 接入AI模型
    return f'echo > {message}'
