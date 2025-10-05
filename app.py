# ==============================================================================
# 1. IMPORTAÇÕES E CONFIGURAÇÕES INICIAIS
# ==============================================================================
import streamlit as st
import pandas as pd

# streamlit run app.py

#Configura o layout para ficar tela cheia
st.set_page_config(layout="wide")

# ==============================================================================
# 2. FUNÇÕES DE LÓGICA E DADOS
# ==============================================================================
@st.cache_data
def carregar_dados():
    df = pd.read_csv("dados_economia_estruturado.csv")
    return df
df = carregar_dados()

# ==============================================================================
# 2. BARRA LATERAL E FILTROS (INPUTS DO USUÁRIO)
# (Tudo que o usuário pode interagir fica agrupado aqui)
# ==============================================================================

#Cria o cabeçalho para os filtros
st.sidebar.header("Filters")

# Cria o seletor de pais
country_filter = st.sidebar.selectbox(  
    label="Select country",options=sorted(df['country'].unique())
)

# Cria o slider de ano
ano_selecionado = st.sidebar.slider(
    "Select year",
    min_value=int(df['year'].min()),
    max_value=int(df['year'].max())
)

# ==============================================================================
# 3. LÓGICA E CÁLCULOS (O "BACK-END" DO DASHBOARD)
# ==============================================================================

# --- DataFrames filtrados ---
df_filtrado = df[df['year'] == ano_selecionado]
df_filtrado_raw = df[df['country'] == country_filter]

# --- Cálculos para os Rankings ---
top_10_maiores = df_filtrado.sort_values(by="prosperity_score", ascending=False).head(10)
top_10_menores = df_filtrado.sort_values(by="prosperity_score", ascending=True).head(10)

# --- PEGAR OS VALORES DO ANO ATUAL E ANTERIOR ---
dados_ano_atual = df_filtrado_raw[df_filtrado_raw['year'] == ano_selecionado]
dados_ano_anterior = df_filtrado_raw[df_filtrado_raw['year'] == ano_selecionado - 1]

# Pega os valores específicos do ano atual
# .iloc[0] é usado para pegar o primeiro (e único) valor da seleção
score_atual = dados_ano_atual['prosperity_score'].iloc[0]
pc_atual = dados_ano_atual['per capita'].iloc[0]
pop_atual = dados_ano_atual['population'].iloc[0]

if not dados_ano_anterior.empty:
    # Pega os valores específicos do ano atual
    # .iloc[0] é usado para pegar o primeiro (e único) valor da seleção
    score_anterior = dados_ano_anterior['prosperity_score'].iloc[0]
    pc_anterior = dados_ano_anterior['per capita'].iloc[0]
    pop_anterior = dados_ano_anterior['population'].iloc[0]

    delta_score = score_atual - score_anterior
    delta_pc = pc_atual - pc_anterior
    delta_pop = pop_atual - pop_anterior
else:
    delta_score = 0
    delta_pc = 0
    delta_pop = 0

# ==============================================================================
# 4. LAYOUT E EXIBIÇÃO DO DASHBOARD (A PÁGINA PRINCIPAL "FRONT-END")
# (Agora, apenas usamos os resultados dos cálculos para "desenhar" a página)
# ==============================================================================

st.title("Anatomy of global prosperity")
st.header("Full Dataset Overview", divider="grey", anchor=None)

#Create for divide my screen in two parts
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Top 10 countrys highest prosperity score")
    st.dataframe(top_10_maiores[['country', 'prosperity_score']])

with col2:
    st.subheader("📉 Top 10 countrys least prosperity score")
    st.dataframe(top_10_menores[['country', 'prosperity_score']])

# --- DADOS BRUTOS EM UM EXPANSOR ---
st.markdown("---")

col1,col2,col3 = st.columns(3)

with st.expander("Click to view raw data for the selected year"):
    with col1:
        st.metric(
            label="Prosperity score",
            value=f"{score_atual:.6f}",
            delta=f"{delta_score:.6f}"
        )
    with col2:
        st.metric(
            label="Per capita score (USD)",
            value=f"${pc_atual:,}",
            delta= delta_pc
        )
    with col3:
        st.metric(
            label="Population score",
            value=f"{pop_atual:,}",
            delta=f"{delta_pop:,}"
        )
    st.dataframe(df_filtrado_raw)
    st.line_chart(df_filtrado_raw.set_index('year')[['population']])
