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

