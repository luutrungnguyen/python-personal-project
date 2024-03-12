from N2G import drawio_diagram
from datetime import datetime
import time

current_time=datetime.now()
nowtime=current_time.strftime("%Y-%m-%d %H:%M:%S")

router='./styles/router.txt'
coresw='./styles/coresw.txt'
asw='./styles/asw.txt'
wlc='./styles/wlc.txt'
ap='./styles/ap.txt'

link_style='./links/gapkhuc.txt'

diagram = drawio_diagram()
diagram.add_diagram("Page-1")

csv_links_data = './csv_links_data.csv'
csv_nodes_data= './csv_links_node.csv'

diagram.from_csv(csv_nodes_data)
diagram.from_csv(csv_links_data)
diagram.layout(algo="kk")
diagram.dump_file(filename="trungnl"+nowtime+"s.drawio", folder="./Output/")
print(nowtime)
print("Đã export file to ./Output")