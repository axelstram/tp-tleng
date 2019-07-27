import random
import generadorDatos as gd
import lexer_rules

class Struct(object):
	def __init__(self, p):
		self.id = p[2]
		self.body = p[3]

	def evaluate(self):
		d = {}
		d['id'] = self.id
		d['structBody'] = self.body
		return d

class StructList(object):
	def __init__(self, p):
		self.struct = p[1]
		self.rest = None

		if len(p) > 2:
			self.rest = p[2]

	def evaluate(self):
		if self.rest is not None:
			#print('self.struct' + str(type(self.struct)))
			#print('self.struct' + str(type(self.struct)))
			return [self.struct] + self.rest
		elif self.struct is not None:
			return [self.struct]

class Main(object):
	def __init__(self, p):
		self.p = p
		self.dependencies = {}

	def create_dependencies_graph(self):
		for struct in self.p[1]:
			print('struct: ' + str(struct))

			basicTypes = ['STRING', 'INT', 'FLOAT', 'BOOL']
			elements = struct['structBody']
			dependencies = []
			for elem in elements:
				#cada elem es una tupla (id, dict con el type)
				elemType = self.getElemType(elem[1])
				if elemType not in basicTypes:
					# print('elemtype: ' + str(elemType))
					dependencies.append(elemType)

			self.dependencies[struct['id']] = dependencies

		print('dependencies: ' + str(self.dependencies))

	def getElemType(self, elem):
		#si es un arreglo o arreglo de arreglos, va iterando hasta el final
		#para encontrar el tipo
		while elem['is_array'] == True:
			elem = elem['type']

		elemType = elem['type']

		return elemType

	def evaluate(self):
		self.create_dependencies_graph()

		if self.has_circular_dependencies():
			raise Exception('Hay dependencias circulares')

		return self.p[1]

	def has_circular_dependencies(self):                     
		G = self.dependencies
	   	color = {u : "white" for u in G}  
		found_cycle = [False]                
	                                         
		for u in G:                          
		    if color[u] == "white":
		        self._dfs_visit(G, u, color, found_cycle)
		    if found_cycle[0]:
		        break
		return found_cycle[0]
	 
	def _dfs_visit(self, G, u, color, found_cycle):
	    if found_cycle[0]:                          
	        return
	    color[u] = "gray"                           

	    for v in G[u]:                              
	        if color[v] == "gray":                  
	            found_cycle[0] = True       
	            return
	        if color[v] == "white":                 
	            self._dfs_visit(G, v, color, found_cycle)
	    color[u] = "black"                          

