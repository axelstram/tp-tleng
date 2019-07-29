import lexer_rules
import parser_rules
import json
import pprint

import generadorDatos as gd

import sys

from ply.lex import lex
from ply.yacc import yacc


if __name__ == "__main__":

	text = str(sys.stdin.readlines()[0])

	lexer = lex(module=lexer_rules)
	parser = yacc(module=parser_rules)

	try:
		expression = parser.parse(text, lexer)
		result, dependencies = expression.evaluate()

		pp = pprint.PrettyPrinter(indent=1)

		print('-------------------')
		pp.pprint(result)


		print('-------------------')
		pp.pprint(dependencies)

		print('-------------------')
		pp.pprint(caca(result, dependencies))



	except BaseException as e:
		print(e)

def caca(result, dependencies):
	main = result[0]
	mainAsDict = armarStruct(main['structBody'])
	
def armarStruct(camposDelStruct)
	structAsDict = {}
	for elem in camposDelStruct:
		valor = None

		if isArray(elem):
			valor = 'gordo'
		elif isStruct(elem):
			valor = armarStruct()
		else:
			valor = gd.generarTipoBasico(elem['type'])

		structAsDict[elem['id']] = valor	