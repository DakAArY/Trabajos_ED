def decimal_a_binario_recursivo(numero):
    if numero == 0:
        return '0'
    if numero == 1:
        return '1'
    
    return decimal_a_binario_recursivo(numero // 2) + str(numero % 2)

print(decimal_a_binario_recursivo(10))
    