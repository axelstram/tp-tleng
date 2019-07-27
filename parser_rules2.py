from lexer_rules import tokens
from expressions import *

# S -> J
def p_inicial(p):
	's : structs'
	p[0] = Main(p)

def p_structs(p):
    '''
    structs : structType structs 
             | empty 
    '''	
    structList = StructList(p)
    p[0] = structList.evaluate()

def p_structType(p):
	'''
    structType : TYPE ID struct
    '''	
	struct = Struct(p)
	p[0] = struct.evaluate()

def p_struct(p):
	'''
    struct : STRUCT L_BRCK elements R_BRCK 
    '''
	p[0] = p[3]

def p_elements(p):
	'''
    elements : element elements
    		 | empty
    '''
	if len(p) <= 2:
	    p[0] = []
	else:
		p[0] = [p[1]] + p[2]

def p_element(p):
	'''
    element : ID type
    '''
	p[0] = (p[1], p[2])

def p_type(p):
    '''
    type : L_SQUARE_BRCK R_SQUARE_BRCK type 
         | basicType
    '''
    d = {}

    if len(p) <= 2:
        d['is_array'] = False
        d['type'] = p[1]
        p[0] = d
    else:
    	d['is_array'] = True
        d['type'] = p[3]
        p[0] = d

def p_basicType(p):
    '''
    basicType : BOOL
          | INT
          | STRING
          | FLOAT
          | ID
          | struct
    '''
    p[0] = p[1]

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None
	


# # J -> S J 
# def p_multiple_structs(p):
# 	'j : s j'
# 	p[0] = StructList(p[1], p[2])

# # J -> lambda
# def p_lambda(p):
# 	'j :'
# 	pass

# # S -> type V struct { E }
# def p_type_id_struct_lbrck_m_rbrck(p):
# 	's : TYPE v STRUCT L_BRCK e R_BRCK'
# 	p[0] = Struct(p[2], p[5])

# # V -> id
# def p_name(p):
# 	'v : ID'
# 	p[0] = Var(p[1])

# # E -> E E
# def p_expr_expr(p):
# 	'e : e e'
# 	p[0] = Tuple(p[1], p[2])

# # E -> V T
# def p_expr_to_term_and_type(p):
# 	'e : v t'
# 	p[0] = VarAndType(p[1], p[2])

# # T -> string | int | bool | float | v
# def p_basic_types(p):
# 	'''t : STRING 
# 	| INT
# 	| BOOL
# 	| FLOAT
# 	| v'''
# 	p[0] = Type(p[1])

# # T -> []T
# def p_array_type(p):
# 	't : L_SQUARE_BRCK R_SQUARE_BRCK t'
# 	p[0] = Array(p[3])

# # T -> struct { E }
# def p_embedded_struct(p):
# 	't : STRUCT L_BRCK e R_BRCK'
# 	p[0] = EmbeddedStruct(p[3])




def p_error(token):
    message = '[Syntax error]'
    if token is not None:
        message += "\ntype:" + token.type
        message += "\nvalue:" + str(token.value)
        message += "\nline:" + str(token.lineno)
        message += "\nposition:" + str(token.lexpos)
	print(message)