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

import json
import urllib.request
import re

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

    addObj = re.search(r'(.*)のタスク追加', event.message.text)

    doneObj = re.search(r'(.*)のタスク完了', event.message.text)

    # print(event.message.text)

    if addObj:
        # print("match")
        # POST
        # postjson=json.dumps(
        #     {
        #         'user_id' : "jafkl23kh45l",
        #         'task_name' : addmatchObj[0][0],
        #         'task_info' : '洗濯物が溜まってきたのでそろそろ畳まないといけない',
        #         'time_limit' : {'year':2018, 'month':10, 'date':18}
        #     }
        # )

        url = "https://04f7bfe9.ngrok.io/tasks/jafkl23kh45l"
        method = "POST"
        headers = {"Content-Type" : "application/json"}

        # PythonオブジェクトをJSONに変換する
        obj = {
            'user_id' : "jafkl23kh45l",
            'task_name' : addObj.group(1),
            'task_info' : '洗濯物が溜まってきたのでそろそろ畳まないといけない',
            'time_limit' : {'year':2018, 'month':10, 'date':18}
            }

        json_data = json.dumps(obj).encode("utf-8")

        # httpリクエストを準備してPOST
        request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
        with urllib.request.urlopen(request) as response:
            response_body = response.read().decode("utf-8")

        #追加完了メッセージ
        message = [
            TextSendMessage(text=addObj.group(1) + 'を追加'),
            TextSendMessage(text='タスクを追加しました')
        ]

        line_bot_api.reply_message(
            event.reply_token,message
        )
    elif doneObj:
        #この処理は省略→#どのタスクを完了するか確認
        #line_bot_api.reply_message(event.reply_token,message=TextSendMessage(text='どのタスクを完了しますか？'))

        #DELETE
        url = "http://04f7bfe9.ngrok.io/tasks/jafkl23kh45l"

        method = "DELETE"
        headers = {"Content-Type" : "application/json"}

        obj = {
            'user_id' : "jafkl23kh45l",
            'task_name' : doneObj.group(1),
            }

        json_data = json.dumps(obj).encode("utf-8")

        # httpリクエストを準備してPOST
        request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
        with urllib.request.urlopen(request) as response:
            response_body = response.read().decode("utf-8")

        # 削除完了メッセージ
        message = [
            TextSendMessage(text=doneObj.group(1)+'を完了しました')
        ]

        line_bot_api.reply_message(
            event.reply_token,message
        )
    elif event.message.text == 'タスク一覧':
        #GET
        # url = 'https://04f7bfe9.ngrok.io/tasks/jafkl23kh45l'
        #
        # tasks={}
        # req = urllib.request.Request(url)
        # with urllib.request.urlopen(req) as res:
        #     tasks = res.read().decode("utf-8")
        #     # print(type(tasks))
        #
        # #一覧メッセージ
        # message = [
        #     TextSendMessage(text='タスク一覧です'),
        #     TextSendMessage(text=tasks),
        # ]

        url = 'https://04f7bfe9.ngrok.io/tasks/jafkl23kh45l'

        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as res:
            data = json.loads(res.read().decode("utf-8"))

        tasks = data['tasks']

        message = [
            TextSendMessage(text='タスク一覧です'),
        ]

        if tasks != [] or tasks != False:
            for task in tasks:
                message.append(TextSendMessage(text='・' + task['task_name']),)
                # print('・' + task['task_name'])
        else:
            message.append(TextSendMessage(text='タスクはありません'))

        line_bot_api.reply_message(
            event.reply_token,message
        )

    else:
        print("not match")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
