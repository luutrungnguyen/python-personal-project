from N2G import drawio_diagram
from datetime import datetime
import time

current_time=datetime.now()
nowtime=current_time.strftime("%Y-%m-%d %H:%M:%S")

diagram = drawio_diagram()
sample_graph={
'nodes': [
    {'id': 'a', 'style': './styles/router.txt', 'label': 'R1', 'width': 78, 'height': 53},
    {'id': 'R2', 'label':'CE12800'},
    {'id': 'c', 'label': 'R3', 'data': {'role': 'access', 'make': 'VendorX'}}
],
'links': [
    {'source': 'a', 'label': 'DF', 'target': 'R2', 'data': {'role': 'uplink'}},
    {'source': 'R2', 'label': 'Copper', 'target': 'c'},
    {'source': 'c', 'label': 'ZR', 'target': 'a'}
]}
diagram.from_dict(sample_graph, width=300, height=200, diagram_name="Page-2")
diagram.layout(algo="kk")
diagram.dump_file(filename="trungnl"+nowtime+"s.drawio", folder="./Output/")
print(nowtime)
print("Đã export file to ./Output")