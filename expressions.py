class Type(object):
	def __init__(self, t):
		self.type = t

	def evaluate(self):
		return self.type

class Tuple(object):

	def __init__(self, left, right):
		self.left = left
		self.right = right

	def evaluate(self):
		left_evaluation = self.left
		right_evaluation = self.right
		
		return str(left_evaluation) + ' ' + str(right_evaluation)

class Struct(object):
	def __init__(self, name, expression):
		self.name = name
		self.expression = expression

	def evaluate(self):
		return 'type ' + self.name + ' struct { ' + self.expression.evaluate() + ' }'