# Dicionários de colunas para normalização

parametros_maquina = {
    "cpu.physical_cores": "num_nucleos",
    "cpu.total_cores": "num_nucleos_virtuais",
    "cpu.cpu_freq.min_mhz": "frequencia_minima",
    "cpu.cpu_freq.max_mhz": "frequencia_maxima",
    "memory.virtual_memory.total": "memoria_virtual",
    "memory.swap_memory.total": "memoria_swap",
    "temperatures.acpitz.0.high": "temperatura_externa_limite_alto",
    "temperatures.acpitz.0.critical": "temperatura_externa_limite_critico",
    "temperatures.pch_skylake.0.high": "temperatura_chipset_limite_alto",
    "temperatures.pch_skylake.0.critical": "temperatura_chipset_limite_critico",
    "temperatures.coretemp.0.high": "temperatura_cpu_geral_limite_alto",
    "temperatures.coretemp.0.critical": "temperatura_cpu_geral_limite_critico",
    "temperatures.coretemp.1.high": "temperatura_cpu_0_limite_alto",
    "temperatures.coretemp.1.critical": "temperatura_cpu_0_limite_critico",
    "temperatures.coretemp.2.high": "temperatura_cpu_1_limite_alto",
    "temperatures.coretemp.2.critical": "temperatura_cpu_1_limite_critico",
    "temperatures.coretemp.3.high": "temperatura_cpu_2_limite_alto",
    "temperatures.coretemp.3.critical": "temperatura_cpu_2_limite_critico",
    "temperatures.coretemp.4.high": "temperatura_cpu_3_limite_alto",
    "temperatures.coretemp.4.critical": "temperatura_cpu_3_limite_critico",
    "temperatures.dell_smm.0.high": "temperatura_dell_cpu_limite_alto",
    "temperatures.dell_smm.0.critical": "temperatura_dell_cpu_limite_critico",
    "temperatures.dell_smm.1.high": "temperatura_dell_ambiente_limite_alto",
    "temperatures.dell_smm.1.critical": "temperatura_dell_ambiente_limite_critico",
    "temperatures.dell_smm.2.high": "temperatura_dell_sodimm_limite_alto",
    "temperatures.dell_smm.2.critical": "temperatura_dell_sodimm_limite_critico",
    "temperatures.dell_smm.3.high": "temperatura_dell_gpu_limite_alto",
    "temperatures.dell_smm.3.critical": "temperatura_dell_gpu_limite_critico",
    "temperatures.iwlwifi_1.0.high": "temperatura_placa_rede_limite_alto",
    "temperatures.iwlwifi_1.0.critical": "temperatura_placa_rede_limite_critico",
}

colunas_dados_sistema = {
    "timestamp": "estampa_de_tempo",
    "cpu.cpu_usage_percent_total": "uso_cpu_geral",
    "cpu.cpu_usage_percent_per_core.0": "uso_cpu_0",
    "cpu.cpu_usage_percent_per_core.1": "uso_cpu_1",
    "cpu.cpu_usage_percent_per_core.2": "uso_cpu_2",
    "cpu.cpu_usage_percent_per_core.3": "uso_cpu_3",
    "cpu.cpu_usage_percent_per_core.4": "uso_cpu_4",
    "cpu.cpu_usage_percent_per_core.5": "uso_cpu_5",
    "cpu.cpu_usage_percent_per_core.6": "uso_cpu_6",
    "cpu.cpu_usage_percent_per_core.7": "uso_cpu_7",
    "cpu.cpu_freq.current_mhz": "frequencia_cpu",
    "memory.virtual_memory.percent": "uso_memoria_virtual",
    "memory.swap_memory.percent": "uso_memoria_swap",
    "disk.disk_io.read_bytes": "bytes_lidos_disco",
    "disk.disk_io.write_bytes": "bytes_escritos_disco",
    "network.bytes_sent": "bytes_enviados_rede",
    "network.bytes_recv": "bytes_recebidos_rede",
    "temperatures.acpitz.0.current": "temperatura_externa",
    "temperatures.pch_skylake.0.current": "temperatura_chipset",
    "temperatures.coretemp.0.current": "temperatura_cpu_geral",
    "temperatures.coretemp.1.current": "temperatura_cpu_0",
    "temperatures.coretemp.2.current": "temperatura_cpu_1",
    "temperatures.coretemp.3.current": "temperatura_cpu_2",
    "temperatures.coretemp.4.current": "temperatura_cpu_3",
    "temperatures.dell_smm.0.current": "temperatura_dell_cpu",
    "temperatures.dell_smm.1.current": "temperatura_dell_ambiente",
    "temperatures.dell_smm.2.current": "temperatura_dell_sodimm",
    "temperatures.dell_smm.3.current": "temperatura_dell_gpu",
    "temperatures.iwlwifi_1.0.current": "temperatura_placa_rede",
    "battery.percent": "bateria_carga",
    "battery.plugged_in": "bateria_carregando",
    "battery.secs_left": "bateria_tempo_restante",
}

colunas_dados_meteorologicos = {
    "datahora": "datahora",
    "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)": "precipitacao",
    "PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)": "pressao_atm",
    "RADIACAO GLOBAL (Kj/m²)": "radiacao",
    "TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)": "temperatura",
    "TEMPERATURA DO PONTO DE ORVALHO (°C)": "temperatura_orvalho",
    "UMIDADE RELATIVA DO AR, HORARIA (%)": "umidade",
    "VENTO, DIREÇÃO HORARIA (gr) (° (gr))": "vento_direcao",
    "VENTO, RAJADA MAXIMA (m/s)": "vento_rajada",
    "VENTO, VELOCIDADE HORARIA (m/s)": "vento_velocidade",
}

colunas_dados_meteorologicos_extremos = {
    "datahora": "datahora",
    "PRESSÃO ATMOSFERICA MAX.NA HORA ANT. (AUT) (mB)": "pressao_atm_max",
    "PRESSÃO ATMOSFERICA MIN. NA HORA ANT. (AUT) (mB)": "pressao_atm_min",
    "TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)": "temperatura_max",
    "TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)": "temperatura_min",
    "TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (°C)": "temperatura_orvalho_max",
    "TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (°C)": "temperatura_orvalho_min",
    "UMIDADE REL. MAX. NA HORA ANT. (AUT) (%)": "umidade_max",
    "UMIDADE REL. MIN. NA HORA ANT. (AUT) (%)": "umidade_min",
}

# Dicionários de tipos para preparação

colunas_str = {
    "dados_maquina":[
        "parametro"
    ],
    "janelas":[],
    "info_sistema":[],
    "dados_meteorologicos":[],
    "dados_meteorologicos_extremos":[],
}

colunas_int = {
    "dados_maquina":[],
    "janelas":[
        "janela"
    ],
    "info_sistema":[
        "bytes_lidos_disco",
        "bytes_escritos_disco",
        "bytes_enviados_rede",
        "bytes_recebidos_rede",
        "bateria_tempo_restante"
    ],
    "dados_meteorologicos":[
        "umidade",
        "vento_direcao"
    ],
    "dados_meteorologicos_extremos":[
        "umidade_max",
        "umidade_min"
    ],
}

colunas_float = {
    "dados_maquina":[
        "valor"
    ],
    "janelas":[],
    "info_sistema":[
        "uso_cpu_geral",
        "uso_cpu_0",
        "uso_cpu_1",
        "uso_cpu_2",
        "uso_cpu_3",
        "uso_cpu_4",
        "uso_cpu_5",
        "uso_cpu_6",
        "uso_cpu_7",
        "frequencia_cpu",
        "uso_memoria_virtual",
        "uso_memoria_swap",
        "temperatura_externa",
        "temperatura_chipset",
        "temperatura_cpu_geral",
        "temperatura_cpu_0",
        "temperatura_cpu_1",
        "temperatura_cpu_2",
        "temperatura_cpu_3",
        "temperatura_dell_cpu",
        "temperatura_dell_ambiente",
        "temperatura_dell_sodimm",
        "temperatura_dell_gpu",
        "temperatura_placa_rede",
        "bateria_carga"
    ],
    "dados_meteorologicos":[
        "precipitacao",
        "pressao_atm",
        "radiacao",
        "temperatura",
        "temperatura_orvalho",
        "vento_rajada",
        "vento_velocidade"
    ],
    "dados_meteorologicos_extremos":[
        "pressao_atm_max",
        "pressao_atm_min",
        "temperatura_max",
        "temperatura_min",
        "temperatura_orvalho_max",
        "temperatura_orvalho_min"
    ],
}

colunas_datetime = {
    "dados_maquina":[],
    "janelas":[
        "inicio",
        "fim"
    ],
    "info_sistema":[
        "estampa_de_tempo"
    ],
    "dados_meteorologicos":[
        "datahora"
    ],
    "dados_meteorologicos_extremos":[
        "datahora"
    ],
}

colunas_bool = {
    "dados_maquina":[],
    "janelas":[],
    "info_sistema":[
        "bateria_carregando"
    ],
    "dados_meteorologicos":[],
    "dados_meteorologicos_extremos":[],
}

# Outras constantes

DATETIME_FORMAT = "%Y-%m-%d_%H:%M:%S"
