INSERT INTO intro_dados_ouro.dim_metrica (id, nome) VALUES (0, "Precipitação");
INSERT INTO intro_dados_ouro.dim_metrica (id, nome) VALUES (1, "Pressão ATM");
INSERT INTO intro_dados_ouro.dim_metrica (id, nome) VALUES (2, "Radiação");
INSERT INTO intro_dados_ouro.dim_metrica (id, nome) VALUES (3, "Temperatura");
INSERT INTO intro_dados_ouro.dim_metrica (id, nome) VALUES (4, "Temperatura de orvalho");
INSERT INTO intro_dados_ouro.dim_metrica (id, nome) VALUES (5, "Umidade");
INSERT INTO intro_dados_ouro.dim_metrica (id, nome) VALUES (6, "Direção do vento");
INSERT INTO intro_dados_ouro.dim_metrica (id, nome) VALUES (7, "Rajada do vento");
INSERT INTO intro_dados_ouro.dim_metrica (id, nome) VALUES (8, "Velocidade do vento");

INSERT INTO intro_dados_ouro.dim_datahora (datahora, mes, ano, hora)
SELECT datahora, MONTH(datahora) as mes, YEAR(datahora) as ano, HOUR(datahora) as hora FROM intro_dados_prata.dados_meteorologicos;
