import lexer_rules
import parser_rules
import json
from pprint import pprint

import sys

from ply.lex import lex
from ply.yacc import yacc


if __name__ == "__main__":

    text = str(sys.stdin.readlines()[0])

    lexer = lex(module=lexer_rules)
    parser = yacc(module=parser_rules)

    expression = parser.parse(text, lexer)
    result = expression.evaluate()
    
    print(result)