import ply.yacc as yacc
import ply.lex as lex
from ply.lex import TOKEN
from Struct import *
from Expression import *

def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)

def t_ID(t):
    r'\[]|[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved_words.keys():
    	t.type = reserved_words.get(t.value)
    	t.value = reserved_words.get(t.value)
    return t
    
#digit            = r'([0-9])'
#nondigit         = r'([_A-Za-z])'
#identifier       = r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)'

#@TOKEN(identifier)
#def t_STRUCT_NAME(t):
#	t.type = 'STRUCT_NAME'
#	return t



reserved_words = {
	'type':      'TYPE',
	'struct':    'STRUCT',
	'string':    'STRING',
	'int':       'INT',
	'float64':   'FLOAT64',
	'bool':      'BOOL',
	'[]':        'ARRAY'
}

tokens = ['L_BRCK', 'R_BRCK', 'L_SQUARE_BRCK', 'R_SQUARE_BRCK', 'ID'] + list(reserved_words.values())


# Regular expression rules for simple tokens
t_L_BRCK = r'{'
t_R_BRCK = r'}'
t_L_SQUARE_BRCK = r'\['
t_R_SQUARE_BRCK = r']'

t_ignore  = ' \t'

data = 'type menem struct { nombre string edad int nacionalidad pais a []struct {b float} }'

lexer = lex.lex()
lexer.input(data)


# ------ parser ---------- (separar en otro archivo despues)

# S -> type id struct { M }
def p_type_id_struct_lbrck_m_rbrck(p):
	's : TYPE id STRUCT LBRCK m RBRCK'
	p[0] = Struct(p[2], p[5])

# M -> M M
def p_expr_expr(p):
	'M : M M'
	p[0] = (p[1], p[2])

# M -> N N
def p_expr_to_terms(p):
	'M : N N'
	p[0] = Expression(p[1], p[2])

# Tokenize
while True:
	tok = lexer.token()
	if not tok:
		break      # No more input
	print(tok)