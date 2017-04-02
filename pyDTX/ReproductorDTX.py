#!usr/bin/env Python
# -*- coding: utf-8 -*-
import configparser
import os
import rtmidi2

import UtilidadesDTX

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtMultimedia import QSoundEffect


from Chip import Chip
from ChipAuto import ChipAuto
from LaneAuto import LaneAuto
from LaneVisual import LaneVisual
from MyWidgetPuntuacion import MyWidgetPuntuacion


class ReproductorDTX(QtWidgets.QGraphicsView):
    """
        Clase GraphicsView ya que pintaremos la canción en sí, además de hacer
        todo el control de la canción
    """
    def __init__(self):
        """
            Creamos los valores iniciales
        """
        QtWidgets.QGraphicsView.__init__(self)
        self.borrar_datos_cancion()
        #Leemos configuracion para configurar dependiendo de valores
        self.leer_config_dtx()

        if self.config_dtx['Graphics']['OpenGl'] == 'true':
            self.setViewport(QtWidgets.QOpenGLWidget())

        #Desactivamos que salgan las barras de scroll
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    def resizeEvent(self, event):
        """
            Esta función es para cuando se haga un resize de la ventana
            siempre estamos viendo la cancion redimensionada en consecuencia
            para ello volvemos a definir el la resolución interna del visor

            event: el evento que ha disparado este resize
        """
        self.fitInView(QtCore.QRectF(0, 0, 1264, 714))

    def keyPressEvent(self, event):
        """
            Han pulsado una tecla, tenemos que comprobar si es de un lane
            la puntuación

            event: el evento de Key que ha disparado esta función
        """
        if event.key() == QtCore.Qt.Key_Escape:
            #Tecla especial para salir
            self.salir()
        elif event.text() in self.dict_teclado:
            #Tenemos esta tecla definida en la configuración de teclado
            tiempo_actual = float(self.timer.elapsed())
            lane_selec = self.dict_teclado[event.text()]
            lane = self.dict_lanes_visual[lane_selec]
            tiempo_puntuacion = lane.comprobar_y_poner_hit(tiempo_actual)
            self.puntuacion.comprobar_puntuacion(tiempo_puntuacion)

    def configurar_teclado_lane(self, lane_en_conf, lane):
        """
            Si el lane no esta en auto cogemos la key y la ponemos en el dicc

            lane_en_conf: Nombre de lane según configuración
            lane: Nombre que se pondra en el diccionario de teclas
        """
        if self.config_drum[lane_en_conf]['auto'] == 'false':
            tecla = self.config_drum[lane_en_conf]['key']
            self.dict_teclado[tecla] = lane

    def configurar_teclado(self):
        """
            Según la configuracion guardada se crea el teclado que usaremos
            para comprobar si se pulsa una tecla a que lane le corresponde
        """
        self.dict_teclado = {}
        self.configurar_teclado_lane('Lane_11', '11')
        self.configurar_teclado_lane('Lane_12', '12')
        self.configurar_teclado_lane('Lane_13', '13')
        self.configurar_teclado_lane('Lane_14', '14')
        self.configurar_teclado_lane('Lane_15', '15')
        self.configurar_teclado_lane('Lane_16', '16')
        self.configurar_teclado_lane('Lane_17', '17')
        self.configurar_teclado_lane('Lane_18', '18')
        self.configurar_teclado_lane('Lane_19', '19')
        self.configurar_teclado_lane('Lane_1A', '1A')
        self.configurar_teclado_lane('Lane_1B', '1B')
        self.configurar_teclado_lane('Lane_1C', '1C')

    def configurar_midi_lane(self, lane_en_conf, lane):
        """
            Dado un lane en concreto tenemos que mirar la configuracion para
            poner sus posibles notas-midi en el dicc, cuidado que puede estar
            duplicadas

            lane_en_conf: Nombre de lane según configuración
            lane: Nombre que se pondra en el diccionario de midi
        """
        if self.config_drum[lane_en_conf]['auto'] == 'false':
            midi1 = int(self.config_drum[lane_en_conf]['midi_1'])
            midi2 = int(self.config_drum[lane_en_conf]['midi_2'])
            if midi1 > 0:
                if midi1 in self.dict_midi:
                    #Esta nota midi ya tiene un lane asociado
                    lista = self.dict_midi[midi1]
                    lista.append(lane)
                    self.dict_midi[midi1] = lista
                else:
                    #Ponemos la nota midi e indicamos el lane asociado
                    lista = []
                    lista.append(lane)
                    self.dict_midi[midi1] = lista
            #Ahora lo mismo para la segunda nota posible de este lane
            if midi2 > 0:
                if midi2 in self.dict_midi:
                    #Esta nota midi ya tiene un lane asociado
                    lista = self.dict_midi[midi2]
                    lista.append(lane)
                    self.dict_midi[midi2] = lista
                else:
                    #Ponemos la nota midi e indicamos el lane asociado
                    lista = []
                    lista.append(lane)
                    self.dict_midi[midi2] = lista

    def configurar_midi(self):
        """
            Según la configuracion guardada se crea el dicc MIDI que usaremos
            para comprobar si se pulsa un MIDI a que lane le corresponde
        """
        self.dict_midi = {}
        self.configurar_midi_lane('Lane_11', '11')
        self.configurar_midi_lane('Lane_12', '12')
        self.configurar_midi_lane('Lane_13', '13')
        self.configurar_midi_lane('Lane_14', '14')
        self.configurar_midi_lane('Lane_15', '15')
        self.configurar_midi_lane('Lane_16', '16')
        self.configurar_midi_lane('Lane_17', '17')
        self.configurar_midi_lane('Lane_18', '18')
        self.configurar_midi_lane('Lane_19', '19')
        self.configurar_midi_lane('Lane_1A', '1A')
        self.configurar_midi_lane('Lane_1B', '1B')
        self.configurar_midi_lane('Lane_1C', '1C')

    def borrar_datos_cancion(self):
        """
            Borramos todos los datos del reproductor
        """
        self.analizando_compas = None
        self.lista_compas = []
        self.dict_bmp = {}
        self.dict_wav = {}
        self.dict_lanes_auto = {}
        self.dict_lanes_visual = {}
        self.bmp = 0
        self.base_bmp = 0
        self.title = ""

    def leer_config_dtx(self):
        """
            Leemos el fichero de configuración del dtx
        """
        self.config_dtx = configparser.ConfigParser()
        self.config_dtx.read('config_dtx.ini')

    def leer_config_drum(self):
        """
            Leemos el fichero de configuración de las teclas y bateria-MIDI
        """
        self.config_drum = configparser.ConfigParser()
        self.config_drum.read('config_drum.ini')

    def crear_lane_visual(self, nombre_lane, lane, color, posicion):
        """
            Creamos un lane visual según datos que nos pasan
            Cuidado si esta en auto según conf también lo tenemos que insertar
            en el diccionario de lanes auto

            nombre_lane: Nombre en la configuración
            lane: Nombre del lane
            color: color que se asociara a lane y por tanto a sus chips
            posicion: posicion en pantalla
        """
        auto = self.config_drum[nombre_lane]['auto']
        lane_creada = LaneVisual(color, posicion, self.tiempo_pantalla)
        self.dict_lanes_visual[lane] = lane_creada
        if auto == 'true':
            self.dict_lanes_auto[lane] = lane_creada

    def reproducir_cancion(self, fichero, tiempo_pantalla):
        """
            Funcion que se llamara para iniciar el reproductor

            fichero: fichero .dtx a reproducir
            tiempo_pantalla: tiempo que tardara un chip en recorrer la pantalla
        """
        #Leemos la configuración ya que puede cambiar entre canciones
        self.leer_config_dtx()
        self.leer_config_drum()

        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.setBackgroundBrush(QtCore.Qt.black)
        #Quitamos 6 pixeles de margen de Qt
        self.scene.setSceneRect(QtCore.QRectF(0, 0, 1264, 714))
        self.setScene(self.scene)

        self.tiempo_pantalla = tiempo_pantalla

        # CANAL MIDI se ha de seleccionar dependiendo de config
        self.midi_in = rtmidi2.MidiIn()
        midi_port = int(self.config_drum['MIDI']['midi_port'])
        if midi_port < len(rtmidi2.get_in_ports()):
            #Puede estar desconectado al menos comprobar que cuadra números
            self.midi_in.open_port(midi_port)

        #Preparamos el teclado y el instrumento midi para
        self.configurar_teclado()
        self.configurar_midi()

        #Crear los lanes automaticos que siempre estaran
        lane_auto = LaneAuto()
        self.dict_lanes_auto['01'] = lane_auto
        lane_auto = LaneAuto()
        self.dict_lanes_auto['61'] = lane_auto
        lane_auto = LaneAuto()
        self.dict_lanes_auto['62'] = lane_auto

        #Analizar el fichero .dtx para tener todos los datos
        print ("-----Analizando dtx para reproduccion-----")

        #Crear lanes según configuración
        #pensar en el Hihat dos lanes misma columna y dos platillos derecha
        #      1A  11  1C  12 14 13 15 17 16
        #          18  1B                 19

        self.crear_lane_visual('Lane_1A', '1A', QtCore.Qt.darkRed, 10)
        self.crear_lane_visual('Lane_11', '11', QtCore.Qt.blue, 110)
        self.crear_lane_visual('Lane_18', '18', QtCore.Qt.white, 110)
        self.crear_lane_visual('Lane_1C', '1C', QtCore.Qt.gray, 210)
        self.crear_lane_visual('Lane_1B', '1B', QtCore.Qt.lightGray, 210)
        self.crear_lane_visual('Lane_12', '12', QtCore.Qt.yellow, 310)
        self.crear_lane_visual('Lane_14', '14', QtCore.Qt.green, 410)
        self.crear_lane_visual('Lane_13', '13', QtCore.Qt.gray, 510)
        self.crear_lane_visual('Lane_15', '15', QtCore.Qt.red, 610)
        self.crear_lane_visual('Lane_17', '17', QtCore.Qt.darkYellow, 710)
        self.crear_lane_visual('Lane_16', '16', QtCore.Qt.blue, 810)
        self.crear_lane_visual('Lane_19', '19', QtCore.Qt.darkBlue, 810)

        compas_actual = 0
        path = os.path.dirname(fichero)

        """
        Analizamos el .dtx para obtener la información inicial
        Información basica de la canción, titulos
        Informacion de bancos de sonidos
        Información de BPM
        Lista de compases y sus notas asociadas si tiene
        """
        fp = open(fichero, "r")
        while True:
            linea = fp.readline()
            if not linea:
                break
            #Limpiamos caracteres raros en la linea
            linea = linea.rstrip('\r\n\t')
            linea = linea.split(";")
            campos = linea[0].split()
            primer_espacio = linea[0].find(" ")
            orden = linea[0][:primer_espacio]
            if orden:
                if not(UtilidadesDTX.es_notacion(orden)):
                    if orden == "#TITLE:":
                        #TITLE
                        self.title = linea[0][primer_espacio + 1:]
                    elif orden == "#PANEL:":
                        #PANEL:
                        print("TODO orden", orden)
                    elif orden[0:4] == "#BPM":
                        if orden[4] == ":":
                            #BMP:
                            self.base_bmp = float(campos[1])
                            self.bmp = float(campos[1])
                        else:
                            #BMPzz:
                            canal = str(orden[4:6])
                            self.dict_bmp[canal] = float(campos[1])
                    elif orden[0:4] == "#WAV":
                        #WAVzz
                        canal = str(orden[4:6])
                        sonido = linea[0][primer_espacio + 1:]
                        posible_file = os.path.join(path, sonido)
                        posible_file = os.path.abspath(posible_file)
                        url = QtCore.QUrl.fromLocalFile(posible_file)
                        url = url.adjusted(QtCore.QUrl.EncodeSpaces)
                        string_url = url.toString()
                        if string_url.endswith('.ogg'):
                            #ogg
                            banco = QMediaPlayer()
                            media = QMediaContent(url)
                            banco.setMedia(media)
                        else:
                            #wav
                            banco = QSoundEffect()
                            banco.setSource(url)
                        self.dict_wav[canal] = banco
                    elif orden[0:7] == "#VOLUME":
                        #VOLUME:
                        canal = str(campos[0][7:9])
                        print ("TODO orden ", orden)
                    else:
                        print ("ORDEN .dtx no implementada :", orden)
                else:
                    #Es una notación de compas,lane, notas
                    compas = int(orden[1:-3])
                    lane = str(orden[4:-1])
                    while compas_actual <= compas:
                        if len(self.lista_compas) <= compas:
                            #Creamos las lanes para este compas
                            compas_vacio = {}
                            compas_vacio['lanes'] = {}
                            self.lista_compas.append(compas_vacio)
                        compas_actual = compas_actual + 1
                    if not(lane in self.lista_compas[compas]):
                        #Ponemos las notas en su compas y lane
                        campo = campos[1].replace('_', '')
                        campo = UtilidadesDTX.separar_strings_grupos_2(campo)
                        self.lista_compas[compas]['lanes'][lane] = campo
                    else:
                        print ("TODO cuidado doble linea para la misma lane")
        fp.close()

        #Creamos la puntuacion
        self.puntuacion = MyWidgetPuntuacion(self.tiempo_pantalla, self.title)
        self.puntuacion_scene = self.scene.addWidget(self.puntuacion)
        self.puntuacion_scene.setPos(900, 80)
        style = "QLabel {background-color: black; color: white;};"
        style = style + "Qwidget{background-color: black; color: white;}"
        self.puntuacion.setStyleSheet(style)

        #Ponemos los bancos de sonidos en los lanes
        for key in self.dict_lanes_auto:
            self.dict_lanes_auto[key].insertar_sonidos(self.dict_wav)
        for key in self.dict_lanes_visual:
            self.dict_lanes_visual[key].insertar_sonidos(self.dict_wav)

        #calculamos tiempo de compases en ms
        #Para ello recorremos toda la lista de compases y tendremos que ir
        #calculando el tiempo de ese compas, cuidado con los cambios de tiempo
        tiempo = 0.0
        for compas in self.lista_compas:
            compas['start'] = tiempo
            lanes = compas['lanes']
            if lanes.get('03'):
                #LANE 03 es un cambio de BMP pero usando sumas y restas
                #Cambio de bmp para el compas actual
                if len(lanes['03']) == 1:
                    self.bmp = self.base_bmp + int(lanes['03'][0], 16)
                    compas['bmp'] = self.bmp
                    tiempo_compas = (60.0 * 4.0 / self.bmp) * 1000
                    tiempo_final = tiempo + tiempo_compas
                else:
                    #Supongo que es un cambio para el compas siguiente
                    compas['bmp'] = self.bmp
                    tiempo_compas = (60.0 * 4.0 / self.bmp) * 1000
                    tiempo_final = tiempo + tiempo_compas
                    self.bmp = self.base_bmp + int(lanes['03'][0], 16)
            elif lanes.get('08'):
                #LANE 08 es un cambio de BMP pero usando BMP totales
                if len(lanes['08']) == 1:
                    #Cambio para el compas actual
                    self.bmp = self.dict_bmp[lanes['08'][0]]
                    compas['bmp'] = self.bmp
                    tiempo_compas = (60.0 * 4.0 / self.bmp) * 1000
                    tiempo_final = tiempo + tiempo_compas
                else:
                    #Supongo que es un cambio para el compas siguiente
                    compas['bmp'] = self.bmp
                    tiempo_compas = (60.0 * 4.0 / self.bmp) * 1000
                    tiempo_final = tiempo + tiempo_compas
                    self.bmp = self.dict_bmp[lanes['08'][-1]]
            else:
                #No hay cambio de bmp
                compas['bmp'] = self.bmp
                tiempo_compas = (60.0 * 4.0 / self.bmp) * 1000
                tiempo_final = tiempo + tiempo_compas
            tiempo = tiempo_final
            compas['tiempo'] = tiempo_compas

        #Ahora que tenemos el tiempo y cambios de bmp podemos poner el
        #tiempo en las notas y quitando las notas no existentes '00'
        for compas in self.lista_compas:
            tiempo = compas['tiempo']
            lanes = compas['lanes']
            if lanes:
                for lane in lanes:
                    notas_tiempo = []
                    num_notas = len(lanes[lane])
                    inc_tiempo = tiempo / num_notas
                    for i in range(0, num_notas):
                        #Creamos las notas con su tiempo asociado
                        nota = lanes[lane][i]
                        if nota != '00':
                            nota_tiempo = [None, None]
                            nota_tiempo[0] = nota
                            #Tiempo Absoluto
                            tiempo_nota = compas['start'] + (inc_tiempo * i)
                            nota_tiempo[1] = tiempo_nota
                            notas_tiempo.append(nota_tiempo)
                    lanes[lane] = notas_tiempo

        #Ya tenemos todos los compases con su tiempo
        self.tiempo_final = tiempo_final + self.tiempo_pantalla

        #Tiempo final preparamos para volver al menu
        self.timer_salida = QtCore.QTimer()
        self.timer_salida.setSingleShot(True)
        self.timer_salida.timeout.connect(self.salir)

        #Timer para bucle principal
        self.timer_bucle_cancion = QtCore.QTimer()
        self.timer_bucle_cancion.setSingleShot(True)
        self.timer_bucle_cancion.timeout.connect(self.animar_cancion)

        #Definimos la funcion del MIDI
        def midi_handler(message, time_stamp):
            """
                Se dispara cuando hay un evento MIDI

                message: el evento MIDI en si
                time_stamp: tiempo diferido hasta que se ha llamado esta función
            """
            if message[0] == 153:
            #Nota On
                if message[1] in self.dict_midi:
                    tiempo_actual = float(self.timer.elapsed())
                    if len(self.dict_midi[message[1]]) == 1:
                        #Solo hay que mirar un lane
                        #Mas optimizado miramos 1 vez y lo ponemos en hit
                        lane_selec = self.dict_midi[message[1]][0]
                        lane = self.dict_lanes_visual[lane_selec]
                        tiempo = lane.comprobar_y_poner_hit(tiempo_actual)
                        self.puntuacion.comprobar_puntuacion(tiempo)
                    else:
                        #Hay que mirar varios lanes
                        tiempo_menor = 10000
                        lista_lanes_menores = []
                        for lane_mirar in self.dict_midi[message[1]]:
                        #Miramos todos los lanes posibles sin poner a hit
                            lane = self.dict_lanes_visual[lane_mirar]
                            tiempo = lane.comprobar_tiempo(tiempo_actual)
                            if tiempo < tiempo_menor:
                                #Nuevo tiempo menor
                                tiempo_menor = tiempo
                                lista_lanes_menores.append(lane)
                            elif tiempo == tiempo_menor:
                                #Cuidado que podemos tener varios lanes
                                lista_lanes_menores.append(lane)
                        #Ponemos a hit
                        for lane in lista_lanes_menores:
                            tiempo = lane.comprobar_y_poner_hit(tiempo_actual)
                            self.puntuacion.comprobar_puntuacion(tiempo)

        #Juntamos el midi a la funcion de entrada
        self.midi_in.callback = midi_handler

        print ("Ya he analizado la canción")

        #Iniciamos el timer inicial para tener control del tiempo que llevamos
        self.timer = QtCore.QElapsedTimer()
        self.timer.start()
        #Iniciamos timer de bucle principal y el de la salida
        self.timer_salida.start(self.tiempo_final + 2 * self.tiempo_pantalla)
        self.timer_bucle_cancion.start(1)

        #Se anima el primer compas para despues ir al bucle principal
        self.analizando_compas = self.lista_compas[0]
        self.lista_compas.pop(0)

    def animar_cancion(self):
        """
            Hay que mirar, siempre depediendo del tiempo:
            insertar chips en su correspodiente lane
            si hay que pasar al siguiente compas
            reproducir sonidos en las lanes auto
            quitar chips de lane por mucho tiempo pasado

        """
        tiempo_actual = float(self.timer.elapsed())
        if self.analizando_compas:
            #Miramos si hay chips para animar
            self.animar_compas(self.analizando_compas, tiempo_actual)

            tiempo_siguiente_compas = self.analizando_compas['tiempo'] + \
                                      self.analizando_compas['start']
            if tiempo_actual >= tiempo_siguiente_compas:
                #pasamos a analizar el siguiente compas
                if self.lista_compas:
                    self.analizando_compas = self.lista_compas[0]
                    self.lista_compas.pop(0)

            #Mirar canales auto que suenen si tienen que sonar y quitamos notas
            for key in self.dict_lanes_auto:
                self.dict_lanes_auto[key].reproducir(tiempo_actual)

            #Borrar las notas antiguas de los lanes visuales
            for key in self.dict_lanes_visual:
                lane = self.dict_lanes_visual[key]
                estado = lane.eliminar_nota_antigua(tiempo_actual)
                if estado:
                    self.puntuacion.aumentar_miss()
        self.timer_bucle_cancion.start(0.1)

    def borrar_nota_analizada_lane(self, lane):
        """
            Quitamos del compas que se esta analizando la primera nota del lane

            lane: lane donde se quitara la primera nota
        """
        lista_compas = self.analizando_compas['lanes'][lane]
        lista_compas.pop(0)
        self.analizando_compas['lanes'][lane] = lista_compas

    def animar_chip(self, chip):
        """
            Tenemos que insertar el chip a la scene para que se pueda pintar

            chip: chip que se insertara en la scene
        """
        self.scene.addItem(chip)

    def animar_chip_lane(self, nota, lane):
        """
            Insertamos la nota en un lane visual y
            le sumamos el tiempo de pantalla al tiempo de la nota
            creamos el chip dependiendo del lane donde tiene que ir

            nota: nota que se tiene que insertar al lane
            lane: lane
        """
        tiempo_final_nota = nota[1] + self.tiempo_pantalla
        chip = Chip(nota[0], tiempo_final_nota)
        color = self.dict_lanes_visual[lane].leer_color()
        posicion = self.dict_lanes_visual[lane].leer_pos()
        chip.set_color(color)
        chip.animar(posicion, self.tiempo_pantalla)
        self.dict_lanes_visual[lane].insertar_chip(chip)
        self.animar_chip(chip)

    def animar_compas(self, compas_actual, tiempo_actual):
        """
            Comprobamos el compas_actual, y dependiendo del tiempo se ira
            animando los chips a sus lanes correspondientes

            compas_actual: compas actual
            tiempo_actual: tiempo actual
        """
        #Analizamos el compas y pasamos los chips a sus lanes correspondientes
        for lane in compas_actual['lanes']:
            if compas_actual['lanes'][lane]:
                #Existe lista de notas
                if compas_actual['lanes'][lane][0]:
                 #Hay una primera nota
                    nota = compas_actual['lanes'][lane][0]
                    tiempo_final_nota = nota[1] + self.tiempo_pantalla
                    #Lanes Auto
                    if lane == '01' or lane == '61' or lane == '62':
                        if tiempo_actual >= nota[1]:
                            chipAuto = ChipAuto(nota[0], tiempo_final_nota)
                            self.dict_lanes_auto[lane].insertar_chip(chipAuto)
                            self.borrar_nota_analizada_lane(lane)
                    #Lanes Visuales
                    elif lane == '11' or lane == '12' or lane == '13' or \
                         lane == '14' or lane == '15' or lane == '16' or \
                         lane == '17' or lane == '18' or lane == '19' or \
                         lane == '1A' or lane == '1B' or lane == '1C':
                        if tiempo_actual >= nota[1]:
                            self.animar_chip_lane(nota, lane)
                            self.borrar_nota_analizada_lane(lane)
                    else:
                        #Comprobamos que no sea lan de control de tiempo
                        #antes de warning
                        if lane != '03' and lane != '08':
                            print("LANE NO IMPLENTADO:", lane)

    def salir(self):
        """
            Volvemos al menu principal, para ello apuntamos en el stackedwidget
            al widget de navegación  y desactivamos el MIDI y la canción
        """
        self.borrar_datos_cancion()
        self.parentWidget().setCurrentIndex(1)
        self.parentWidget().update()
        self.parentWidget().repaint()
        self.midi_in = None