import pandas as pd
import numpy as np
from constantes import *

def transforma_colunas_str(df, df_nome):
  for coluna in colunas_str[df_nome]:
    df[coluna] = df[coluna].astype(str)
  return df

def transforma_colunas_int(df, df_nome):
  for coluna in colunas_int[df_nome]:
    df[coluna] = df[coluna].astype("Int64")
  return df

def transforma_colunas_float(df, df_nome):
  for coluna in colunas_float[df_nome]:
    try:
      df[coluna] = df[coluna].astype(float)
    except:
      # df[coluna] = "0" + df[coluna].astype(str)
      df[coluna] = df[coluna].str.replace(",", ".")
      df[coluna] = df[coluna].astype(float)
  return df

def transforma_colunas_datetime(df, df_nome, formato_datahora):
  for coluna in colunas_datetime[df_nome]:
    df[coluna] = pd.to_datetime(
        df[coluna],
        format=formato_datahora,
        errors="coerce"
    )
  return df

def transforma_colunas_bool(df, df_nome):
  for coluna in colunas_bool[df_nome]:
    df[coluna] = df[coluna].map({"True": True, "False":False}).astype(bool)
  return df

def transforma_colunas(df, df_nome, formato_datahora=DATETIME_FORMAT):
  assert df_nome in colunas_int, f"{df_nome} não é um dataframe válido"

  df = transforma_colunas_str(df, df_nome)
  df = transforma_colunas_int(df, df_nome)
  df = transforma_colunas_float(df, df_nome)
  df = transforma_colunas_datetime(df, df_nome, formato_datahora)
  df = transforma_colunas_bool(df, df_nome)

  return df

def preenche_valores_vazios(df, coluna_referencia):
    df = df.sort_values(coluna_referencia)
    df = df.set_index(coluna_referencia)
    df = df.interpolate(method="ffill")
    return df.reset_index()
