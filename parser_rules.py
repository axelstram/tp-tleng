from lexer_rules import tokens
from expressions import *

# I -> S | lambda
def p_inicial(p):
	'i : s'
	'  | lambda'
	p[0] = p[1]

def p_inicial_dos(p):
	'i : s i'
	p[0] = Tuple(p[1], p[2])

# lambda
def p_lambda(p):
	'lambda :'
	pass

# S -> type id struct { E }
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
	p[0] = Tuple(p[1], p[2])

# T -> type
def p_type_string(p):
	'''t : STRING 
	| INT
	| BOOL
	| FLOAT
	| ID'''
	p[0] = Type(p[1])



def p_error(token):
    message = '[Syntax error]'
    if token is not None:
        message += "\ntype:" + token.type
        message += "\nvalue:" + str(token.value)
        message += "\nline:" + str(token.lineno)
        message += "\nposition:" + str(token.lexpos)
	print(message)