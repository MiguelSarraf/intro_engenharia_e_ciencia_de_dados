USE intro_dados_ouro;

CREATE TABLE metricas_hora (
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
	temperatura_cpu_geral float
);

CREATE TABLE dim_datahora (
	datahora datetime,
	mes int,
	ano int,
	hora int
);

CREATE TABLE dim_metrica (
	id int,
	nome varchar(25)
);
