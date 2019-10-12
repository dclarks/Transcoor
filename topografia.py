#--coding: utf-8 --
#!/usr/bin/env python   # (if running from bash)
import math

from PySide.QtCore import *
from PySide.QtGui import *
#from PySide import QtCore, QtGui

#import transCor
import re

import ezdxf

from PySide import QtCore, QtGui
from transCor import JanelaPrincipal

class Topografia(JanelaPrincipal):
    def __init__(self, parent=None):
        JanelaPrincipal.pushButton_3.clicked.connect(self.estounotopografia)


    def estounotopografia(self):
        print "estou lá"







#import ezdxf
# Create a new drawing in the DXF format of AutoCAD 2010
dwg = ezdxf.new('ac1024')
# Create a block with the name 'FLAG'
flag = dwg.blocks.new(name='ponto')
# Add DXF entities to the block 'FLAG'.
# The default base point (= insertion point) of the block is (0, 0).
#flag.add_polyline2d([(0, 0), (0, 5), (4, 3), (0, 3)])  # the flag as 2D polyline

dwg.styles.new('custom', dxfattribs={'font': 'arial.ttf', 'width': 0.8})  # Arial, default width factor of 0.8
flag.add_circle((0, 0), 0.5, dxfattribs={'color': 3})  # mark the base point with a circle
flag.add_attrib("e", "example text", dxfattribs={'style': 'custom'}).set_pos((3, 7), align='MIDDLE_CENTER')
#flag.add_text("teste")
flag.add_text("MURO",dxfattribs={'color': 1}).set_pos((0, 2.2), align='CENTER') # color 1 = vermelho
flag.add_text("1", dxfattribs={'color':2}).set_pos((0,1), align='CENTER') # color 3 = verde, color 2 = amarelo

# Get the modelspace of the drawing.
modelspace = dwg.modelspace()
# Add a block reference to the block named 'FLAG' at the coordinates 'point'.
modelspace.add_blockref('ponto', (100, 100), dxfattribs={'xscale':1,'yscale':1,'rotation':0, 'layer': 'Pontos', 'name': 'eu'})
#modelspace.add_blockref('ponto', (0, 0), dxfattribs={'xscale':1,'yscale':1,'rotation':-15, 'layer': 'Pontos', 'name': 'eu'})

#modelspace.add_text("1", dxfattribs={'style': 'custom', 'height': 1}).set_pos((102, 102), align='RIGHT')

# Define some attributes for the block 'FLAG', placed relative to the base point, (0, 0) in this case.
#flag.add_attdef('NAME', (0.5, -0.5), {'height': 0.5, 'color': 3})
#flag.add_attdef('XPOS', (0.5, -1.0), {'height': 0.25, 'color': 4})
#flag.add_attdef('YPOS', (0.5, -1.5), {'height': 0.25, 'color': 4})





dwg.layers.new(name='MyLines', dxfattribs={'linetype': 'DASHED', 'color': 7})
my_lines = dwg.layers.get('MyLines')
my_lines.is_on()   # True if layer is on
modelspace.add_line((0, 0), (100, 0), dxfattribs={'layer': 'Lines'})


# Save the drawing.
dwg.saveas("topografiaDXF.dxf")
print "topografiaDXF ok!"


