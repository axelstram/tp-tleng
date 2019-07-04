import random

class Type(object):
	def __init__(self, t):
		self.type = t.lower()

	def evaluate(self):
		return self.type

class Array(object):
	def __init__(self, t):
		self.type = "array"
		
		if t.type == 'int':
			self.l = random.sample(range(1,100), random.sample(range(1,5),1)[0])
		elif t.type == 'float':
			self.l = [round(random.random(), 2) for i in range(random.sample(range(1,5),1)[0])]
		elif t.type == 'bool':
			self.l = [bool(random.getrandbits(1)) for i in range(random.sample(range(1,5),1)[0])]
		elif t.type == 'array':
			self.l = [t.l, t.l]
		elif t.type == 'struct':
			self.l = t.evaluate()
		else:
			self.l = ['carlos', 'saul', 'I']

	def evaluate(self):
		return '[' + ' '.join(str(e) for e in self.l) + ']'

class Var(object):
	def __init__(self, t):
		self.type = t.lower()

	def evaluate(self):
		return str(self.type)

class Tuple(object):

	def __init__(self, left, right):
		self.left = left
		self.right = right

	def evaluate(self):
		left_evaluation = self.left.evaluate()
		right_evaluation = self.right.evaluate()
		
		return str(left_evaluation) + ' ' + str(right_evaluation)

class Struct(object):
	def __init__(self, name, expression):
		self.name = name
		self.expression = expression

	def evaluate(self):
		return 'type ' + self.name.evaluate() + ' struct { ' + self.expression.evaluate() + ' }'