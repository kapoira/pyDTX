# -*- coding: utf-8 -*-

import os
import configparser

import UtilidadesDTX

from PyQt5 import QtWidgets
from PyQt5 import QtGui

from WidgetNavegacion import Ui_WidgetNavegacion


class MyWidgetNavegacion(QtWidgets.QWidget):
    """
        Classe Widget donde se podra navegar entre los directorios de canciones
        viendo la información de los .dtx y .def además de poder configurar el
        nivel de sincronización
    """

    def __init__(self):
        """
            Creamos los valores iniciales
        """
        super(MyWidgetNavegacion, self).__init__()

        self.ui = Ui_WidgetNavegacion()
        self.ui.setupUi(self)
        self.ui.listWidget.itemSelectionChanged.connect(self.cambio_seleccion)

        #Conectamos los botones a sus funciones
        self.ui.downButton.clicked.connect(self.seleccion_abajo)
        self.ui.upButton.clicked.connect(self.seleccion_arriba)
        self.ui.backButton.clicked.connect(self.seleccion_back)
        self.ui.selectButton.clicked.connect(self.seleccion_select)
        self.ui.changedirButton.clicked.connect(self.seleccion_changedir)
        self.ui.l1_Button.clicked.connect(self.seleccion_select_l1)
        self.ui.l2_Button.clicked.connect(self.seleccion_select_l2)
        self.ui.l3_Button.clicked.connect(self.seleccion_select_l3)
        self.ui.l4_Button.clicked.connect(self.seleccion_select_l4)
        self.ui.l5_Button.clicked.connect(self.seleccion_select_l5)
        self.ui.speed_inc_Button.clicked.connect(self.speed_inc)
        self.ui.speed_dec_Button.clicked.connect(self.speed_dec)

        #Instalamos los filtros en los botones de l1..l5 para poder actualizar
        self.ui.l1_Button.installEventFilter(self)
        self.ui.l2_Button.installEventFilter(self)
        self.ui.l3_Button.installEventFilter(self)
        self.ui.l4_Button.installEventFilter(self)
        self.ui.l5_Button.installEventFilter(self)

        #Leemos la configuracion de pydtx
        config_dtx = configparser.ConfigParser()
        config_dtx.read('config_dtx.ini')

        #Leemos la configuracion del dtx para tener el tiempo de pantalla
        self.config_dtx = configparser.ConfigParser()
        self.config_dtx.read('config_dtx.ini')
        self.tiempo_pantalla = int(self.config_dtx['DTX']['speed'])
        self.ui.speed_label.setText(str(self.tiempo_pantalla))

        self.path_songs = config_dtx['Songs']['path']
        self.path_songs_inicial = config_dtx['Songs']['path']

        #Rehacemos toda la lista de directorios
        self.rehacer_lista()

    def eventFilter(self, source, event):
        """
            Si se activa el focus en un button de l1..l5 tenemos que actualizar
            la información en pantalla
        """
        if source == self.ui.l1_Button:
            if event.type() == QtGui.QFocusEvent.FocusIn:
                #Han seleccionado el L1
                datos = self.lista_info_items[self.seleccionado][4][2]
                self.actualizar_datos(datos)
        elif source == self.ui.l2_Button:
            if event.type() == QtGui.QFocusEvent.FocusIn:
                #Han seleccionado el L2
                datos = self.lista_info_items[self.seleccionado][3][2]
                self.actualizar_datos(datos)
        elif source == self.ui.l3_Button:
            if event.type() == QtGui.QFocusEvent.FocusIn:
                #Han seleccionado el L3
                datos = self.lista_info_items[self.seleccionado][2][2]
                self.actualizar_datos(datos)
        elif source == self.ui.l4_Button:
            if event.type() == QtGui.QFocusEvent.FocusIn:
                #Han seleccionado el L4
                datos = self.lista_info_items[self.seleccionado][1][2]
                self.actualizar_datos(datos)
        elif source == self.ui.l5_Button:
            if event.type() == QtGui.QFocusEvent.FocusIn:
                #Han seleccionado el L5
                datos = self.lista_info_items[self.seleccionado][0][2]
                self.actualizar_datos(datos)
        #Devolvemos False para que el handler de Qt5 pueda continuar su trabajo
        return False

    def speed_inc(self):
        """
            Tenemos que disminuir el tiempo de pantalla
            comprobar limite de 100ms
        """
        if self.tiempo_pantalla > 100:
            self.tiempo_pantalla = self.tiempo_pantalla - 100
            self.ui.speed_label.setText(str(self.tiempo_pantalla))

    def speed_dec(self):
        """
            Tenemos que aumentar el tiempo de pantalla
            comprobar limite de 5000ms
        """
        if self.tiempo_pantalla < 5000:
            self.tiempo_pantalla = self.tiempo_pantalla + 100
            self.ui.speed_label.setText(str(self.tiempo_pantalla))

    def seleccion_abajo(self):
        """
            Tenemos que seleccionar siguiente objeto de la lista de items y
            actualizar
        """
        if ((self.seleccionado + 1) < len(self.lista_items)):
            self.seleccionado = self.seleccionado + 1
            self.ui.listWidget.setCurrentRow(self.seleccionado)

    def seleccion_arriba(self):
        """
            Tenemos que seleccionar objeto anterior de la lista de items y
            actualizar
        """
        if self.seleccionado > 0:
            self.seleccionado = self.seleccionado - 1
            self.ui.listWidget.setCurrentRow(self.seleccionado)

    def seleccion_back(self):
        """
            Intentamos subir un nivel en el árbol de directorio si hemos llegado
            al nivel inicial volvemos al menú principal
        """
        if self.path_songs == self.path_songs_inicial:
            self.parentWidget().setCurrentIndex(0)
        else:
            self.path_songs = os.path.dirname(self.path_songs)
            self.rehacer_lista()

    def cambio_seleccion(self):
        """
            Se ha cambiado la seleccion de la lista de items, por lo que se
            tiene que actualizar toda la información de la pantalla
        """
        self.seleccionado = self.ui.listWidget.currentRow()
        #Borramos toda la información de las canciones de la pantalla
        self.imagenCancion = None
        self.ui.imagenCancion.clear()
        self.ui.label_name.setText("Author:")
        self.ui.label_dificulty.setText("Dificulty:")
        self.ui.label_others.setText("")
        #Desactivamos los botones de l1..l5
        self.ui.l1_Button.hide()
        self.ui.l2_Button.hide()
        self.ui.l3_Button.hide()
        self.ui.l4_Button.hide()
        self.ui.l5_Button.hide()
        #Desactivamos el botón de un .dtx
        self.ui.selectButton.hide()
        #Desactivamos el botón de cambiar de directorio
        self.ui.changedirButton.hide()
        #Pasamos a analizar el elemento seleccionado
        if len(self.lista_info_items[self.seleccionado]) == 4:
            #Es un .dtx
            self.ui.selectButton.show()
            self.actualizar_datos(self.lista_info_items[self.seleccionado])
        elif len(self.lista_info_items[self.seleccionado]) == 5:
            #Estamos en un set.def, actualizamos los l1..l5
            self.actualizar_button_label(self.ui.l1_Button, 4)
            self.actualizar_button_label(self.ui.l2_Button, 3)
            self.actualizar_button_label(self.ui.l3_Button, 2)
            self.actualizar_button_label(self.ui.l4_Button, 1)
            self.actualizar_button_label(self.ui.l5_Button, 0)
        else:
            #Es un directorio
            self.ui.changedirButton.show()

    def actualizar_button_label(self, button, posicion):
        """
            Tenemos que actualizar un botón de estilo lX con los valores
            que nos indican

            button: boton que tenemos que modificar
            posicion: apunta a los datos que tenemos que usar
        """
        info_label = self.lista_info_items[self.seleccionado][posicion]
        if info_label[1]:
                button.setText(info_label[0])
                button.show()
                self.actualizar_datos(info_label[2])

    def actualizar_datos(self, datos):
        """
            Actualizar los datos de la canción con la informacion que nos pasan

            datos: datos de la cancion
        """
        if datos[0]:
            self.imagenCancion = QtGui.QPixmap(datos[0])
            self.ui.imagenCancion.setPixmap(self.imagenCancion)
        if datos[1]:
            self.ui.label_name.setText(datos[1])
        if datos[2]:
            self.ui.label_dificulty.setText(datos[2])
        if datos[3]:
            self.ui.label_others.setText(datos[3])

    def seleccion_changedir(self):
        """
            Tenemos que cambiar el directorio actual al seleccionado
        """
        self.path_songs = self.lista_items[self.seleccionado]
        self.rehacer_lista()

    def seleccion_select(self):
        """
            Selecciona el .dtx y comenzamos la cancion con el tiempo actual
        """
        self.parentWidget().setCurrentIndex(4)
        path = self.lista_items[self.seleccionado]
        encontrado = False
        #Buscamos el dtx de ese directorio
        for name in os.listdir(path):
            dtx_file = os.path.join(path, name)
            if name.endswith('.dtx') or name.endswith('.DTX'):
                if not(encontrado):
                    #Comenzamos el reproductor
                    widgetDTX = self.parentWidget().currentWidget()
                    widgetDTX.reproducir_cancion(dtx_file, self.tiempo_pantalla)
                    encontrado = True

    def seleccion_label(self, selec):
        """
            Estamos en un boton de L1..L5 tenemos que comenzar la canción
            con el tiempo actual

            selec: apuntara al .dtx de este label
        """
        self.parentWidget().setCurrentIndex(4)
        path = self.lista_info_items[self.seleccionado][selec][1]
        widgetDTX = self.parentWidget().currentWidget()
        widgetDTX.reproducir_cancion(path, self.tiempo_pantalla)

    def seleccion_select_l1(self):
        """
            Se ha pulsado el boton l1 comenzamos la canción de este botón
        """
        self.seleccion_label(4)

    def seleccion_select_l2(self):
        """
            Se ha pulsado el boton l2 comenzamos la canción de este botón
        """
        self.seleccion_label(3)

    def seleccion_select_l3(self):
        """
            Se ha pulsado el boton l3 comenzamos la canción de este botón
        """
        self.seleccion_label(2)

    def seleccion_select_l4(self):
        """
            Se ha pulsado el boton l4 comenzamos la canción de este botón
        """
        self.seleccion_label(1)

    def seleccion_select_l5(self):
        """
            Se ha pulsado el boton l5 comenzamos la canción de este botón
        """
        self.seleccion_label(0)

    def rehacer_lista(self):
        """
            Tenemos que buscar toda la información dentro del directorio actual
        """
        #Borramos toda la información gráfica
        self.ui.listWidget.clear()
        self.lista_items = []
        self.lista_info_items = []
        #Buscamos todos los subdirectorios
        lista_subdirec = UtilidadesDTX.buscar_subdirectorios(self.path_songs)
        for name in lista_subdirec:
            #Actualizamos por cada subdirectorio
            self.ui.listWidget.addItem(name)
            posible_file = os.path.join(self.path_songs, name)
            self.lista_items.append(posible_file)
            info_directorio = UtilidadesDTX.buscar_info_directorio(posible_file)
            self.lista_info_items.append(info_directorio)
        #Si hay subdirectorios ya seleccionamos el primero
        self.seleccionado = 0
        if len(self.lista_items) > 0:
            self.ui.listWidget.setCurrentRow(self.seleccionado)