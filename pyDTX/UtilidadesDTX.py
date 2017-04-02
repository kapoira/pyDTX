# -*- coding: utf-8 -*-

import os


def separar_strings_grupos_2(string):
    """
        Crear una lista separada en grupos de 2 caracteres para obtener
        normalmente las notas de un lane

        string: string original

        return: string separado en grupos de 2 caracteres
    """
    return [string[i:i + 2] for i in range(0, len(string), 2)]


def es_notacion(string):
    """
        Quitando al string que nos pasan
        el primer caracter y los tres ultimos sabremos
        si es una notacion de objetos para un compas sino sera una orden

        string: string original

        return: true si quitando primer y tres últimos caracteres es un integer
    """
    try:

        int(string[1:-3])
        return True
    except:
        return False


def buscar_subdirectorios(directorio):
    """
        Dado un directorio crearemos una lista con sus subdirectorios

        directorio: directorio donde comprobaremos sus subdirectorios

        return : lista de subdirectorios
    """
    lista_directorios = []
    for name in os.listdir(directorio):
        posible_file = os.path.join(directorio, name)
        if os.path.isdir(posible_file):
            lista_directorios.append(name)
    return lista_directorios


def buscar_info_directorio(directorio):
    """
        Buscara informacion de los posibles archivos .dtx/.def en un directorio
        Es la información que se empleara en los menus

        directorio: directorio donde buscaremos la información

        return: info del directorio, lista vacia si no hay info
    """
    posible_file = os.path.join(directorio, 'set.def')
    if os.path.exists(posible_file):
        return conseguir_info_set_def(posible_file)
    posible_file = os.path.join(directorio, 'SET.DEF')
    if os.path.exists(posible_file):
        return conseguir_info_set_def(posible_file)
    posible_file = os.path.join(directorio, 'box.def')
    if os.path.exists(posible_file):
        print("TODO Conseguir info box.def")
        return []
    posible_file = os.path.join(directorio, 'BOX.DEF')
    if os.path.exists(posible_file):
        print("TODO Conseguir info BOX.DEF")
        return []
    #Tendremos que buscar algún dtx al no existir ningún .def
    for name in os.listdir(directorio):
        posible_file = os.path.join(directorio, name)
        if name.endswith('.dtx') or name.endswith('.DTX'):
            return conseguir_info_dtx(posible_file)
    return []


def conseguir_info_set_def(archivo):
    """
        Analizamos el set.def y rellenamos una lista con 5 posibles items,
        cada uno con tres valores: label , file.dtx, información de ese .dtx

        archivo: archivo que analizaremos

        return: lista con la información de ese set.def
    """
    #Creamos la lista vacia, para añadir la información que encontremos
    lista_info = [[None, None, None],
                  [None, None, None],
                  [None, None, None],
                  [None, None, None],
                  [None, None, None]]

    fp = open(archivo, "r")
    while True:
        linea = fp.readline()
        if not linea:
            break
        #Limpiamos caracteres especiales de la linea
        linea = linea.rstrip('\r\n\t')
        linea = linea.split(";")

        #la posible orden es desde el inicio hasta el primer espacio
        primer_espacio = linea[0].find(" ")
        orden = linea[0][:primer_espacio]

        """Comprobamos si hay información tipo
        #LXLABEL:
        #LXFILE:
            """
        if orden:
            if orden == "#L1LABEL:":
                lista_info[0][0] = linea[0][primer_espacio + 1:]
            elif orden == "#L1FILE:":
                archivo_local = linea[0][primer_espacio + 1:]
                path = os.path.dirname(archivo)
                archivo_dtx = os.path.join(path, archivo_local)
                info_dtx = conseguir_info_dtx(archivo_dtx)
                lista_info[0][2] = info_dtx
                lista_info[0][1] = archivo_dtx
            elif orden == "#L2LABEL:":
                lista_info[1][0] = linea[0][primer_espacio + 1:]
            elif orden == "#L2FILE:":
                archivo_local = linea[0][primer_espacio + 1:]
                path = os.path.dirname(archivo)
                archivo_dtx = os.path.join(path, archivo_local)
                info_dtx = conseguir_info_dtx(archivo_dtx)
                lista_info[1][2] = info_dtx
                lista_info[1][1] = archivo_dtx
            elif orden == "#L3LABEL:":
                lista_info[2][0] = linea[0][primer_espacio + 1:]
            elif orden == "#L3FILE:":
                archivo_local = linea[0][primer_espacio + 1:]
                path = os.path.dirname(archivo)
                archivo_dtx = os.path.join(path, archivo_local)
                info_dtx = conseguir_info_dtx(archivo_dtx)
                lista_info[2][2] = info_dtx
                lista_info[2][1] = archivo_dtx
            elif orden == "#L4LABEL:":
                lista_info[3][0] = linea[0][primer_espacio + 1:]
            elif orden == "#L4FILE:":
                archivo_local = linea[0][primer_espacio + 1:]
                path = os.path.dirname(archivo)
                archivo_dtx = os.path.join(path, archivo_local)
                info_dtx = conseguir_info_dtx(archivo_dtx)
                lista_info[3][2] = info_dtx
                lista_info[3][1] = archivo_dtx
            elif orden == "#L5LABEL:":
                lista_info[4][0] = linea[0][primer_espacio + 1:]
            elif orden == "#L5FILE:":
                archivo_local = linea[0][primer_espacio + 1:]
                path = os.path.dirname(archivo)
                archivo_dtx = os.path.join(path, archivo_local)
                info_dtx = conseguir_info_dtx(archivo_dtx)
                lista_info[4][2] = info_dtx
                lista_info[4][1] = archivo_dtx
    fp.close()
    return lista_info


def conseguir_info_dtx(archivo):
    """
        Conseguir información de un .dtx, se devolvera una lista de 4 items
        imagen preview, titulo del .dtx, dificultad del .dtx, panel del .dtx

        archivo: archivo .dtx que analizaremos

        return: lista con la información del dtx
    """
    #Creamos la lista vacia
    lista_info = [None, None, None, None]
    fp = open(archivo, "r")
    while True:
        linea = fp.readline()
        if not linea:
            break
        #Limpiamos la linea de caracteres especiales
        linea = linea.rstrip('\r\n')
        linea = linea.split(";")

        #la posible orden es desde el inicio hasta el primer espacio
        primer_espacio = linea[0].find(" ")
        orden = linea[0][:primer_espacio]
        if orden:
            if orden == "#TITLE:":
                lista_info[1] = linea[0][primer_espacio + 1:]
            elif orden == "#DLEVEL:":
                lista_info[2] = linea[0][primer_espacio + 1:]
            elif orden == "#PREIMAGE:":
                archivo_local = linea[0][primer_espacio + 1:]
                path = os.path.dirname(archivo)
                archivo_imagen = os.path.join(path, archivo_local)
                lista_info[0] = archivo_imagen
            elif orden == "#PANEL:":
                lista_info[3] = linea[0][primer_espacio + 1:]
    fp.close()
    return lista_info
