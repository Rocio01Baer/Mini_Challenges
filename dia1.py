def invertir_cadena(cadena):
    # Utilizamos slicing para invertir la cadena
    cadena_invertida = cadena[::-1]
    return cadena_invertida

# Función principal para ejecutar el programa
def main():
    # Solicitar al usuario que ingrese una cadena
    cadena = input("Ingrese una cadena de caracteres: ")
    
    # Llamar a la función para invertir la cadena
    cadena_invertida = invertir_cadena(cadena)
    
    # Mostrar la cadena invertida
    print("La cadena invertida es:", cadena_invertida)

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
