
def mostrar_datos(cadena):
    for valor in Datos:
        if valor == cadena:
            return Datos[valor]



       
   
    

Datos = {  

    "Camila": {
        "Nombre" : "Camila",
        "Apellido" : "Fernandez",
        "DNI"   : 44333556,
        "Fecha-Nacimiento": "12/04/2017",
        "Tutor" : "Fransico Fernandez",
        "Notas" : {"Matematica": 8, "Lengua":7, "Artistica":10},
        "Faltas" : 2,
        "Amonestaciones" : "Ninguna"
    },
    
    "Manuel" : {
        "Nombre" : "Manuel",
        "Apellido" : "Molina",
        "DNI"   : 44994335,
        "Fecha-Nacimiento": "06/08/2017",
        "Tutor" : "Fransico Fernandez",
        "Notas" : {"Matematica": 6, "Lengua":8, "Artistica":8},
        "Faltas" : 3,
        "Amonestaciones" : "Ninguna",
    },

    "Luisana" : {
        "Nombre" : "Luisana",
        "Apellido" : "Sabedra",
        "DNI"   : 44322333,
        "Fecha-Nacimiento": "18/10/2017",
        "Tutor" : "Fransico Fernandez",
        "Notas" : {"Matematica": 10, "Lengua":5, "Artistica":7},
        "Faltas" : 6,
        "Amonestaciones" : "Ninguna",
    },



      }

while True:
    opcion = input("ESCUELA Nº 5032\n1.Datos de Alumnos\n2.Modificar datos de Alumnos\n3.Agregar Alumno\n4.Expulsar Alumno" \
                    "\n5.Salir\n-->: ")
    if opcion == '1':
        nombre = input("Ingrese Nombre del Alumno: ")
        resul = mostrar_datos(nombre)
        print(resul)
    elif opcion == '2':
        nombre = input("Ingrese Nombre del Alumno: ")
        editar = input("<Seleccione>\n1.Nombre\n2.Apellido\n3.DNI\n4.Fecha de Nacimiento\n5.tutor\n6.Notas\n7.Faltas" \
                        "\n8.Amonestaciones\n-->: ")
                       
                       
                       


        

    
            
        
   

