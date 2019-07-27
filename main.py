import lexer_rules
import parser_rules
import parser_rules2
import json
import pprint

import sys

from ply.lex import lex
from ply.yacc import yacc


if __name__ == "__main__":

    text = str(sys.stdin.readlines()[0])

    lexer = lex(module=lexer_rules)
    parser = yacc(module=parser_rules2)

    expression = parser.parse(text, lexer)
    result = expression.evaluate()
    pp = pprint.PrettyPrinter(indent=1)

    print('-------------------')
    pp.pprint(result)