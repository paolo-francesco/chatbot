{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 AppleColorEmoji;}
{\colortbl;\red255\green255\blue255;\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c100000\c100000\c100000;}
\paperw11900\paperh16840\margl1440\margr1440\vieww20100\viewh12540\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import telepot\
from telepot.loop import MessageLoop\
\
# Replace '\expnd0\expndtw0\kerning0
6544954684:AAFOO7tG48gRFLtAFPVzD1iRguFh0exqaBY\kerning1\expnd0\expndtw0 ' with the actual API token you received from BotFather\
bot = telepot.Bot('\expnd0\expndtw0\kerning0
6544954684:AAFOO7tG48gRFLtAFPVzD1iRguFh0exqaBY\kerning1\expnd0\expndtw0 ')\
\
# This dictionary will store the available stock of vape pens\
stock = \{\
    '
\f1 \expnd0\expndtw0\kerning0
\uc0\u55358 \u57040 
\f0  Blueberry Kush - Indica\kerning1\expnd0\expndtw0 ': 33,\
    '
\f1 \expnd0\expndtw0\kerning0
\uc0\u55356 \u57118 
\f0  Sunset Sherbet - Hybrid\kerning1\expnd0\expndtw0 ':  34,\
    '
\f1 \expnd0\expndtw0\kerning0
\uc0\u55356 \u57200 
\f0  London Pound Cake - Hybrid\kerning1\expnd0\expndtw0 ': 31,\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0     '
\f1 \expnd0\expndtw0\kerning0
\uc0\u55356 \u57170 
\f0  Cherry Lime Haze - Hybrid\kerning1\expnd0\expndtw0 ': 36,\
    '
\f1 \expnd0\expndtw0\kerning0
\uc0\u55356 \u57165 
\f0  Pineapple Express - Hybrid\kerning1\expnd0\expndtw0 ': 32,\
    '
\f1 \expnd0\expndtw0\kerning0
\uc0\u55357 \u56401 
\f0  Royal Jelly - Hybrid\kerning1\expnd0\expndtw0 ': 10\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 \}\
\
def handle_message(msg):\
    content_type, chat_type, chat_id = telepot.glance(msg)\
    \
    if content_type == 'text':\
        command = msg['text']\
        if command == '/start':\
            bot.sendMessage(chat_id, "Welcome to the Vape Pen Store! Use /help to see available commands.")\
        elif command == '/help':\
            help_message = "Available commands:\\n"\
            help_message += "/start - Start the bot and receive a welcome message.\\n"\
            help_message += "/help - Display this help message.\\n"\
            help_message += "/stock - View available vape pens and quantities.\\n"\
            help_message += "/order [pen_name] - Place an order for a specific vape pen."\
            bot.sendMessage(chat_id, help_message)\
        elif command == '/stock':\
            stock_message = "Available Vape Pens:\\n"\
            for pen, quantity in stock.items():\
                stock_message += f"\{pen\}: \{quantity\} in stock\\n"\
            bot.sendMessage(chat_id, stock_message)\
        elif command.startswith('/order'):\
            _, pen_name = command.split(' ', 1)\
            if pen_name in stock:\
                if stock[pen_name] > 0:\
                    stock[pen_name] -= 1\
                    bot.sendMessage(chat_id, f"Your order for \{pen_name\} has been placed. Thank you!")\
                else:\
                    bot.sendMessage(chat_id, f"Sorry, \{pen_name\} is currently out of stock.")\
            else:\
                bot.sendMessage(chat_id, "Vape pen not found. Please check the available pens using /stock.")\
        else:\
            bot.sendMessage(chat_id, "Sorry, I don't understand that command. Use /help to see available commands.")\
\
# Start the message loop to continuously listen for incoming messages\
MessageLoop(bot, handle_message).run_as_thread()\
\
# Keep the program running\
while True:\
    pass\
}