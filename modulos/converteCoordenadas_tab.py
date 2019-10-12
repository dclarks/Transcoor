#!/usr/bin/python3
#--coding: utf-8 --

try:
    from PySide import QtGui, QtCore
    from PySide.QtGui import *
    from PySide.QtCore import *
except ImportError:
    from PySide2 import QtGui, QtCore, QtWidgets
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *



class converteCoordenadas(QtWidgets.QDialog):
   'Common base class for all employees'


   def __init__(self):
       QtWidgets.QDialog.__init__(self,parent=None)
       self.ui = JanelaPrincipal()




