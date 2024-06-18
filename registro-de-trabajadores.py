def registrar_trabajador():
    print("\nRegistro de Trabajador")
    nombre=input("Nombre: ")
    apellido=input("Apellido: ")
    cargo=input("Cargo (CEO, Desarrollador, Analista de datos): ")
    while cargo not in cargo:
        print("Cargo no válido. Los cargos válidos son:", cargo)
        cargo = input("Cargo (CEO, Desarrollador, Analista de datos): ")
    sueldo_bruto = float(input("Sueldo Bruto: "))
    desc_salud = sueldo_bruto * 0.07
    desc_afp = sueldo_bruto * 0.12
    liquido_pagar = sueldo_bruto - desc_salud - desc_afp
#diccionario de plantilla de empleados
    empleado = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Cargo": cargo,
        "Sueldo Bruto": sueldo_bruto,
        "Desc. Salud": desc_salud,
        "Desc. AFP": desc_afp,
        "Líquido a pagar": liquido_pagar
    }