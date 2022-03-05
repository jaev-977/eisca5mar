def saludar(nombre):
	return "Hola %s" % nombre

def sumar(*args):
	res = 0
	for i in args:
		res += i
	return res

def mayor_edad(edad):
	return edad > 18

def devolver_variable(var):
	return var