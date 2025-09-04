def factorial_recursivo(n):
    if n < 0:
        raise ValueError("El factorial no esta definido para numeros negativos")

    # Caso base
    if n == 0 or n == 1:
        return 1

    return n * factorial_recursivo(n - 1)

def main():
    print("Ingresa un numero para calcular su factorial")

    try:
        numero = int(input("Ingresa un numero entero: "))

        resultado = factorial_recursivo(numero)

        print(f"\nEl factorial de {numero} es: {resultado}")
        print(f"{numero}! = {resultado}")

    except ValueError as e:
        if "invalid literal" in str(e):
            print("Error: Por favor ingresa un numero entero valido")
        else:
            print(f"Error: {e}")
    except RecursionError:
        print("Error: El numero es demasiado grande para calcular recursivamente")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
