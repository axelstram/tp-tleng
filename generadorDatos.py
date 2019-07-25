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