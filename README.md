Anatomia da Prosperidade Global: Uma Análise de Indicadores Econômicos

Visão Geral do Projeto
Este projeto de análise de dados de ponta a ponta (end-to-end) investiga um dataset de indicadores econômicos globais para decifrar os fatores que definem a prosperidade de uma nação. Utilizando um pipeline de ferramentas padrão do mercado (SQL, Python, Power BI e Streamlit), o projeto abrange desde a extração e estruturação inicial dos dados, passando pela limpeza e engenharia de features, até a apresentação dos resultados em dashboards interativos. O objetivo foi demonstrar o ciclo completo de análise, transformando dados brutos em insights acionáveis e narrativas de dados coesas em múltiplas plataformas.

Questões de Negócio Orientadoras
A análise foi guiada pelas seguintes questões:

Perfil do País Próspero: Quais são as características comuns das nações com os maiores e menores indicadores de prosperidade?

Relações entre Indicadores: Como diferentes métricas (população, investimento, comércio) se correlacionam com a riqueza per capita?

Índice de Prosperidade: É possível criar um score unificado que meça a prosperidade de forma mais holística do que apenas a renda?

Evolução Histórica: Como a jornada da prosperidade de diferentes países e regiões se desenrolou ao longo do tempo?

Metodologia e Ferramentas Utilizadas
Fase 1: SQL - Engenharia e Estruturação de Dados
Objetivo: Transformar os dados brutos em um banco de dados relacional, limpo e pronto para a análise.

Ações Chave:

ETL (Extração, Transformação e Carga): Carregamento dos dados em uma tabela de staging no SQL Server.

Limpeza e Modelagem de Dados: Resolução de problemas de formatação e tratamento de valores nulos.

Enriquecimento de Dados: Utilização de JOIN para fundir a tabela principal com uma tabela auxiliar de continentes.

Habilidades Demonstradas: SQL, Modelagem de Dados Relacional, Processos de ETL, JOIN.

Fase 2: Python - Limpeza, Análise e Engenharia de Features
Objetivo: Conectar ao banco de dados, realizar uma análise exploratória profunda (EDA), tratar anomalias complexas e criar a principal métrica do projeto, o "Índice de Prosperidade".

Ações Chave:

Conexão e Extração: Uso de SQLAlchemy e Pandas para extrair os dados do SQL Server.

Análise Exploratória (EDA): Investigação dos Top 10 e Bottom 10 países, análise de tendências temporais com Matplotlib/Seaborn e criação de uma matriz de correlação.

Limpeza Avançada: Tratamento de anomalias baseadas em contexto histórico (ex: países "(Former)") e problemas de qualidade de dados.

Engenharia de Features: Criação de métricas per capita e desenvolvimento de um "Índice de Prosperidade" customizado.

Habilidades Demonstradas: Python, Pandas, Análise Exploratória de Dados (EDA), Engenharia de Features, Storytelling com Dados, Análise Crítica.

Fase 3: Visualização e Apresentação Interativa (Power BI & Streamlit)
Objetivo: Apresentar os insights da análise em duas plataformas distintas, demonstrando versatilidade na comunicação de dados.

Sub-fase 3.1: Power BI - Business Intelligence e Storytelling

Ações Chave:

Conexão e Carga: Importação do CSV limpo para o Power BI, com validações no Power Query.

Criação de Medidas (DAX): Desenvolvimento de métricas de negócio usando DAX (Data Analysis Expressions) para criar KPIs dinâmicos (ex: Total de Países = DISTINCTCOUNT(Tabela[country])).

Design e Visualização: Construção de um dashboard com visuais interconectados (filtros, gráficos, mapas, KPIs) para permitir a exploração dos dados.

Habilidades Demonstradas: Business Intelligence (BI), Power Query, DAX, Design de Dashboards, Storytelling com Dados.

Sub-fase 3.2: Streamlit - Desenvolvimento de Aplicações de Dados

Ações Chave:

Desenvolvimento da Interface: Criação de um layout web customizado com múltiplas abas (st.tabs), colunas (st.columns) e uma barra lateral (st.sidebar).

Interatividade Avançada: Implementação de widgets (st.slider, st.selectbox) e filtros dependentes (país dependente do continente).

Visualização Dinâmica: Exibição de KPIs com deltas (st.metric), rankings e gráficos (incluindo a integração com Plotly Express para mapas interativos) que reagem em tempo real às seleções do usuário.

Habilidades Demonstradas: Streamlit, UI/UX para Aplicações de Dados, Desenvolvimento de Aplicações Web com Python, Publicação de Aplicações (Deploy).

Principais Insights Descobertos
A prosperidade per capita está predominantemente concentrada em nações pequenas com economias especializadas, enquanto as nações menos prósperas são marcadas por instabilidade crônica.

Existe uma diferença fundamental entre Poder Econômico Absoluto e Prosperidade Per Capita. A criação de um índice com métricas per capita foi crucial para capturar essa nuance.

A análise histórica de países específicos revelou como eventos geopolíticos e crises humanitárias se refletem diretamente nos dados, reforçando a necessidade de análise contextual.

Produto Final: Os Dashboards Interativos
O resultado final é uma análise completa apresentada em duas plataformas interativas.

Dashboard Power BI:
<img width="1378" height="771" alt="image" src="https://github.com/user-attachments/assets/34a20fbb-4f56-4a61-9b0b-0007a685ca7d" />


Aplicação Web Streamlit:
<img width="1919" height="938" alt="Streamlit_app" src="https://github.com/user-attachments/assets/e8bab001-721a-4956-b1f7-54a0badfdab5" />


Acesse as ferramentas ao vivo:

Link para o App Streamlit: https://thiago-borges-anatomy-of-global-indicators.streamlit.app/


Próximos Passos (Future Work)
Machine Learning: Aplicar algoritmos de clusterização (como K-Means) para segmentar os países em perfis econômicos de forma automática.

Análise Preditiva: Utilizar modelos de séries temporais para prever a trajetória futura do Índice de Prosperidade.
