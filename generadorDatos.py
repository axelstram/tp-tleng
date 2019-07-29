import random
import string

# aux

def randomString(stringLength=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# generadores
def generarString():
	return '\"' +  randomString() + '\"'

def generarInt():
	return random.sample(range(1,100),1)[0]

def generarFloat():
	return round(random.uniform(1,100), 2)

def generarBool():
	return bool(random.getrandbits(1))

def generarTipoBasico(tipo):
	valor = None
	if tipo == 'INT':
		valor = generarInt()
	elif tipo == 'STRING':
		valor = generarString()
	elif tipo == 'BOOL':
		valor = generarBool()
	elif tipo == 'FLOAT':
		valor = generarFloat()

	return valor

def generarArreglo(elem):
	dimensions = 0

	while elem['type']['is_array'] == True:
		elem = elem['type']
		dimensions += 1

	tipo = elem['type']
	size = random.randint(1,5)
	res = [generarTipoBasico(tipo) for i in range(size)]

	for _ in range(dimensions, 0, -1):
		size = random.randint(1,3)
		res = [res*size]

	return res

