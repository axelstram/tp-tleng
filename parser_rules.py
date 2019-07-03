from lexer_rules import tokens
from expressions import *

# S -> type id struct { M }
def p_type_id_struct_lbrck_m_rbrck(p):
	's : TYPE n STRUCT L_BRCK m R_BRCK'
	p[0] = Struct(p[2], p[5])

# N -> id
def p_name(p):
	'n : ID'
	p[0] = p[1]

# M -> M M
def p_expr_expr(p):
	'm : m m'
	p[0] = Tuple(p[1], p[2])


#def p_lambda(p):
#	'm : '
#	p[0] = None

# M -> N T
def p_expr_to_term_and_type(p):
	'm : n t'
	p[0] = Tuple(p[1], p[2])

# T -> type
def p_type_string(p):
	'''t : STRING 
	| INT
	| BOOL
	| FLOAT'''
	p[0] = p[1].lower()



def p_error(token):
    message = '[Syntax error]'
    if token is not None:
        message += "\ntype:" + token.type
        message += "\nvalue:" + str(token.value)
        message += "\nline:" + str(token.lineno)
        message += "\nposition:" + str(token.lexpos)
	print(message)