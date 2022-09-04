from flask import Flask, request
from linebot.models import *
from linebot import *

app = Flask(__name__)

line_bot_api = LineBotApi('fAUOsZ+4JtvBhy9AftYq4irrhJo1XfTUSJ7qcQurAyrr0WsURc6fOnFgHaD3tySs9W/qIh+1igd+NMlaMG6h5vPRihd30gZ2JebgDsaWHJIHgFm2d4w+UsR6hzQce32HjGwf+O/gaD5zO+OyeUyPMwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9a9e8827e193aa5562d987e27e5ae8b9')

@app.route("/callback", methods=['POST'])
def callback():
    body = request.get_data(as_text=True)
    # print(body)
    req = request.get_json(silent=True, force=True)
    intent = req["queryResult"]["intent"]["displayName"]
    text = req['originalDetectIntentRequest']['payload']['data']['message']['text']
    reply_token = req['originalDetectIntentRequest']['payload']['data']['replyToken']
    id = req['originalDetectIntentRequest']['payload']['data']['source']['userId']
    disname = line_bot_api.get_profile(id).display_name

    print('id = ' + id)
    print('name = ' + disname)
    print('text = ' + text)
    print('intent = ' + intent)
    print('reply_token = ' + reply_token)

    reply(intent,text,reply_token,id,disname)

    return 'OK'


def reply(intent,text,reply_token,id,disname):
    if intent == 'intent 5':
        text_message = TextSendMessage(text='ทดสอบสำเร็จแล้ว')
        line_bot_api.reply_message(reply_token,text_message)

if __name__ == "__main__":
    app.run()


# Fix bugs part
@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


if __name__ == '__main__':
    app.run(debug=True)
