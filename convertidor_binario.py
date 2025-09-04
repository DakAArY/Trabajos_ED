def decimal_a_binario(numero):
    if numero == 0:
        return '0'
    
    binario = ''
    while numero > 0:
        binario = str(numero % 2) + binario
        numero //= 2
    return binario

print(decimal_a_binario(10))