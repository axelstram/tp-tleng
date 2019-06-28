import ply.yacc as yacc
import ply.lex as lex
from ply.lex import TOKEN
 
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

tokens = ['CORCHETE_IZQ', 'CORCHETE_DER', 'L_SQUARE_BRCK', 'R_SQUARE_BRCK', 'ID'] + list(reserved_words.values())


# Regular expression rules for simple tokens
t_CORCHETE_IZQ = r'{'
t_CORCHETE_DER = r'}'
t_L_SQUARE_BRCK = r'\['
t_R_SQUARE_BRCK = r']'

t_ignore  = ' \t'

data = 'type menem struct { nombre string edad int nacionalidad pais a []struct {b float} }'

lexer = lex.lex()
lexer.input(data)

# Tokenize
while True:
	tok = lexer.token()
	if not tok:
		break      # No more input
	print(tok)