#lista en blanco para agregar empleados y cargos.
empleados = []
cargos = ["CEO", "Desarrollador", "Analista de datos"] # Cargos
while cargo not in cargos:
        print("Cargo no válido. Los cargos válidos son:", cargos)
        cargo = input("Cargo (CEO, Desarrollador, Analista de datos): ")