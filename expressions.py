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
			return [self.struct] + self.rest
		elif self.struct is not None:
			return [self.struct]

class Main(object):
	def __init__(self, p):
		self.p = p
		self.dependencies = {}
		self.basicTypes = ['STRING', 'INT', 'FLOAT', 'BOOL']
		
	def evaluate(self):
		self.create_dependencies_graph()

		if self.has_undefined_dependencies():
			raise Exception('Se estan usando tipos no definidos')

		if self.has_circular_dependencies():
			raise Exception('Hay dependencias circulares')

		if self.has_duplicated_type_definitions():
			raise Exception('Hay definiciones de tipos duplicadas')

		if self.has_duplicated_field_definitions():
			raise Exception('Hay campos duplicados')

		return self.p[1]

	def convert_to_json(self):
		return gd.generate_json(self.evaluate())
	
	def create_dependencies_graph(self):
		for struct in self.p[1]:

			elements = struct['structBody']
			dependencieList = []

			for elem in elements:
				#cada elem es un dic con clave id y type (que a su vez es otro dic)
				elemType = self.get_elem_type(elem['type'])

				if is_struct(elemType):
					dependencieList = self.add_inner_dependencies(dependencieList, elemType)
				elif elemType not in self.basicTypes:
					dependencieList.append(elemType)

			self.dependencies[struct['id']] = dependencieList

		#print('dependencies: ' + str(self.dependencies))

	def get_elem_type(self, elem):
		#si es un arreglo o arreglo de arreglos, va iterando hasta el final
		#para encontrar el tipo
		while elem['is_array']:
			elem = elem['type']

		elemType = elem['type']

		return elemType

	def add_inner_dependencies(self, dependencies, elements):
		for elem in elements:
			elem = self.get_elem_type(elem['type'])

			if is_struct(elem):
				dependencies = self.add_inner_dependencies(dependencies, elem)
			else:
				if elem not in self.basicTypes:
					dependencies.append(elem)

		return dependencies

	def has_circular_dependencies(self):                     
		G = self.dependencies
		color = {u : "white" for u in G}  
		found_cycle = [False]                
		                                     
		for u in G:                          
		    if color[u] == "white":
		        self.dfs_visit(G, u, color, found_cycle)
		    if found_cycle[0]:
		        break
		return found_cycle[0]
	 
	def dfs_visit(self, G, u, color, found_cycle):
	    if found_cycle[0]:                          
	        return
	    color[u] = "gray"                           

	    for v in G[u]:                              
	        if color[v] == "gray":                  
	            found_cycle[0] = True       
	            return
	        if color[v] == "white":                 
	            self.dfs_visit(G, v, color, found_cycle)
	    color[u] = "black"

	def has_undefined_dependencies(self):
		for dependencies in self.dependencies.values():
			for dependency in dependencies:
				if (dependency not in self.dependencies.keys()):
					return True

		return False

	def has_duplicated_type_definitions(self):
		ids = []

		for struct in self.p[1]:
			ids.append(struct['id'])

		return len(ids) != len(set(ids))

	def has_duplicated_field_definitions(self):
		for struct in self.p[1]:

			elements = struct['structBody']
			fields = []

			for elem in elements:
				fields.append(elem['id'])

			if len(fields) != len(set(fields)):
				return True

		return False

def is_struct(e):
	return isinstance(e, list)