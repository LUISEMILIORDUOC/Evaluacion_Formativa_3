trabajadores=[]

def CrearTrabajador():
    print("Ingresar Nombre del Trabajador");
    nombre=input()

    print("Ingresar el apellido del trabajador");
    apellido=input()

    print("Ingrese el cargo");
    cargo=input()

    print("Ingrese el sueldo Bruto");
    sueldoBruto=int(input())
    descSalud = sueldoBruto * (7 / sueldoBruto)
    descAFP = sueldoBruto * (10 / sueldoBruto)
    sueldoLiquido = sueldoBruto - descSalud - descAFP
    trabajador = {
        'nombre': nombre,
        'apellido': apellido,
        'sueldoBruto': sueldoBruto,
        'descSalud': descSalud,
        'descAFP': descAFP,
        'sueldoLiquido': sueldoLiquido
        }
    trabajadores.append(trabajador)
        
def ListarTrabajadores(): 
    for trabajador in trabajadores:
        for key, value in trabajador.items():
            print(f"{key}: {value}")
        
CrearTrabajador()
ListarTrabajadores()