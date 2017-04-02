# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from PyQt5 import QtWidgets


class Chip(QtWidgets.QGraphicsWidget):
    """
        Clase chip gráfico, sera un chip, (nota y tiempo) y debera tener la
        información gráfica para Qt, animación y como pintarse
        también guardara si esta nota ya se ha pulsado en la bateria
    """

    def __init__(self, nota, tiempo):
        """
            Creamos los valores iniciales

            nota: banco asociado a la nota
            tiempo: tiempo de la nota
        """
        super(QtWidgets.QGraphicsWidget, self).__init__()
        self.tiempo = tiempo
        self.nota = nota
        self.animacion_nota = False
        self.color = False
        self.hit = False
        self.prop = False

    def paint(self, painter, option, widget):
        """
            Definimos como se ha de pintar una Chip grafico en qt
            Es un rectangulo de color(este color dependera de la lane)

            painter: Que painter usaremos lo ponemos por qt
            option: Opciones del painter esto lo tenemos poner por qt
            widget: Sobre que widget se pinta lo ponemos por qt
        """
        painter.fillRect(self.rect(), self.color)

    def leer_tiempo(self):
        """
            Devolvemos el valor del tiempo de la nota

            return: tiempo
        """
        return self.tiempo

    def leer_nota(self):
        """
            Devolvemos la nota (banco de sonido) asociado al chip

            return: nota
        """
        return self.nota

    def leer_hit(self):
        """
            Devolvemos el valor de si ha sido golpeado este chip

            return: hit
        """
        return self.hit

    def set_hit(self):
        """
            Indicamos que esta nota ya acaba de tocar
        """
        self.hit = True

    def set_color(self, color):
        """
            Definimos el color del chip, dependera de la lane

            color : color a asociar al chip
        """
        self.color = color

    def animar(self, posicion, tiempo):
        """
            Creamos la animación y la guardamos en el mismo chip
            La nota comienza arriba de la pantalla e ira hasta abajo

            posicion: posicion horizontal del chip para esta animacion
            tiempo: tiempo que tardara el chip en bajar
            return: devolvemos la animacion para que qt la pueda pintar
        """
        geometry = QtCore.QByteArray(b'geometry')
        self.prop = QtCore.QPropertyAnimation(self, geometry)
        self.prop.setDuration(tiempo)
        self.prop.setStartValue(QtCore.QRect(posicion, 0, 80, 10))
        self.prop.setEndValue(QtCore.QRect(posicion, 720, 80, 10))
        self.animacion_nota = QtCore.QParallelAnimationGroup()
        self.animacion_nota.addAnimation(self.prop)
        self.animacion_nota.start()
        return self.animacion_nota