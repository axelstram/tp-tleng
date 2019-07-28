def t_error(t):
    print('entro')
    print("Illegal character '%s'" % t.value[0])
    #t.lexer.skip(1)
    raise BaseException('Error de lexer')

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved_words.keys():
    	t.type = reserved_words.get(t.value)
    	t.value = reserved_words.get(t.value)
    return t

reserved_words = {
	'type':      'TYPE',
	'struct':    'STRUCT',
	'string':    'STRING',
	'int':       'INT',
	'float64':   'FLOAT',
	'bool':      'BOOL'
}

tokens = ['L_BRCK', 'R_BRCK', 'L_SQUARE_BRCK', 'R_SQUARE_BRCK', 'ID'] + list(reserved_words.values())

t_L_BRCK = r'{'
t_R_BRCK = r'}'
t_L_SQUARE_BRCK = r'\['
t_R_SQUARE_BRCK = r']'

t_ignore  = '\n\t '