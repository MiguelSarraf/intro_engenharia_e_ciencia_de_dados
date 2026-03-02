# Preparação

O processo de preparação se baseia em coletar as duas entradas geradas pela camada de ingestão e processá-las para estarem limpas, formatadas e normalizadas dentro do banco de dados de saída.

O banco de dados é instanciado pelo Makefile durante o comando `make env` rodado no processo base do repositório.

Diferentemente da forma abordado no curso, aqui aplicamos as sub-etapas da preparação na ordem: Normalização; Preparação; Limpeza. Com isso, simplificamos as tratativas necessárias em cada camada.

Uma vez que a ingestão esteja completa, podemos executar rapidamente a preparação através do comando:

```
make prepara
```

A formatação de todas as tabelas finais, de ambas as entradas, é feita através de uma função única que verifica e formata cada campo de acordo com [dicionários específicos para cada tipo](https://github.com/MiguelSarraf/intro_engenharia_e_ciencia_de_dados/blob/3d4c25bffc9b693abcf7f27e91c01f31abe18d44/prepara%C3%A7%C3%A3o/constantes.py#L98-L206).

Abaixo, estão descritos, sucintamente, todos os procedimentos aplicados sobre os arquivos de entrada.

## Monitoramento do sistema

As informações principais dessa entrada são os dados coletados do sistema que variam ao longo do tempo.

Não obstante, o arquivo de entrada também mostra informações constantes da máquina (como número de CPUs e tamanho da memória) e a janela a que cada linha corresponde.

Podemos simplificar nosso esquema de banco de dados para a FN2 removendo, para uma tabela apartada, os parâmetros fixos da máquina. Como nosso caso de uso é ainda mais simples, pois usamos máquinas locais para execução (logo, não haverá mais de uma configuração de máquina), salvaremos estes valores fixos no formato chave-valor. O conjuto de valores fixos considerados, com seus nomes traduzidos está disponível [aqui](https://github.com/MiguelSarraf/intro_engenharia_e_ciencia_de_dados/blob/3d4c25bffc9b693abcf7f27e91c01f31abe18d44/prepara%C3%A7%C3%A3o/constantes.py#L3-L34).

Como a coluna janela depende da estampa de tempo, podemos realizar um mapeamento temporal entre o começo e o fim de cada janela. Assim, devemos reduzir o nosso esquema para a FNDC.

As colunas restante do arquivo dependem única e exclusivamente da estampa de tempo e, assim, estão completamente normalizadas. O mapeamento dessas colunas om seus nomes traduzidos está disponível [aqui](https://github.com/MiguelSarraf/intro_engenharia_e_ciencia_de_dados/blob/3d4c25bffc9b693abcf7f27e91c01f31abe18d44/prepara%C3%A7%C3%A3o/constantes.py#L36-L69)

Para limpeza desses dados, são removidos os valores nulos da tabela de parâmetros fixos e removidas as linhas de informações do sistema com estampa de tempo nula. Para os valores vazios de informação do sistema, é feito um preenchimento com o último valor não vazio.

## Condições meteorológicas

Essa tabela mostra os parâmetros horários das condições do clima na cidade.

As tabela já respeita a FN2, pois todos os atributos dependem da chave primária, o par data-hora, mas existe uma mistura de funções.

Há campos relativos a medições pontuais e campos que registram os valores máximos e mínimos de alguns atributos para a hora anterior. Isso fere a FN3 e, para corrigir, é preciso separar aquilo que é medição pontual do que é valores extremos.

Fora isso, as tabelas estão completamente normalizadas. O mapeamento dessas colunas om seus nomes traduzidos está disponível [aqui](https://github.com/MiguelSarraf/intro_engenharia_e_ciencia_de_dados/blob/3d4c25bffc9b693abcf7f27e91c01f31abe18d44/prepara%C3%A7%C3%A3o/constantes.py#L71-L94)

Para limpeza, simplesmente se excluem as linhas onde há valores nulos, pois eles mostram erros na fonte de dados. A única exceção à essa regra é o campo de radiação solar, pois a ausência de valores representa um período noturno e podem ser substituídos por 0.
