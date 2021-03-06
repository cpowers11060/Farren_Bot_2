import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

app = Flask(__name__)

'''
Note that the group me message api is based on the following
dictionary:
{
  "attachments": [],
  "avatar_url": "http://i.groupme.com/123456789",
  "created_at": 1302623328,
  "group_id": "1234567890",
  "id": "1234567890",
  "name": "John",
  "sender_id": "12345",
  "sender_type": "user",
  "source_guid": "GUID",
  "system": false,
  "text": "Hello world ☃☃",
  "user_id": "1234567890"
}
'''

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  if 'hot' in data['text']:
    msg = 'Stay hot and beautiful, {}. I love you.'.format(data['name']
  # We don't want to reply to ourselves!
  #if data['name'] != 'Chris Farren Bot':
    #msg = '{}, you sent "{}".'.format(data['name'], data['text'])
    #send_message(msg)

  return "ok", 200






def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : os.getenv('GROUPME_BOT_ID'),
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
