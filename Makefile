#!/bin/bash


env:
	if [ ! -d "intro_venv" ]; then \
		python3 -m venv intro_venv; \
	fi

	@echo "export PASTA_RAIZ=$(shell pwd)" > environment_variables.sh
	@echo "export PASTA_INGESTAO=${ROOT_PATH}/ingestão/resultados/" >> environment_variables.sh
	chmod +x environment_variables.sh

	mkdir -p $(shell pwd)/ingestão/resultados/

requirements: requirements.txt
	pip3 install -r requirements.txt

gera_info_sistema:
	python3 ingestão/gera_dados.py

ingere_info_sistema:
	python3 ingestão/processa_json.py

ingere_inmet: parametros.txt
	cat parametros.txt | python3 ingestão/baixa_inmet.py
