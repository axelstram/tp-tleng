import lexer_rules
import parser_rules
import pprint

import sys

from ply.lex import lex
from ply.yacc import yacc


if __name__ == "__main__":

	text = "".join(sys.stdin)

	lexer = lex(module=lexer_rules)
	parser = yacc(module=parser_rules)
	pp = pprint.PrettyPrinter(indent=1)

	try:
		expression = parser.parse(text, lexer)
		result = expression.convert_to_json()

		pp.pprint(expression.convert_to_json())

	except BaseException as e:
		print(e)

