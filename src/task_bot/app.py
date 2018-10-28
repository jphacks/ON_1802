from flask import Flask, request, abort
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

# 環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=event.message.text))

    if event.message.text == 'タスク追加':
        # POST

        #追加完了メッセージ
        message = [
            TextSendMessage(text='洗濯を追加'),
            TextSendMessage(text='タスクを追加しました')
        ]

        line_bot_api.reply_message(
            event.reply_token,message
        )
    elif event.message.text == 'タスク完了':
        #DELETE
        
        #追加完了メッセージ
        message = [
            TextSendMessage(text='洗濯を完了しました')
        ]

        line_bot_api.reply_message(
            event.reply_token,message
        )
    elif event.message.text == 'タスク一覧':
        #GET

        #一覧メッセージ
        message = [
            TextSendMessage(text='タスク一覧です'),
            
        ]

        line_bot_api.reply_message(
            event.reply_token,message
        )

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
