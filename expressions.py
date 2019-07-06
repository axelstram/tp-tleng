import random
import string 

def randomString(stringLength=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

class Type(object):
	def __init__(self, t):
		self.type = t.lower()
		self.dependencies = None

	def evaluate(self):
		if self.type == 'string':
			return '\"' +  randomString() + '\"'
		if self.type == 'int':
			return random.sample(range(1,100),1)[0]
		if self.type == 'float':
			return round(random.uniform(1,100), 2)
		if self.type == 'bool':
			return bool(random.getrandbits(1))
		else:
			if self.dependencies is not None:

				for struct in self.dependencies:
					if struct.getType().type == self.type:
		 			 	return struct.evaluate()

	def get(self):
		return self.type

	def setDependencies(self, all_other_structs):
		self.dependencies = all_other_structs

class Array(object):
	def __init__(self, t):
		self.type = "array"
		self.elementType = t
		self.dependencies = None

	def evaluate(self):
		self.elementType.setDependencies(self.dependencies)

		values = []
		size = random.sample(range(1,5),1)[0]
		for i in range(size):
			values.append(self.elementType.evaluate())

		# return str(values)
		return '[' + ', '.join(str(e) for e in values) + ']'

	def setDependencies(self, all_other_structs):
		self.dependencies = all_other_structs

class Var(object):
	def __init__(self, name):
		self.name = name.lower()

	def evaluate(self):
		return str(self.name)

class Tuple(object):
	def __init__(self, left, right):
		self.left = left
		self.right = right
		self.dependencies = None

	def evaluate(self):
		left_evaluation = self.left.evaluate()
		right_evaluation = self.right.evaluate()
		
		return str(left_evaluation) + ',\n' + str(right_evaluation)

	def setDependencies(self, all_other_structs):
		self.dependencies = all_other_structs
		self.left.setDependencies(self.dependencies)
		self.right.setDependencies(self.dependencies)

class VarAndType(object):
	def __init__(self, var, t):
		self.var = var
		self.type = t

	def evaluate(self):
		left_evaluation = self.var.evaluate()
		right_evaluation = self.type.evaluate()
		
		return "\"" + str(left_evaluation) + "\"" + ": " + str(right_evaluation)

	def setDependencies(self, all_other_structs):
		self.type.setDependencies(all_other_structs)

class Struct(object):
	def __init__(self, t, expression):
		self.type = t
		self.expression = expression

	def evaluate(self):
		return '{ ' + self.expression.evaluate() + ' }'

	def getType(self):
		return self.type

	def setDependencies(self, all_other_structs):
		self.expression.setDependencies(all_other_structs)

class EmbeddedStruct(object):
	def __init__(self, expression):
		self.type = "struct"
		self.expression = expression

	def evaluate(self):
		return '{ ' + self.expression.evaluate() + ' }'

	def setDependencies(self, all_other_structs):
		self.expression.setDependencies(all_other_structs)

class StructList(object):
	def __init__(self, left, right=None):
		self.left = left
		self.right = right

	def evaluate(self):
		#otro caso base
		if not self.right:
			return [self.left]
		elif type(self.right) == Struct:
			#caso base
			return [self.left, self.right]
		else:
			#MultiStructs
			l = self.right.evaluate()
			l.append(self.left)
			return l

	def get(self):
		return self.left_struct

class Main(object):
	def __init__(self, mainStruct, s):
		self.mainStruct = mainStruct
		self.all_structs = s

	def evaluate(self):
		if type(self.all_structs) is StructList:
			all_structs_list = self.all_structs.evaluate()

			for i in range(len(all_structs_list)):
				struct = all_structs_list[i]
				all_structs_except_current = all_structs_list[:i] + all_structs_list[i+1:]

				struct.setDependencies(all_structs_except_current)

			self.mainStruct.setDependencies(all_structs_list)

		return self.mainStruct.evaluate()