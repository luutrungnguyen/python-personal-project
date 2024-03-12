from tkinter import *
from tkinter import filedialog
from netmiko import ConnectHandler
import netmiko
import smtplib
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
from datetime import datetime
from tkinter import ttk
from time import strftime
from datetime import date
import time
import sys
import os
import tkinter.font
from colorama import Fore, Back, Style


current_time=datetime.now()
string = current_time.strftime('%H:%M:%S %p')
nowtime=current_time.strftime("%Y-%m-%d %H:%M:%S")
current_date=current_time.strftime("%d")
current_month=current_time.strftime("%m")
current_year=current_time.strftime("%Y")

root = Tk()
#root.withdraw()
root.title('Lookup Information Tool')
#root.iconbitmap()
root.geometry("700x550")
img=PhotoImage(file='logo.png')
image=PhotoImage(file='icon.png')
root.configure(bg='orange')
# define background
#background=PhotoImage(file='trungnl.png')
#my_bg = Label(root, image = background)
#my_bg.place(x=0, y=0, relwidth=1, relheight=1)
root.iconphoto(False, image)
Label(root,image=img, bg="orange").pack()
i = int(0)
output=''




def internet():   
    fp=open('total_infor1.txt','r+')
    lines=fp.readlines()
    select = Choices.get()
    if (select == bigcstoresChoices[0]):
        ip_ftth=lines[0].split(",")[0]
        acc_ftth=lines[0].split(",")[1]
        isp_ftth=lines[0].split(",")[2]
        store=lines[0].split(",")[3]
        address=lines[0].split(",")[7]
        contact=lines[0].split(",")[8]       
        sdt=lines[0].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[1]):
        ip_ftth=lines[1].split(",")[0]
        acc_ftth=lines[1].split(",")[1]
        isp_ftth=lines[1].split(",")[2]
        store=lines[1].split(",")[3]
        address=lines[1].split(",")[7]
        contact=lines[1].split(",")[8]
        sdt=lines[1].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)
    if (select == bigcstoresChoices[2]):
        ip_ftth=lines[2].split(",")[0]
        acc_ftth=lines[2].split(",")[1]
        isp_ftth=lines[2].split(",")[2]
        store=lines[2].split(",")[3]
        address=lines[2].split(",")[7]
        contact=lines[2].split(",")[8]
        sdt=lines[2].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)

    if (select == bigcstoresChoices[3]):
        ip_ftth=lines[3].split(",")[0]
        acc_ftth=lines[3].split(",")[1]
        isp_ftth=lines[3].split(",")[2]
        store=lines[3].split(",")[3]
        address=lines[3].split(",")[7]
        contact=lines[3].split(",")[8]
        sdt=lines[3].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)

    if (select == bigcstoresChoices[4]):
        ip_ftth=lines[4].split(",")[0]
        acc_ftth=lines[4].split(",")[1]
        isp_ftth=lines[4].split(",")[2]
        store=lines[4].split(",")[3]
        address=lines[4].split(",")[7]
        contact=lines[4].split(",")[8]
        sdt=lines[4].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)  

    if (select == bigcstoresChoices[5]):
        ip_ftth=lines[5].split(",")[0]
        acc_ftth=lines[5].split(",")[1]
        isp_ftth=lines[5].split(",")[2]
        store=lines[5].split(",")[3]
        address=lines[5].split(",")[7]
        contact=lines[5].split(",")[8]
        sdt=lines[5].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[6]):
        ip_ftth=lines[6].split(",")[0]
        acc_ftth=lines[6].split(",")[1]
        isp_ftth=lines[6].split(",")[2]
        store=lines[6].split(",")[3]
        address=lines[6].split(",")[7]
        contact=lines[6].split(",")[8]
        sdt=lines[6].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[7]):
        ip_ftth=lines[7].split(",")[0]
        acc_ftth=lines[7].split(",")[1]
        isp_ftth=lines[7].split(",")[2]
        store=lines[7].split(",")[3]
        address=lines[7].split(",")[7]
        contact=lines[7].split(",")[8]
        sdt=lines[7].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[8]):
        ip_ftth=lines[8].split(",")[0]
        acc_ftth=lines[8].split(",")[1]
        isp_ftth=lines[8].split(",")[2]
        store=lines[8].split(",")[3]
        address=lines[8].split(",")[7]
        contact=lines[8].split(",")[8]
        sdt=lines[8].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)

    if (select == bigcstoresChoices[9]):
        ip_ftth=lines[9].split(",")[0]
        acc_ftth=lines[9].split(",")[1]
        isp_ftth=lines[9].split(",")[2]
        store=lines[9].split(",")[3]
        address=lines[9].split(",")[7]
        contact=lines[9].split(",")[8]
        sdt=lines[9].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[10]):
        ip_ftth=lines[10].split(",")[0]
        acc_ftth=lines[10].split(",")[1]
        isp_ftth=lines[10].split(",")[2]
        store=lines[10].split(",")[3]
        address=lines[10].split(",")[7]
        contact=lines[10].split(",")[8]
        sdt=lines[10].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[11]):
        ip_ftth=lines[11].split(",")[0]
        acc_ftth=lines[11].split(",")[1]
        isp_ftth=lines[11].split(",")[2]
        store=lines[11].split(",")[3]
        address=lines[11].split(",")[7]
        contact=lines[11].split(",")[8]
        sdt=lines[11].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)   

    if (select == bigcstoresChoices[12]):
        ip_ftth=lines[12].split(",")[0]
        acc_ftth=lines[12].split(",")[1]
        isp_ftth=lines[12].split(",")[2]
        store=lines[12].split(",")[3]
        address=lines[12].split(",")[7]
        contact=lines[12].split(",")[8]
        sdt=lines[12].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)   

    if (select == bigcstoresChoices[13]):
        ip_ftth=lines[13].split(",")[0]
        acc_ftth=lines[13].split(",")[1]
        isp_ftth=lines[13].split(",")[2]
        store=lines[13].split(",")[3]
        address=lines[13].split(",")[7]
        contact=lines[13].split(",")[8]
        sdt=lines[13].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[14]):
        ip_ftth=lines[14].split(",")[0]
        acc_ftth=lines[14].split(",")[1]
        isp_ftth=lines[14].split(",")[2]
        store=lines[14].split(",")[3]
        address=lines[14].split(",")[7]
        contact=lines[14].split(",")[8]
        sdt=lines[14].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[15]):
        ip_ftth=lines[15].split(",")[0]
        acc_ftth=lines[15].split(",")[1]
        isp_ftth=lines[15].split(",")[2]
        store=lines[15].split(",")[3]
        address=lines[15].split(",")[7]
        contact=lines[15].split(",")[8]
        sdt=lines[15].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[16]):
        ip_ftth=lines[16].split(",")[0]
        acc_ftth=lines[16].split(",")[1]
        isp_ftth=lines[16].split(",")[2]
        store=lines[16].split(",")[3]
        address=lines[16].split(",")[7]
        contact=lines[16].split(",")[8]
        sdt=lines[16].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)   

    if (select == bigcstoresChoices[17]):
        ip_ftth=lines[17].split(",")[0]
        acc_ftth=lines[17].split(",")[1]
        isp_ftth=lines[17].split(",")[2]
        store=lines[17].split(",")[3]
        address=lines[17].split(",")[7]
        contact=lines[17].split(",")[8]
        sdt=lines[17].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[18]):
        ip_ftth=lines[18].split(",")[0]
        acc_ftth=lines[18].split(",")[1]
        isp_ftth=lines[18].split(",")[2]
        store=lines[18].split(",")[3]
        address=lines[18].split(",")[7]
        contact=lines[18].split(",")[8]
        sdt=lines[18].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)  

    if (select == bigcstoresChoices[19]):
        ip_ftth=lines[19].split(",")[0]
        acc_ftth=lines[19].split(",")[1]
        isp_ftth=lines[19].split(",")[2]
        store=lines[19].split(",")[3]
        address=lines[19].split(",")[7]
        contact=lines[19].split(",")[8]
        sdt=lines[19].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[20]):
        ip_ftth=lines[20].split(",")[0]
        acc_ftth=lines[20].split(",")[1]
        isp_ftth=lines[20].split(",")[2]
        store=lines[20].split(",")[3]
        address=lines[20].split(",")[7]
        contact=lines[20].split(",")[8]
        sdt=lines[20].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[21]):
        ip_ftth=lines[21].split(",")[0]
        acc_ftth=lines[21].split(",")[1]
        isp_ftth=lines[21].split(",")[2]
        store=lines[21].split(",")[3]
        address=lines[21].split(",")[7]
        contact=lines[21].split(",")[8]
        sdt=lines[21].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[22]):
        ip_ftth=lines[22].split(",")[0]
        acc_ftth=lines[22].split(",")[1]
        isp_ftth=lines[22].split(",")[2]
        store=lines[22].split(",")[3]
        address=lines[22].split(",")[7]
        contact=lines[22].split(",")[8]
        sdt=lines[22].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[23]):
        ip_ftth=lines[23].split(",")[0]
        acc_ftth=lines[23].split(",")[1]
        isp_ftth=lines[23].split(",")[2]
        store=lines[23].split(",")[3]
        address=lines[23].split(",")[7]
        contact=lines[23].split(",")[8]
        sdt=lines[23].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[24]):
        ip_ftth=lines[24].split(",")[0]
        acc_ftth=lines[24].split(",")[1]
        isp_ftth=lines[24].split(",")[2]
        store=lines[24].split(",")[3]
        address=lines[24].split(",")[7]
        contact=lines[24].split(",")[8]
        sdt=lines[24].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)    

    if (select == bigcstoresChoices[25]):
        ip_ftth=lines[25].split(",")[0]
        acc_ftth=lines[25].split(",")[1]
        isp_ftth=lines[25].split(",")[2]
        store=lines[25].split(",")[3]
        address=lines[25].split(",")[7]
        contact=lines[25].split(",")[8]
        sdt=lines[25].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)  

    if (select == bigcstoresChoices[26]):
        ip_ftth=lines[26].split(",")[0]
        acc_ftth=lines[26].split(",")[1]
        isp_ftth=lines[26].split(",")[2]
        store=lines[26].split(",")[3]
        address=lines[26].split(",")[7]
        contact=lines[26].split(",")[8]
        sdt=lines[26].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)  

    if (select == bigcstoresChoices[27]):
        ip_ftth=lines[27].split(",")[0]
        acc_ftth=lines[27].split(",")[1]
        isp_ftth=lines[27].split(",")[2]
        store=lines[27].split(",")[3]
        address=lines[27].split(",")[7]
        contact=lines[27].split(",")[8]
        sdt=lines[27].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)  

    if (select == bigcstoresChoices[28]):
        ip_ftth=lines[28].split(",")[0]
        acc_ftth=lines[28].split(",")[1]
        isp_ftth=lines[28].split(",")[2]
        store=lines[28].split(",")[3]
        address=lines[28].split(",")[7]
        contact=lines[28].split(",")[8]
        sdt=lines[28].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[29]):
        ip_ftth=lines[29].split(",")[0]
        acc_ftth=lines[29].split(",")[1]
        isp_ftth=lines[29].split(",")[2]
        store=lines[29].split(",")[3]
        address=lines[29].split(",")[7]
        contact=lines[29].split(",")[8]
        sdt=lines[29].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[30]):
        ip_ftth=lines[30].split(",")[0]
        acc_ftth=lines[30].split(",")[1]
        isp_ftth=lines[30].split(",")[2]
        store=lines[30].split(",")[3]
        address=lines[30].split(",")[7]
        contact=lines[30].split(",")[8]
        sdt=lines[30].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[31]):
        ip_ftth=lines[31].split(",")[0]
        acc_ftth=lines[31].split(",")[1]
        isp_ftth=lines[31].split(",")[2]
        store=lines[31].split(",")[3]
        address=lines[31].split(",")[7]
        contact=lines[31].split(",")[8]
        sdt=lines[31].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[32]):
        ip_ftth=lines[32].split(",")[0]
        acc_ftth=lines[32].split(",")[1]
        isp_ftth=lines[32].split(",")[2]
        store=lines[32].split(",")[3]
        address=lines[32].split(",")[7]
        contact=lines[32].split(",")[8]
        sdt=lines[32].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[33]):
        ip_ftth=lines[33].split(",")[0]
        acc_ftth=lines[33].split(",")[1]
        isp_ftth=lines[33].split(",")[2]
        store=lines[33].split(",")[3]
        address=lines[33].split(",")[7]
        contact=lines[33].split(",")[8]
        sdt=lines[33].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)

    if (select == bigcstoresChoices[34]):
        ip_ftth=lines[34].split(",")[0]
        acc_ftth=lines[34].split(",")[1]
        isp_ftth=lines[34].split(",")[2]
        store=lines[34].split(",")[3]
        address=lines[34].split(",")[7]
        contact=lines[34].split(",")[8]
        sdt=lines[34].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[35]):
        ip_ftth=lines[35].split(",")[0]
        acc_ftth=lines[35].split(",")[1]
        isp_ftth=lines[35].split(",")[2]
        store=lines[35].split(",")[3]
        address=lines[35].split(",")[7]
        contact=lines[35].split(",")[8]
        sdt=lines[35].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)

    if (select == bigcstoresChoices[36]):
        ip_ftth=lines[36].split(",")[0]
        acc_ftth=lines[36].split(",")[1]
        isp_ftth=lines[36].split(",")[2]
        store=lines[36].split(",")[3]
        address=lines[36].split(",")[7]
        contact=lines[36].split(",")[8]
        sdt=lines[36].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[37]):
        ip_ftth=lines[37].split(",")[0]
        acc_ftth=lines[37].split(",")[1]
        isp_ftth=lines[37].split(",")[2]
        store=lines[37].split(",")[3]
        address=lines[37].split(",")[7]
        contact=lines[37].split(",")[8]
        sdt=lines[37].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)   

    if (select == bigcstoresChoices[38]):
        ip_ftth=lines[38].split(",")[0]
        acc_ftth=lines[38].split(",")[1]
        isp_ftth=lines[38].split(",")[2]
        store=lines[38].split(",")[3]
        address=lines[38].split(",")[7]
        contact=lines[38].split(",")[8]
        sdt=lines[38].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)   

    if (select == bigcstoresChoices[39]):
        ip_ftth=lines[39].split(",")[0]
        acc_ftth=lines[39].split(",")[1]
        isp_ftth=lines[39].split(",")[2]
        store=lines[39].split(",")[3]
        address=lines[39].split(",")[7]
        contact=lines[39].split(",")[8]
        sdt=lines[39].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)   

    if (select == bigcstoresChoices[40]):
        ip_ftth=lines[40].split(",")[0]
        acc_ftth=lines[40].split(",")[1]
        isp_ftth=lines[40].split(",")[2]
        store=lines[40].split(",")[3]
        address=lines[40].split(",")[7]
        contact=lines[40].split(",")[8]
        sdt=lines[40].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)   

    if (select == bigcstoresChoices[41]):
        ip_ftth=lines[41].split(",")[0]
        acc_ftth=lines[41].split(",")[1]
        isp_ftth=lines[41].split(",")[2]
        store=lines[41].split(",")[3]
        address=lines[41].split(",")[7]
        contact=lines[41].split(",")[8]
        sdt=lines[41].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)    

    if (select == bigcstoresChoices[42]):
        ip_ftth=lines[42].split(",")[0]
        acc_ftth=lines[42].split(",")[1]
        isp_ftth=lines[42].split(",")[2]
        store=lines[42].split(",")[3]
        address=lines[42].split(",")[7]
        contact=lines[42].split(",")[8]
        sdt=lines[42].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)       

    if (select == bigcstoresChoices[43]):
        ip_ftth=lines[43].split(",")[0]
        acc_ftth=lines[43].split(",")[1]
        isp_ftth=lines[43].split(",")[2]
        store=lines[43].split(",")[3]
        address=lines[43].split(",")[7]
        contact=lines[43].split(",")[8]
        sdt=lines[43].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[44]):
        ip_ftth=lines[44].split(",")[0]
        acc_ftth=lines[44].split(",")[1]
        isp_ftth=lines[44].split(",")[2]
        store=lines[44].split(",")[3]
        address=lines[44].split(",")[7]
        contact=lines[44].split(",")[8]
        sdt=lines[44].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)  

    if (select == bigcstoresChoices[45]):
        ip_ftth=lines[45].split(",")[0]
        acc_ftth=lines[45].split(",")[1]
        isp_ftth=lines[45].split(",")[2]
        store=lines[45].split(",")[3]
        address=lines[45].split(",")[7]
        contact=lines[45].split(",")[8]
        sdt=lines[45].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[46]):
        ip_ftth=lines[46].split(",")[0]
        acc_ftth=lines[46].split(",")[1]
        isp_ftth=lines[46].split(",")[2]
        store=lines[46].split(",")[3]
        address=lines[46].split(",")[7]
        contact=lines[46].split(",")[8]
        sdt=lines[46].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)     

    if (select == bigcstoresChoices[47]):
        ip_ftth=lines[47].split(",")[0]
        acc_ftth=lines[47].split(",")[1]
        isp_ftth=lines[47].split(",")[2]
        store=lines[47].split(",")[3]
        address=lines[47].split(",")[7]
        contact=lines[47].split(",")[8]
        sdt=lines[47].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result)  

    if (select == bigcstoresChoices[48]):
        ip_ftth=lines[48].split(",")[0]
        acc_ftth=lines[48].split(",")[1]
        isp_ftth=lines[48].split(",")[2]
        store=lines[48].split(",")[3]
        address=lines[48].split(",")[7]
        contact=lines[48].split(",")[8]
        sdt=lines[48].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[49]):
        ip_ftth=lines[49].split(",")[0]
        acc_ftth=lines[49].split(",")[1]
        isp_ftth=lines[49].split(",")[2]
        store=lines[49].split(",")[3]
        address=lines[49].split(",")[7]
        contact=lines[49].split(",")[8]
        sdt=lines[49].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[50]):
        ip_ftth=lines[50].split(",")[0]
        acc_ftth=lines[50].split(",")[1]
        isp_ftth=lines[50].split(",")[2]
        store=lines[50].split(",")[3]
        address=lines[50].split(",")[7]
        contact=lines[50].split(",")[8]
        sdt=lines[50].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Account: '+acc_ftth+'\n04. Service Provider: '+isp_ftth+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: nhanlh@vnpt.vn; support.vnp@vnpt.vn'                         
        print(result)
        Output.insert(END, result) 
                                                                                                                                                                                                                                                                                                               

def mpls():
    fp=open('total_infor1.txt','r+')
    lines=fp.readlines()
    select = Choices.get()
    if (select == bigcstoresChoices[0]):
        store=lines[0].split(",")[3]
        acc_mpls1=lines[0].split(",")[4]
        acc_mpls2=lines[0].split(",")[5]
        isp_mpls=lines[0].split(",")[6]
        address=lines[0].split(",")[7]
        contact=lines[0].split(",")[8]
        sdt=lines[0].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                         
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[1]):
        store=lines[1].split(",")[3]
        acc_mpls1=lines[1].split(",")[4]
        acc_mpls2=lines[1].split(",")[5]
        isp_mpls=lines[1].split(",")[6]
        address=lines[1].split(",")[7]
        contact=lines[1].split(",")[8]
        sdt=lines[1].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)

    if (select == bigcstoresChoices[2]):
        store=lines[2].split(",")[3]
        acc_mpls1=lines[2].split(",")[4]
        acc_mpls2=lines[2].split(",")[5]
        isp_mpls=lines[2].split(",")[6]
        address=lines[2].split(",")[7]
        contact=lines[2].split(",")[8]
        sdt=lines[2].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)

    if (select == bigcstoresChoices[3]):
        store=lines[3].split(",")[3]
        acc_mpls1=lines[3].split(",")[4]
        acc_mpls2=lines[3].split(",")[5]
        isp_mpls=lines[3].split(",")[6]
        address=lines[3].split(",")[7]
        contact=lines[3].split(",")[8]
        sdt=lines[3].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)

    if (select == bigcstoresChoices[4]):
        store=lines[4].split(",")[3]
        acc_mpls1=lines[4].split(",")[4]
        acc_mpls2=lines[4].split(",")[5]
        isp_mpls=lines[4].split(",")[6]
        address=lines[4].split(",")[7]
        contact=lines[4].split(",")[8]
        sdt=lines[4].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)  

    if (select == bigcstoresChoices[5]):
        store=lines[5].split(",")[3]
        acc_mpls1=lines[5].split(",")[4]
        acc_mpls2=lines[5].split(",")[5]
        isp_mpls=lines[5].split(",")[6]
        address=lines[5].split(",")[7]
        contact=lines[5].split(",")[8]
        sdt=lines[5].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[6]):
        store=lines[6].split(",")[3]
        acc_mpls1=lines[6].split(",")[4]
        acc_mpls2=lines[6].split(",")[5]
        isp_mpls=lines[6].split(",")[6]
        address=lines[6].split(",")[7]
        contact=lines[6].split(",")[8]
        sdt=lines[6].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[7]):
        store=lines[7].split(",")[3]
        acc_mpls1=lines[7].split(",")[4]
        acc_mpls2=lines[7].split(",")[5]
        isp_mpls=lines[7].split(",")[6]
        address=lines[7].split(",")[7]
        contact=lines[7].split(",")[8]
        sdt=lines[7].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[8]):
        store=lines[8].split(",")[3]
        acc_mpls1=lines[8].split(",")[4]
        acc_mpls2=lines[8].split(",")[5]
        isp_mpls=lines[8].split(",")[6]
        address=lines[8].split(",")[7]
        contact=lines[8].split(",")[8]
        sdt=lines[8].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)

    if (select == bigcstoresChoices[9]):
        store=lines[9].split(",")[3]
        acc_mpls1=lines[9].split(",")[4]
        acc_mpls2=lines[9].split(",")[5]
        isp_mpls=lines[9].split(",")[6]
        address=lines[9].split(",")[7]
        contact=lines[9].split(",")[8]
        sdt=lines[9].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[10]):
        store=lines[10].split(",")[3]
        acc_mpls1=lines[10].split(",")[4]
        acc_mpls2=lines[10].split(",")[5]
        isp_mpls=lines[10].split(",")[6]
        address=lines[10].split(",")[7]
        contact=lines[10].split(",")[8]
        sdt=lines[10].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[11]):
        store=lines[11].split(",")[3]
        acc_mpls1=lines[11].split(",")[4]
        acc_mpls2=lines[11].split(",")[5]
        isp_mpls=lines[11].split(",")[6]
        address=lines[11].split(",")[7]
        contact=lines[11].split(",")[8]
        sdt=lines[11].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)   

    if (select == bigcstoresChoices[12]):
        store=lines[12].split(",")[3]
        acc_mpls1=lines[12].split(",")[4]
        acc_mpls2=lines[12].split(",")[5]
        isp_mpls=lines[12].split(",")[6]
        address=lines[12].split(",")[7]
        contact=lines[12].split(",")[8]
        sdt=lines[12].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)   

    if (select == bigcstoresChoices[13]):
        store=lines[13].split(",")[3]
        acc_mpls1=lines[13].split(",")[4]
        acc_mpls2=lines[13].split(",")[5]
        isp_mpls=lines[13].split(",")[6]
        address=lines[13].split(",")[7]
        contact=lines[13].split(",")[8]
        sdt=lines[13].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[14]):
        store=lines[14].split(",")[3]
        acc_mpls1=lines[14].split(",")[4]
        acc_mpls2=lines[14].split(",")[5]
        isp_mpls=lines[14].split(",")[6]
        address=lines[14].split(",")[7]
        contact=lines[14].split(",")[8]
        sdt=lines[14].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[15]):
        store=lines[15].split(",")[3]
        acc_mpls1=lines[15].split(",")[4]
        acc_mpls2=lines[15].split(",")[5]
        isp_mpls=lines[15].split(",")[6]
        address=lines[15].split(",")[7]
        contact=lines[15].split(",")[8]
        sdt=lines[15].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[16]):
        store=lines[16].split(",")[3]
        acc_mpls1=lines[16].split(",")[4]
        acc_mpls2=lines[16].split(",")[5]
        isp_mpls=lines[16].split(",")[6]
        address=lines[16].split(",")[7]
        contact=lines[16].split(",")[8]
        sdt=lines[16].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)   

    if (select == bigcstoresChoices[17]):
        store=lines[17].split(",")[3]
        acc_mpls1=lines[17].split(",")[4]
        acc_mpls2=lines[17].split(",")[5]
        isp_mpls=lines[17].split(",")[6]
        address=lines[17].split(",")[7]
        contact=lines[17].split(",")[8]
        sdt=lines[17].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[18]):
        store=lines[18].split(",")[3]
        acc_mpls1=lines[18].split(",")[4]
        acc_mpls2=lines[18].split(",")[5]
        isp_mpls=lines[18].split(",")[6]
        address=lines[18].split(",")[7]
        contact=lines[18].split(",")[8]
        sdt=lines[18].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)  

    if (select == bigcstoresChoices[19]):
        store=lines[19].split(",")[3]
        acc_mpls1=lines[19].split(",")[4]
        acc_mpls2=lines[19].split(",")[5]
        isp_mpls=lines[19].split(",")[6]
        address=lines[19].split(",")[7]
        contact=lines[19].split(",")[8]
        sdt=lines[19].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[20]):
        store=lines[20].split(",")[3]
        acc_mpls1=lines[20].split(",")[4]
        acc_mpls2=lines[20].split(",")[5]
        isp_mpls=lines[20].split(",")[6]
        address=lines[20].split(",")[7]
        contact=lines[20].split(",")[8]
        sdt=lines[20].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[21]):
        store=lines[21].split(",")[3]
        acc_mpls1=lines[21].split(",")[4]
        acc_mpls2=lines[21].split(",")[5]
        isp_mpls=lines[21].split(",")[6]
        address=lines[21].split(",")[7]
        contact=lines[21].split(",")[8]
        sdt=lines[21].split(",")[9]
        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[22]):
        store=lines[22].split(",")[3]
        acc_mpls1=lines[22].split(",")[4]
        acc_mpls2=lines[22].split(",")[5]
        isp_mpls=lines[22].split(",")[6]
        address=lines[22].split(",")[7]
        contact=lines[22].split(",")[8]
        sdt=lines[22].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[23]):
        store=lines[23].split(",")[3]
        acc_mpls1=lines[23].split(",")[4]
        acc_mpls2=lines[23].split(",")[5]
        isp_mpls=lines[23].split(",")[6]
        address=lines[23].split(",")[7]
        contact=lines[23].split(",")[8]
        sdt=lines[23].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[24]):
        store=lines[24].split(",")[3]
        acc_mpls1=lines[24].split(",")[4]
        acc_mpls2=lines[24].split(",")[5]
        isp_mpls=lines[24].split(",")[6]
        address=lines[24].split(",")[7]
        contact=lines[24].split(",")[8]
        sdt=lines[24].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)    

    if (select == bigcstoresChoices[25]):
        store=lines[25].split(",")[3]
        acc_mpls1=lines[25].split(",")[4]
        acc_mpls2=lines[25].split(",")[5]
        isp_mpls=lines[25].split(",")[6]
        address=lines[25].split(",")[7]
        contact=lines[25].split(",")[8]
        sdt=lines[25].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)  

    if (select == bigcstoresChoices[26]):
        store=lines[26].split(",")[3]
        acc_mpls1=lines[26].split(",")[4]
        acc_mpls2=lines[26].split(",")[5]
        isp_mpls=lines[26].split(",")[6]
        address=lines[26].split(",")[7]
        contact=lines[26].split(",")[8]
        sdt=lines[26].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)  

    if (select == bigcstoresChoices[27]):
        store=lines[27].split(",")[3]
        acc_mpls1=lines[27].split(",")[4]
        acc_mpls2=lines[27].split(",")[5]
        isp_mpls=lines[27].split(",")[6]
        address=lines[27].split(",")[7]
        contact=lines[27].split(",")[8]
        sdt=lines[27].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)  

    if (select == bigcstoresChoices[28]):
        store=lines[28].split(",")[3]
        acc_mpls1=lines[28].split(",")[4]
        acc_mpls2=lines[28].split(",")[5]
        isp_mpls=lines[28].split(",")[6]
        address=lines[28].split(",")[7]
        contact=lines[28].split(",")[8]
        sdt=lines[28].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[29]):
        store=lines[29].split(",")[3]
        acc_mpls1=lines[29].split(",")[4]
        acc_mpls2=lines[29].split(",")[5]
        isp_mpls=lines[29].split(",")[6]
        address=lines[29].split(",")[7]
        contact=lines[29].split(",")[8]
        sdt=lines[29].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[30]):
        store=lines[30].split(",")[3]
        acc_mpls1=lines[30].split(",")[4]
        acc_mpls2=lines[30].split(",")[5]
        isp_mpls=lines[30].split(",")[6]
        address=lines[30].split(",")[7]
        contact=lines[30].split(",")[8]
        sdt=lines[30].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[31]):
        store=lines[31].split(",")[3]
        acc_mpls1=lines[31].split(",")[4]
        acc_mpls2=lines[31].split(",")[5]
        isp_mpls=lines[31].split(",")[6]
        address=lines[31].split(",")[7]
        contact=lines[31].split(",")[8]
        sdt=lines[31].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[32]):
        store=lines[32].split(",")[3]
        acc_mpls1=lines[32].split(",")[4]
        acc_mpls2=lines[32].split(",")[5]
        isp_mpls=lines[32].split(",")[6]
        address=lines[32].split(",")[7]
        contact=lines[32].split(",")[8]
        sdt=lines[32].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[33]):
        store=lines[33].split(",")[3]
        acc_mpls1=lines[33].split(",")[4]
        acc_mpls2=lines[33].split(",")[5]
        isp_mpls=lines[33].split(",")[6]
        address=lines[33].split(",")[7]
        contact=lines[33].split(",")[8]
        sdt=lines[33].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)

    if (select == bigcstoresChoices[34]):
        store=lines[34].split(",")[3]
        acc_mpls1=lines[34].split(",")[4]
        acc_mpls2=lines[34].split(",")[5]
        isp_mpls=lines[34].split(",")[6]
        address=lines[34].split(",")[7]
        contact=lines[34].split(",")[8]
        sdt=lines[34].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[35]):
        store=lines[35].split(",")[3]
        acc_mpls1=lines[35].split(",")[4]
        acc_mpls2=lines[35].split(",")[5]
        isp_mpls=lines[35].split(",")[6]
        address=lines[35].split(",")[7]
        contact=lines[35].split(",")[8]
        sdt=lines[35].split(",")[9] 

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)

    if (select == bigcstoresChoices[36]):
        store=lines[36].split(",")[3]
        acc_mpls1=lines[36].split(",")[4]
        acc_mpls2=lines[36].split(",")[5]
        isp_mpls=lines[36].split(",")[6]
        address=lines[36].split(",")[7]
        contact=lines[36].split(",")[8]
        sdt=lines[36].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[37]):
        store=lines[37].split(",")[3]
        acc_mpls1=lines[37].split(",")[4]
        acc_mpls2=lines[37].split(",")[5]
        isp_mpls=lines[37].split(",")[6]
        address=lines[37].split(",")[7]
        contact=lines[37].split(",")[8]
        sdt=lines[37].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)   

    if (select == bigcstoresChoices[38]):
        store=lines[38].split(",")[3]
        acc_mpls1=lines[38].split(",")[4]
        acc_mpls2=lines[38].split(",")[5]
        isp_mpls=lines[38].split(",")[6]
        address=lines[38].split(",")[7]
        contact=lines[38].split(",")[8]
        sdt=lines[38].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)   

    if (select == bigcstoresChoices[39]):
        store=lines[39].split(",")[3]
        acc_mpls1=lines[39].split(",")[4]
        acc_mpls2=lines[39].split(",")[5]
        isp_mpls=lines[39].split(",")[6]
        address=lines[39].split(",")[7]
        contact=lines[39].split(",")[8]
        sdt=lines[39].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)   

    if (select == bigcstoresChoices[40]):
        store=lines[40].split(",")[3]
        acc_mpls1=lines[40].split(",")[4]
        acc_mpls2=lines[40].split(",")[5]
        isp_mpls=lines[40].split(",")[6]
        address=lines[40].split(",")[7]
        contact=lines[40].split(",")[8]
        sdt=lines[40].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)   

    if (select == bigcstoresChoices[41]):
        store=lines[41].split(",")[3]
        acc_mpls1=lines[41].split(",")[4]
        acc_mpls2=lines[41].split(",")[5]
        isp_mpls=lines[41].split(",")[6]
        address=lines[41].split(",")[7]
        contact=lines[41].split(",")[8]
        sdt=lines[41].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)    

    if (select == bigcstoresChoices[42]):
        store=lines[42].split(",")[3]
        acc_mpls1=lines[42].split(",")[4]
        acc_mpls2=lines[42].split(",")[5]
        isp_mpls=lines[42].split(",")[6]
        address=lines[42].split(",")[7]
        contact=lines[42].split(",")[8]
        sdt=lines[42].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)       

    if (select == bigcstoresChoices[43]):
        store=lines[43].split(",")[3]
        acc_mpls1=lines[43].split(",")[4]
        acc_mpls2=lines[43].split(",")[5]
        isp_mpls=lines[43].split(",")[6]
        address=lines[43].split(",")[7]
        contact=lines[43].split(",")[8]
        sdt=lines[43].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)         

    if (select == bigcstoresChoices[44]):
        store=lines[44].split(",")[3]
        acc_mpls1=lines[44].split(",")[4]
        acc_mpls2=lines[44].split(",")[5]
        isp_mpls=lines[44].split(",")[6]
        address=lines[44].split(",")[7]
        contact=lines[44].split(",")[8]
        sdt=lines[44].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)         

    if (select == bigcstoresChoices[45]):
        store=lines[45].split(",")[3]
        acc_mpls1=lines[45].split(",")[4]
        acc_mpls2=lines[45].split(",")[5]
        isp_mpls=lines[45].split(",")[6]
        address=lines[45].split(",")[7]
        contact=lines[45].split(",")[8]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)         

    if (select == bigcstoresChoices[46]):
        store=lines[46].split(",")[3]
        acc_mpls1=lines[46].split(",")[4]
        acc_mpls2=lines[46].split(",")[5]
        isp_mpls=lines[46].split(",")[6]
        address=lines[46].split(",")[7]
        contact=lines[46].split(",")[8]
        sdt=lines[46].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result)       

    if (select == bigcstoresChoices[47]):
        store=lines[47].split(",")[3]
        acc_mpls1=lines[47].split(",")[4]
        acc_mpls2=lines[47].split(",")[5]
        isp_mpls=lines[47].split(",")[6]
        address=lines[47].split(",")[7]
        contact=lines[47].split(",")[8]
        sdt=lines[47].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[48]):
        store=lines[48].split(",")[3]
        acc_mpls1=lines[48].split(",")[4]
        acc_mpls2=lines[48].split(",")[5]
        isp_mpls=lines[48].split(",")[6]
        address=lines[48].split(",")[7]
        contact=lines[48].split(",")[8]
        sdt=lines[48].split(",")[9]  

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[49]):
        store=lines[49].split(",")[3]
        acc_mpls1=lines[49].split(",")[4]
        acc_mpls2=lines[49].split(",")[5]
        isp_mpls=lines[49].split(",")[6]
        address=lines[49].split(",")[7]
        contact=lines[49].split(",")[8]
        sdt=lines[49].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

    if (select == bigcstoresChoices[50]):
        store=lines[50].split(",")[3]
        acc_mpls1=lines[50].split(",")[4]
        acc_mpls2=lines[50].split(",")[5]
        isp_mpls=lines[50].split(",")[6]
        address=lines[50].split(",")[7]
        contact=lines[50].split(",")[8]
        sdt=lines[50].split(",")[9]

        result = '01. Store Code: '+store+'\n02. Primary Line: '+acc_mpls1+'\n03. Secondary Line: '+acc_mpls2+'\n04. Service Provider: '+isp_mpls+'\n05. Address: '+address+'\n06. Technical Contact: '+contact+' - '+sdt+'\n07. Email ISP: haint78@viettel.com.vn, cskhdn@viettel.com.vn'                      
        print(result)
        Output.insert(END, result) 

                                                             

    fp=open('total_infor1.txt','r+')
    lines=fp.readlines()
    select = Choices.get()
    if (select == bigcstoresChoices[0]):
        ip_ftth=lines[0].split(",")[0]
        store=lines[0].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[1]):
        ip_ftth=lines[1].split(",")[0]
        store=lines[1].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 

    if (select == bigcstoresChoices[2]):
        ip_ftth=lines[2].split(",")[0]
        store=lines[2].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 

    if (select == bigcstoresChoices[3]):
        ip_ftth=lines[3].split(",")[0]
        store=lines[3].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 

    if (select == bigcstoresChoices[4]):
        ip_ftth=lines[4].split(",")[0]
        store=lines[4].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[5]):
        ip_ftth=lines[5].split(",")[0]
        store=lines[5].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[6]):
        ip_ftth=lines[6].split(",")[0]
        store=lines[6].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[7]):
        ip_ftth=lines[7].split(",")[0]
        store=lines[7].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[8]):
        ip_ftth=lines[8].split(",")[0]
        store=lines[8].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 

    if (select == bigcstoresChoices[9]):
        ip_ftth=lines[9].split(",")[0]
        store=lines[9].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[10]):
        ip_ftth=lines[10].split(",")[0]
        store=lines[10].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[11]):
        ip_ftth=lines[11].split(",")[0]
        store=lines[11].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 
 
    if (select == bigcstoresChoices[12]):
        ip_ftth=lines[12].split(",")[0]
        store=lines[12].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 
 
    if (select == bigcstoresChoices[13]):
        ip_ftth=lines[13].split(",")[0]
        store=lines[13].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[14]):
        ip_ftth=lines[14].split(",")[0]
        store=lines[14].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[15]):
        ip_ftth=lines[15].split(",")[0]
        store=lines[15].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[16]):
        ip_ftth=lines[16].split(",")[0]
        store=lines[16].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 
 
    if (select == bigcstoresChoices[17]):
        ip_ftth=lines[17].split(",")[0]
        store=lines[17].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[18]):
        ip_ftth=lines[18].split(",")[0]
        store=lines[18].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[19]):
        ip_ftth=lines[19].split(",")[0]
        store=lines[19].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[20]):
        ip_ftth=lines[20].split(",")[0]
        store=lines[20].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[21]):
        ip_ftth=lines[21].split(",")[0]
        store=lines[21].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[22]):
        ip_ftth=lines[22].split(",")[0]
        store=lines[22].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[23]):
        ip_ftth=lines[23].split(",")[0]
        store=lines[23].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[24]):
        ip_ftth=lines[24].split(",")[0]
        store=lines[24].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[25]):
        ip_ftth=lines[25].split(",")[0]
        store=lines[25].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[26]):
        ip_ftth=lines[26].split(",")[0]
        store=lines[26].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[27]):
        ip_ftth=lines[27].split(",")[0]
        store=lines[27].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[28]):
        ip_ftth=lines[28].split(",")[0]
        store=lines[28].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[29]):
        ip_ftth=lines[29].split(",")[0]
        store=lines[29].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[30]):
        ip_ftth=lines[30].split(",")[0]
        store=lines[30].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[31]):
        ip_ftth=lines[31].split(",")[0]
        store=lines[31].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[32]):
        ip_ftth=lines[32].split(",")[0]
        store=lines[32].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[33]):
        ip_ftth=lines[33].split(",")[0]
        store=lines[33].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 

    if (select == bigcstoresChoices[34]):
        ip_ftth=lines[34].split(",")[0]
        store=lines[34].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[35]):
        ip_ftth=lines[35].split(",")[0]
        store=lines[35].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 

    if (select == bigcstoresChoices[36]):
        ip_ftth=lines[36].split(",")[0]
        store=lines[36].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[37]):
        ip_ftth=lines[37].split(",")[0]
        store=lines[37].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[38]):
        ip_ftth=lines[38].split(",")[0]
        store=lines[38].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[39]):
        ip_ftth=lines[39].split(",")[0]
        store=lines[39].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[40]):
        ip_ftth=lines[40].split(",")[0]
        store=lines[40].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[41]):
        ip_ftth=lines[41].split(",")[0]
        store=lines[41].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[42]):
        ip_ftth=lines[42].split(",")[0]
        store=lines[42].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[43]):
        ip_ftth=lines[43].split(",")[0]
        store=lines[43].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[44]):
        ip_ftth=lines[44].split(",")[0]
        store=lines[44].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[45]):
        ip_ftth=lines[45].split(",")[0]
        store=lines[45].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[46]):
        ip_ftth=lines[46].split(",")[0]
        store=lines[46].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[47]):
        ip_ftth=lines[47].split(",")[0]
        store=lines[47].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[48]):
        ip_ftth=lines[48].split(",")[0]
        store=lines[48].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[49]):
        ip_ftth=lines[49].split(",")[0]
        store=lines[49].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[50]):
        ip_ftth=lines[50].split(",")[0]
        store=lines[50].split(",")[3]

        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

def internetcheck():
    fp=open('total_infor1.txt','r+')
    lines=fp.readlines()
    select = Choices.get()
    if (select == bigcstoresChoices[0]):
        ip_ftth=lines[0].split(",")[0]
        store=lines[0].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","").replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: \n'+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[1]):
        ip_ftth=lines[1].split(",")[0]
        store=lines[1].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 

    if (select == bigcstoresChoices[2]):
        ip_ftth=lines[2].split(",")[0]
        store=lines[2].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 

    if (select == bigcstoresChoices[3]):
        ip_ftth=lines[3].split(",")[0]
        store=lines[3].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 

    if (select == bigcstoresChoices[4]):
        ip_ftth=lines[4].split(",")[0]
        store=lines[4].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[5]):
        ip_ftth=lines[5].split(",")[0]
        store=lines[5].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[6]):
        ip_ftth=lines[6].split(",")[0]
        store=lines[6].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[7]):
        ip_ftth=lines[7].split(",")[0]
        store=lines[7].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[8]):
        ip_ftth=lines[8].split(",")[0]
        store=lines[8].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 

    if (select == bigcstoresChoices[9]):
        ip_ftth=lines[9].split(",")[0]
        store=lines[9].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[10]):
        ip_ftth=lines[10].split(",")[0]
        store=lines[10].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[11]):
        ip_ftth=lines[11].split(",")[0]
        store=lines[11].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 
 
    if (select == bigcstoresChoices[12]):
        ip_ftth=lines[12].split(",")[0]
        store=lines[12].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 
 
    if (select == bigcstoresChoices[13]):
        ip_ftth=lines[13].split(",")[0]
        store=lines[13].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[14]):
        ip_ftth=lines[14].split(",")[0]
        store=lines[14].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[15]):
        ip_ftth=lines[15].split(",")[0]
        store=lines[15].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[16]):
        ip_ftth=lines[16].split(",")[0]
        store=lines[16].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 
 
    if (select == bigcstoresChoices[17]):
        ip_ftth=lines[17].split(",")[0]
        store=lines[17].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[18]):
        ip_ftth=lines[18].split(",")[0]
        store=lines[18].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[19]):
        ip_ftth=lines[19].split(",")[0]
        store=lines[19].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[20]):
        ip_ftth=lines[20].split(",")[0]
        store=lines[20].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[21]):
        ip_ftth=lines[21].split(",")[0]
        store=lines[21].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[22]):
        ip_ftth=lines[22].split(",")[0]
        store=lines[22].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[23]):
        ip_ftth=lines[23].split(",")[0]
        store=lines[23].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[24]):
        ip_ftth=lines[24].split(",")[0]
        store=lines[24].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[25]):
        ip_ftth=lines[25].split(",")[0]
        store=lines[25].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[26]):
        ip_ftth=lines[26].split(",")[0]
        store=lines[26].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[27]):
        ip_ftth=lines[27].split(",")[0]
        store=lines[27].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[28]):
        ip_ftth=lines[28].split(",")[0]
        store=lines[28].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[29]):
        ip_ftth=lines[29].split(",")[0]
        store=lines[29].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[30]):
        ip_ftth=lines[30].split(",")[0]
        store=lines[30].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[31]):
        ip_ftth=lines[31].split(",")[0]
        store=lines[31].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[32]):
        ip_ftth=lines[32].split(",")[0]
        store=lines[32].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[33]):
        ip_ftth=lines[33].split(",")[0]
        store=lines[33].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 

    if (select == bigcstoresChoices[34]):
        ip_ftth=lines[34].split(",")[0]
        store=lines[34].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[35]):
        ip_ftth=lines[35].split(",")[0]
        store=lines[35].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 

    if (select == bigcstoresChoices[36]):
        ip_ftth=lines[36].split(",")[0]
        store=lines[36].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[37]):
        ip_ftth=lines[37].split(",")[0]
        store=lines[37].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[38]):
        ip_ftth=lines[38].split(",")[0]
        store=lines[38].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[39]):
        ip_ftth=lines[39].split(",")[0]
        store=lines[39].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[40]):
        ip_ftth=lines[40].split(",")[0]
        store=lines[40].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[41]):
        ip_ftth=lines[41].split(",")[0]
        store=lines[41].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[42]):
        ip_ftth=lines[42].split(",")[0]
        store=lines[42].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[43]):
        ip_ftth=lines[43].split(",")[0]
        store=lines[43].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[44]):
        ip_ftth=lines[44].split(",")[0]
        store=lines[44].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[45]):
        ip_ftth=lines[45].split(",")[0]
        store=lines[45].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[46]):
        ip_ftth=lines[46].split(",")[0]
        store=lines[46].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[47]):
        ip_ftth=lines[47].split(",")[0]
        store=lines[47].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[48]):
        ip_ftth=lines[48].split(",")[0]
        store=lines[48].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[49]):
        ip_ftth=lines[49].split(",")[0]
        store=lines[49].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

    if (select == bigcstoresChoices[50]):
        ip_ftth=lines[50].split(",")[0]
        store=lines[50].split(",")[3]

        dv={'device_type': 'cisco_ios',
            'ip': '10.0.255.2',
            'username': 'nguyen-luu-trung01',
            'password': '2112Daniel!@#',
            'secret': '2112Daniel!@#',
            'verbose': False
           }
        dv = ConnectHandler(**dv)
        dv.enable()
        ping_cmd = dv.send_command("ping "+ip_ftth+" repeat 100")
        print(ping_cmd)
        ping_result = ping_cmd.splitlines()[4].split()
        packet_loss = ping_result[5].replace(",","")
        latency = ping_result[9]
        internet_check_result = '01. Store: '+store+'\n02. Public IP Address: '+ip_ftth+'\n03. Status: '+packet_loss+'\n04. Latency min/avg/max: '+latency+' ms\n05. Output Command: '+ping_cmd
        print(internet_check_result)
        Output.insert(END, internet_check_result) 
 

def mplscheck():
    notice = 'Comming Soon!!!'
    Output.insert(END,notice) 


def mail():
    mail_tem = 'Dear Viettel Team,\n\nNhờ Team check gấp giúp line MPLS tại cửa hàng sau nhé! Hiện tại đang mất kết nối:\nPrimary Line: b240_ow_naictttmdvqtbcd4\nSecondary Line: b240_ow_naictttmdvqtbcd5\nAddress: ĐT293 - Xã Tân Tiến - Yên Dũng - Bắc Giang\nContact : Đỗ Xuân Trường - +84974395734\n\nThanks & Best Regard!'
    Output.insert(END,mail_tem)


dv={'device_type': 'cisco_ios',
    'ip': '10.0.255.2',
    'username': 'nguyen-luu-trung01',
    'password': '2112Daniel!@#',
    'secret': '2112Daniel!@#',
    'verbose': False
    }


def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

# will look more attractive
lbl = Label(root, font = ('calibri', 20, 'bold'),
            background = 'orange',
            foreground = 'black')
# Placing clock at the centre
lbl.pack()
time()

def show():
    Output.delete(1.0, END)
# Clear box
def clear():
    Output.delete(1.0, END)
def complete():
    loadingLabel.config(text='Testing completed')
# code open folder
def openFile():
    tf = filedialog.askopenfilename(
        initialdir="./Log",
        title="Open Log File",
        filetypes=(("Text Files", "*.txt"),("All Files", "*.*"))
        )
    pathh.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    Output.insert(END, data)
    tf.close()


panel = Label(text = "Please Choose The Store! ", font=('Agency FB', 22), fg="black", bg = "orange")
panel.pack()
bigcstoresChoices = ['100_SSC','101_Big C Dong Nai','102_Big C An Lac','103_Big C  Mien Dong','104_Big C Thang Long','106_Big C HaiPhong','107_Big C Da Nang'
,'108_Big C Go Vap','109_Big C Hue','110_Big C Garden','111_Big C Phu Thanh','112_Big C Vinh','113_Big C Vinh Phuc','114_Big C Nam Dinh','115_Big C Tan Hiep'
,'116_Big C Long Bien','117_Big C Hai Duong','118_Big C Thanh Hoa','119_Big C Me Linh','120_Big C Can Tho','121_Big C Binh Duong','122_Big C Truong Chinh'
,'123_Big C Di An','124_Big C Viet Tri','125_Big C Ninh Binh','126_Big C Da Lat','127_Big C An Phu','128_Big C Ha Long','129_Big C Quy Nhon','130_Big C Nha Trang'
,'131_Big C Bac Giang','132_Big C Ha Dong','133_Big C Nguyen Thi Thap','134_Big C Thao Dien','135_Big C Le Trong Tan','136_Big C Au Co','137_GO! My Tho'
,'138_GO! Nguyen Xien','139_GO! Quang Ngai','140_GO! Tra Vinh','141_GO! Buon Ma Thuot','142_GO! Ben Tre','143_GO! Ba Ria','144_GO! Thai Nguyen','145_GO! Thai Binh'
,'146_Mini go! Tây Ninh','14x_Mini go! Tam Ky','147_GO! Lao Cai','14x_Warehouse Ha Noi','14x_Warehouse Da Lat','FIS Services']
Choices = ttk.Combobox(root, values=bigcstoresChoices, font=('Agency FB', 15))
Choices.pack()
'''
nkstoresChoices = ['Thu Duc','Truong Chinh','Go Vap','Phu Nhuan','An Lac','Quan 2','Binh Tan','Quang Trung','Quan 7','Phan Van Hon','Binh Thanh','Cu Chi','Quan 9','Lac Long Quan','Tan Phu',
                    'Datacenter','An Giang','Ben Tre','Bac Lieu','Ca Mau','Can Tho','Kien Giang','Tien Giang','Tra Vinh','Vinh Long','Binh Duong','Di An','Thuan An','Bien Hoa','Dong Nai','Trang Bom','Tan Hiep',
                    'Phan Thiet','Vung Tau','Ba Ria','Hoc Mon','Song Than','DakLak','Gia Lai','Nha Trang','Qui Nhon','Kho Qui Nhon','Da Lat','Kho Da Lat','Da Nang','Quang Ngai','Ba Dinh','Ha Dong','SIS Thang Long',
                    'Long Bien','Hai Phong','Nghe An','Nam Dinh','Viet Tri','Thanh Hoa','Kho Ha Noi']

option = ttk.Combobox(root, values=nkstoresChoices, font=('Agency FB', 20))
option.pack(pady=10)
'''

panel1 = Label(text = "OUTPUT WINDOW                                                                     ",
            font=('Agency FB', 17, 'bold'),
            bg="orange",
            bd=1,
            relief='sunken',
            justify='left')

Output = Text(root, height = 10, width = 100, bg = "white")
button_frame = Frame(root, bg="orange")

internet_button = Button(button_frame, height = 2, width = 10, bg="black", fg="white" , text = "Internet", command = lambda:internet())
internet_button.grid(row=0, column=0, padx=10)

mpls_button = Button(button_frame, height = 2, width = 10, bg="black", fg="white" , text = "Mpls", command = lambda:mpls())
mpls_button.grid(row=1, column=0, padx=10)


internet_check = Button(button_frame, height = 2, width = 10, bg="black", fg="white", text="Internet Checker", command= lambda:internetcheck())
internet_check.grid(row=0, column=1, padx=10)

mpls_check = Button(button_frame, height = 2, width = 10, bg="black", fg="white", text="Mpls Checker", command= lambda:mplscheck())
mpls_check.grid(row=1, column=1, padx=10)


clear_button = Button(button_frame, height = 2, width = 10, bg="black", fg="white", text="Clear", command= lambda:clear())
clear_button .grid(row=0, column=2, padx=10)

open_button = Button(button_frame, height = 2, width = 10, bg="black", fg="white" , text="Open Folder", command= lambda:openFile())
open_button.grid(row=1, column=2, padx=10)

mail_template = Button(button_frame, height = 2, width = 10, bg="black", fg="white" , text="Mail Template", command= lambda:mail())
mail_template.grid(row=0, column=3, padx=10)

quit_folder = Button(button_frame, height = 2, width = 10, bg="black", fg="red" , text="Quit", command= root.quit)
quit_folder.grid(row=1, column=3, padx=10)
#bottomLabel = Label(text='Created by |> Nguyen Luu Trung', font=('Agency FB', 10))
pathh = Entry(root, bg="light blue")
pathh.pack(pady=5)

loadingLabel = Label(root, text='App developed by |> Nguyen Luu Trung', font=('Agency FB',10), bg="orange")
panel1.pack()
Output.pack(pady=15)
button_frame.pack()

#bottomLabel.pack(pady=10)
loadingLabel.pack(pady=5)
root.mainloop()
