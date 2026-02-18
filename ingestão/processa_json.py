import json
import os
import pandas as pd


def achata_json(data, chave_pai="", separador="."):
    items = {}

    if isinstance(data, dict):
        for chave, valor in data.items():
            nova_chave = f"{chave_pai}{separador}{chave}" if chave_pai else chave
            items.update(achata_json(valor, nova_chave, separador))

    elif isinstance(data, list):
        for indice, item in enumerate(data):
            nova_chave = f"{chave_pai}{separador}{indice}" if chave_pai else str(indice)
            items.update(achata_json(item, nova_chave, separador))

    else:
        items[chave_pai] = data

    return items


def proxima_janela(parquet):
    if not os.path.exists(parquet):
        return 0

    dados = pd.read_parquet(parquet)

    if "janela" not in dados.columns or dados.empty:
        return 0

    return dados["janela"].max() + 1


def processa_pasta_json(pasta, parquet):
    jsons = [
        arquivo for arquivo in os.listdir(pasta)
        if arquivo.endswith(".json")
    ]

    janela = proxima_janela(parquet)
    linhas = []

    for nome in jsons:
        caminho_completo = os.path.join(pasta, nome)

        with open(caminho_completo, "r") as arquivo:
            data = json.load(arquivo)

        novos_dados = achata_json(data)
        novos_dados["janela"] = janela

        linhas.append(novos_dados)

    saida = pd.DataFrame(linhas)

    # Se já existe parquet, concatenar
    if os.path.exists(parquet):
        atual = pd.read_parquet(parquet)
        saida = pd.concat([atual, saida], ignore_index=True)

    # Salvar parquet
    saida.to_parquet(parquet, index=False)

    # Remover JSONs processados
    for nome in jsons:
        os.remove(os.path.join(pasta, nome))


JSON_FOLDER = os.environ.get("PASTA_INGESTAO")
PARQUET_OUTPUT = JSON_FOLDER+"system_monitoring.parquet"

processa_pasta_json(JSON_FOLDER, PARQUET_OUTPUT)

