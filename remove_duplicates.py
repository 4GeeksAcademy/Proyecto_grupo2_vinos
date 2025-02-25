def remove_duplicates(file_path):
    # Leer el contenido del archivo
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Eliminar duplicados usando un conjunto
    unique_lines = set(lines)

    # Contar duplicados
    duplicates_count = len(lines) - len(unique_lines)

    # Guardar el nuevo archivo sin duplicados sobre el mismo archivo
    with open(file_path, 'w') as file:
        file.writelines(unique_lines)

    # Mostrar resultados
    print(f"Total de duplicados eliminados: {duplicates_count}")
    print(f"Total de registros únicos restantes: {len(unique_lines)}")
    print(f"Archivo actualizado: {file_path}")

# Ejemplo de uso
file_path = '\Datos preparados\def_espumoso_1.txt'  # Cambia esto por el nombre de tu archivo
remove_duplicates(file_path)