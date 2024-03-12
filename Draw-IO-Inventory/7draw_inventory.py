from N2G import drawio_diagram

from datetime import datetime
import time

current_time=datetime.now()
nowtime=current_time.strftime("%Y-%m-%d %H:%M:%S")

existing_graph = {
    "nodes": [
        {"id": "node-1"},
        {"id": "node-2"},
        {"id": "node-3"}
],
    "links": [
        {"source": "node-1", "target": "node-2", "label": "bla1"},
        {"source": "node-2", "target": "node-3", "label": "bla2"},
    ]
}
new_graph = {
    "nodes": [
        {"id": "node-99"},
        {"id": "node-100", "style": "./styles/router.txt", "width": 78, "height": 53},
    ],
    "links": [
        {"source": "node-2", "target": "node-3", "label": "bla2"},
        {"source": "node-99", "target": "node-3", "label": "bla99"},
        {"source": "node-100", "target": "node-99", "label": "bla10099"},
    ]
}
drawing = drawio_diagram()
drawing.from_dict(data=existing_graph)
drawing.compare(new_graph)
drawing.layout(algo="kk")
drawing.dump_file(filename="trungnl"+nowtime+"s.drawio", folder="./Output/")
print(nowtime)
print("Đã export file to ./Output")