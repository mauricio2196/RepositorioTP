
def mostrar_datos(dni):
    doc=str(dni)
    if doc in Datos:
        print(Datos[doc])
   
    

def modificar_datos(dni,indice,valor,i=None):
    from datetime import datetime

    doc=str(dni)
    claves = ["Nombre","Apellido","DNI","Fecha-Nacimiento","Tutor","Notas","Faltas","Amonestaciones"]
    materias = ["Matematica","Lengua","Artistica"]
   
    if doc in Datos:
        indice-= 1
        clave = claves[indice]
        if clave == "Notas":
            i-=1
            if i is not None:
                nota = materias[i]
                Datos[doc]["Notas"][nota] = valor
                print(f"{nota}:{valor}")     
        elif clave == "DNI":
            doc_nuevo = str(valor)
            Datos[doc_nuevo] = Datos[doc]
            Datos[doc_nuevo]["DNI"] = int(valor)
            del Datos[doc]
            print(f"{clave}:{valor}")
        elif clave == "Fecha-Nacimiento":
            datetime.strptime(valor,"%d-%m-%Y")
            Datos[doc][clave] = valor
            print(f"{clave}:{valor}")
        else:
            Datos[doc][clave] = valor
            print(f"{clave}:{valor}") 

     

       


Datos = {
  
    "4433556":{
        "Nombre" : "Camila",
        "Apellido" : "Fernandez",
        "DNI"   : 44333556,
        "Fecha-Nacimiento": "12/04/2017",
        "Tutor" : "Fransico Fernandez",
        "Notas" : {"Matematica": 8, "Lengua":7, "Artistica":10},
        "Faltas" : 2,
        "Amonestaciones" : "Ninguna"
    },
   
   
   "44994335" : {
        "Nombre" : "Manuel",
        "Apellido" : "Molina",
        "DNI"   : 44994335,
        "Fecha-Nacimiento": "06/08/2017",
        "Tutor" : "Maximo Molina",
        "Notas" : {"Matematica": 6, "Lengua":8, "Artistica":8},
        "Faltas" : 3,
        "Amonestaciones" : "Ninguna",
    },

    "44322333" : {
        "Nombre" : "Luisana",
        "Apellido" : "Sabedra",
        "DNI"   : 44322333,
        "Fecha-Nacimiento": "18/10/2017",
        "Tutor" : "Silvio Sabedra",
        "Notas" : {"Matematica": 10, "Lengua":5, "Artistica":7},
        "Faltas" : 6,
        "Amonestaciones" : "Ninguna",
    },

    }


 



while True:
    opcion = input("ESCUELA Nº 5032\n1.Datos de Alumnos\n2.Modificar datos de Alumnos\n3.Agregar Alumno\n4.Expulsar Alumno" \
                    "\n5.Salir\n-->: ")
    if opcion == '1':
        dni = input("Ingrese DNI: ")
        mostrar_datos(dni)
    elif opcion == '2':
        dni = input("Ingrese DNI: ")
        mod = int(input("<Seleccione a Modificar>\n1.Nombre\n2.Apellido\n3.DNI\n4.Fecha-Nacimiento\n5.tutor\n6.Notas\n7.Faltas" \
                        "\n8.Amonestaciones\n-->: "))
        if mod == 6:
            materia = int(input("<Seleccione>\n1.Matematica\n2.Lengua\n3.Artistica"))
            editar = input("Ingrese la Nota: ")
            modificar_datos(dni,mod,editar,materia)
        else:
            editar = input("Ingrese lo Nuevo: ")
            modificar_datos(dni,mod,editar)
        
        
       

                       
                       
                       


        

    
            
        
   

