# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets

from WidgetPuntuacion import Ui_WidgetPuntuacion


class MyWidgetPuntuacion(QtWidgets.QWidget):
    """
        Widget que se empleara para poner la puntuación mientras se reproduce
        la canción
    """

    def __init__(self, tiempo_pantalla, title):
        """
            Creamos los valores iniciales

            tiempo_pantalla: para calcular nivel de sincronización con las notas
            title: información del titulo que se pondra encima de la puntuación
        """
        super(MyWidgetPuntuacion, self).__init__()

        self.ui = Ui_WidgetPuntuacion()
        self.ui.setupUi(self)

        #Ponemos todos los valores a 0
        self.combo = 0
        self.num_notas = 0
        self.max_combo = 0
        self.perfect = 0
        self.great = 0
        self.good = 0
        self.poor = 0
        self.miss = 0

        #Ponemos el titulo
        self.ui.title_text_label.setText(title)

        #Calculamos los valores de sincronización de las notas
        self.tiempo_perfect = tiempo_pantalla / 15
        self.tiempo_great = tiempo_pantalla / 10
        self.tiempo_good = tiempo_pantalla / 5
        self.tiempo_poor = tiempo_pantalla / 2

        #Ponemos en los textLabels los valores iniciales
        self.ui.perfect_text_Label.setText(str(self.perfect))
        self.ui.perfect_per_Label.setText("%")
        self.ui.great_text_Label.setText(str(self.great))
        self.ui.great_per_Label.setText("%")
        self.ui.good_text_Label.setText(str(self.good))
        self.ui.good_per_Label.setText("%")
        self.ui.poor_text_Label.setText(str(self.poor))
        self.ui.poor_per_Label.setText("%")
        self.ui.miss_text_Label.setText(str(self.miss))
        self.ui.miss_per_Label.setText("%")
        self.ui.max_combo_text_Label.setText(str(self.max_combo))
        self.ui.max_combo_per_Label.setText("%")

    def comprobar_puntuacion(self, tiempo_puntuacion):
        """
            Actualizamos el num_de_notas y comparamos el tiempo_puntuación con
            la sincronización de la canción para puntuar y actualizar
            la puntuación visualmente en concordancia

            Mientras sea great o good se va aumentando el combo actual.

            tiempo_puntuacion: tiempo de diferencia con una nota
        """
        self.num_notas = self.num_notas + 1

        if tiempo_puntuacion <= self.tiempo_perfect:
            #Tiempo esta en perfect
            self.perfect = self.perfect + 1
            self.combo = self.combo + 1
            if self.combo > self.max_combo:
                self.max_combo = self.combo
        elif tiempo_puntuacion <= self.tiempo_great:
            #Tiempo esta en great
            self.great = self.great + 1
            self.combo = self.combo + 1
            if self.combo > self.max_combo:
                self.max_combo = self.combo
        elif tiempo_puntuacion <= self.tiempo_good:
            #Tiempo esta en great, pondremos combo a 0
            self.good = self.good + 1
            self.combo = 0
        elif tiempo_puntuacion <= self.tiempo_poor:
            #Tiempo esta en poor, pondremos combo a 0
            self.poor = self.poor + 1
            self.combo = 0
        else:
            #Es un miss, pondremos combo a 0
            self.miss = self.miss + 1
            self.combo = 0
        self.actualizar_puntuacion()

    def actualizar_puntuacion(self):
        """
            Actualizamos todos los textos del widget de puntuación
        """
        #Ponemos cuantas notas de cada llevamos actualmente
        self.ui.perfect_text_Label.setText(str(self.perfect))
        self.ui.great_text_Label.setText(str(self.great))
        self.ui.good_text_Label.setText(str(self.good))
        self.ui.poor_text_Label.setText(str(self.poor))
        self.ui.miss_text_Label.setText(str(self.miss))
        self.ui.max_combo_text_Label.setText(str(self.max_combo))

        #Preparamos los textos de los porcentajes
        perfect_float = round((self.perfect / self.num_notas) * 100, 2)
        perfect_per = str(perfect_float) + "%"
        great_float = round((self.great / self.num_notas) * 100, 2)
        great_per = str(great_float) + "%"
        good_float = round((self.good / self.num_notas) * 100, 2)
        good_per = str(good_float) + "%"
        poor_float = round((self.poor / self.num_notas) * 100, 2)
        poor_per = str(poor_float) + "%"
        miss_float = round((self.miss / self.num_notas) * 100, 2)
        miss_per = str(miss_float) + "%"
        max_combo_float = round((self.max_combo / self.num_notas) * 100, 2)
        max_combo_per = str(max_combo_float) + "%"

        #Ponemos los textos de los porcentajes
        self.ui.perfect_per_Label.setText(perfect_per)
        self.ui.great_per_Label.setText(great_per)
        self.ui.good_per_Label.setText(good_per)
        self.ui.poor_per_Label.setText(poor_per)
        self.ui.miss_per_Label.setText(miss_per)
        self.ui.max_combo_per_Label.setText(max_combo_per)

    def aumentar_miss(self):
        """
            Esta función normalmente se llamara ya que una nota no ha sido
            tocada, por lo que actualizamos puntuación y puntuación visual en
            concordancia
        """
        self.num_notas = self.num_notas + 1
        self.miss = self.miss + 1
        self.combo = 0
        self.actualizar_puntuacion()