# -*- coding: utf-8 -*-

import configparser

from PyQt5 import QtWidgets

from WidgetConfigurarDTX import Ui_WidgetConfigurarDTX


class MyWidgetConfigurarDTX(QtWidgets.QWidget):
    """
        Classe Widget tendra sera donde se configuren tocas las teclas tanto
        las de teclado como las de bateria-MIDI
    """

    def __init__(self):
        """
            Creamos los valores iniciales
        """
        super(MyWidgetConfigurarDTX, self).__init__()

        self.ui = Ui_WidgetConfigurarDTX()
        self.ui.setupUi(self)

        #Conectamos los botones
        self.ui.exitButton.pressed.connect(self.exit)
        self.ui.saveButton.pressed.connect(self.save_config_dtx)
        self.ui.speed_SpinBox.valueChanged.connect(self.visualizar_tiempos)

        #Leemos la configuracion y ponemos los valores en la información gráfica
        self.leer_config_dtx()

    def exit(self):
        """
            Volvemos al menu principal, para ello apuntamos en el stackedwidget
            al principal
        """
        self.parentWidget().setCurrentIndex(0)

    def leer_config_dtx(self):
        """
            Leemos el fichero de configuración del dtx, y según sus valores
            ponemos los elementos gráficos
        """
        #Leemos el fichero de configuración
        self.config_dtx = configparser.ConfigParser()
        self.config_dtx.read('config_dtx.ini')
        #Ponemos los elementos gráficos según el fichero
        if self.config_dtx['Graphics']['OpenGl'] == 'true':
            self.ui.checkBox_Gl.setChecked(True)
        else:
            self.ui.checkBox_Gl.setChecked(False)
        self.ui.theme_LineEdit.setText(self.config_dtx['Graphics']['theme'])
        self.ui.songs_LineEdit.setText(self.config_dtx['Songs']['path'])
        tiempo = int(self.config_dtx['DTX']['speed'])
        self.ui.speed_SpinBox.setValue(tiempo)
        self.visualizar_tiempos(tiempo)

    def save_config_dtx(self):
        """
            Analizamos los elementos gráficos y según ellos escribimos en el
            fichero de configuración
        """
        self.config_dtx['DTX'] = {}
        self.config_dtx['DTX']['speed'] = str(self.ui.speed_SpinBox.value())

        theme = self.ui.theme_LineEdit.text()
        self.config_dtx['Graphics']['theme'] = theme
        songs = self.ui.songs_LineEdit.text()
        self.config_dtx['Songs']['path'] = songs
        if self.ui.checkBox_Gl.checkState():
            self.config_dtx['Graphics']['opengl'] = 'true'
        else:
            self.config_dtx['Graphics']['opengl'] = 'false'
        #Grabamos el fichero
        with open('config_dtx.ini', 'w') as configfile:
            self.config_dtx.write(configfile)

    def visualizar_tiempos(self, tiempo):
        """
            Calculamos los tiempos de sincronización y los ponemos en sus
            elementos gráficos para que de esta manera se pueda conocer el nivel
            de sincronización

            tiempo: tiempo base que se empleara para calcular la sincronización
        """
        #Calculamos los valores según tiempo
        #tiempo base es el tiempo que tarda un chip en recorrer toda la pantalla
        tiempo_limpio = str(round(tiempo / 15, 2))
        perfect = "-" + tiempo_limpio + ".." + tiempo_limpio + "ms"
        tiempo_limpio = str(round(tiempo / 10, 2))
        great = "-" + tiempo_limpio + ".." + tiempo_limpio + "ms"
        tiempo_limpio = str(round(tiempo / 5, 2))
        good = "-" + tiempo_limpio + ".." + tiempo_limpio + "ms"
        tiempo_limpio = str(round(tiempo / 2, 2))
        poor = "-" + tiempo_limpio + ".." + tiempo_limpio + "ms"

        #Actualizmos los Labels
        self.ui.perfect_time_Label.setText(perfect)
        self.ui.great_time_Label.setText(great)
        self.ui.good_time_Label.setText(good)
        self.ui.poor_time_Label.setText(poor)
