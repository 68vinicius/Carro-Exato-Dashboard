import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Data/dataset_reparos_2024.csv')

st.set_page_config(page_title='Dashboard Carro Exato')
st.markdown('<h1 style="text-align: center;">Diagnósticos e Manutenções</h1>', unsafe_allow_html=True)
st.image('https://github.com/68vinicius/Carro-Exato-Dashboard/raw/main/Imagens/CarroExatoBanner.jpg', caption='www.carroexato.com.br')
st.subheader('Explore os Detalhes das Manutenções')
st.markdown('Apresentamos uma variedade de manutenções recentes feitas pela Carro Exato, desde problemas comuns como falhas no motor até questões específicas como vazamentos de óleo. Convidamos você a explorar nossos dados e visualizar detalhes das manutenções realizadas.')

meses = df['data'].str.slice(3, 10).unique()
mes_selecionado = st.selectbox('Selecione o Mês:', meses)

class GerenciadorKPI:
    def __init__(self, dataframe):
        self.df = dataframe
        self.df_mes = None

    def filtrar_por_mes(self, mes):
        self.df_mes = self.df[self.df['data'].str.contains(mes)]

    def calcular_kpis(self):
        if self.df_mes is None:
            raise ValueError('DataFrame não filtrado. Chame o método filtrar_por_mes primeiro.')
        
        total_diagnosticos = self.df_mes.shape[0]
        custo_total_pecas = self.df_mes['valor_peca'].sum()
        custo_total_maodeobra = self.df_mes['valor_maodeobra'].sum()
        return total_diagnosticos, custo_total_pecas, custo_total_maodeobra

    def display_kpis(self):
        total_diagnosticos, custo_total_pecas, custo_total_maodeobra = self.calcular_kpis()

        col1, col2, col3 = st.columns(3)
        col1.metric('Total de Serviços', total_diagnosticos)
        col2.metric('Custo Total de Peças', f'R$ {custo_total_pecas:,.2f}')
        col3.metric('Custo Total de Mão de Obra', f'R$ {custo_total_maodeobra:,.2f}')

    def diagnostico_analise(self):
        if self.df_mes is None:
            raise ValueError('DataFrame não filtrado. Chame o método filtrar_por_mes primeiro.')
        
        diagnostico_contagem = self.df_mes['diagnostico'].value_counts().reset_index()
        diagnostico_contagem.columns = ['diagnostico', 'contagem']
        diagnostico_mais_frequente = diagnostico_contagem['diagnostico'].iloc[0]
        quantidade_diagnosticos = diagnostico_contagem['contagem'].iloc[0]
        return diagnostico_contagem, diagnostico_mais_frequente, quantidade_diagnosticos

    def display_diagnostico_analise(self):
        diagnostico_contagem, diagnostico_mais_frequente, quantidade_diagnosticos = self.diagnostico_analise()
        st.write(f'O diagnóstico mais frequente foi {diagnostico_mais_frequente} com {quantidade_diagnosticos} ocorrências.')
        st.subheader('Análise de Diagnósticos:')
        fig = px.bar(diagnostico_contagem,
                    x='diagnostico',
                    y='contagem',
                    title='Contagem de Diagnósticos',
                    labels={'diagnostico': 'Diagnóstico', 'contagem': 'Contagem'},
                    color='contagem',  
                    color_continuous_scale='Blues',  
                    text='contagem',  
                    height=600)
        fig.update_layout(
            title='Contagem de Diagnósticos', 
            xaxis_title='',
            yaxis_title='Contagem',
            xaxis_title_font=dict(size=14),
            yaxis_title_font=dict(size=14),
            xaxis_tickangle=-45,  
            yaxis=dict(range=[0, diagnostico_contagem['contagem'].max() + 10]),  
            margin=dict(l=50, r=50, t=60, b=50) 
        )
        st.plotly_chart(fig)

gerenciador_kpi = GerenciadorKPI(df)
gerenciador_kpi.filtrar_por_mes(mes_selecionado)

gerenciador_kpi.display_kpis()
gerenciador_kpi.display_diagnostico_analise()

diagnostico_contagem = gerenciador_kpi.df_mes['diagnostico'].value_counts().reset_index()
diagnostico_contagem.columns = ['diagnostico', 'contagem']

# Gráficos

# Pizza
fig = px.pie(diagnostico_contagem, names='diagnostico', values='contagem',
             title='Distribuição de Diagnósticos',
             height=600)
st.plotly_chart(fig)

# Distribuição de Diagnósticos por Localização
fig = px.bar(gerenciador_kpi.df_mes, x='localizacao_cliente', color='diagnostico', 
             title='Distribuição de Diagnósticos por Localização',
             labels={'localizacao_cliente': 'Localização', 'diagnostico': 'Diagnóstico'},
             height=400)
st.plotly_chart(fig)

# Dispersão dos Valores das Peças e da Mão de Obra
fig = px.scatter(gerenciador_kpi.df_mes, x='valor_peca', y='valor_maodeobra', color='tipo_servico',
                 title='Valor das Peças vs Valor da Mão de Obra por Tipo de Serviço',
                 labels={'valor_peca': 'Valor das Peças', 'valor_maodeobra': 'Valor da Mão de Obra'},
                 size='pecas_trocadas', hover_name='veiculo',
                 height=450)
st.plotly_chart(fig)

# Matriz de Correlação
matriz_de_correlacao = gerenciador_kpi.df_mes[['valor_peca', 'valor_maodeobra', 'pecas_trocadas']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(matriz_de_correlacao, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlação')
st.pyplot(plt)

# Boxplot
st.markdown('')
plt.figure(figsize=(12, 6))
sns.boxplot(data=gerenciador_kpi.df_mes[['valor_peca', 'valor_maodeobra']])
plt.title('Distribuição dos Valores das Peças e da Mão de Obra')
st.pyplot(plt)

# Seletores
st.markdown('')
opcao = st.selectbox('Selecione um Diagnóstico:', gerenciador_kpi.df_mes['diagnostico'].unique())
st.write(gerenciador_kpi.df_mes[gerenciador_kpi.df_mes['diagnostico'] == opcao])    

# Widgets Adicionais 
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
    - **5. Posso contribuir com o projeto?** Sim, contribuições são bem-vindas!
    """)

st.info(f'Estes dados foram coletados em {mes_selecionado}.')