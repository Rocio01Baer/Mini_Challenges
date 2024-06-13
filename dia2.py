def tabla_de_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def main():
    # Pedir al usuario que ingrese un número
    numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
    
    # Llamar a la función para mostrar la tabla de multiplicar
    tabla_de_multiplicar(numero)

if __name__ == "__main__":
    main()
