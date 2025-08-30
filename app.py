import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from dotenv import load_dotenv

load_dotenv(override=True)

lin_dot_api = LineBotApi(os.getenv(["ACSECC_TOKEN"]))
handlr = wbHookHandler = os.getenv("ACSECC_TOKEN")

app = Flask(__name__)


@app.route("/")
def index():
    return "You call index()"

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        hanlder.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    
    return 'OK'
    


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))


 

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
