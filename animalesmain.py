import sys              # Carpeta sistema para python, lo necesitamos para poder abrir aplicaciones
from PyQt5 import QtWidgets     #importa widgets
from PyQt5.QtWidgets import QDialog, QApplication, QTreeWidgetItem  #Ejecutar y QTreeWidgetItem caracteristicas de los widget
from PyQt5.uic import loadUi    #pip install pyuic5-tool
import xml.etree.ElementTree as et      #Carga el arbol

class Ventana(QDialog):     #Es la ventana principal

    def __init__(self):             #Variable base para llamar a la instancia principal
        super(Ventana, self).__init__()
        loadUi("Ventana.ui", self)
        arbolStr=open("Animales.xml", "r").read()
        self.mostrarArbol(arbolStr)     #"arbolStr" es una especie de string que contiene tódo el XML

    def mostrarArbol(self, arbolStr):
        arbol=et.fromstring(arbolStr)       #apunta al root
        self.treeWidget.setColumnCount(1)   #Solo necesitamos una columna --En este caso
        tags=QTreeWidgetItem([arbol.tag])
        self.treeWidget.addTopLevelItem(tags)      #Toma el tag del primer item y lo coloca como raiz del arbol

        def llenarArbol(tags, arbolStr):
            for child in arbolStr:
                branch=QTreeWidgetItem([child.tag])
                tags.addChild(branch)
                llenarArbol(branch, child)
            # if arbolStr.text is not None:
            #     contenido=arbolStr.text
            #     tags.addChild(QTreeWidgetItem([contenido]))

        llenarArbol(tags, arbol)


#Abrir
App=QApplication(sys.argv)
MainWindow=Ventana()
widget=QtWidgets.QStackedWidget()
widget.addWidget(MainWindow)
widget.setFixedWidth(500)
widget.setFixedHeight(400)
widget.show()
App.exec()
