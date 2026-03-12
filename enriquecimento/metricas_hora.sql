SET @NUM_CLASSES = (SELECT ROUND(POWER(COUNT(*),0.5),0) FROM intro_dados_prata.dados_meteorologicos);

INSERT INTO intro_dados_ouro.metricas_hora (datahora, metrica, valor, classe)
SELECT * FROM (
	SELECT
		datahora,
		0 AS metrica,
		precipitacao AS valor,
		ROUND(
				(
					precipitacao -
					(SELECT MIN(precipitacao) FROM intro_dados_prata.dados_meteorologicos)
				)/(
				(
					(SELECT MAX(precipitacao) FROM intro_dados_prata.dados_meteorologicos) -
					(SELECT MIN(precipitacao) FROM intro_dados_prata.dados_meteorologicos)
				)/@NUM_CLASSES)
		) AS classe
		FROM intro_dados_prata.dados_meteorologicos
	UNION ALL
	SELECT
		datahora,
		1 AS metrica,
		pressao_atm AS valor,
		ROUND(
				(
					pressao_atm -
					(SELECT MIN(pressao_atm) FROM intro_dados_prata.dados_meteorologicos)
				)/(
				(
					(SELECT MAX(pressao_atm) FROM intro_dados_prata.dados_meteorologicos) -
					(SELECT MIN(pressao_atm) FROM intro_dados_prata.dados_meteorologicos)
				)/@NUM_CLASSES)
		) AS classe
		FROM intro_dados_prata.dados_meteorologicos
	UNION ALL
	SELECT
		datahora,
		2 AS metrica,
		radiacao AS valor,
		ROUND(
				(
					radiacao -
					(SELECT MIN(radiacao) FROM intro_dados_prata.dados_meteorologicos)
				)/(
				(
					(SELECT MAX(radiacao) FROM intro_dados_prata.dados_meteorologicos) -
					(SELECT MIN(radiacao) FROM intro_dados_prata.dados_meteorologicos)
				)/@NUM_CLASSES)
		) AS classe
		FROM intro_dados_prata.dados_meteorologicos
	UNION ALL
	SELECT
		datahora,
		3 AS metrica,
		temperatura AS valor,
		ROUND(
				(
					temperatura -
					(SELECT MIN(temperatura) FROM intro_dados_prata.dados_meteorologicos)
				)/(
				(
					(SELECT MAX(temperatura) FROM intro_dados_prata.dados_meteorologicos) -
					(SELECT MIN(temperatura) FROM intro_dados_prata.dados_meteorologicos)
				)/@NUM_CLASSES)
		) AS classe
		FROM intro_dados_prata.dados_meteorologicos
	UNION ALL
	SELECT
		datahora,
		4 AS metrica,
		temperatura_orvalho AS valor,
		ROUND(
				(
					temperatura_orvalho -
					(SELECT MIN(temperatura_orvalho) FROM intro_dados_prata.dados_meteorologicos)
				)/(
				(
					(SELECT MAX(temperatura_orvalho) FROM intro_dados_prata.dados_meteorologicos) -
					(SELECT MIN(temperatura_orvalho) FROM intro_dados_prata.dados_meteorologicos)
				)/@NUM_CLASSES)
		) AS classe
		FROM intro_dados_prata.dados_meteorologicos
	UNION ALL
	SELECT
		datahora,
		5 AS metrica,
		umidade AS valor,
		ROUND(
				(
					umidade -
					(SELECT MIN(umidade) FROM intro_dados_prata.dados_meteorologicos)
				)/(
				(
					(SELECT MAX(umidade) FROM intro_dados_prata.dados_meteorologicos) -
					(SELECT MIN(umidade) FROM intro_dados_prata.dados_meteorologicos)
				)/@NUM_CLASSES)
		) AS classe
		FROM intro_dados_prata.dados_meteorologicos
	UNION ALL
	SELECT
		datahora,
		6 AS metrica,
		vento_direcao AS valor,
		ROUND(
				(
					vento_direcao -
					(SELECT MIN(vento_direcao) FROM intro_dados_prata.dados_meteorologicos)
				)/(
				(
					(SELECT MAX(vento_direcao) FROM intro_dados_prata.dados_meteorologicos) -
					(SELECT MIN(vento_direcao) FROM intro_dados_prata.dados_meteorologicos)
				)/@NUM_CLASSES)
		) AS classe
		FROM intro_dados_prata.dados_meteorologicos
	UNION ALL
	SELECT
		datahora,
		7 AS metrica,
		vento_rajada AS valor,
		ROUND(
				(
					vento_rajada -
					(SELECT MIN(vento_rajada) FROM intro_dados_prata.dados_meteorologicos)
				)/(
				(
					(SELECT MAX(vento_rajada) FROM intro_dados_prata.dados_meteorologicos) -
					(SELECT MIN(vento_rajada) FROM intro_dados_prata.dados_meteorologicos)
				)/@NUM_CLASSES)
		) AS classe
		FROM intro_dados_prata.dados_meteorologicos
	UNION ALL
	SELECT
		datahora,
		8 AS metrica,
		vento_velocidade AS valor,
		ROUND(
				(
					vento_velocidade -
					(SELECT MIN(vento_velocidade) FROM intro_dados_prata.dados_meteorologicos)
				)/(
				(
					(SELECT MAX(vento_velocidade) FROM intro_dados_prata.dados_meteorologicos) -
					(SELECT MIN(vento_velocidade) FROM intro_dados_prata.dados_meteorologicos)
				)/@NUM_CLASSES)
		) AS classe
		FROM intro_dados_prata.dados_meteorologicos
) resultado
