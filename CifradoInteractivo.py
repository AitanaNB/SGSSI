cadena = input("Introduce el texto cifrado:\n")

#contar frecuenciade letras
letras=dict()

for letra in cadena:
        if letra.isalpha(): #ignorar los caracteres que no son letras
            letras[letra] = letras.get(letra,0) +1

#ordenar letras por frecuencia
print("Frecuencia de letras:")
letrasOrdenadas= sorted(letras, key=letras.get, reverse=True)
print(letrasOrdenadas)
print("\n")

# Lista de letras más frecuentes en español
frecs= ['E', 'A', 'O', 'S', 'N', 'R', 'I', 'L', 'D', 'C', 'T', 'U', 'M', 'P', 'B', 'G', 'V', 'Y', 'Q', 'H', 'F', 'Z', 'J', 'Ñ', 'X', 'K', 'W']

print("Caracteres más comunes:")
print(frecs)
print("\n")

#Crear sustitucion inicial por frecuencia OP 2
def sustOriginal():
    sustituciones={}
    for i,letra in enumerate(letrasOrdenadas):
        if i<len(frecs):
            sustituciones[letra] = frecs[i]
        else:
            sustituciones[letra]=letra
    return sustituciones
    
#Inicio sin sustituciones
sustituciones={}

# Aplicar sustituciones
def aplicarSustituciones(texto, sustituciones):
    resultado = ""
    for c in texto:
        if c in sustituciones:
            resultado += sustituciones[c]
        else:
            resultado += c
    return resultado
    
#BUCLE interactivo
while True:
    print("\nTEXTO DESCIFRADO:\n")
    print(aplicarSustituciones(cadena, sustituciones))
    
    print("\nSUSTITUCIONES ACTUALES:")
    if sustituciones:
        for clave in sorted(sustituciones):
            print(f"{clave} → {sustituciones[clave]}", end=' | ')
        print("\nCaracteres más comunes GENERAL:")
        print(frecs)
        print("\n")
        
        print("\nCaracteres en ESTE texto:")
        print(letrasOrdenadas)
        print("\n")
    else:
        print("(sin sustituciones, texto original)")
        
    print("\n\nOpciones:")
    print(" - Escribe A=W para cambiar sustitución")
    print(" - Pulsa 1 para volver al texto original")
    print(" - Pulsa 2 para aplicar sustitución por frecuencia")
    print(" - ENTER dos veces para salir")
    
    entrada = input("> ").strip().upper()
    
    if entrada == "":
        confirmar = input("¿Deseas salir? Pulsa ENTER de nuevo para salir o cualquier tecla para seguir:\n> ").strip()
        if confirmar == "":
            break
        else:
            continue
    elif entrada == "1":
        sustituciones = {}
        print("Texto original restaurado.")
    elif entrada == "2":
        sustituciones = sustOriginal()
        print("Sustitución por frecuencia aplicada.")
    elif len(entrada) == 3 and entrada[1] == '=':
        letra_origen = entrada[0]
        letra_destino = entrada[2]
        if letra_origen.isalpha() and letra_destino.isalpha():
            sustituciones[letra_origen] = letra_destino
        else:
            print("\nLetras, por favor. O exploto.")
    else:
        print("\nUna opción válida, por favor. O exploto.")
    
