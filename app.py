#Rodar local -> streamlit run "C:\Users\Thiag\OneDrive\Desktop\Projetos\Projetos para evoluir\Interconnected\Global_Economy_Indicators\Dataset\app\app.py"

# ==============================================================================
# 1. Imports and initial settings
# ==============================================================================
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

# Import dataframe of structure dataset
@st.cache_data
def carregar_dados():
    df = pd.read_csv("dados_economia_estruturado.csv")
    return df
df = carregar_dados()


# Set layout url_page
st.set_page_config(
                    layout="wide",
                    page_icon= '📊',
                    page_title= 'Anatomy of global prosperity'
                )

# ==============================================================================
# 2. Formatting and data functions
# ==============================================================================

# Formatting numeric data
def formatar_numero(value, precision=1):
    # Check if type is in my group
    if not isinstance(value, (int, float, np.number)):
        return value 
    signal = ''
    if value < 0:
        signal = '-'
        value = abs(value)

    if value >= 1_000_000_000_000:
        format_value = value / 1_000_000_000_000
        suffix = 'Tri'
    elif value >= 1_000_000_000:
        format_value = value / 1_000_000_000
        suffix = 'Bi'
    elif value >= 1_000_000:
        format_value = value / 1_000_000
        suffix = 'Mi'
    elif value >= 1_000:
        format_value = value / 1_000
        suffix = 'k' # kilo (thousand)
    else:
        return f'{signal}{value:,.0f}'
    
    return f'{signal}{format_value:,.{precision}f} {suffix}'

# ==============================================================================
# 3. Sidebar and filters (Users inputs)
# ==============================================================================

st.sidebar.markdown(f"🔎 {len(df['country'].unique())} countries analyzed")

#Create the header for the filters
st.sidebar.header("📌 Filters",divider="grey")

# --- CONTINENT FILTER ---
# Create the list of unique continents and sort
continent_list = sorted(df['Continent'].unique())
options_selectbox_continents = ['Global'] + continent_list
# Create the selector continent
continent_filter = st.sidebar.selectbox(
    label="Select continent",
    options=options_selectbox_continents
)
# Condition for global selector, because was not original in dataset
if continent_filter == 'Global':
    df_continent = df.copy()
else:
    df_continent = df[df['Continent'] == continent_filter]

# --- YEAR FILTER ---
# Create year slider
selected_year = st.sidebar.slider(
    "Select year",
    min_value=int(df['year'].min()),
    max_value=int(df['year'].max())
)

st.sidebar.markdown("---")

# --- Professional assign and link ---

# HTML code to direct to my link
st.sidebar.markdown(
    """
    <div style="text-align: center; font-size: 12px; color: grey;">
        <p>Designed by Thiago Prochnow Borges</p>
        <a href="https://www.linkedin.com/in/thiagopborges" target="_blank">LinkedIn</a> | 
        <a href="https://github.com/ThiagoPBorges" target="_blank">GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)

# ==============================================================================
# 4. Logic and calculations (Back-end)
# ==============================================================================

# --- Ranking calculations (related only for year) ---
df_filter_year = df_continent[df_continent['year'] == selected_year]

resumos_decadas = {
    1970: "Marked by the Oil Crisis and the stagflation in Western economies, with the growth of exporting powers as a Japan.",
    1980: "The decade of cold war late, debt crisis into South America and the beginning of economy opening of China.",
    1990: "Defined by globalization post-cold war , the boom of tecnology (bubble 'dot com') and the reestructure of economies in the east European.",
    2000: "Started with the explosion of the internet bubble, follow by global strong growth driven by commodities and by rise of China. Finished with financial crisis of 2008.",
    2010: "The decade of slow recovery post-2008, rise of social media, comercial tensions between USA and China, and the beginning of new era of technological globalization.",
    2020: "Started by COVID-19 pandemic, that causes a disruption unprecedented in suply chains and global economies."
}


# ==============================================================================
# 5. Layout and visual dashboard (Front-end)
# ==============================================================================

coltitle,colmap  = st.columns(2)

with coltitle:
    st.title("🌎 Anatomy of Global Prosperity")
    # --- Session of history context ---
    # Get the year selected (ex: 1985) and transform this into a decade (1980)
    select_decade = (selected_year // 10) * 10 

    # Show the summary of decade
if select_decade in resumos_decadas:
    st.write(f"**📚 Context of the decade {select_decade}:** {resumos_decadas[select_decade]}")
st.markdown("---")

with colmap:
    fig_map = px.choropleth(
        data_frame=df_filter_year,
        locations='country',
        locationmode='country names',
        color='prosperity_score',
        color_continuous_scale='Blues',
        projection='natural earth',
        hover_name='country',
        hover_data={'prosperity_score': ':.3f', 'population': ':.0f', 'per capita': ':.2f'}
    )
    fig_map.update_geos(
    lataxis_range=[-90, 90], # Limita o arrasto vertical
    lonaxis_range=[-180, 180] # Limita o arrasto horizontal
    )
    fig_map.update_layout(
        height=300,
        margin={"r":0,"t":5,"l":0,"b":0}
        )
        
st.plotly_chart(fig_map, use_container_width=True)


# ==============================================================================
# 5. Create tabs
# ==============================================================================
tab1, tab2 = st.tabs(["Overview & Rankings", "Individual Analysis"])

with tab1:

    st.header(f"Rankings of prosperity for year {selected_year}", divider="grey")

    top_5_best = df_filter_year.sort_values(by="prosperity_score", ascending=False).head(5)
    top_5_worst = df_filter_year.sort_values(by="prosperity_score", ascending=True).head(5)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏆 Top 5 countries highest prosperity score")
        st.dataframe(top_5_best[['country', 'prosperity_score']])

    with col2:
        st.subheader("📉 Top 5 countries least prosperity score")
        st.dataframe(top_5_worst[['country', 'prosperity_score']])

    st.info(
            """
            **About the prosperity_score**

            This score is calculated based on the median of several key indicators:
            * Gross capital formation
            * Exports of goods and services
            * Imports of goods and services
            * Household consumption expenditure
            * Agriculture, hunting, forestry, fishing
            * Mining, manufacturing, utilities
            """
        )


with tab2:
    st.header("Individual Analysis", divider="grey")

    # --- COUNTRY FILTER ---
    # Create the list of unique countries and sort
    country_list = sorted(df_continent['country'].unique())
    # Added "Global" option to the top of list
    options_selectbox_country = ['Global'] + country_list

    # Create country selector
    country_filter = st.selectbox(
        label="Select country",
        options=options_selectbox_country
    )

    # Set dataframe for Global option
    if country_filter == 'Global':
        df_filtrado_raw = df_continent.groupby('year').agg(
            population=('population', 'sum'),
            prosperity_score=('prosperity_score', 'mean'),
            per_capita=('per capita', 'mean'),
            imports_of_goods_and_services=('imports of goods and services', 'sum'),
            exports_of_goods_and_services=('exports of goods and services', 'sum')
        ).reset_index()

    else:
        # Raw/original dataframe
        df_filtrado_raw = df_continent[df_continent['country'] == country_filter]

    # Variables for current and previous date
    data_current_year = df_filtrado_raw[df_filtrado_raw['year'] == selected_year]
    data_previous_year = df_filtrado_raw[df_filtrado_raw['year'] == selected_year - 1]

    # Avoid errors if it does not exist
    score_current, pc_current, pop_current, export_current, imports_current, trade_balance = 0, 0, 0, 0, 0, 0
    delta_score, delta_pc, delta_pop, delta_export, delta_imports, delta_trade_balance = 0, 0, 0, 0, 0, 0


    if not data_current_year.empty:
        # Columns was renamed in the aggregation, so we need to check both possible names
        pc_col_name = 'per_capita' if 'per_capita' in data_current_year.columns else 'per capita'
        imports_col_name = 'imports_of_goods_and_services' if 'imports_of_goods_and_services' in data_current_year.columns else 'imports of goods and services'
        exports_col_name = 'exports_of_goods_and_services' if 'exports_of_goods_and_services' in data_current_year.columns else 'exports of goods and services'

        # Get the values of current year
        score_current = data_current_year['prosperity_score'].iloc[0]
        pc_current = data_current_year[pc_col_name].iloc[0]
        pop_current = data_current_year['population'].iloc[0]
        export_current = data_current_year[exports_col_name ].iloc[0]
        imports_current = data_current_year[imports_col_name].iloc[0]
        trade_balance = export_current - imports_current

    if not data_previous_year.empty:
        # Columns was renamed in the aggregation, so we need to check both possible names
        pc_col_name_pre = 'per_capita' if 'per_capita' in data_previous_year.columns else 'per capita'
        imports_col_name_pre = 'imports_of_goods_and_services' if 'imports_of_goods_and_services' in data_previous_year.columns else 'imports of goods and services'
        exports_col_name_pre = 'exports_of_goods_and_services' if 'exports_of_goods_and_services' in data_previous_year.columns else 'exports of goods and services'
        

        # Get the values of previous year
        score_previous = data_previous_year['prosperity_score'].iloc[0]
        pc_previous = data_previous_year[pc_col_name_pre].iloc[0]
        pop_previous = data_previous_year['population'].iloc[0]
        export_previous = data_previous_year[exports_col_name_pre].iloc[0]
        imports_previous = data_previous_year[imports_col_name_pre].iloc[0]
        
        # Calculation of deltas
        delta_score = score_current - score_previous
        delta_pc = pc_current - pc_previous
        delta_pop = pop_current - pop_previous
        delta_export = export_current - export_previous
        delta_import = imports_current - imports_previous
        delta_trade_balance = trade_balance - (export_previous - imports_previous)


    if not data_current_year.empty:
        
        col1,col2,col3,col4 = st.columns(4)

        with col1:
            st.metric(
                label="Population",
                value=formatar_numero(pop_current, precision=2),
                delta=formatar_numero(delta_pop, precision=2),
                help= "Total population for the selected scope and year."
            )
        with col2:
            st.metric(
                label="Prosperity Score",
                value=f"{score_current:.6f}",
                delta=f"{delta_score:.6f}",
                help="Calculated prosperity index (0-1 scale)."
            )
        with col3:
                st.metric(
                label="Per Capita (USD)",
                value=f"$ {formatar_numero(pc_current, precision=2)}",
                delta=formatar_numero(delta_pc, precision=2),
                help="Gross National Income per person (average income)."
            )
        with col4:
            st.metric(
                label="Trade Balance (USD)",
                value=f"$ {formatar_numero(trade_balance, precision=2)}",
                delta=formatar_numero(delta_trade_balance, precision=2),
                help="Exports - Imports"
            )



        # --- Line graph and raw data---
        st.subheader("Evolution of indicators")

        # --- Logic for create the index data---
        df_index = df_filtrado_raw[['year', 'population', 'per_capita', 'prosperity_score']].copy()

        # get the first year of data
        primeiro_ano_df = df_index.iloc[0]

        # Loop for divide each column by her value in year
        for col in ['population', 'per_capita', 'prosperity_score']:
            df_index.loc[:, col] = (df_index[col] / primeiro_ano_df[col]) * 1

        # --- Displays the Indexed graphic ---
        st.line_chart(data=df_index.set_index('year'))

        # Below the graph, the dataframe was set in an expander
        with st.expander("Click to view raw data for the selected year"):
            if country_filter == 'Global':
                st.dataframe(df_filtrado_raw)
                
            else:
                st.dataframe(df_filtrado_raw.iloc[:,:-14])
