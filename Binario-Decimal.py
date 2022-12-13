numero_binario = '1001'

numero_decimal = 0 #aquí iremos sumando el resultado de cada multiplicación

for posicion, digito_string in enumerate(numero_binario[::-1]):
	numero_decimal += int(digito_string) * 2 ** posicion

print(f'El número decimal que buscamos es {numero_decimal}')
posicion = len(numero_binario) - 1 #posición del primer dígito por la izquierda

for digito_string in numero_binario:
	digito = int(digito_string)
	print(f'Dígito: {digito}, posición: {posicion}')
	posicion -= 1 # restamos 1 a la posición
     
