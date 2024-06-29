import streamlit as st
import pandas as pd 
from sklearn.preprocessing import LabelEncoder as le

df = pd.read_csv('Data/trabalhos.csv')
label_encoder = le()

cols_to_encode = ['Diagnostico', 'Trabalho Realizado', 'Troca do Componente']
for col in cols_to_encode:
    df[f'{col}_encoded'] = label_encoder.fit_transform(df[col])

st.set_page_config(page_title='Dashboard Carro Exato')

with st.container():
    st.markdown("<h1 style='text-align: center;'>Carro Exato</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Manutenções e Diagnósticos Realizadas</h2>", unsafe_allow_html=True)

with st.container():
    st.write('---')

st.image("https://github.com/68vinicius/Carro-Exato-Dashboard/raw/main/Imagens/CarroExatoBanner.jpg", caption="www.carroexato.com.br")

st.subheader('Explore os Detalhes das Manutenções')
st.markdown("Apresentamos uma variedade de manutenções recentes feitas pela Carro Exato, desde problemas comuns como falhas no motor até questões específicas como vazamentos de óleo. Convidamos você a explorar nossos dados e visualizar detalhes das manutenções realizadas.")

# Seletores
opcao = st.selectbox('Selecione um Diagnóstico:', df['Diagnostico'].unique())
st.write(df[df['Diagnostico'] == opcao])

# Gráfico de Barras 
with st.container():
    diagnostico_contagem = df['Diagnostico'].value_counts()
    st.bar_chart(diagnostico_contagem)

# Tabela
st.subheader('Registro de Manutenções Realizadas')
st.write(df)

st.sidebar.title('Informações Adicionais')
st.sidebar.info('Estes dados foram coletados em maio de 2024.')

# Widgets Adicionais 
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
    st.sidebar.markdown("### Contato")
    st.sidebar.markdown("""
    Esse Projeto tem como objetivo Analisar Dados de Manutenção de Veículos da Carro Exato visa explorar e visualizar dados de manutenções realizadas:
    
    Principais Funcionalidades:
    - **1. Qual é o objetivo deste projeto?** Analisar e visualizar dados de manutenção de veículos.
    - **2. Quais ferramentas foram utilizadas?** Python, Pandas, Matplotlib e Streamlit.
    - **3. Como posso executar o projeto?** Execute *python graficos.py* para os gráficos e streamlit *run dashboard.py* para o dashboard.
    - **4. Onde estão os dados?** No arquivo *Data/trabalhos.csv.*
    - **5. Posso contribuir com o projeto?.** Sim, contribuições são bem-vindas!
                    
    """)

st.info('Estes dados foram coletados em maio de 2024.')
