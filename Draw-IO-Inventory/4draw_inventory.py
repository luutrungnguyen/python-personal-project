from N2G import drawio_diagram
from datetime import datetime
import time

current_time=datetime.now()
nowtime=current_time.strftime("%Y-%m-%d %H:%M:%S")

link_style = "./links/gapkhuc.txt"

diagram = drawio_diagram()
'''
sample_list_graph = [
    {'source': {'id': 'SW1'}, 'target': 'R1', 'label': 'Gig0/1--Gi2'},
    {'source': 'R2', 'target': 'SW1', "data": {"speed": "1G", "media": "10G-LR"}},
    {'source': {'id':'a', 'label': 'R3'}, 'target': 'SW1'},
    {'source': 'SW1', 'target': 'R4'}
]
'''
sample_list_graph = [
    {'source': 'SW1', 'target': 'R1', 'label': 'Gig0/1--Gi2'},
    {'source': 'R2', 'target': 'SW1', 'label': 'Gig0/1--Gi2'},
    {'source': 'R3', 'target': 'SW1', 'label': 'Gig0/1--Gi2'},
    {'source': 'SW1', 'target': 'R4', 'label': 'Gig0/1--Gi2'}
]

diagram.from_list(sample_list_graph, width=300, height=200, diagram_name="Page-1")
diagram.layout(algo="kk")
diagram.dump_file(filename="trungnl"+nowtime+"s.drawio", folder="./Output/")
print(nowtime)
print("Đã export file to ./Output")