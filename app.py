from flask import Flask, request, jsonify
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os
import requests, json



app = Flask(__name__)

# Your Channel Access Token and Channel Secret
CHANNEL_ACCESS_TOKEN = os.environ['CHANNEL_ACCESS_TOKEN']
CHANNEL_SECRET = os.environ['CHANNEL_SECRET']

# Set up the LineBotApi and WebhookHandler
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

# Webhook to handle incoming messages from LINE
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except Exception as e:
        print(f"Error: {e}")
        return 'Error', 400

    return 'OK', 200

# Event handler for receiving messages
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # Extract the user ID (UUID) from the event
    user_id = event.source.user_id  # This is the user ID for the person interacting with the bot
    
    # Print the user ID (you can store it or use it as needed)
    print(f"User ID: {user_id}")

    # Respond to the user with a confirmation message
    line_bot_api.reply_message(
        event.reply_token,
        TextMessage(text=f"Your User ID is: {user_id}")
    )

if __name__ == '__main__':
    app.run(debug=True)
