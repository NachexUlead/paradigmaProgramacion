import re

# Leer el contenido del archivo el_quijote.txt
with open("quijote.txt", "r", encoding="utf-8") as f:
    quijote_text = f.read()

# Dividir en líneas (útil para ubicar ocurrencias en caso de expansión)
lines = quijote_text.splitlines()

# Lista de resultados
results = []

# 1. Cabeceras de capítulo (ej. "CAPÍTULO I", "CAPITULO XXV")
regex1 = re.compile(r'CAP[IÍ]TULO\s+[IVXLCDM0-9]+', re.IGNORECASE)
matches1 = list(regex1.finditer(quijote_text))
results.append(f"1. Expresion: {regex1.pattern} | Resultados: {len(matches1)}")

# 2. Palabras antes y después de la 'y' para enumerar cosas (ej. 'espada y escudo')
regex2 = re.compile(r'\b(\w+)\s+y\s+(\w+)\b', re.IGNORECASE)
matches2 = list(regex2.finditer(quijote_text))
results.append(f"2. Expresion: {regex2.pattern} | Resultados: {len(matches2)}")

# 3. Sílabas pra-pre-pri-pro-pru seguidas de una letra d
regex3 = re.compile(r'\b(?:pra|pre|pri|pro|pru)d', re.IGNORECASE)
matches3 = list(regex3.finditer(quijote_text))
results.append(f"3. Expresion: {regex3.pattern} | Resultados: {len(matches3)}")

# 4. Palabras distintas que empiezan con cra-cre-cri-cro-cru
regex4 = re.compile(r'\b(cra|cre|cri|cro|cru)\w*', re.IGNORECASE)
matches4 = set(m.group(0).lower() for m in regex4.finditer(quijote_text))
results.append(f"4. Expresion: {regex4.pattern} | Resultados únicos: {len(matches4)}")

# 5. Palabras que terminan en cho-cha-che-chi-chu
regex5 = re.compile(r'\b\w*(cho|cha|che|chi|chu)\b', re.IGNORECASE)
matches5 = list(regex5.finditer(quijote_text))
results.append(f"5. Expresion: {regex5.pattern} | Resultados: {len(matches5)}")

# Guardar resultados
with open("busqueda-quijote.txt", "w", encoding="utf-8") as f:
    for r in results:
        f.write(r + "\n")

print("Analisis completado. Resultados guardados en 'busqueda-quijote.txt'")
