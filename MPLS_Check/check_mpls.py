from netmiko import ConnectHandler
import netmiko
#import nkdevices.txt
import smtplib
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from datetime import date

output=''
id1=''
shd1=''
isp1=''
add1=''
id_temp=''
maduongtruyen=''

#read file and get information
fp=open('mpls.txt','r+')
lines=fp.readlines()



#create backup filename format: hostname_IP_date_month_year
current_time=datetime.now()
current_date=current_time.strftime("%d")
current_month=current_time.strftime("%m")
current_year=current_time.strftime("%Y")
dt_string = current_time.strftime("%d/%m/%Y %H:%M:%S")
print("Ngay va gio hien tai =", dt_string)

id_temp=input("*********** Enter ID Store *************\n")


for i in range(0,len(lines)):
 if id_temp in lines[i]:
  id1=lines[i].split(",")[0]
  shd1=lines[i].split(",")[1]
  isp1=lines[i].split(",")[2]
  add1=lines[i].split(",")[3]


  print("Thông tin cửa hàng: \nID: "+id1+"\nMã đường truyền: "+shd1+" & "+shd1+"\nĐịa chỉ: "+add1+"\n")
  output+="MESSAGE Content:\nDear Viettel Team,\n\nCheck giúp 2 line MPLS tại địa chỉ sau nhé, hiên tại đang mất kết nối:\n"+shd1+"\nAddress: "+add1+"\nContact : Mr Truong - 0974395734\n\nThanks & Best Regard!\n----------------------\nNguyen Luu Trung (Mr.)\nIT Network Specialist\nMobile: +84 945 00 02 03 | Tele/Whatsapp/Zalo: +84 962 981 773\nEmail: trung.luu.nguyen@vn.centralretail.com"

  print(output+"\n\n")
 else:
   print("Sai cú pháp mã cửa hàng. Ví dụ: Thang Long, Vinh, Go Vap...")


#send email
fromaddr = 'luutrungnguyen.crv01@gmail.com'
toaddr = 'luutrungnguyen.94@gmail.com'
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'CRV - BAO SU CO MPLS LINE'
msg.attach(MIMEText(output+"\n\n", 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("luutrungnguyen.crv01@gmail.com", "2112Daniel!@#")
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()
print("Da gui email den "+toaddr)
