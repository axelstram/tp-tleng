import random
import generadorDatos as gd

class Type(object):
	def __init__(self, t):
		self.type = t.lower()
		self.dependencies = None

	def evaluate(self):
		if self.type == 'string':
			return gd.generarString()
		if self.type == 'int':
			return gd.generarInt()
		if self.type == 'float':
			return gd.generarFloat()
		if self.type == 'bool':
			return gd.generarBool()
		else:
			if self.dependencies is not None:

				for struct in self.dependencies:
					if struct.getType().type == self.type:
		 			 	return struct.evaluate()

	def get(self):
		return self.type

	def setDependencies(self, all_other_structs):
		self.dependencies = all_other_structs

# class Array(object):
# 	def __init__(self, p):
# 		self.p = (1, p)

# 	def evaluate(self):
# 		return self.p
	# def evaluate(self):
	# 	self.elementType.setDependencies(self.dependencies)

	# 	values = []
	# 	size = random.sample(range(1,5),1)[0]
	# 	for i in range(size):
	# 		values.append(self.elementType.evaluate())

	# 	return '[' + ', '.join(str(e) for e in values) + ']'

# 	def setDependencies(self, all_other_structs):
# 		self.dependencies = all_other_structs

# class Var(object):
# 	def __init__(self, name):
# 		self.name = name.lower()

# 	def evaluate(self):
# 		return str(self.name)

# class Tuple(object):
# 	def __init__(self, left, right):
# 		self.left = left
# 		self.right = right
# 		self.dependencies = None

# 	def evaluate(self):
# 		left_evaluation = self.left.evaluate()
# 		right_evaluation = self.right.evaluate()
		
# 		return str(left_evaluation) + ',\n' + str(right_evaluation)

# 	def setDependencies(self, all_other_structs):
# 		self.dependencies = all_other_structs
# 		self.left.setDependencies(self.dependencies)
# 		self.right.setDependencies(self.dependencies)

# class VarAndType(object):
# 	def __init__(self, var, t):
# 		self.var = var
# 		self.type = t

# 	def evaluate(self):
# 		left_evaluation = self.var.evaluate()
# 		right_evaluation = self.type.evaluate()
		
# 		return "\"" + str(left_evaluation) + "\"" + ": " + str(right_evaluation)

# 	def setDependencies(self, all_other_structs):
# 		self.type.setDependencies(all_other_structs)

class Struct(object):
	def __init__(self, p):
		self.id = p[2]
		self.body = p[3]

	def evaluate(self):
		#return '{ ' + self.expression.evaluate() + ' }'
		d = {}
		d['id'] = self.id
		d['structBody'] = self.body
		return d
	# def getType(self):
	# 	return self.type

	# def setDependencies(self, all_other_structs):
	# 	self.expression.setDependencies(all_other_structs)

# class EmbeddedStruct(object):
# 	def __init__(self, expression):
# 		self.type = "struct"
# 		self.expression = expression

# 	def evaluate(self):
# 		return '{ ' + self.expression.evaluate() + ' }'

# 	def setDependencies(self, all_other_structs):
# 		self.expression.setDependencies(all_other_structs)

class StructList(object):
	def __init__(self, p):
		self.struct = p[1]
		self.rest = None

		if len(p) > 2:
			self.rest = p[2]

	def evaluate(self):
		if self.rest is not None:
			return [self.struct] + [self.rest]
		elif self.struct is not None:
			return [self.struct]
		# #otro caso base
		# if not self.right:
		# 	return [self.left]
		# elif type(self.right) == Struct:
		# 	#caso base
		# 	return [self.left, self.right]
		# else:
		# 	#MultiStructs
		# 	l = self.right.evaluate()
		# 	l.append(self.left)
		# 	return l

	# def get(self):
	# 	return self.left_struct

class Main(object):
	def __init__(self, p):
		self.p = p
		self.dependencies = {}

	def create_dependencies_graph(self):
		pass

	def has_circular_dependencies(self):
		return False

	def evaluate(self):
		self.create_dependencies_graph()

		if self.has_circular_dependencies():
			raise Exception('Hay dependencias circulares')

		return self.p[1]

	# def evaluate(self):
	# 	if type(self.all_structs) is StructList:
	# 		all_structs_list = self.all_structs.evaluate()

	# 		for i in range(len(all_structs_list)):
	# 			struct = all_structs_list[i]
	# 			all_structs_except_current = all_structs_list[:i] + all_structs_list[i+1:]

	# 			struct.setDependencies(all_structs_except_current)

	# 		self.mainStruct.setDependencies(all_structs_list)

	# 	return self.mainStruct.evaluate()