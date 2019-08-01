#!/bin/bash
rm -r tests/resultados/
mkdir -p tests/resultados

for file in tests/*.*; do 
	python main.py <$file >tests/resultados/resultado_${file##*/}; 
	echo -e "$\e[1;32m***************** input: ${file}*****************\e[0;39m";
		cat $file; 
	echo ''
	echo -e "$\e[0;32m----------------- output --------------------\e[0;39m"
		cat tests/resultados/resultado_${file##*/};
	echo ''
done