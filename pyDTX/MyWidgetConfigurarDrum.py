# -*- coding: utf-8 -*-

import configparser
import rtmidi2

from PyQt5 import QtWidgets

from WidgetConfigurarDrum import Ui_WidgetConfigurarDrum


class MyWidgetConfigurarDrum(QtWidgets.QWidget):
    """
        Classe Widget tendra sera donde se configuren tocas las teclas tanto
        las de teclado como las de bateria-MIDI
    """

    def __init__(self):
        """
            Creamos los valores iniciales
        """
        super(MyWidgetConfigurarDrum, self).__init__()

        self.ui = Ui_WidgetConfigurarDrum()
        self.ui.setupUi(self)

        #Leemos la configuracion
        self.leer_config_drum()

        #Conectamos los botones a sus funciones
        self.ui.exitButton.pressed.connect(self.exit)
        self.ui.saveConfigurationButton.pressed.connect(self.save_config_drum)
        self.ui.portsConnectedButton.pressed.connect(self.view_ports)
        self.ui.viewNotesButton.pressed.connect(self.view_note)

        self.midi_in = None

    def view_ports(self):
        """
            Mostramos en el text asociado, que puertos (instrumentos) MIDI
            vemos conectados.
        """
        #Creamos el texto para que sea más legible que puertos estamos viendo
        i = 0
        text = ""
        for port in rtmidi2.get_in_ports():
            text = text + str(i) + " : " + port + "\n"
            i = i + 1
        #Ponemos en el label asociado todos los puertos que estamos viendo
        self.ui.portsConnectedTextEdit.setPlainText(text)

    def view_note(self):
        """
            Conectamos la bateria-MIDI al midi Handler
        """

        def midi_handler(message, time_stamp):
            """
                Si detectamos un mensaje MIDI de tipo note-on ponemos la nota
                en el line edir asociado

                message: message MIDI
                time_stamp: tiempo diferido desde el mensaje hasta ahora
            """
            if message[0] == 153:
            #Nota On
                self.ui.viewNotesLineEdit.setText(str(message[1]))

        self.midi_in = rtmidi2.MidiIn()
        midi_port = self.ui.portMidiSpinBox.value()
        if midi_port < len(rtmidi2.get_in_ports()):
            #Puede estar desconectado al menos comprobar que cuadra números
            self.midi_in.open_port(midi_port)
                #Juntamos el midi a la funcion de entrada
        self.midi_in.callback = midi_handler

    def exit(self):
        """
            Volvemos al menu principal, para ello apuntamos en el stackedwidget
            al widget principal y desactivamos el MIDI
        """
        self.midi_in = None
        self.ui.viewNotesLineEdit.setText("")
        self.parentWidget().setCurrentIndex(0)

    def leer_lane_drum(self, lane, auto, midi1, midi2, key):
        """
            Coger los valores del lane según configuración y ponerlos
            en las variables

            lane: lane de la que leeremos los datos
            auto: checkbox a poner el valor auto
            midi1: Spinbox a poner el valor del midi1 de este lane
            midi2: Spinbox a poner el valor del midi2 de este lane
            key: Textbox a poner el valor del teclado de este lane
        """
        if self.config_drum[lane]['auto'] == 'true':
            auto.setChecked(True)
        else:
            auto.setChecked(False)
        midi1.setValue(int(self.config_drum[lane]['midi_1']))
        midi2.setValue(int(self.config_drum[lane]['midi_2']))
        key.setText(self.config_drum[lane]['key'])

    def leer_config_drum(self):
        """
            Leemos el fichero de configuración del drum y modificamos todos
            los elementos gráficos

        """
        #Leemos el fichero de configuración
        self.config_drum = configparser.ConfigParser()
        self.config_drum.read('config_drum.ini')
        midi_port = self.config_drum['MIDI']['midi_port']
        self.ui.portMidiSpinBox.setValue(int(midi_port))

        #Lane11
        self.leer_lane_drum('Lane_11',
                             self.ui.auto_lane11_CheckBox,
                             self.ui.midi1_lane11_SpinBox,
                             self.ui.midi2_lane11_SpinBox,
                             self.ui.key_lane_11_LineEdit)
        #Lane12
        self.leer_lane_drum('Lane_12',
                             self.ui.auto_lane12_CheckBox,
                             self.ui.midi1_lane12_SpinBox,
                             self.ui.midi2_lane12_SpinBox,
                             self.ui.key_lane_12_LineEdit)
        #Lane12
        self.leer_lane_drum('Lane_13',
                             self.ui.auto_lane13_CheckBox,
                             self.ui.midi1_lane13_SpinBox,
                             self.ui.midi2_lane13_SpinBox,
                             self.ui.key_lane_13_LineEdit)
        #Lane14
        self.leer_lane_drum('Lane_14',
                             self.ui.auto_lane14_CheckBox,
                             self.ui.midi1_lane14_SpinBox,
                             self.ui.midi2_lane14_SpinBox,
                             self.ui.key_lane_14_LineEdit)
        #Lane15
        self.leer_lane_drum('Lane_15',
                             self.ui.auto_lane15_CheckBox,
                             self.ui.midi1_lane15_SpinBox,
                             self.ui.midi2_lane15_SpinBox,
                             self.ui.key_lane_15_LineEdit)
        #Lane16
        self.leer_lane_drum('Lane_16',
                             self.ui.auto_lane16_CheckBox,
                             self.ui.midi1_lane16_SpinBox,
                             self.ui.midi2_lane16_SpinBox,
                             self.ui.key_lane_16_LineEdit)
        #Lane17
        self.leer_lane_drum('Lane_17',
                             self.ui.auto_lane17_CheckBox,
                             self.ui.midi1_lane17_SpinBox,
                             self.ui.midi2_lane17_SpinBox,
                             self.ui.key_lane_17_LineEdit)
        #Lane18
        self.leer_lane_drum('Lane_18',
                             self.ui.auto_lane18_CheckBox,
                             self.ui.midi1_lane18_SpinBox,
                             self.ui.midi2_lane18_SpinBox,
                             self.ui.key_lane_18_LineEdit)
        #Lane19
        self.leer_lane_drum('Lane_19',
                             self.ui.auto_lane19_CheckBox,
                             self.ui.midi1_lane19_SpinBox,
                             self.ui.midi2_lane19_SpinBox,
                             self.ui.key_lane_19_LineEdit)
        #Lane1A
        self.leer_lane_drum('Lane_1A',
                             self.ui.auto_lane1A_CheckBox,
                             self.ui.midi1_lane1A_SpinBox,
                             self.ui.midi2_lane1A_SpinBox,
                             self.ui.key_lane_1A_LineEdit)
        #Lane1B
        self.leer_lane_drum('Lane_1B',
                             self.ui.auto_lane1B_CheckBox,
                             self.ui.midi1_lane1B_SpinBox,
                             self.ui.midi2_lane1B_SpinBox,
                             self.ui.key_lane_1B_LineEdit)
        #Lane1C
        self.leer_lane_drum('Lane_1C',
                             self.ui.auto_lane1C_CheckBox,
                             self.ui.midi1_lane1C_SpinBox,
                             self.ui.midi2_lane1C_SpinBox,
                             self.ui.key_lane_1C_LineEdit)

    def guardar_lane_drum(self, lane, auto, midi1, midi2, key):
        """
            Guardamos en la configuración los valores del lane

            lane: lane de la que guardaremos los datos
            auto:  valor auto de la lane
            midi1: valor del midi1 de este lane
            midi2: valor del midi2 de este lane
            key:  valor del teclado de este lane
        """
        self.config_drum[lane] = {}
        if auto:
            self.config_drum[lane]['auto'] = 'true'
        else:
            self.config_drum[lane]['auto'] = 'false'
        self.config_drum[lane]['midi_1'] = midi1
        self.config_drum[lane]['midi_2'] = midi2
        self.config_drum[lane]['key'] = key

    def save_config_drum(self):
        """
            Salvamos los valores del widget en el fichero de configuración
        """
        self.config_drum['MIDI'] = {}
        midi_port = self.ui.portMidiSpinBox.value()
        self.config_drum['MIDI']['midi_port'] = str(midi_port)

        #Lane 11
        self.guardar_lane_drum('Lane_11',
                                self.ui.auto_lane11_CheckBox.checkState(),
                                str(self.ui.midi1_lane11_SpinBox.value()),
                                str(self.ui.midi2_lane11_SpinBox.value()),
                                self.ui.key_lane_11_LineEdit.text())
        #Lane 12
        self.guardar_lane_drum('Lane_12',
                                self.ui.auto_lane12_CheckBox.checkState(),
                                str(self.ui.midi1_lane12_SpinBox.value()),
                                str(self.ui.midi2_lane12_SpinBox.value()),
                                self.ui.key_lane_12_LineEdit.text())
        #Lane 13
        self.guardar_lane_drum('Lane_13',
                                self.ui.auto_lane13_CheckBox.checkState(),
                                str(self.ui.midi1_lane13_SpinBox.value()),
                                str(self.ui.midi2_lane13_SpinBox.value()),
                                self.ui.key_lane_13_LineEdit.text())
        #Lane 14
        self.guardar_lane_drum('Lane_14',
                                self.ui.auto_lane14_CheckBox.checkState(),
                                str(self.ui.midi1_lane14_SpinBox.value()),
                                str(self.ui.midi2_lane14_SpinBox.value()),
                                self.ui.key_lane_14_LineEdit.text())
        #Lane 15
        self.guardar_lane_drum('Lane_15',
                                self.ui.auto_lane15_CheckBox.checkState(),
                                str(self.ui.midi1_lane15_SpinBox.value()),
                                str(self.ui.midi2_lane15_SpinBox.value()),
                                self.ui.key_lane_15_LineEdit.text())
        #Lane 16
        self.guardar_lane_drum('Lane_16',
                                self.ui.auto_lane16_CheckBox.checkState(),
                                str(self.ui.midi1_lane16_SpinBox.value()),
                                str(self.ui.midi2_lane16_SpinBox.value()),
                                self.ui.key_lane_16_LineEdit.text())
        #Lane 17
        self.guardar_lane_drum('Lane_17',
                                self.ui.auto_lane17_CheckBox.checkState(),
                                str(self.ui.midi1_lane17_SpinBox.value()),
                                str(self.ui.midi2_lane17_SpinBox.value()),
                                self.ui.key_lane_17_LineEdit.text())
        #Lane 18
        self.guardar_lane_drum('Lane_18',
                                self.ui.auto_lane18_CheckBox.checkState(),
                                str(self.ui.midi1_lane18_SpinBox.value()),
                                str(self.ui.midi2_lane18_SpinBox.value()),
                                self.ui.key_lane_18_LineEdit.text())
        #Lane 19
        self.guardar_lane_drum('Lane_19',
                                self.ui.auto_lane19_CheckBox.checkState(),
                                str(self.ui.midi1_lane19_SpinBox.value()),
                                str(self.ui.midi2_lane19_SpinBox.value()),
                                self.ui.key_lane_19_LineEdit.text())
        #Lane 1A
        self.guardar_lane_drum('Lane_1A',
                                self.ui.auto_lane1A_CheckBox.checkState(),
                                str(self.ui.midi1_lane1A_SpinBox.value()),
                                str(self.ui.midi2_lane1A_SpinBox.value()),
                                self.ui.key_lane_1A_LineEdit.text())
        #Lane 1B
        self.guardar_lane_drum('Lane_1B',
                                self.ui.auto_lane1B_CheckBox.checkState(),
                                str(self.ui.midi1_lane1B_SpinBox.value()),
                                str(self.ui.midi2_lane1B_SpinBox.value()),
                                self.ui.key_lane_1B_LineEdit.text())
        #Lane 1C
        self.guardar_lane_drum('Lane_1C',
                                self.ui.auto_lane1C_CheckBox.checkState(),
                                str(self.ui.midi1_lane1C_SpinBox.value()),
                                str(self.ui.midi2_lane1C_SpinBox.value()),
                                self.ui.key_lane_1C_LineEdit.text())
        #Guardamos en el fichero
        with open('config_drum.ini', 'w') as configfile:
            self.config_drum.write(configfile)