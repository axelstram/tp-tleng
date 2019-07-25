from lexer_rules import tokens
from expressions import *

# I -> S J
def p_inicial(p):
	'i : s j'
	p[0] = Main(p[1], p[2])

# J -> S J 
def p_multiple_structs(p):
	'j : s j'
	p[0] = StructList(p[1], p[2])

# J -> lambda
def p_lambda(p):
	'j :'
	pass

# S -> type V struct { E }
def p_type_id_struct_lbrck_m_rbrck(p):
	's : TYPE v STRUCT L_BRCK e R_BRCK'
	p[0] = Struct(p[2], p[5])

# V -> id
def p_name(p):
	'v : ID'
	p[0] = Var(p[1])

# E -> E E
def p_expr_expr(p):
	'e : e e'
	p[0] = Tuple(p[1], p[2])

# E -> V T
def p_expr_to_term_and_type(p):
	'e : v t'
	p[0] = VarAndType(p[1], p[2])

# T -> string | int | bool | float | v
def p_basic_types(p):
	'''t : STRING 
	| INT
	| BOOL
	| FLOAT
	| v'''
	p[0] = Type(p[1])

# T -> []T
def p_array_type(p):
	't : L_SQUARE_BRCK R_SQUARE_BRCK t'
	p[0] = Array(p[3])

# T -> struct { E }
def p_embedded_struct(p):
	't : STRUCT L_BRCK e R_BRCK'
	p[0] = EmbeddedStruct(p[3])




def p_error(token):
    message = '[Syntax error]'
    if token is not None:
        message += "\ntype:" + token.type
        message += "\nvalue:" + str(token.value)
        message += "\nline:" + str(token.lineno)
        message += "\nposition:" + str(token.lexpos)
	print(message)