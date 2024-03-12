from netmiko import ConnectHandler
import netmiko
import smtplib
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from datetime import datetime
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
import telegram
import json
from emoji import emojize
import emoji
from datetime import datetime
from datetime import date

current_time=datetime.now()
string = current_time.strftime('%H:%M:%S %p')
nowtime=current_time.strftime("%Y-%m-%d %H:%M:%S")
current_date=current_time.strftime("%d")
current_month=current_time.strftime("%m")
current_year=current_time.strftime("%Y")

#### token for bot:
bot_token = '1830492648:AAEWRM1Fb0egoXFYBOiy9nWNTgbYJE7-yiU'    #### change bot token
bot_chatID = '-435755743'   ### change chat id of user

def telegram_bot_sendtext(bot_message,bot_tokenid, bot_chatid):
    send_text = 'https://api.telegram.org/bot' + bot_tokenid + '/sendMessage?chat_id=' + bot_chatid + \
            '&parse_mode=Markdown&text=' + bot_message
    print (send_text)
    response = requests.get(send_text)
    return response.json()

bot = telegram.Bot(token=bot_token)
print (bot)
telegram_bot_sendtext("Hi Buddy!!! Welcome to My Testing!\n\U0001F643\U0001F643\U0001F643 MPLS Latency Program! \U0001F643\U0001F643\U0001F643",bot_token,bot_chatID)

#read file and get information
fp=open('ipaddress.txt','r+')
lines=fp.readlines()

for i in range(0,len(lines)):
    type=lines[i].split(",")[0]
    store=lines[i].split(",")[1]
    main=lines[i].split(",")[2]
    backup=lines[i].split(",")[3].rstrip()
#create devices
    device={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
          }

#Login and ping check
    net_connect=ConnectHandler(**device)
    print("Processing!!!!\n")

    command1="ping "+main+" repeat 3"
    send_command1 = net_connect.send_command_timing(command1)
    print(send_command1)
    result1 = send_command1.splitlines()[3].split()
    delay1 = result1[9]
    print(delay1)
    for ms in send_command1.splitlines():
        ms = delay1.split("/")
        min = ms[0]
        avg = ms[1]
        max = ms[2]
    print("Current Latency to "+store+" via Main Line [min/avg/max] - "+delay1+" ms\n")
    
    command2="ping "+backup+" repeat 3"
    send_command2 = net_connect.send_command_timing(command2)
    print(send_command2)
    result2 = send_command2.splitlines()[3].split()
    delay2 = result2[9]
    print(delay2)
    for ms in send_command1.splitlines():
        ms = delay1.split("/")
        min = ms[0]
        avg = ms[1]
        max = ms[2]
    print("Current Latency to "+store+" via Backup Line [min/avg/max] - "+delay2+" ms\n")

def start(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='Loading.....!!!!!')
    message="Current Latency to "+store+" via Main Line [min/avg/max] - "+delay1+" ms\nCurrent Latency to "+store+" via Backup Line [min/avg/max] - "+delay2+" ms\n"
    context.bot.send_message(chat_id = update.message.chat_id,text = message)

def emojis(update, context):
    msg = '\U0001F916 This_is_a_Robot_face!\n'
    msg += '\U0001F600 This is a smiling face!\n'
    msg += '\U0001F4AC This is a mail icon!\n'
    msg += '\U0001F90D\U0001F5A4\U0001F90E\U0001F9E1\U0001F49B\n'
    context.bot.send_message(chat_id = update.message.chat_id,text = msg)

def main():
    updater = Updater('1830492648:AAEWRM1Fb0egoXFYBOiy9nWNTgbYJE7-yiU')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('emojis',emojis))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


fromaddr = 'luutrungnguyen.crv01@gmail.com'
toaddr = 'trung.luu.nguyen@vn.centralretail.com'
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'MPLS Latency Checking'
msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("luutrungnguyen.crv01@gmail.com", "2112Daniel!@#")
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()
print("Send email completed! "+toaddr)
