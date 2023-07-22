from chat import bot


if __name__ == '__main__':
    app = bot.create_chatbot()
    app.launch(share=True, favicon_path=r"static/favicon.ico")
