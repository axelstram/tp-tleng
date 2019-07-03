class Type(object):
	def __init__(self, t):
		self.type = t.lower()

	def evaluate(self):
		return self.type

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