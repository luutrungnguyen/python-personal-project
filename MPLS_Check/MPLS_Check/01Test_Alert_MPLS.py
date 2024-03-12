from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
import telegram
import json
from emoji import emojize
import emoji

from datetime import datetime
from datetime import date

fp=open('mpls1.txt','r+')
lines=fp.readlines()

#### token for bot:
bot_token = '1939837867:AAGC8KI7LeFrHDEjYK9eHgGHfoncR4Egw3c'    #### change bot token
bot_chatID = '-546033511'   ### change chat id of user

def telegram_bot_sendtext(bot_message,bot_tokenid, bot_chatid):
    send_text = 'https://api.telegram.org/bot' + bot_tokenid + '/sendMessage?chat_id=' + bot_chatid + \
            '&parse_mode=Markdown&text=' + bot_message
    print (send_text)
    response = requests.get(send_text)
    return response.json()

bot = telegram.Bot(token=bot_token)
print (bot)
telegram_bot_sendtext("Hi Buddy!!! Welcome to My Testing!\n\U0001F691\U0001F691\U0001F691 Báo sự cố MPLS or FTTH??? \U0001F691\U0001F691\U0001F691",bot_token,bot_chatID)

def MPLS(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U0001F44B\U0001F44B\U0001F44B Hello Guy! Please input STORES CODE \U0001F44B\U0001F44B\U0001F44B')
    telegram_bot_sendtext('\U0001F916 Example: TRA VINH - TraVinh, BEN TRE - BenTre, HUE - Hue, Ha Noi WH - KhoHaNoi, SSC Office - SSC...',bot_token,bot_chatID)

###ThangLong------------------
def ThangLong(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Thăng Long Store! \U000026A0\U000026A0\U000026A0')
    id_temp='ThangLong'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###TheGarden------------------
def TheGarden(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin The Garden Store! \U000026A0\U000026A0\U000026A0')
    id_temp='TheGarden'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###LongBien------------------
def LongBien(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Long Biên Store! \U000026A0\U000026A0\U000026A0')
    id_temp='LongBien'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###MeLinh------------------
def MeLinh(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Mê Linh Store! \U000026A0\U000026A0\U000026A0')
    id_temp='MeLinh'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###HaDong------------------
def HaDong(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Hà Đông Store! \U000026A0\U000026A0\U000026A0')
    id_temp='HaDong'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###LeTrongTan------------------
def LeTrongTan(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Lê Trọng Tấn Store! \U000026A0\U000026A0\U000026A0')
    id_temp='LeTrongTan'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###KhoHaNoi------------------
def KhoHaNoi(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Hà Nội WH! \U000026A0\U000026A0\U000026A0')
    id_temp='KhoHaNoi'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###HaiDuong------------------
def HaiDuong(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Hải Dương Store! \U000026A0\U000026A0\U000026A0')
    id_temp='HaiDuong'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###HaiPhong------------------
def HaiPhong(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Hải Phòng Store! \U000026A0\U000026A0\U000026A0')
    id_temp='HaiPhong'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###HaLong------------------
def HaLong(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Hạ Long Store! \U000026A0\U000026A0\U000026A0')
    id_temp='HaLong'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###NamDinh------------------
def NamDinh(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Nam Định Store! \U000026A0\U000026A0\U000026A0')
    id_temp='NamDinh'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###VinhPhuc------------------
def VinhPhuc(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Vĩnh Phúc Store! \U000026A0\U000026A0\U000026A0')
    id_temp='VinhPhuc'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###NinhBinh------------------
def NinhBinh(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Binh Bình Store! \U000026A0\U000026A0\U000026A0')
    id_temp='NinhBinh'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###ThanhHoa------------------
def ThanhHoa(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Thanh Hóa Store! \U000026A0\U000026A0\U000026A0')
    id_temp='ThanhHoa'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###VietTri------------------
def VietTri(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Việt Trì Store! \U000026A0\U000026A0\U000026A0')
    id_temp='VietTri'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###BacGiang------------------
def BacGiang(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Bắc Giang Store! \U000026A0\U000026A0\U000026A0')
    id_temp='BacGiang'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###DaLat------------------
def DaLat(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Đà Lạt Store! \U000026A0\U000026A0\U000026A0')
    id_temp='DaLat'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###KhoDaLat------------------
def KhoDaLat(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Đà Lạt WH! \U000026A0\U000026A0\U000026A0')
    id_temp='KhoDaLat'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###QuyNhon------------------
def QuyNhon(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Quy Nhơn Store! \U000026A0\U000026A0\U000026A0')
    id_temp='QuyNhon'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###Hue------------------
def Hue(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Huế Store! \U000026A0\U000026A0\U000026A0')
    id_temp='Hue'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###NhaTrang------------------
def NhaTrang(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Nha Trang Store! \U000026A0\U000026A0\U000026A0')
    id_temp='NhaTrang'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###Vinh------------------
def Vinh(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Vinh Store! \U000026A0\U000026A0\U000026A0')
    id_temp='Vinh'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###DongNai------------------
def DongNai(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Đồng Nai Store! \U000026A0\U000026A0\U000026A0')
    id_temp='DongNai'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###TanHiep------------------
def TanHiep(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Tân Hiệp Store! \U000026A0\U000026A0\U000026A0')
    id_temp='TanHiep'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###BinhDuong------------------
def BinhDuong(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Bình Dương Store! \U000026A0\U000026A0\U000026A0')
    id_temp='BinhDuong'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###DiAn------------------
def DiAn(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Dĩ An Store! \U000026A0\U000026A0\U000026A0')
    id_temp='DiAn'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###CanTho------------------
def CanTho(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Cần Thơ Store! \U000026A0\U000026A0\U000026A0')
    id_temp='CanTho'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###MyTho------------------
def MyTho(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Mỹ Tho Store! \U000026A0\U000026A0\U000026A0')
    id_temp='MyTho'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###DaNang------------------
def DaNang(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Đà Nẵng Store! \U000026A0\U000026A0\U000026A0')
    id_temp='DaNang'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###SSC------------------
def SSC(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin SSC Office! \U000026A0\U000026A0\U000026A0')
    id_temp='SSC'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###AnLac------------------
def AnLac(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin An Lạc Store! \U000026A0\U000026A0\U000026A0')
    id_temp='AnLac'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###TruongChinh------------------
def TruongChinh(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Trường Chinh Store! \U000026A0\U000026A0\U000026A0')
    id_temp='TruongChinh'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###MienDong------------------
def MienDong(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Miền Đông Store! \U000026A0\U000026A0\U000026A0')
    id_temp='MienDong'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###GoVap------------------
def GoVap(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Gò Vấp Store! \U000026A0\U000026A0\U000026A0')
    id_temp='GoVap'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###PhuThanh------------------
def PhuThanh(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Phú Thạnh Store! \U000026A0\U000026A0\U000026A0')
    id_temp='PhuThanh'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###AnPhu------------------
def AnPhu(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin An Phú Store! \U000026A0\U000026A0\U000026A0')
    id_temp='AnPhu'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###NguyenThiThap------------------
def NguyenThiThap(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Nguyễn Thị Thập Store! \U000026A0\U000026A0\U000026A0')
    id_temp='NguyenThiThap'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###ThaoDien------------------
def ThaoDien(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Thảo Điền Store! \U000026A0\U000026A0\U000026A0')
    id_temp='ThaoDien'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###AuCo------------------
def AuCo(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Âu Cơ Store! \U000026A0\U000026A0\U000026A0')
    id_temp='AuCo'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###QuangNgai------------------
def QuangNgai(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Quảng Ngải Store! \U000026A0\U000026A0\U000026A0')
    id_temp='QuangNgai'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###TraVinh------------------
def TraVinh(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Trà Vinh Store! \U000026A0\U000026A0\U000026A0')
    id_temp='TraVinh'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###BuonMeThuot------------------
def BuonMeThuot(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Buôn Mê Thuột Store! \U000026A0\U000026A0\U000026A0')
    id_temp='BuonMeThuot'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###FISService------------------
def FISService(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin MPLS Line FIS Services! \U000026A0\U000026A0\U000026A0')
    id_temp='FISService'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###TamKy------------------
def TamKy(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Tam Kỳ Store! \U000026A0\U000026A0\U000026A0')
    id_temp='TamKy'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###NguyenXien------------------
def NguyenXien(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Nguyễn Xiển Store! \U000026A0\U000026A0\U000026A0')
    id_temp='NguyenXien'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###BenTre------------------
def BenTre(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Bến Tre Store! \U000026A0\U000026A0\U000026A0')
    id_temp='BenTre'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)
###ThaiNguyen------------------
def ThaiNguyen(update, context):
    context.bot.sendMessage(chat_id = update.message.chat_id, text='\U000026A0\U000026A0\U000026A0 Thông tin Thái Nguyên Store! \U000026A0\U000026A0\U000026A0')
    id_temp='ThaiNguyen'
    for i in range(0,len(lines)):
        if id_temp in lines[i]:
            id1=lines[i].split(",")[0]
            shd1=lines[i].split(",")[1]
            shd2=lines[i].split(",")[2]
            isp1=lines[i].split(",")[3]
            add1=lines[i].split(",")[4]
            contact=lines[i].split(",")[5]
            sdt=lines[i].split(",")[6]

            print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd2+"\nĐịa chỉ: "+add1+"\nContact: "+contact+" - "+sdt)
            output="\U00002709\U00002709\U00002709 MESSAGE Content \U00002709\U00002709\U00002709\nMail to: haint78@viettel.com.vn; cskhdn@viettel.com.vn\nDear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: "+shd1+"\nSecondary Line: "+shd2+"\nAddress: "+add1+"\nContact : "+contact+" - "+sdt+"\n\n\U00002709\U00002709\U00002709 Thanks & Best Regard! \U00002709\U00002709\U00002709"
            context.bot.send_message(chat_id = update.message.chat_id,text = output)

def emojis(update, context):
    msg = '\U0001F916 This_is_a_Robot_face!\n'
    msg += '\U0001F600 This is a smiling face!\n'
    msg += '\U0001F4AC This is a mail icon!\n'
    msg += '\U0001F90D\U0001F5A4\U0001F90E\U0001F9E1\U0001F49B\n'
    context.bot.send_message(chat_id = update.message.chat_id,text = msg)

def main():
    updater = Updater('1939837867:AAGC8KI7LeFrHDEjYK9eHgGHfoncR4Egw3c')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('ThangLong',ThangLong))
    dp.add_handler(CommandHandler('TheGarden',TheGarden))
    dp.add_handler(CommandHandler('LongBien',LongBien))
    dp.add_handler(CommandHandler('MeLinh',MeLinh))
    dp.add_handler(CommandHandler('HaDong',HaDong))
    dp.add_handler(CommandHandler('LeTrongTan',LeTrongTan))
    dp.add_handler(CommandHandler('KhoHaNoi',KhoHaNoi))
    dp.add_handler(CommandHandler('HaiDuong',HaiDuong))
    dp.add_handler(CommandHandler('HaiPhong',HaiPhong))
    dp.add_handler(CommandHandler('NamDinh',NamDinh))
    dp.add_handler(CommandHandler('HaLong',HaLong))
    dp.add_handler(CommandHandler('VinhPhuc',VinhPhuc))
    dp.add_handler(CommandHandler('NinhBinh',NinhBinh))
    dp.add_handler(CommandHandler('ThanhHoa',ThanhHoa))
    dp.add_handler(CommandHandler('VietTri',VietTri))
    dp.add_handler(CommandHandler('BacGiang',BacGiang))
    dp.add_handler(CommandHandler('DaLat',DaLat))
    dp.add_handler(CommandHandler('KhoDaLat',KhoDaLat))
    dp.add_handler(CommandHandler('QuyNhon',QuyNhon))
    dp.add_handler(CommandHandler('Hue',Hue))
    dp.add_handler(CommandHandler('NhaTrang',NhaTrang))
    dp.add_handler(CommandHandler('Vinh',Vinh))
    dp.add_handler(CommandHandler('DongNai',DongNai))
    dp.add_handler(CommandHandler('TanHiep',TanHiep))
    dp.add_handler(CommandHandler('BinhDuong',BinhDuong))
    dp.add_handler(CommandHandler('DiAn',DiAn))
    dp.add_handler(CommandHandler('CanTho',CanTho))
    dp.add_handler(CommandHandler('MyTho',MyTho))
    dp.add_handler(CommandHandler('DaNang',DaNang))
    dp.add_handler(CommandHandler('SSC',SSC))
    dp.add_handler(CommandHandler('AnLac',AnLac))
    dp.add_handler(CommandHandler('TruongChinh',TruongChinh))
    dp.add_handler(CommandHandler('MienDong',MienDong))
    dp.add_handler(CommandHandler('GoVap',GoVap))
    dp.add_handler(CommandHandler('PhuThanh',PhuThanh))
    dp.add_handler(CommandHandler('AnPhu',AnPhu))
    dp.add_handler(CommandHandler('NguyenThiThap',NguyenThiThap))
    dp.add_handler(CommandHandler('ThaoDien',ThaoDien))
    dp.add_handler(CommandHandler('AuCo',AuCo))
    dp.add_handler(CommandHandler('QuangNgai',QuangNgai))
    dp.add_handler(CommandHandler('TraVinh',TraVinh))
    dp.add_handler(CommandHandler('BuonMeThuot',BuonMeThuot))
    dp.add_handler(CommandHandler('FISService',FISService))
    dp.add_handler(CommandHandler('TamKy',TamKy))
    dp.add_handler(CommandHandler('NguyenXien',NguyenXien))
    dp.add_handler(CommandHandler('BenTre',BenTre))
    dp.add_handler(CommandHandler('ThaiNguyen',ThaiNguyen))
    dp.add_handler(CommandHandler('MPLS',MPLS))
    dp.add_handler(CommandHandler('emojis',emojis))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
