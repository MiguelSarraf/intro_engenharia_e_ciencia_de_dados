#!/bin/bash


env:
	if [ ! -d "intro_venv" ]; then \
		python3 -m venv intro_venv; \
	fi

	@echo "export PASTA_RAIZ=$(shell pwd)" > environment_variables.sh
	@echo "export PASTA_INGESTAO=${ROOT_PATH}/ingestão/resultados/" >> environment_variables.sh
	@echo "export USUARIO_ENGENHARIA=engenheiro_dados" >> environment_variables.sh
	@echo "export USUARIO_ENGENHARIA_SENHA=Uma_senha_muuuuuuuuu1to_segura" >> environment_variables.sh
	@echo "export DATABASE_PRATA=intro_dados_prata" >> environment_variables.sh
	chmod +x environment_variables.sh

	mkdir -p $(shell pwd)/ingestão/resultados/
	mkdir -p $(shell pwd)/ingestão/erros/

	sudo mysql -u root < preparação/cria_acesso.sql
	sudo mysql -u root < preparação/cria_tabelas.sql
	sudo mysql -u root < preparação/cria_permissoes.sql

requirements: requirements.txt
	pip3 install -r requirements.txt

gera_info_sistema:
	python3 ingestão/gera_dados.py

ingere_info_sistema:
	python3 ingestão/processa_json.py

ingere_inmet: parametros.txt
	cat parametros.txt | python3 ingestão/baixa_inmet.py

prepara: ingestão/resultados/system_monitoring.parquet ingestão/resultados/dados_estacao.parquet
	python3 preparação/prepara_monitoramento_sistema.py
	python3 preparação/prepara_condicoes_meteorologicas.py
