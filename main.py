# Lista para almacenar la información de los empleados
empleados = []

# Lista de cargos predefinidos
cargos = ["CEO", "Desarrollador", "Analista de datos"]

def registrar_trabajador():
    print("\n=== Registro de Trabajador ===")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cargo = input("Cargo (CEO, Desarrollador, Analista de datos): ")
    
    # Validar que el cargo sea válido
    while cargo not in cargos:
        print("Cargo no válido. Los cargos válidos son:", cargos)
        cargo = input("Cargo (CEO, Desarrollador, Analista de datos): ")
    
    # Ingresar sueldo bruto
    sueldo_bruto = float(input("Sueldo Bruto: "))
    
    # Calcular descuentos y sueldo líquido
    desc_salud = sueldo_bruto * 0.07
    desc_afp = sueldo_bruto * 0.12
    liquido_pagar = sueldo_bruto - desc_salud - desc_afp
    
    # Crear diccionario del empleado
    empleado = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Cargo": cargo,
        "Sueldo Bruto": sueldo_bruto,
        "Desc. Salud": desc_salud,
        "Desc. AFP": desc_afp,
        "Líquido a pagar": liquido_pagar
    }
    # Agregar empleado a la lista
    empleados.append(empleado)
    print("Trabajador registrado exitosamente.\n")