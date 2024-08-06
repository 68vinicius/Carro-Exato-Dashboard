import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados
df = pd.read_csv('Data/dataset_reparos_2024.csv')

# Configurar página Streamlit
st.set_page_config(page_title='Dashboard Carro Exato')
st.markdown('<h1 style=\'text-align: center;\'>Diagnósticos e Manutenções</h1>', unsafe_allow_html=True)
st.image('https://github.com/68vinicius/Carro-Exato-Dashboard/raw/main/Imagens/CarroExatoBanner.jpg', caption='www.carroexato.com.br')
st.subheader('Explore os Detalhes das Manutenções de Maio')
st.markdown('Apresentamos uma variedade de manutenções recentes feitas pela Carro Exato, desde problemas comuns como falhas no motor até questões específicas como vazamentos de óleo. Convidamos você a explorar nossos dados e visualizar detalhes das manutenções realizadas.')

# Converter coluna de data
df['data'] = pd.to_datetime(df['data'], dayfirst=True)

# Filtrar apenas o mês de maio
df_maio = df[df['data'].dt.month == 5]

# KPIs
total_diagnosticos = df_maio.shape[0]
custo_total_pecas = df_maio['valor_peca'].sum()
custo_total_maodeobra = df_maio['valor_maodeobra'].sum()

col1, col2, col3 = st.columns(3)
col1.metric('Total de Serviços', total_diagnosticos)
col2.metric('Custo Total de Peças', f'R$ {custo_total_pecas}')
col3.metric('Custo Total de Mão de Obra', f'R$ {custo_total_maodeobra}')

diagnostico_contagem = df_maio['diagnostico'].value_counts()
diagnostico_mais_frequente = diagnostico_contagem.idxmax()
quantidade_diagnosticos = diagnostico_contagem.max()

def plotar_grafico_componentes(dados):
    fig, ax = plt.subplots(figsize=(12, 8))
    componentes_contagem = dados['troca_componente'].value_counts()
    wedges, texts, autotexts = ax.pie(
        componentes_contagem,
        labels=componentes_contagem.index,
        autopct='%1.1f%%',
        startangle=140,
        colors=sns.color_palette('pastel'),
        wedgeprops=dict(width=0.3)
    )
    ax.set_title('Distribuição de Componentes Trocados', fontsize=16)
    plt.setp(autotexts, size=10, weight='bold')
    plt.setp(texts, size=12)
    return fig

def plotar_grafico_linha_tempo_trabalho(dados):
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.scatterplot(data=dados, x='data', y='trabalho_realizado', hue='trabalho_realizado', palette='viridis', s=100, ax=ax)
    ax.set_xlabel('Data', fontsize=14)
    ax.set_ylabel('Trabalho Realizado', fontsize=14)
    ax.set_title('Data x Trabalho Realizado', fontsize=16)
    ax.grid(True)
    return fig

# Exibir gráficos atualizados
st.subheader('Distribuição de Componentes Trocados')
fig_componentes = plotar_grafico_componentes(df_maio)
st.pyplot(fig_componentes)

st.subheader('Data x Trabalho Realizado')
fig_linha_tempo_trabalho = plotar_grafico_linha_tempo_trabalho(df_maio)
st.pyplot(fig_linha_tempo_trabalho)

# Tabela com dados filtrados
st.subheader('Registro de Manutenções Realizadas')
st.write(df_maio)

# Informações adicionais na barra lateral
st.sidebar.title('Informações Adicionais')
st.sidebar.subheader('Opções Adicionais')

opcao_sidebar = st.sidebar.selectbox('Selecione uma Opção:', ['Informações Gerais', 'Contato', 'FAQ'])
if opcao_sidebar == 'Informações Gerais':
    st.sidebar.markdown("### Informações Gerais")
    st.sidebar.markdown("""
    Esse Projeto tem como objetivo Analisar Dados de Manutenção de Veículos da Carro Exato visa explorar e visualizar dados de manutenções realizadas:
    
    Principais Funcionalidades:
    - **Dashboard Interativo**
    - **Visualizações Detalhadas**
    - **Facilidade de Uso**
                        
    Utilizando técnicas de análise e visualização de dados, ele oferece insights sobre diagnósticos frequentes, troca de componentes, entre outros.
    """)

elif opcao_sidebar == 'Contato':
    st.sidebar.markdown("""
    Para mais informações ou dúvidas, entre em contato:
    
    - **Telefone:** (11) 4055-3475
    - **LinkedIn:** [@CarroExato](https://www.linkedin.com/company/carroexato/)
    - **Instagram:** [@CarroExato](https://www.instagram.com/carroexato)
    - **E-mail:** contato@carroexato.com
    """)

elif opcao_sidebar == 'FAQ':
    st.sidebar.markdown("### FAQ")
    st.sidebar.markdown("""
    Esse Projeto tem como objetivo Analisar Dados de Manutenção de Veículos da Carro Exato visa explorar e visualizar dados de manutenções realizadas:
    
    Principais Funcionalidades:
    - **1. Qual é o objetivo deste projeto?** Analisar e visualizar dados de manutenção de veículos.
    - **2. Quais ferramentas foram utilizadas?** Python, Pandas, Matplotlib e Streamlit.
    - **3. Como posso executar o projeto?** Execute *streamlit run dashboard.py* para o dashboard.
    - **4. Onde estão os dados?** No arquivo *Data/trabalhos.csv.*
    - **5. Posso contribuir com o projeto?.** Sim, contribuições são bem-vindas!
                    
    """)

st.sidebar.info('Estes dados foram coletados em maio de 2024.')
st.info('Estes dados foram coletados em maio de 2024.')