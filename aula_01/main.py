#Sem parâmetros e sem retorno

def imprimirOla():

	print("Olá Pessoal")

	print("Bem-vindos ao novo semestre")



#Com parâmetros e com retorno

def getCalcularSalario( horas, valorHora):

	if horas == None or valorHora == None :

		return None

	else:

		salario = horas * valorHora

		return salario



#Com parâmetros e sem retorno

def imprimirSalario(horas, valorHora):

	salario = horas * valorHora	

	print( "Salário: ", salario)



#Com parâmetros e sem retorno

def imprimirSalario2(horas = 220, valorHora = 10):

	salario = getCalcularSalario( horas, valorHora)	

	print( "Salário: ", salario)



#Sem parâmetros e com retorno

def getValorPI():

	return 3.14



areaCirculo = getValorPI() * ( 2 * 2 )

print( "Área do círculo com raio 2: " , areaCirculo)



imprimirSalario2( )

imprimirSalario2( 150 )

imprimirSalario2( 100 , 20 )

imprimirSalario2( None , 15 )