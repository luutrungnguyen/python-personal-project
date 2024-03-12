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

root = Tk()

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

button_frame = Frame(root, bg="orange")
mpls_button = Button(button_frame, height = 2, width = 10, bg="black", fg="white" , text = "Mpls", command = lambda:mpls())
mpls_button.grid(row=0, column=1, padx=10)

root.mainloop()