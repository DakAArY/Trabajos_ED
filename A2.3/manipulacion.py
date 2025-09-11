def mostrar_arreglo(arreglo):
    elementos = " , ".join(str(x) for x in arreglo)
    print(f"Elementos: << {elementos} >>")

def buscar_recursivo(arreglo, numero, indice=0):
    #caso base: si se llega al final del arreglo
    if indice >= len(arreglo):
        return -1

    #caso base: si se encuentra el numero
    if arreglo[indice] == numero:
        return indice

    #caso recursivo
    return buscar_recursivo(arreglo, numero, indice + 1)

def main():
    arreglo = None

    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1.- Inicializar arreglo de datos")
        print("2.- Ingresar un número")
        print("3.- Eliminar un número")
        print("4.- Buscar un elemento")
        print("5.- Salir")

        try:
            opcion = int(input("seleccione una opcion: "))
        except ValueError:
            print("Error: Ingrese unja seleccion valida.")
            continue

        if opcion == 1:
            try:
                tamaño = int(input("ingrese el tamaño del arreglo: "))
                if tamaño <= 0:
                    print("el tamaño debe ser un numero positivo.")
                    continue
                arreglo = [0] * tamaño
                mostrar_arreglo(arreglo)
                print("Arreglo inicializado correctamente.")
            except ValueError:
                print("Error: Ingrese un numero valido.")


        elif opcion == 2:
            if arreglo is None:
                print("Primero debe inicializar el arreglo (opción 1).")
                continue

            try:
                numero = int(input("Ingrese un numero (no cero): "))
                if numero == 0:
                    print("No se permite ingresar el numero cero.")
                    continue


                posicion = buscar_recursivo(arreglo, numero)
                if posicion != -1:
                    print(f"El numero {numero} ya existe en la posicion {posicion}.")
                    continue


                posicion_disponible = buscar_recursivo(arreglo, 0)
                if posicion_disponible == -1:
                    print("El arreglo está lleno. No se pueden ingresar mas elementos.")
                    continue

                arreglo[posicion_disponible] = numero
                print(f"Numero {numero} ingresado en la posicion {posicion_disponible}.")
                mostrar_arreglo(arreglo)
            except ValueError:
                print("Por favor, ingrese un numero valido.")


        elif opcion == 3:
            if arreglo is None:
                print("Primero debe inicializar el arreglo (opcion 1).")
                continue

            mostrar_arreglo(arreglo)
            try:
                numero = int(input("Ingrese el numero que desea eliminar: "))
                posicion = buscar_recursivo(arreglo, numero)

                if posicion == -1:
                    print(f"El numero {numero} no existe en el arreglo.")
                    continue

                arreglo[posicion] = 0
                print(f"Numero {numero} eliminado correctamente.")
                mostrar_arreglo(arreglo)
            except ValueError:
                print("ingrese un numero valido.")


        elif opcion == 4:
            if arreglo is None:
                print("primero debe inicializar el arreglo (opcion 1).")
                continue

            try:
                numero = int(input("Ingrese el numero que desea buscar: "))
                posicion = buscar_recursivo(arreglo, numero)

                if posicion == -1:
                    print(f"El numero {numero} no existe en el arreglo.")
                else:
                    print(f"El numero {numero} se encuentra en la posición {posicion}.")
            except ValueError:
                print("ingrese un número válido.")


        elif opcion == 5:
            print("Saliendo del programa. Adios")
            break

        else:
            print("Opcion no valida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
