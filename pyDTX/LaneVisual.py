# -*- coding: utf-8 -*-

from LaneAuto import LaneAuto


class LaneVisual(LaneAuto):
    """
        Clase Lane Visual deriva del Lane Automatico,
        Tiene la información gráfica del Lane
        y también la la confifuración de los tiempos del reproductor
    """

    def __init__(self, color, posicion, tiempo_pantalla):
        """
            Creamos los valores iniciales
            Borramos el reproductor de sonidos .ogg que si que tienen los Auto

            color: color que se pondra en todas los chips de este lane
            posicion: posicion en la pantalla de este lane
            tiempo_pantalla: tiempo que tardara un chip en recorrer la pantalla
        """
        super(LaneVisual, self).__init__()

        self.color = color
        self.posicion = posicion
        self.tiempo_pantalla = tiempo_pantalla
        self.tiempo_poor = self.tiempo_pantalla / 2

    def leer_color(self):
        """
            Devolvemos el valor del color del lane

            return: color
        """
        return self.color

    def leer_pos(self):
        """
            Devolvemos el valor de la posicion del lane

            return: posicion
        """
        return self.posicion

    def comprobar_y_poner_hit(self, tiempo_actual):
        """
            Encontrar la nota más cercana al tiempo actual, ponerla a hit
            y devolver la diferencia de tiempo para poder puntuar
            si no existe nota más cercana devolvemos valor de 10000 ms

            tiempo_actual: tiempo actual para comparar con tiempo de notas

            return: diferencia de tiempo en la nota más cercana
        """
        tiempo_menor = 10000
        nota_mas_cercana = None

        for nota in self.lista_chips:
            if not(nota.leer_hit()):
                #Si hay nota sin pulsar comprobamos tiempo
                if abs(nota.leer_tiempo() - tiempo_actual) < tiempo_menor:
                    tiempo_menor = abs(nota.leer_tiempo() - tiempo_actual)
                    nota_mas_cercana = nota
        if nota_mas_cercana:
            nota_mas_cercana.set_hit()
        return tiempo_menor

    def comprobar_tiempo(self, tiempo_actual):
        """
            Encontrar la nota más cercana al tiempo actual
            y devolver la diferencia de tiempo para poder puntuar
            si no existe nota más cercana devolvemos valor de 10000 ms

            tiempo_actual: tiempo actual para comparar con tiempo de notas

            return: diferencia de tiempo en la nota más cercana
        """
        tiempo_menor = 10000
        for nota in self.lista_chips:
            if not(nota.leer_hit()):
                #Si hay nota sin pulsar comprobamos tiempo
                if abs(nota.leer_tiempo() - tiempo_actual) < tiempo_menor:
                    tiempo_menor = abs(nota.leer_tiempo() - tiempo_actual)
        return tiempo_menor

    def eliminar_nota_antigua(self, tiempo_actual):
        """
            Si la primera nota en la lista es igual o mayor al tiempo actual
            más el tiempo posible de una nota con la peor puntuacion
            se ha de elimar esa nota, tenemos que devolver true si eliminos
            nota que no se ha pulsado ya que sera un miss

            tiempo_actual: tiempo actual

            return true si ha eliminado nota sin hit, false de otra manera
        """
        if self.lista_chips:
            nota = self.lista_chips[0]
            tiempo_final = nota.leer_tiempo() + self.tiempo_poor
            if tiempo_actual >= tiempo_final:
                estado = nota.leer_hit()
                self.lista_chips.pop(0)
                return not(estado)
        return False