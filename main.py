import lexer_rules
import parser_rules

from sys import argv, exit

from ply.lex import lex
from ply.yacc import yacc


if __name__ == "__main__":

    text = 'type menem struct { nombre []string } type sida struct { asd int }'

    lexer = lex(module=lexer_rules)
    parser = yacc(module=parser_rules)

    expression = parser.parse(text, lexer)
    result = expression.evaluate()
    
    print(result)
    #lexer.input(text)

    #while True:
    #    tok = lexer.token()
    #    if not tok:
    #        break      # No more input
    #    print(tok)
