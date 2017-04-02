# -*- coding: utf-8 -*-

import configparser

from PyQt5 import QtWidgets

from MainWindowQt5 import Ui_MainWindow


class MyMainWindowQt5(QtWidgets.QMainWindow):
    """
        Classe Main Window tendra el stackwidget principal, y por defecto pondra
        la pantalla inicial
    """

    def __init__(self):
        """
            Creamos los valores iniciales
        """
        super(MyMainWindowQt5, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Conectamos los botones de la pantalla principal
        self.ui.button_StartGame.pressed.connect(self.cambiar_a_navegacion)
        self.ui.button_ConfigureDrum.pressed.connect(self.cambiar_drum_keys)
        self.ui.button_ConfigureDTX.clicked.connect(self.cambiar_config_dtx)
        self.ui.button_Quit.clicked.connect(self.salir)

        #Cargamos configuracion de dtx ya que el tema depende de la conf
        config_dtx = configparser.ConfigParser()
        config_dtx.read('config_dtx.ini')
        theme = config_dtx['Graphics']['theme']

        #Ponemos el background dependiendo de la configuración
        style_sheet = "#Principal{border-image: url(" + theme + \
                       "/background_menu.jpg) stretch stretch " + "; }"

        self.ui.Principal.setStyleSheet(style_sheet)

    def cambiar_a_navegacion(self):
        """
            Cambiamos el stackedwidget al widget de navegación
        """
        self.ui.stackedWidget.setCurrentIndex(1)

    def cambiar_drum_keys(self):
        """
            Cambiamos el stackedwidget al widget de configurar las teclas
        """
        self.ui.stackedWidget.setCurrentIndex(2)

    def cambiar_config_dtx(self):
        """
            Cambiamos el stackedwidget al widget de configurar de pydtx
        """
        self.ui.stackedWidget.setCurrentIndex(3)

    def cambiar_menu_principal(self):
        """
            Cambiamos el stackedwidget al widget inicial
        """
        self.ui.stackedWidget.setCurrentIndex(0)

    def cambiar_reproduccion(self):
        """
            Cambiaremos al widget de reproduccion
            esta funcion la llamaran antes de comenzar una cancion
        """
        self.ui.stackedWidget.setCurrentIndex(4)

    def salir(self):
        """
            Salir del programa, para ello cerramos el stacked widget
        """
        self.close()
