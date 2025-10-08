# 🌎 Anatomia da Prosperidade Global: Uma Análise de Indicadores Econômicos

## 📜 Visão Geral do Projeto

Este projeto de análise de dados de ponta a ponta (*end-to-end*) investiga um dataset de indicadores econômicos globais para decifrar os fatores que definem a prosperidade de uma nação.

Utilizando um pipeline de ferramentas padrão do mercado (**SQL**, **Python** e **Power BI/Streamlit**), o projeto demonstra o ciclo completo de análise: desde a extração e estruturação dos dados, passando pela limpeza e engenharia de features, até a apresentação dos resultados em dashboards interativos e uma aplicação web.

---

## 🎯 Questões de Negócio Orientadoras

A análise foi guiada para responder às seguintes questões:

1.  **Perfil do País Próspero:** Quais são as características comuns das nações nos extremos de prosperidade?
2.  **Relações entre Indicadores:** Como métricas de população, investimento e comércio se correlacionam com a riqueza per capita?
3.  **Índice de Prosperidade:** É possível criar um score unificado que meça a prosperidade de forma mais holística do que apenas a renda?
4.  **Evolução Histórica:** Como a jornada da prosperidade de diferentes países e regiões se desenrolou ao longo do tempo?

---

## 🛠️ Metodologia e Ferramentas Utilizadas

O projeto foi dividido em três fases, simulando um ambiente de análise de dados profissional.

### Fase 1: 🗃️ SQL - Engenharia e Estruturação de Dados

* **Objetivo:** Transformar os dados brutos em um banco de dados relacional, limpo e pronto para a análise.
* **Ações Chave:**
    * **ETL:** Carregamento dos dados em uma tabela de staging no SQL Server.
    * **Modelagem de Dados:** Resolução de problemas de formatação e tratamento de valores nulos.
    * **Enriquecimento de Dados:** Utilização de `JOIN` para fundir a tabela principal com dados geográficos (continentes).
* **Habilidades Demonstradas:** `SQL`, `Modelagem de Dados`, `Processos de ETL`, `JOIN`.

### Fase 2: 🐍 Python - Limpeza, Análise e Engenharia de Features

* **Objetivo:** Realizar uma análise exploratória profunda (EDA), tratar anomalias complexas e criar a principal métrica do projeto, o "Índice de Prosperidade".
* **Ações Chave:**
    * **Análise Exploratória (EDA):** Investigação de rankings (Top/Bottom 10), análise de tendências temporais (`Matplotlib`/`Seaborn`) e criação de uma matriz de correlação.
    * **Limpeza Avançada:** Tratamento de anomalias baseadas em contexto histórico (ex: países "(Former)") e problemas de qualidade de dados.
    * **Engenharia de Features:** Criação de métricas `per capita` e desenvolvimento de um "Índice de Prosperidade" customizado.
* **Habilidades Demonstradas:** `Python`, `Pandas`, `Análise Exploratória de Dados (EDA)`, `Engenharia de Features`, `Storytelling com Dados`.

### Fase 3: 📊 Visualização Interativa (Power BI & Streamlit)

* **Objetivo:** Apresentar os insights da análise em duas plataformas distintas, demonstrando versatilidade na comunicação de dados.

#### Power BI - Business Intelligence e Storytelling
* **Ações Chave:**
    * **ETL com Power Query:** Validação de tipos de dados e transformações.
    * **Criação de Medidas (DAX):** Desenvolvimento de KPIs dinâmicos (ex: `Total de Países = DISTINCTCOUNT(...)`).
    * **Design de Dashboard:** Construção de uma interface interativa com filtros, gráficos, mapas e KPIs.
* **Habilidades Demonstradas:** `Business Intelligence (BI)`, `Power Query`, `DAX`, `Design de Dashboards`.

#### Streamlit - Desenvolvimento de Aplicações de Dados
* **Ações Chave:**
    * **Desenvolvimento da Interface:** Criação de um layout web customizado com múltiplas abas (`st.tabs`), colunas e uma barra lateral.
    * **Interatividade Avançada:** Implementação de widgets e filtros dependentes (país dependente do continente).
    * **Visualização Dinâmica:** Exibição de KPIs com deltas (`st.metric`), rankings e gráficos (`Plotly Express`) que reagem em tempo real.
* **Habilidades Demonstradas:** `Streamlit`, `UI/UX para Dashboards`, `Desenvolvimento Web com Python`, `Deploy de Aplicações`.

---

## 💡 Principais Insights Descobertos

* A **prosperidade per capita** está predominantemente concentrada em nações pequenas com economias especializadas, enquanto as **nações menos prósperas** são marcadas por instabilidade crônica.
* Existe uma diferença fundamental entre **Poder Econômico Absoluto** e **Prosperidade Per Capita**, uma nuance que a criação de um índice com métricas per capita ajudou a esclarecer.
* A análise histórica revelou como **eventos geopolíticos e crises humanitárias** se refletem diretamente nos dados, reforçando a necessidade de análise contextual.

---

## 🚀 Produto Final: Os Dashboards Interativos

A análise completa foi apresentada em duas plataformas interativas.

### Dashboard Power BI:
<img width="1378" height="771" alt="image" src="https://github.com/user-attachments/assets/34a20fbb-4f56-4a61-9b0b-0007a685ca7d" />

### Aplicação Web Streamlit:
<img width="1919" height="938" alt="Streamlit_app" src="https://github.com/user-attachments/assets/e8bab001-721a-4956-b1f7-54a0badfdab5" />


### **Acesse as ferramentas ao vivo:**
➡️ **[Aplicação Web Streamlit](https://thiago-borges-anatomy-of-global-indicators.streamlit.app/)** *(Adicione o link do Power BI publicado aqui, se tiver)*

---

## 🔮 Próximos Passos (Future Work)

* **Machine Learning:** Aplicar algoritmos de clusterização (como K-Means) para segmentar os países em perfis econômicos de forma automática.
* **Análise Preditiva:** Utilizar modelos de séries temporais para prever a trajetória futura do Índice de Prosperidade.
