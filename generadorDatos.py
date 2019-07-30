import random
import string
import json
# aux

def randomString(stringLength=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# generadores
def generateString():
	return '\"' +  randomString() + '\"'

def generateInt():
	return random.sample(range(1,100),1)[0]

def generateFloat():
	return round(random.uniform(1,100), 2)

def generateBool():
	return bool(random.getrandbits(1))

def generateBasicType(tipo):
	value = None
	if tipo == 'INT':
		value = generateInt()
	elif tipo == 'STRING':
		value = generateString()
	elif tipo == 'BOOL':
		value = generateBool()
	elif tipo == 'FLOAT':
		value = generateFloat()
	else:
		raise Exception("ERROR, {} NO ES UN TIPO BASICO".format(tipo))

	return value

def generateArray(elem, definitions):
	dimensions = 0

	while isArray(elem):
		elem = elem['type']
		dimensions += 1

	size = random.randint(1,5)
	res = [generateValue(elem, definitions) for i in range(size)]

	for _ in range(dimensions-1, 0, -1):
		size = random.randint(1,3)
		res = [res*size]

	return res

def isArray(elem):
	return elem['type']['is_array']

def isStruct(elem):
	return type(elem['type']['type']) == list

def isBasicType(elem):
	return (elem['type']['type'] in ['INT', 'STRING', 'BOOL', 'FLOAT'])

def generateValue(elem, definitions):
	value = None

	if isArray(elem):
		value = generateArray(elem, definitions)
	elif isStruct(elem):
		value = generateStruct(elem['type']['type'], definitions)
	elif isBasicType(elem):
		value = generateBasicType(elem['type']['type'])
	else: 
		#es un nuevo tipo de datos (i.e. struct)
		value = generateStruct(definitions[elem['type']['type']], definitions)

	return value

def generateStruct(camposDelStruct, definitions):
	structAsDict = {}

	for elem in camposDelStruct:
		structAsDict[elem['id']] = generateValue(elem, definitions)

	return structAsDict

def generate_json(structs):
	definitions = dict([(s['id'], s['structBody']) for s in structs])
	mainStructAsDict = generateStruct(structs[0]['structBody'], definitions)

	return mainStructAsDict

