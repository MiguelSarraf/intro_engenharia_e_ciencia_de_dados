import requests
import zipfile
import io
import pandas as pd
import sys
import os


def baixar_dados(estacao, ano):
    url = f"https://portal.inmet.gov.br/uploads/dadoshistoricos/{ano}.zip"
    
    response = requests.get(url)
    response.raise_for_status()

    with zipfile.ZipFile(io.BytesIO(response.content)) as arquivo_zip:
        arquivos = arquivo_zip.namelist()
        
        # Filtrar estação
        arquivos = [arquivo for arquivo in arquivos if estacao in arquivo]
        
        dados = []
        #Itera sobre todos os arquivos do ano para salvar em um único dataframe
        for arquivo_estacao in arquivos:
            with arquivo_zip.open(arquivo_estacao) as arquivo:
                # Arquivo vem com header de 8 linhas com informações sobre a estação
                df = pd.read_csv(arquivo, sep=';', encoding="latin-1", skiprows=8)
                dados.append(df)
        dados = pd.concat(dados)
    
    return dados

JSON_FOLDER = os.environ.get("PASTA_INGESTAO")
PARQUET_OUTPUT = JSON_FOLDER+"dados_estacao.parquet"

if len(sys.argv) != 3:
    estacao = input("Qual o código da estação a ser extraída? ")
    ano = input("Qual ano para extração? ")
else:
    estacao = sys.argv[1]
    ano = sys.argv[2]

assert ano.isnumeric(), "Ano deve ser um valor numérico"

df = baixar_dados(estacao, ano)

df.to_parquet(PARQUET_OUTPUT, index=False)

