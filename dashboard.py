import streamlit as st
import pandas as pd 
from sklearn.preprocessing import LabelEncoder as le

dados = pd.read_csv('data/trabalhos.csv')
df = pd.DataFrame(dados)
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

# Gráfico de Barras 
with st.container():
    diagnostico_contagem = df['Diagnostico'].value_counts()
    st.bar_chart(diagnostico_contagem)

# Seletores
opcao = st.selectbox('Selecione um Diagnóstico:', df['Diagnostico'].unique())
st.write(df[df['Diagnostico'] == opcao])

# Tabela
st.subheader('Registro de Manutenções Realizadas')
st.write(df)

st.info('Estes dados foram coletados em maio de 2024.')
