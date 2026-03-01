import os
import pandas as pd
import numpy as np
from varname import nameof
from sqlalchemy import create_engine
from constantes import *
from funcoes_comuns import *

caminho_dados_ingeridos = os.environ.get("PASTA_RAIZ") + os.environ.get("PASTA_INGESTAO")
caminho_arquivo = caminho_dados_ingeridos + "dados_estacao.parquet"

usuario = os.environ.get("USUARIO_ENGENHARIA")
senha = os.environ.get("USUARIO_ENGENHARIA_SENHA")
host = "localhost"
porta = 3306
database = os.environ.get("DATABASE_PRATA")

condicoes_meteorologicas = pd.read_parquet(caminho_arquivo)

# Normalização

condicoes_meteorologicas["datahora"] = condicoes_meteorologicas["Data"]+condicoes_meteorologicas["Hora UTC"].str.strip(" UTC")

dados_meteorologicos = condicoes_meteorologicas[colunas_dados_meteorologicos.keys()]
dados_meteorologicos = dados_meteorologicos.rename(columns=colunas_dados_meteorologicos)

dados_meteorologicos_extremos = condicoes_meteorologicas[colunas_dados_meteorologicos_extremos.keys()]
dados_meteorologicos_extremos = dados_meteorologicos_extremos.rename(columns=colunas_dados_meteorologicos_extremos)

# Formatação

dados_meteorologicos = transforma_colunas(dados_meteorologicos, nameof(dados_meteorologicos), formato_datahora="%Y/%m/%d%H%M")
dados_meteorologicos_extremos = transforma_colunas(dados_meteorologicos_extremos, nameof(dados_meteorologicos_extremos), formato_datahora="%Y/%m/%d%H%M")

# Limpeza

dados_meteorologicos["radiacao"] = dados_meteorologicos["radiacao"].fillna(0)
dados_meteorologicos = dados_meteorologicos.dropna()

dados_meteorologicos_extremos = dados_meteorologicos_extremos.dropna()

# Escrita dos resultados

engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{database}")

dados_meteorologicos.to_sql(nameof(dados_meteorologicos), con=engine, if_exists="replace", index=False)
dados_meteorologicos_extremos.to_sql(nameof(dados_meteorologicos_extremos), con=engine, if_exists="replace", index=False)

engine.dispose()
