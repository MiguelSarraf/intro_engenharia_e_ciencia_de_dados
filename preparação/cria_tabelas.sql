USE intro_dados_prata;

CREATE TABLE info_sistema (
	estampa_de_tempo timestamp,
    uso_cpu_geral float,
    uso_cpu_0 float,
    uso_cpu_1 float,
    uso_cpu_2 float,
    uso_cpu_3 float,
    uso_cpu_4 float,
    uso_cpu_5 float,
    uso_cpu_6 float,
    uso_cpu_7 float,
    frequencia_cpu float,
    uso_memoria_virtual float,
    uso_memoria_swap float,
    bytes_lidos_disco int,
    bytes_escritos_disco int,
    bytes_enviados_rede int,
    bytes_recebidos_rede int,
    temperatura_externa float,
    temperatura_chipset float,
    temperatura_cpu_geral float,
    temperatura_cpu_0 float,
    temperatura_cpu_1 float,
    temperatura_cpu_2 float,
    temperatura_cpu_3 float,
    temperatura_dell_cpu float,
    temperatura_dell_ambiente float,
    temperatura_dell_sodimm float,
    temperatura_dell_gpu float,
    temperatura_placa_rede float,
    bateria_carga float,
    bateria_carregando bool,
    bateria_tempo_restante int
);

CREATE TABLE dados_maquina (
	parametro varchar(50),
    valor float
);

CREATE TABLE janelas (
	janela int,
    inicio datetime,
    fim datetime
);

CREATE TABLE dados_meteorologicos (
	datahora datetime,
    precipitacao float,
    pressao_atm float,
    radiacao float,
    temperatura float,
    temperatura_orvalho float,
    umidade float,
    vento_direcao float,
    vento_rajada float,
    vento_velocidade float
);

CREATE TABLE dados_meteorologicos_extremos (
	datahora datetime,
    pressao_atm_max float,
    pressao_atm_min float,
    temperatura_max float,
    temperatura_min float,
    temperatura_orvalho_max float,
    temperatura_orvalho_min float,
    umidade_max float,
    umidade_min float
);