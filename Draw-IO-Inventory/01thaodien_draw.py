from N2G import drawio_diagram
from datetime import datetime
import time

current_time=datetime.now()
nowtime=current_time.strftime("%Y-%m-%d %H:%M:%S")

# Define style nha bro
router='./styles/router.txt'
coresw='./styles/coresw.txt'
asw='./styles/asw.txt'
wlc='./styles/wlc.txt'
ap='./styles/ap.txt'

# Define link nha bro
link_style='./links/gapkhuc.txt'
poe_link='./links/poe_link.txt'

diagram = drawio_diagram()
diagram.add_diagram("Page-1")

# add note nha bro
diagram.add_node(id="TDien-Office-SW1",style=asw)
diagram.add_node(id="TDien-R1",style=router)
diagram.add_node(id="TD-Office-SW03",style=asw)
diagram.add_node(id="TDien-Office-SW2",style=asw)
diagram.add_node(id="ThaoDien-WLC-3504",style=wlc)
diagram.add_node(id="TDien-Elec-SW2",style=asw)
diagram.add_node(id="TDien-Elec-SW1",style=asw)
diagram.add_node(id="TD-B1-A19",style=ap)
diagram.add_node(id="TD-B1-A14",style=ap)
diagram.add_node(id="TD-B1-A15",style=ap)
diagram.add_node(id="TD-B1-A16",style=ap)
diagram.add_node(id="TD-B1-A17",style=ap)
diagram.add_node(id="TD-B1-B03",style=ap)
diagram.add_node(id="TD-B1-A20",style=ap)
diagram.add_node(id="AP003a.7dd4.6d00",style=ap)
diagram.add_node(id="AP0062.ec20.6110",style=ap)
diagram.add_node(id="TD-B1-A13",style=ap)
diagram.add_node(id="TD-B1-A03",style=ap)
diagram.add_node(id="TD-B1-A12",style=ap)
diagram.add_node(id="TD-B1-A11",style=ap)
diagram.add_node(id="TD-B1-A10",style=ap)
diagram.add_node(id="TD-B1-A01",style=ap)
diagram.add_node(id="TD-B1-A06",style=ap)
diagram.add_node(id="TD-B1-A07",style=ap)
diagram.add_node(id="TD-B1-A04",style=ap)
diagram.add_node(id="TD-B1-A05",style=ap)
diagram.add_node(id="TD-B1-A08",style=ap)
diagram.add_node(id="TD-B1-A09",style=ap)
diagram.add_node(id="AP0062.ec19.6bac",style=ap)

# Add link nha Bro
diagram.add_link("TDien-R1","TDien-Office-SW1",label="Gig 0/0/1 to Fas 0/43",style=link_style)
diagram.add_link("TDien-Office-SW2","TDien-Office-SW1",label="Fas 0/48 to Fas 0/48",style=link_style)
diagram.add_link("TDien-Office-SW2","TDien-Office-SW1",label="Fas 0/47 to Fas 0/47",style=link_style)
diagram.add_link("TDien-Office-SW2","ThaoDien-WLC-3504",label="Fas 0/46 to Gig 0/0/1",style=link_style)
diagram.add_link("TD-Office-SW03","TDien-Office-SW1",label="Fas 0/46 to Gig 1/0/24",style=link_style)
diagram.add_link("TD-Office-SW03","TDien-Office-SW1",label="Fas 0/45 to Gig 1/0/23",style=link_style)
diagram.add_link("TD-Office-SW03","AP003a.7dd4.6d00",label="Gig 1/0/15 to Gig 0",style=poe_link)
diagram.add_link("TD-Office-SW03","AP0062.ec20.6110",label="Gig 1/0/14 to Gig 0",style=poe_link)
diagram.add_link("TD-Office-SW03","TD-B1-A13",label="Gig 1/0/13 to Gig 0",style=poe_link)
diagram.add_link("TD-Office-SW03","TD-B1-A03",label="Gig 1/0/3 to Gig 0",style=poe_link)
diagram.add_link("TD-Office-SW03","TD-B1-A12",label="Gig 1/0/12 to Gig 0",style=poe_link)
diagram.add_link("TD-Office-SW03","TD-B1-A11",label="Gig 1/0/11 to Gig 0",style=poe_link)
diagram.add_link("TD-Office-SW03","TD-B1-A10",label="Gig 1/0/10 to Gig 0",style=poe_link)
diagram.add_link("TD-Office-SW03","TD-B1-A01",label="Gig 1/0/1 to Gig 0",style=poe_link)
diagram.add_link("TD-Office-SW03","TD-B1-A06",label="Gig 1/0/6 to Gig 0",style=poe_link)
diagram.add_link("TD-Office-SW03","TD-B1-A07",label="Gig 1/0/7 to Gig 0",style=poe_link)
diagram.add_link("TD-Office-SW03","TD-B1-A04",label="Gig 1/0/4 to Gig 0",style=poe_link)
diagram.add_link("TD-Office-SW03","TD-B1-A05",label="Gig 1/0/5 to Gig 0",style=poe_link)
diagram.add_link("TD-Office-SW03","TD-B1-A08",label="Gig 1/0/8 to Gig 0",style=poe_link)
diagram.add_link("TD-Office-SW03","TD-B1-A09",label="Gig 1/0/9 to Gig 0",style=poe_link)
diagram.add_link("TD-Office-SW03","TDien-Elec-SW2",label="Gig 1/0/25 to Gig 1/0/25",style=link_style)
diagram.add_link("TD-Office-SW03","AP0062.ec19.6bac",label="Gig 1/0/2 to Gig 0",style=poe_link)
diagram.add_link("TDien-Elec-SW1","TDien-Elec-SW2",label="Fas 0/48 to Gig 1/0/24",style=poe_link)
diagram.add_link("TDien-Elec-SW1","TDien-Elec-SW2",label="Fas 0/47 to Gig 1/0/23",style=poe_link)
diagram.add_link("TDien-Elec-SW2","TD-B1-A19",label="Gig 1/0/9 to Gig 0",style=poe_link)
diagram.add_link("TDien-Elec-SW2","TD-B1-A14",label="Gig 1/0/5 to Gig 0",style=poe_link)
diagram.add_link("TDien-Elec-SW2","TD-B1-A15",label="Gig 1/0/1 to Gig 0",style=poe_link)
diagram.add_link("TDien-Elec-SW2","TD-B1-A16",label="Gig 1/0/2 to Gig 0",style=poe_link)
diagram.add_link("TDien-Elec-SW2","TD-B1-A17",label="Gig 1/0/8 to Gig 0",style=poe_link)
diagram.add_link("TDien-Elec-SW2","TD-B1-B03",label="Gig 1/0/3 to Gig 0",style=poe_link)
diagram.add_link("TDien-Elec-SW2","TD-B1-A20",label="Gig 1/0/10 to Gig 0",style=poe_link)


diagram.layout(algo="kk")
diagram.dump_file(filename="trungnl"+nowtime+"s.drawio", folder="./Output/")
print(nowtime)
print("Đã export file to ./Output")