#!usr/bin/env Python3
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets

from MyMainWindowQt5 import MyMainWindowQt5
from MyWidgetNavegacion import MyWidgetNavegacion
from MyWidgetConfigurarDrum import MyWidgetConfigurarDrum
from MyWidgetConfigurarDTX import MyWidgetConfigurarDTX
from ReproductorDTX import ReproductorDTX


version = "1.0.0"


def main():
    """
     Programa principal creamos ventana principal, stacked widgets
    """

    print ("pyDTX", version, "<kapoira@gmail.com>")

    #Crear la aplicacion y cargar la configuracion de los archivos
    app = QtWidgets.QApplication(sys.argv)

    #Creamos la ventana principal
    mainWindow = MyMainWindowQt5()

    #Creamos las ventanas en stack para ya tenerlas en memoria
    ui_widgetNavegacion = MyWidgetNavegacion()
    mainWindow.ui.stackedWidget.insertWidget(1, ui_widgetNavegacion)
    ui_widgetConfigurarDrum = MyWidgetConfigurarDrum()
    mainWindow.ui.stackedWidget.insertWidget(2, ui_widgetConfigurarDrum)
    ui_widgetConfigurarDTX = MyWidgetConfigurarDTX()
    mainWindow.ui.stackedWidget.insertWidget(3, ui_widgetConfigurarDTX)
    ui_widgetReproductor = ReproductorDTX()
    mainWindow.ui.stackedWidget.insertWidget(4, ui_widgetReproductor)

    #Bucle principal
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    """
    La llamada desde terminal ejecuta el codigo main()
    """
    main()