contador = 0
somador =0
while contador < 5:
    contador = contador + 1
    valor = float(input("type the" + str(contador)+"º value:"))
    somador = somador + valor
    input(print('soma = ', somador))