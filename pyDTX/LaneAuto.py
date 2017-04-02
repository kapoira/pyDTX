# -*- coding: utf-8 -*-


class LaneAuto():
    """
        Clase Lane Automatico, sera un lane, una lista de chips
        Tiene asociado un reproductor de sonidos rapidos .wav
        y otro de sonidos lentos .ogg
        También tenemos el banco de sonidos de la canción
    """

    def __init__(self):
        """
            Creamos los valores iniciales
        """
        self.lista_chips = []
        self.banco_sonidos = {}

    def insertar_chip(self, chip):
        """
            Insertamos un chip al final de la lista

            chip: chip a insertar
        """
        self.lista_chips.append(chip)

    def insertar_sonidos(self, banco_sonidos):
        """
            Definimos el banco de sonidos

            banco_sonidos:  Banco de sonidos de la canción
        """
        self.banco_sonidos = banco_sonidos

    def reproducir(self, tiempo_actual):
        """
            Se buscara el primer chip  y si justo estamos cuando ha de sonar
            reproduciremos su sonido y lo quitamos

            tiempo_actual: tiempo actual
        """
        #Comprobar que existe el primer chip
        if self.lista_chips:
            nota = self.lista_chips[0]
            if nota.leer_tiempo() <= tiempo_actual:
                #Tenemos que reproducir su sonido asociado
                self.banco_sonidos[nota.leer_nota()].play()
                self.lista_chips.pop(0)