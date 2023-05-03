import names
from faker import Faker

# Generar 6500 nombres y apellidos
full_names = []
for i in range(6500):
    full_name = names.get_full_name()
    full_names.append(full_name)

    # Generar un nombre y apellido aleatorio adicional con faker
    full_name = Faker().name()
    full_names.append(full_name)

# Escribir los nombres y apellidos en un archivo de texto
with open('nombres_apellidos.txt', 'w') as f:
    for name in full_names:
        f.write(name + '\n')