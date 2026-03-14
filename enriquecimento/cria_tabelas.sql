USE intro_dados_ouro;

CREATE TABLE clima_hora (
	datahora datetime,
	metrica int,
	valor float,
	classe int
);

CREATE TABLE dados_maquina (
	parametro varchar(50),
	valor float
);

CREATE TABLE maquina_clima (
	datahora datetime,
	precipitacao float,
	pressao_atm float,
	radiacao float,
	temperatura float,
	temperatura_orvalho float,
	umidade float,
	vento_direcao float,
	vento_rajada float,
	vento_velocidade float,
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
	bytes_lidos_disco bigint,
	bytes_escritos_disco bigint,
	bytes_enviados_rede bigint,
	bytes_recebidos_rede bigint,
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
	bateria_tempo_restante bigint
);

CREATE TABLE dim_datahora (
	datahora datetime,
	dia int,
	mes int,
	ano int,
	hora int
);

CREATE TABLE dim_metrica (
	id int,
	nome varchar(25)
);
