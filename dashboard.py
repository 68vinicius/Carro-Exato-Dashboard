import streamlit as st
import pandas as pd

df = pd.read_csv('Data/dataset_diagnostico_reparos_maio_2024.csv')

st.set_page_config(page_title='Dashboard Carro Exato')
st.title('Manutenções e Diagnósticos Realizados')
st.image("https://github.com/68vinicius/Carro-Exato-Dashboard/raw/main/Imagens/CarroExatoBanner.jpg", caption="www.carroexato.com.br")
st.subheader('Explore os Detalhes das Manutenções')
st.markdown("Apresentamos uma variedade de manutenções recentes feitas pela Carro Exato, desde problemas comuns como falhas no motor até questões específicas como vazamentos de óleo. Convidamos você a explorar nossos dados e visualizar detalhes das manutenções realizadas.")

# Diagnóstico mais Frequente
diagnostico_contagem = df['diagnostico'].value_counts()
diagnostico_mais_frequente = diagnostico_contagem.idxmax()
quantidade_diagnosticos = diagnostico_contagem.max()

with st.container():
    st.subheader('Análise de Diagnósticos:')
    st.write(f"O diagnóstico mais frequente foi '{diagnostico_mais_frequente}' com {quantidade_diagnosticos} ocorrências.")
    st.bar_chart(diagnostico_contagem)

# Seletores
opcao = st.selectbox('Selecione um Diagnóstico:', df['diagnostico'].unique())
st.write(df[df['diagnostico'] == opcao])

# Tabela
st.subheader('Registro de Manutenções Realizadas')
st.write(df)

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
st.sidebar.info('Estes dados foram coletados em maio de 2024.')