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
	d = {}
	d['id'] = p[1]
	d['type'] = p[2]
	p[0] = d

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

def p_error(token):
    message = '[Syntax error]'
    if token is not None:
        message += "\ntype:" + token.type
        message += "\nvalue:" + str(token.value)
        message += "\nline:" + str(token.lineno)
        message += "\nposition:" + str(token.lexpos)
	print(message)