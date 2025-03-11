from flask import Flask, request, jsonify
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os
import requests, json



app = Flask(__name__)

# Your Channel Access Token and Channel Secret
CHANNEL_ACCESS_TOKEN10 = os.environ['CHANNEL_ACCESS_TOKEN10']
CHANNEL_SECRET10 = os.environ['CHANNEL_SECRET10']

# # Your Channel Access Token and Channel Secret
# CHANNEL_ACCESS_TOKEN11 = os.environ['CHANNEL_ACCESS_TOKEN11']
# CHANNEL_SECRET11 = os.environ['CHANNEL_SECRET11']

# # Your Channel Access Token and Channel Secret
# CHANNEL_ACCESS_TOKEN3 = os.environ['CHANNEL_ACCESS_TOKEN3']
# CHANNEL_SECRET3 = os.environ['CHANNEL_SECRET3']

# # Your Channel Access Token and Channel Secret
# CHANNEL_ACCESS_TOKEN4 = os.environ['CHANNEL_ACCESS_TOKEN4']
# CHANNEL_SECRET4 = os.environ['CHANNEL_SECRET4']

# # Your Channel Access Token and Channel Secret
# CHANNEL_ACCESS_TOKEN5 = os.environ['CHANNEL_ACCESS_TOKEN5']
# CHANNEL_SECRET5 = os.environ['CHANNEL_SECRET5']

# # Your Channel Access Token and Channel Secret
# CHANNEL_ACCESS_TOKEN6 = os.environ['CHANNEL_ACCESS_TOKEN6']
# CHANNEL_SECRET6 = os.environ['CHANNEL_SECRET6']

# # Your Channel Access Token and Channel Secret
# CHANNEL_ACCESS_TOKEN7 = os.environ['CHANNEL_ACCESS_TOKEN7']
# CHANNEL_SECRET7 = os.environ['CHANNEL_SECRET7']

# # Your Channel Access Token and Channel Secret
# CHANNEL_ACCESS_TOKEN8 = os.environ['CHANNEL_ACCESS_TOKEN8']
# CHANNEL_SECRET8 = os.environ['CHANNEL_SECRET8']

# # Your Channel Access Token and Channel Secret
# CHANNEL_ACCESS_TOKEN9 = os.environ['CHANNEL_ACCESS_TOKEN9']
# CHANNEL_SECRET9 = os.environ['CHANNEL_SECRET9']



# Set up the LineBotApi and WebhookHandler
line_bot_api1 = LineBotApi(CHANNEL_ACCESS_TOKEN10)
handler1 = WebhookHandler(CHANNEL_SECRET10)

# # Set up the LineBotApi and WebhookHandler
# line_bot_api2 = LineBotApi(CHANNEL_ACCESS_TOKEN11)
# handler2 = WebhookHandler(CHANNEL_SECRET11)

# # Set up the LineBotApi and WebhookHandler
# line_bot_api3 = LineBotApi(CHANNEL_ACCESS_TOKEN3)
# handler3 = WebhookHandler(CHANNEL_SECRET3)

# # Set up the LineBotApi and WebhookHandler
# line_bot_api4 = LineBotApi(CHANNEL_ACCESS_TOKEN4)
# handler4 = WebhookHandler(CHANNEL_SECRET4)


# # Set up the LineBotApi and WebhookHandler
# line_bot_api5 = LineBotApi(CHANNEL_ACCESS_TOKEN5)
# handler5 = WebhookHandler(CHANNEL_SECRET5)

# # Set up the LineBotApi and WebhookHandler
# line_bot_api6 = LineBotApi(CHANNEL_ACCESS_TOKEN6)
# handler6 = WebhookHandler(CHANNEL_SECRET6)

# # Set up the LineBotApi and WebhookHandler
# line_bot_api7 = LineBotApi(CHANNEL_ACCESS_TOKEN7)
# handler7 = WebhookHandler(CHANNEL_SECRET7)

# # Set up the LineBotApi and WebhookHandler
# line_bot_api8 = LineBotApi(CHANNEL_ACCESS_TOKEN8)
# handler8 = WebhookHandler(CHANNEL_SECRET8)

# # Set up the LineBotApi and WebhookHandler
# line_bot_api9 = LineBotApi(CHANNEL_ACCESS_TOKEN9)
# handler9 = WebhookHandler(CHANNEL_SECRET9)



# Webhook to handle incoming messages from LINE
@app.route("/callback10", methods=['POST'])
def callback10():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler1.handle(body, signature)
    except Exception as e:
        print(f"Error: {e}")
        return 'Error', 400

    return 'OK', 200

# # Webhook to handle incoming messages from LINE
# @app.route("/callback11", methods=['POST'])
# def callback11():
#     signature = request.headers['X-Line-Signature']
#     body = request.get_data(as_text=True)

#     try:
#         handler2.handle(body, signature)
#     except Exception as e:
#         print(f"Error: {e}")
#         return 'Error', 400

#     return 'OK', 200

# #Webhook to handle incoming messages from LINE
# @app.route("/callback3", methods=['POST'])
# def callback3():
#     signature = request.headers['X-Line-Signature']
#     body = request.get_data(as_text=True)

#     try:
#         handler3.handle(body, signature)
#     except Exception as e:
#         print(f"Error: {e}")
#         return 'Error', 400

#     return 'OK', 200

# # Webhook to handle incoming messages from LINE
# @app.route("/callback4", methods=['POST'])
# def callback4():
#     signature = request.headers['X-Line-Signature']
#     body = request.get_data(as_text=True)

#     try:
#         handler4.handle(body, signature)
#     except Exception as e:
#         print(f"Error: {e}")
#         return 'Error', 400

#     return 'OK', 200

# # Webhook to handle incoming messages from LINE
# @app.route("/callback5", methods=['POST'])
# def callback5():
#     signature = request.headers['X-Line-Signature']
#     body = request.get_data(as_text=True)

#     try:
#         handler5.handle(body, signature)
#     except Exception as e:
#         print(f"Error: {e}")
#         return 'Error', 400

#     return 'OK', 200

# # Webhook to handle incoming messages from LINE
# @app.route("/callback6", methods=['POST'])
# def callback6():
#     signature = request.headers['X-Line-Signature']
#     body = request.get_data(as_text=True)

#     try:
#         handler6.handle(body, signature)
#     except Exception as e:
#         print(f"Error: {e}")
#         return 'Error', 400

#     return 'OK', 200

# # Webhook to handle incoming messages from LINE
# @app.route("/callback7", methods=['POST'])
# def callback7():
#     signature = request.headers['X-Line-Signature']
#     body = request.get_data(as_text=True)

#     try:
#         handler7.handle(body, signature)
#     except Exception as e:
#         print(f"Error: {e}")
#         return 'Error', 400

#     return 'OK', 200


# # Webhook to handle incoming messages from LINE
# @app.route("/callback8", methods=['POST'])
# def callback8():
#     signature = request.headers['X-Line-Signature']
#     body = request.get_data(as_text=True)

#     try:
#         handler8.handle(body, signature)
#     except Exception as e:
#         print(f"Error: {e}")
#         return 'Error', 400

#     return 'OK', 200


# # Webhook to handle incoming messages from LINE
# @app.route("/callback9", methods=['POST'])
# def callback9():
#     signature = request.headers['X-Line-Signature']
#     body = request.get_data(as_text=True)

#     try:
#         handler9.handle(body, signature)
#     except Exception as e:
#         print(f"Error: {e}")
#         return 'Error', 400

#     return 'OK', 200





# Event handler for receiving messages
@handler1.add(MessageEvent, message=TextMessage)
def handle_message1(event):
    # Extract the user ID (UUID) from the event
    user_id = event.source.user_id  # This is the user ID for the person interacting with the bot
    
    # Print the user ID (you can store it or use it as needed)
    print(f"User ID: {user_id}")

    # Respond to the user with a confirmation message
    line_bot_api1.reply_message(
        event.reply_token,
        TextMessage(text=f"Your User ID is: {user_id}")
    )

# # Event handler for receiving messages
# @handler2.add(MessageEvent, message=TextMessage)
# def handle_message2(event):
#     # Extract the user ID (UUID) from the event
#     user_id = event.source.user_id  # This is the user ID for the person interacting with the bot
    
#     # Print the user ID (you can store it or use it as needed)
#     print(f"User ID: {user_id}")

#     # Respond to the user with a confirmation message
#     line_bot_api2.reply_message(
#         event.reply_token,
#         TextMessage(text=f"Your User ID is: {user_id}")
#     )

# # Event handler for receiving messages
# @handler3.add(MessageEvent, message=TextMessage)
# def handle_message3(event):
#     # Extract the user ID (UUID) from the event
#     user_id = event.source.user_id  # This is the user ID for the person interacting with the bot
    
#     # Print the user ID (you can store it or use it as needed)
#     print(f"User ID: {user_id}")

#     # Respond to the user with a confirmation message
#     line_bot_api3.reply_message(
#         event.reply_token,
#         TextMessage(text=f"Your User ID is: {user_id}")
#     )

# # Event handler for receiving messages
# @handler4.add(MessageEvent, message=TextMessage)
# def handle_message4(event):
#     # Extract the user ID (UUID) from the event
#     user_id = event.source.user_id  # This is the user ID for the person interacting with the bot
    
#     # Print the user ID (you can store it or use it as needed)
#     print(f"User ID: {user_id}")

#     # Respond to the user with a confirmation message
#     line_bot_api4.reply_message(
#         event.reply_token,
#         TextMessage(text=f"Your User ID is: {user_id}")
#     )

# # Event handler for receiving messages
# @handler5.add(MessageEvent, message=TextMessage)
# def handle_message5(event):
#     # Extract the user ID (UUID) from the event
#     user_id = event.source.user_id  # This is the user ID for the person interacting with the bot
    
#     # Print the user ID (you can store it or use it as needed)
#     print(f"User ID: {user_id}")

#     # Respond to the user with a confirmation message
#     line_bot_api5.reply_message(
#         event.reply_token,
#         TextMessage(text=f"Your User ID is: {user_id}")
#     )

# # Event handler for receiving messages
# @handler6.add(MessageEvent, message=TextMessage)
# def handle_message6(event):
#     # Extract the user ID (UUID) from the event
#     user_id = event.source.user_id  # This is the user ID for the person interacting with the bot
    
#     # Print the user ID (you can store it or use it as needed)
#     print(f"User ID: {user_id}")

#     # Respond to the user with a confirmation message
#     line_bot_api6.reply_message(
#         event.reply_token,
#         TextMessage(text=f"Your User ID is: {user_id}")
#     )

# # Event handler for receiving messages
# @handler7.add(MessageEvent, message=TextMessage)
# def handle_message7(event):
#     # Extract the user ID (UUID) from the event
#     user_id = event.source.user_id  # This is the user ID for the person interacting with the bot
    
#     # Print the user ID (you can store it or use it as needed)
#     print(f"User ID: {user_id}")

#     # Respond to the user with a confirmation message
#     line_bot_api7.reply_message(
#         event.reply_token,
#         TextMessage(text=f"Your User ID is: {user_id}")
#     )

# # Event handler for receiving messages
# @handler8.add(MessageEvent, message=TextMessage)
# def handle_message8(event):
#     # Extract the user ID (UUID) from the event
#     user_id = event.source.user_id  # This is the user ID for the person interacting with the bot
    
#     # Print the user ID (you can store it or use it as needed)
#     print(f"User ID: {user_id}")

#     # Respond to the user with a confirmation message
#     line_bot_api8.reply_message(
#         event.reply_token,
#         TextMessage(text=f"Your User ID is: {user_id}")
#     )

# # Event handler for receiving messages
# @handler9.add(MessageEvent, message=TextMessage)
# def handle_message9(event):
#     # Extract the user ID (UUID) from the event
#     user_id = event.source.user_id  # This is the user ID for the person interacting with the bot
    
#     # Print the user ID (you can store it or use it as needed)
#     print(f"User ID: {user_id}")

#     # Respond to the user with a confirmation message
#     line_bot_api9.reply_message(
#         event.reply_token,
#         TextMessage(text=f"Your User ID is: {user_id}")
#     )






if __name__ == '__main__':
    app.run(debug=True)
