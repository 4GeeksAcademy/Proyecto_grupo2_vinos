import os

# Nombre del archivo de entrada
nombre_archivo = 'espumoso+100.txt' #Aqui ponéis el nombre del archivo de txt

# Abrir el archivo de texto y leer los enlaces
with open(nombre_archivo, 'r') as file:
    enlaces = file.readlines()

# Limpiar los enlaces y formatearlos con una coma al final
enlaces_formateados = [f'"{enlace.strip()}",' for enlace in enlaces]

# Unir los enlaces formateados con saltos de línea
resultado = '\n'.join(enlaces_formateados)

# Crear el nombre del archivo de salida
nombre_archivo_salida = f'format_{os.path.basename(nombre_archivo)}'

# Guardar el resultado en el nuevo archivo
with open(nombre_archivo_salida, 'w') as file:
    file.write(resultado)

print(f'Los enlaces formateados se han guardado en: {nombre_archivo_salida}')