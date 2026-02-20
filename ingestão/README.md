# Ingestão

O processo de ingestão definido consiste em 2 etapas:
1. Monitoramento de informações de sistema da máquina local
1. Download de informações metereológicas do site da [INMET](https://tempo.inmet.gov.br/)

Para a primeira parte, foram criados 2 scripts para simular uma ingestão por fluxo. Um script [simula a emissão dos dados dos sensores, escrevendo em formato JSON](https://github.com/MiguelSarraf/intro_engenharia_e_ciencia_de_dados/blob/main/ingest%C3%A3o/gera_dados.py) e o outro [lê diversos JSONs e salvar os dados em um arquivo parquet](https://github.com/MiguelSarraf/intro_engenharia_e_ciencia_de_dados/blob/main/ingest%C3%A3o/processa_json.py). Este segundo script é o script de ingestão propriamente dito, conforme estudado na teoria.

Para rodar os scripts, basta chamá-los via python e os resultados serão escritos na pasta "resultados" dentro do diretório "ingestão" deste projeto.

```
python3 ingestão/gera_dados.py
python3 ingestão/processa_json.py
```

Ou ainda, é possível fazer estas execuções através de comando `make`.

```
make gera_info_sistema
make ingere_info_sistema
```

Para fins de geração de dados de teste para o curso, os dois códigos foram agendados para serem executados através de cron jobs no sistema:

```
*/2 * * * * python3 <caminho_para_pasta>/intro_engenharia_e_ciencia_de_dados/ingestão/gera_dados.py
0 * * * * python3 <caminho_para_pasta>/intro_engenharia_e_ciencia_de_dados/ingestão/processa_json.py
```

Dessa forma, o primeiro script executa a cada 2 minutos e o segundo a cada 1 hora, processando cerca de 30 JSONs por vez.

Para a segunda parte, foi criado um script para simular uma ingestão por lote. [Ele acessa a API do portal do INMET, baixa todos os arquivos do ano e filtra apenas aqueles das estações meteorológicas desejadas para abrir e salva tudo com parquet](https://github.com/MiguelSarraf/intro_engenharia_e_ciencia_de_dados/blob/main/ingest%C3%A3o/baixa_inmet.py).

Para rodar o script, basta executá-lo via Python passando o código da estação e ano desejados via linha de comando. O Código da estação pode ser identificado pela [interface gráfica do INMET](https://tempo.inmet.gov.br/) ao selecionar a estação pelo seu nome.

Baixando os dados do Mirante de Santana (São Paulo) para o ano de 2026:

```
python3 ingestão/baixa_inmet.py A701 2026
```

Se estes valores não forem fornecidos na linha de comando, dois prompts serão exibidos para que os valores sejam passados durante a execução.

Ainda é possível criar um arquivo `parametros.txt` contendo o código da estação e o ano em linhas consecutivas e executar a rotina de extração via comando `make`.

```
[parametros.txt]
A701
2026
```

```
make ingere_inmet
```
