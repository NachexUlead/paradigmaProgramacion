import re

# Leer el contenido del archivo
with open("Pi125MDP.txt", "r") as file:
    pi_data = file.read()

# Diccionario con los patrones y descripciones
searches = {
    1: (r'1415', "todas las ocurrencias de la secuencia 1415"),
    2: (r'1415[13579]', "1415 seguido de un digito impar"),
    3: (r'[02468]{3}', "3 digitos pares seguidos"),
    4: (r'[02468]{3}9', "3 digitos pares seguidos de un 9"),
    5: (r'[02468]{3}[13579]', "3 digitos pares seguidos de un digito impar"),
    6: (r'[02468]{3}[09]', "3 digitos pares seguidos de un 0 o 9"),
    7: (r'[02468]{2}([13579]{1,3})?', "2 pares seguidos con 1 a 3 impares opcionales"),
    8: (r'[13579]{2}0', "2 impares seguidos de un 0"),
    9: (r'[13579][02468]{2,}', "1 impar seguido de al menos 2 pares"),
    10: (r'11[13579]', "111,113,115,117 o 119"),
    11: (r'11[13579][02468]', "111,113,115,117 o 119 seguidos de un par"),
}

# Guardar resultados en un archivo
with open("busqueda-pi.txt", "w") as out_file:
    for num, (pattern, description) in searches.items():
        matches = re.findall(pattern, pi_data)
        out_file.write(f"{num}. Expresion: {pattern} | Resultados: {len(matches)} - {description}\n")

print("Analisis completado. Resultados guardados en 'busqueda-pi.txt'")
