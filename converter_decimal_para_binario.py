def decoradora(func):
    def decora(n):
        resultado = func(n)
        binario  = ''
        for num in resultado:
            binario += str(num)
        return int(binario)
    return decora

@decoradora
def converter_decimal_para_binario(num):
    total = num
    auxiliar = 0
    resto = 0
    resultado = []

    while total > 0:

        auxiliar = total
        total //= 2
        auxiliar %= 2 
        resultado.append(auxiliar)

    resultado.reverse()

    return resultado

print(converter_decimal_para_binario(167))