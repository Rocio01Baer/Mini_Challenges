def contar_vocales(cadena):
    # Convertir la cadena a minúsculas para considerar todas las vocales
    cadena = cadena.lower()
    
    # Inicializar un contador para las vocales
    contador = 0
    
    # Definir las vocales
    vocales = "aeiou"
    
    # Recorrer cada caracter en la cadena
    for caracter in cadena:
        # Verificar si el caracter es una vocal
        if caracter in vocales:
            contador += 1
    
    return contador

def main():
    # Pedir al usuario que ingrese una cadena
    cadena = input("Ingrese una cadena de texto: ")
    
    # Llamar a la función para contar vocales
    num_vocales = contar_vocales(cadena)
    
    # Mostrar el resultado
    print(f"El número de vocales en la cadena '{cadena}' es: {num_vocales}")

if __name__ == "__main__":
    main()
