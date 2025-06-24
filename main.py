"""


from diccionario_alumno import mostrar_datos




while True:
    opcion = input("ESCUELA Nº 5032\n1.Datos de Alumnos\n2.Modificar datos de Alumnos\n3.Agregar Alumno\n4.Expulsar Alumno" \
                    "\n5.Salir\n-->: ")
    if opcion == '1':
        nombre = input("Ingrese Nombre del Alumno: ")
        resul = mostrar_datos(nombre)
        print(resul)
"""