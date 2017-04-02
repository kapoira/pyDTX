# -*- coding: utf-8 -*-


class ChipAuto():
    """
        Clase, sera un chip, (nota y tiempo)
    """

    def __init__(self, nota, tiempo):
        """
            Creamos los valores iniciales

            nota: banco asociado a la nota
            tiempo: tiempo de la nota
        """
        self.tiempo = tiempo
        self.nota = nota

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