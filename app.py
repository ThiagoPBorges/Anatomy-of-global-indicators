#Rodar local -> streamlit run "C:\Users\Thiag\OneDrive\Desktop\Projetos\Projetos para evoluir\Interconnected\Global_Economy_Indicators\Dataset\app\app.py"

# ==============================================================================
# 1. IMPORTAÇÕES E CONFIGURAÇÕES INICIAIS
# ==============================================================================
import streamlit as st
import pandas as pd
import numpy as np

#Configura o layout para ficar tela cheia
st.set_page_config(layout="wide")

# ==============================================================================
# 2. FUNÇÕES DE LÓGICA E DADOS
# ==============================================================================

def formatar_numero(valor, precisao=1):
    # A MUDANÇA ESTÁ AQUI: Adicionamos np.number para aceitar tipos do NumPy
    if not isinstance(valor, (int, float, np.number)):
        return valor 

    sinal = ''
    if valor < 0:
        sinal = '-'
        valor = abs(valor)

    if valor >= 1_000_000_000:
        valor_formatado = valor / 1_000_000_000
        sufixo = 'Bi'
    elif valor >= 1_000_000:
        valor_formatado = valor / 1_000_000
        sufixo = 'Mi'
    elif valor >= 1_000:
        valor_formatado = valor / 1_000
        sufixo = 'mil'
    else:
        return f'{sinal}{valor:,.0f}'
    
    return f'{sinal}{valor_formatado:,.{precisao}f} {sufixo}'

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

# Cria a lista de países únicos e a ordena
lista_paises = sorted(df['country'].unique())

# Adiciona a opção "Global" no início da lista
opcoes_selectbox = ['Global'] + lista_paises

# Cria o seletor de pais
country_filter = st.sidebar.selectbox(
    label="Select country",
    options=opcoes_selectbox
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

# --- Cálculos para os Rankings (baseado apenas no ano) ---
df_filtrado_ano = df[df['year'] == ano_selecionado]
top_10_maiores = df_filtrado_ano.sort_values(by="prosperity_score", ascending=False).head(5)
top_10_menores = df_filtrado_ano.sort_values(by="prosperity_score", ascending=True).head(5)

if country_filter == 'Global':
    # --- CAMINHO GLOBAL: Agrega os dados de todos os países por ano ---
    df_filtrado_raw = df.groupby('year').agg(
        population=('population', 'sum'),
        per_capita=('per capita', 'mean'),
        prosperity_score=('prosperity_score', 'mean'),
        imports_of_goods_and_services=('imports of goods and services', 'sum'),
        exports_of_goods_and_services=('exports of goods and services', 'sum')
    ).reset_index()

else:
    # --- CAMINHO PAÍS: Filtra para o país selecionado (lógica original) ---
    df_filtrado_raw = df[df['country'] == country_filter]

# --- OBTENÇÃO DOS DADOS PARA O ANO ATUAL E ANTERIOR (unificado) ---
dados_ano_atual = df_filtrado_raw[df_filtrado_raw['year'] == ano_selecionado]
dados_ano_anterior = df_filtrado_raw[df_filtrado_raw['year'] == ano_selecionado - 1]

# --- CÁLCULO DAS MÉTRICAS E DELTAS (unificado) ---
# Inicializa as variáveis para evitar erros se não houver dados
score_atual, pc_atual, pop_atual, export_atual, imports_atual, trade_balance = 0, 0, 0, 0, 0, 0
delta_score, delta_pc, delta_pop, delta_export, delta_imports, delta_trade_balance = 0, 0, 0, 0, 0, 0

if not dados_ano_atual.empty:
    # Renomeamos as colunas na agregação, então precisamos verificar os dois nomes possíveis
    pc_col_name = 'per_capita' if 'per_capita' in dados_ano_atual.columns else 'per capita'
    imports_col_name = 'imports_of_goods_and_services' if 'imports_of_goods_and_services' in dados_ano_atual.columns else 'imports of goods and services'
    exports_col_name = 'exports_of_goods_and_services' if 'exports_of_goods_and_services' in dados_ano_atual.columns else 'exports of goods and services'

    # Pega os valores do ano atual
    score_atual = dados_ano_atual['prosperity_score'].iloc[0]
    pc_atual = dados_ano_atual[pc_col_name].iloc[0]
    pop_atual = dados_ano_atual['population'].iloc[0]
    export_atual = dados_ano_atual[exports_col_name].iloc[0]
    imports_atual = dados_ano_atual[imports_col_name].iloc[0]
    trade_balance = export_atual - imports_atual

if not dados_ano_anterior.empty:
    # Pega os valores do ano anterior
    pc_col_name_ant = 'per_capita' if 'per_capita' in dados_ano_anterior.columns else 'per capita'
    imports_col_name_ant = 'imports_of_goods_and_services' if 'imports_of_goods_and_services' in dados_ano_anterior.columns else 'imports of goods and services'
    exports_col_name_ant = 'exports_of_goods_and_services' if 'exports_of_goods_and_services' in dados_ano_anterior.columns else 'exports of goods and services'
    
    score_anterior = dados_ano_anterior['prosperity_score'].iloc[0]
    pc_anterior = dados_ano_anterior[pc_col_name_ant].iloc[0]
    pop_anterior = dados_ano_anterior['population'].iloc[0]
    export_anterior = dados_ano_anterior[exports_col_name_ant].iloc[0]
    imports_anterior = dados_ano_anterior[imports_col_name_ant].iloc[0]
    
    # Calcula os deltas
    delta_score = score_atual - score_anterior
    delta_pc = pc_atual - pc_anterior
    delta_pop = pop_atual - pop_anterior
    delta_export = export_atual - export_anterior
    delta_imports = imports_atual - imports_anterior
    delta_trade_balance = trade_balance - (export_anterior - imports_anterior)


# ==============================================================================
# 4. LAYOUT E EXIBIÇÃO DO DASHBOARD (A PÁGINA PRINCIPAL "FRONT-END")
# (Agora, apenas usamos os resultados dos cálculos para "desenhar" a página)
# ==============================================================================

num_paises = len(df['country'].unique())
st.markdown(
            f"**{num_paises}** países analisados"
            )

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

col1,col2,col3,col4 = st.columns(4)

with st.expander("Click to view raw data for the selected year"):
    with col1:
        st.metric(
            label="Population score",
            value=formatar_numero(pop_atual, precisao=2),
            delta=formatar_numero(delta_pop, precisao=2),
            help= "Quantity of people in the country"
        )
    with col2:
        st.metric(
            label="Prosperity score",
            value=f"{score_atual:.6f}",
            delta=f"{delta_score:.6f}",
            help="Ranking related to the country prosperity"
        )
    with col3:
        st.metric(
            label="Per capita score (USD)",
            value=f"${pc_atual:,}",
            delta= delta_pc
        )
    with col4:
        st.metric(
            label="Trade comercial (USD)",
            value=f"$ {formatar_numero(trade_balance, precisao=2)}",
            delta=formatar_numero(delta_trade_balance, precisao=2)
        )

    

   # --- GRÁFICO DE LINHA E DADOS BRUTOS ---
    st.subheader("Historical Data")

    # Ajusta as colunas do gráfico de linha para a visão Global
    if country_filter == 'Global':
        y = ["population", "per_capita", "prosperity_score"]
    else:
        y = ["population", "per capita", "prosperity_score"]

    st.line_chart(
        data=df_filtrado_raw.set_index('year'), # Usar 'year' como índice melhora a exibição
        y= y,
        use_container_width=True
    )
    if country_filter == 'Global':
        st.dataframe(df_filtrado_raw)
        
    else:
        st.dataframe(df_filtrado_raw.iloc[:,:-14])

    
