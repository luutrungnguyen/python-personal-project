from N2G import drawio_diagram
from datetime import datetime
import time

current_time=datetime.now()
nowtime=current_time.strftime("%Y-%m-%d %H:%M:%S")

diagram = drawio_diagram()
csv_links_data = """"source","label","target"
"a","DF","b"
"b","Copper","c"
"b","Copper","e"
d,FW,e
"""
csv_nodes_data=""""id","label","style","width","height"
a,"R12","./styles/router.txt",78,53
"b","R2",,,
"c","R3",,,
"d","SW22",,,
"e","R1",,,
"""
diagram.from_csv(csv_nodes_data)
diagram.from_csv(csv_links_data)
diagram.layout(algo="kk")
diagram.dump_file(filename="trungnl"+nowtime+"s.drawio", folder="./Output/")
print(nowtime)
print("Đã export file to ./Output")