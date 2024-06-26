import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Data/trabalhos.csv')
df.head()

datas = df['Data']
clientes = df['Cliente']
componentes = df['Troca do Componente']
peças = df['Peças Trocadas']
diagnosticos = df['Diagnostico']

# Grafico 1
peças_diagnosticos = diagnosticos.value_counts()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
peças_diagnosticos.plot(kind='barh', ax=ax1)

ax1.set_xlabel('Diagnósticos')
ax1.set_ylabel('Quantidade')
ax1.set_title('Quantidade de Diagnósticos por Tipo')

# Grafico 2
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')
contagem_data = df['Data'].value_counts().sort_index()

ax2.scatter(contagem_data.index, contagem_data.values, color='green', alpha=0.7)
ax2.set_title('Linha do Tempo de Diagnósticos')
ax2.set_xlabel('Data')
ax2.set_ylabel('Número de Trabalhos')

# Grafico 3
plt.figure(figsize=(10, 6))  
plt.plot(datas, marker='o', linestyle='-', color='b', label='Diagnósticos')

plt.xlabel('Data')
plt.ylabel('Diagnóstico')
plt.title('Linha do Tempo de Diagnósticos')

plt.show()

# Testes
print(peças_diagnosticos)