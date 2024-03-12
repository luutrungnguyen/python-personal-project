from N2G import drawio_diagram
from datetime import datetime
import time

current_time=datetime.now()
nowtime=current_time.strftime("%Y-%m-%d %H:%M:%S")

diagram = drawio_diagram()
diagram.add_diagram("Page-1")
diagram.add_node(id="R1", data={"a": "b", "c": "d"}, url="http://google.com")
diagram.add_diagram("Page-2")
diagram.add_node(id="R2", url="Page-1")
diagram.add_node(id="R3")
diagram.add_link("R2", "R3", label="uplink", data={"speed": "1G", "media": "10G-LR"}, url="http://cmdb.local")
diagram.dump_file(filename="trungnl"+nowtime+"s.drawio", folder="./Output/")
print(nowtime)
print("Đã export file to ./Output")