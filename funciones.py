import csv #este import es para importar el archivo para del lenguaje normal a un archivo .csv 
trabajadores=[]#lista donde se agregara a los trabajadores.
#se añade los datos de los trabajadores  para verse reflejado en las planillas.
def CrearTrabajador():
    print("Ingresar Nombre del Trabajador");
    nombre=input()

    print("Ingresar el apellido del trabajador");
    apellido=input()

    print("Ingrese el cargo");
    cargo=input()

    print("Ingrese el sueldo Bruto");
    sueldoBruto=float(input())
    descSalud = sueldoBruto * 0.07-sueldoBruto#calculos de descuento de fonasa y afp en este caso modelo
    descAFP = sueldoBruto * 0.1-sueldoBruto
    sueldoLiquido = sueldoBruto - descSalud - descAFP
   #diccionario de datos del trabajador.
    trabajador = {
        'nombre': nombre,
        'apellido': apellido,
        'cargo': cargo,
        'sueldoBruto': sueldoBruto,
        'descSalud': descSalud,
        'descAFP': descAFP,
        'sueldoLiquido': sueldoLiquido
        }
    trabajadores.append(trabajador)#este .append se utiliza para agregar al diccionario los datos en la variable trabajador.
        #esta parte se hizo con chat gpt ya que alvaro lo hizo claramente con este programa y no entendi su definicion en la lista de trabajadores.
def ListaTrabajadores():#se modifica porque el compañero lo copio directamente de chat gpt sin modificar nada.
    print("\n****Lista de Trabajadores ****")
    for trabajador in trabajadores:
        for key, value in trabajador.items():
            print(f"{key}: {value}")
        print("")
#plantilla de datos por agregar al usuario , todo esto se importara en un archivo .csv , donde se puede ver en un excel .
def ImprimirPlanilla():
    print("\n****Imprimir Planilla de Sueldos****")
    seleccion = input("Selecciona un cargo para imprimir (CEO, Desarrollador, Analista de datos), o 'todos' para todos: ")
    
    if seleccion == 'todos':
        trabajadores_filtrados = trabajadores
        nombre_archivo = "planilla_todos.csv"
    elif seleccion in cargos:
        trabajadores_filtrados = [trab for trab in trabajadores if trab["cargo"] == seleccion]
        nombre_archivo = f"planilla_{seleccion.lower()}.csv"
    else:
        print("Cargo no válido.\n")
        return

    # se escribe datos en el archivo .csv
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:#el encoding se utilizo para los manejos de comas y se paso el otro dia en clases cuando rodrigo dio la solucion.
        writer = csv.DictWriter(archivo, fieldnames=["nombre", "apellido", "cargo", "sueldoBruto", "descSalud", "descAFP", "sueldoLiquido"])
        writer.writeheader()
        for trab in trabajadores_filtrados:
            writer.writerow(trab)
    
    print(f"Archivo '{nombre_archivo}' guardado correctamente\n")
#inicio de menu 
def main():
    while True:
        print("=== Menú ===")
        print("1. Registrar trabajador")
        print("2. Listar todos los trabajadores")
        print("3. Imprimir planilla de sueldos")
        print("4. Salir del programa")
        
        opcion = input("Elige una opción: ")
        
        if opcion == 1:
            CrearTrabajador()
        elif opcion == 2:
            ListarTrabajadores()
        elif opcion == 3:
            ImprimirPlanilla()
        elif opcion == 4:
            print("Chaolin flojin, programa cerrao.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.\n")

if __name__ == "__main__":#esto no me salio y preferi preguntarle a mis compañeros
    main()
    #esto ultimo lo hice con ayuda del chat gpt(el name==)
