INSERT INTO intro_dados_ouro.maquina_clima (
	datahora,
	precipitacao,
	pressao_atm,
	radiacao,
	temperatura,
	temperatura_orvalho,
	umidade,
	vento_direcao,
	vento_rajada,
	vento_velocidade,
	temperatura_cpu_geral
)
SELECT
	datahora,
        precipitacao,
        pressao_atm,
        radiacao,
        temperatura,
        temperatura_orvalho,
        umidade,
        vento_direcao,
        vento_rajada,
        vento_velocidade,
        temperatura_cpu_geral
FROM intro_dados_prata.dados_meteorologicos dm
INNER JOIN (
    SELECT estampa_de_tempo,
           AVG(temperatura_cpu_geral) AS temperatura_cpu_geral
    FROM (
        SELECT DATE_FORMAT(estampa_de_tempo, '%Y-%m-%d %H:00:00') AS estampa_de_tempo,
               temperatura_cpu_geral
        FROM intro_dados_prata.info_sistema
    ) r
    GROUP BY estampa_de_tempo
) sys
ON dm.datahora = sys.estampa_de_tempo;
