# Enriquecimento

A camada de enriquecimento visa preparar os dados e tabelas para as camadas posteriores do fluxo de vida do dado, i.e. visualização e inteligência.

Para a camada de visualização, foi montado o protótipo de dashboard abaixo:

![Protótipo de dashboard com dois filtros, datahora e métrica, 7 cards de KPIs explicitando os parâmetros da mauina que foi monitorada, um gráfico de linha com o valor da métrica selecionada por datahora, um histograma da métrica selecionada, um gráfico de linha da temperatura geral da cpu por datahora e um gráfico de dispersão da temperatura geral da cpu pela métrica selecionada.](https://github.com/MiguelSarraf/intro_engenharia_e_ciencia_de_dados/blob/main/enriquecimento/prototipo_relatorio.png)

Para a camada de inteligência, será necessária uma tabela com todas as informações coletadas da máquina pareadas com todos os dados do clima ingeridos do INMET.

Com essas necessidades, foi gerado o seguinte diagrama de pé de galinha com as tabelas que precisam estar na camada ouro:

![Diagrama de banco de dados com 2 tabelas dimensão, listando as metricas e listando as datas disponíveis, e 3 tabelas fato, uma listando os parâmetros da máquina, uma relacionando as metricas a cada hora e uma listando todos os parâmetros de máquina e de clima para cada hora.](https://github.com/MiguelSarraf/intro_engenharia_e_ciencia_de_dados/blob/main/enriquecimento/esquema_tabelas_ouro.png)

Alguns valores estão duplicados entre as tabelas, mas isso não consititui um problema, pois eles serão utilizados em cenários distintos.

Para execução de todos os scripts de enriquecimento dos dados, basta rodar a receita do Makefile:

```make enriquece```

Cada um dos processacementos específicos, está explicado abaixo.

## Dimensão metrica

A dimensão de métricas foi criada manualmente, atribuindo um identificador numérico único para cada campo e associando com um texto em português descritivo.

## Dimensão datahora

A dimensão de datahora foi criada selecionando todas as datas presentes na tabelas de dados meteorologicos da camada prata e extraindo os valores de ano, mes, dia e hora delas.

## Fato dados_maquina

A tabela fato com os dados da máquina é uma cópia exata da tabela homônima na camada prata.

## Fato clima_hora

A tabela fato com os dados climáticos foi criada realizando a união de 9 selects individuais separando cada uma das métrica coletadas por hora.

## Fato maquina_clima

A tabela fato que correlaciona as medições da máquina com os dados do clima foi gerada fazendo-se um inner join entre a tabela de dados meteorológicos com a tabela de informações do sistema agrupada por hora.
