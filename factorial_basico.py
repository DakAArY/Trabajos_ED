def factorial_iterativo(n):
    if n < 0:
        raise ValueError("El factorial no esta definido para numeros negativcos")

    if n == 0 or n == 1:
        return 1

    resultado = 1
    for i in range(2, n + 1):
        resultado *= i

    return resultado

def main():
    print("Ingresa un numero para calcular su factorial")

    try:
        numero = int(input("Ingresa un numero entero: "))

        resultado = factorial_iterativo(numero)

        print(f"\nEl factorial de {numero} es: {resultado}")
        print(f"{numero}! = {resultado}")

    except ValueError as e:
        if "invalid literal" in str(e):
            print("Error: Por favor ingresa un numero entreo valido")
        else:
            print(f"Error: {e}")
    except ExceptionGroup as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
