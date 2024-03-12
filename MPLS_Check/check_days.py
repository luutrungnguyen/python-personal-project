from datetime import datetime

# đối tượng datetime chứa ngày và giờ hiện tại
# viết bởi Quantrimang.com
now = datetime.now()
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Ngay va gio hien tai =", dt_string)	