from N2G import drawio_diagram
from datetime import datetime
import time

current_time=datetime.now()
nowtime=current_time.strftime("%Y-%m-%d %H:%M:%S")

diagram = drawio_diagram()
old_graph = {
'nodes': [
    {'id': 'R1'}, {'id': 'R2'}, {'id': 'R3'},
    ],
'edges': [
    {'source': 'R1', 'target': 'R2'},
    {'source': 'R2', 'target': 'R3'},
    {'source': 'R3', 'target': 'R1'}
]}
new_graph = {
'nodes': [
    {'id': 'R1'}, {'id': 'R2'}, {'id': 'R4'},
    ],
'edges': [
    {'source': 'R1', 'target': 'R2'},
    {'source': 'R2', 'target': 'R4'}
]}
diagram.add_diagram("Page-1", width=500, height=500)
diagram.from_dict(old_graph)
diagram.compare(new_graph)
diagram.layout(algo="kk")
diagram.dump_file(filename="trungnl"+nowtime+"s.drawio", folder="./Output/")
print(nowtime)
print("Đã export file to ./Output")