import os
import pandas as pd
import numpy as np
from varname import nameof
from sqlalchemy import create_engine
from constantes import *
from funcoes_comuns import *

caminho_dados_ingeridos = os.environ.get("PASTA_RAIZ") + os.environ.get("PASTA_INGESTAO")
caminho_arquivo = caminho_dados_ingeridos + "system_monitoring.parquet"

usuario = os.environ.get("USUARIO_ENGENHARIA")
senha = os.environ.get("USUARIO_ENGENHARIA_SENHA")
host = "localhost"
porta = 3306
database = os.environ.get("DATABASE_PRATA")

monitoramento_sistema = pd.read_parquet(caminho_arquivo)

# Normalização

dados_maquina = monitoramento_sistema[parametros_maquina.keys()]
dados_maquina = dados_maquina.drop_duplicates()
dados_maquina = dados_maquina.rename(columns=parametros_maquina)
dados_maquina = dados_maquina.melt(var_name="parametro", value_name="valor")

janelas = monitoramento_sistema.groupby("janela").agg({"timestamp":["min", "max"]}).reset_index()
janelas.columns = ["janela", "inicio", "fim"]

info_sistema = monitoramento_sistema[colunas_dados_sistema.keys()]
info_sistema = info_sistema.rename(columns=colunas_dados_sistema)

# Formatação

dados_maquina = transforma_colunas(dados_maquina, nameof(dados_maquina))
janelas = transforma_colunas(janelas, nameof(janelas))
info_sistema = transforma_colunas(info_sistema, nameof(info_sistema))

# Limpeza

dados_maquina = dados_maquina[dados_maquina["valor"].notna()]
info_sistema = info_sistema[info_sistema["estampa_de_tempo"].notna()]
info_sistema = preenche_valores_vazios(info_sistema, "estampa_de_tempo")

# Escrita dos resultados

engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{database}")

dados_maquina.to_sql(nameof(dados_maquina), con=engine, if_exists="replace", index=False)
janelas.to_sql(nameof(janelas), con=engine, if_exists="replace", index=False)
info_sistema.to_sql(nameof(info_sistema), con=engine, if_exists="replace", index=False)

engine.dispose()
