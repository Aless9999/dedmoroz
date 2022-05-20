from flask import Flask, request
from flask import jsonify
import requests
import json


app = Flask(__name__)

URL = 'https://api.telegram.org/bot5019823751:AAE0K6MqTcVnaNqqujTTjXMfLS5Oa__JavQ/'


def main(URL):
    r = requests.get(URL + 'getMe')
    write_json(r.json())



def get_chat_id():
    r = requests.get(URL + 'getUpdates')
    r = r.json()
    chat_id = r ['result'][-1]['message']['chat']['id']
    return chat_id
    



def write_json(data, filname = 'answer.json'):
    with open(filname, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False) 



def send_message(chat_id, text='Text'):
    answer = {'chat_id': chat_id,
               'text': text}
    r= requests.post(URL + 'sendMessage', json=answer) 
    return r.json()          



@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        write_json(r)
        return jsonify(r)

    return 'Bot welcoms you!'





if __name__== '__main__':
    app.run()

    
    