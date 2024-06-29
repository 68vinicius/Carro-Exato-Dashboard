import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Data/trabalhos.csv')

datas = pd.to_datetime(df['Data'], dayfirst=True)
clientes = df['Cliente']
trabalho = df['Trabalho Realizado']
componentes = df['Troca do Componente']
peças = df['Peças Trocadas']
diagnosticos = df['Diagnostico']

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))

# Gráfico 1 - Diagnóstico x Quantidade de Trabalhos Realizados
peças_diagnosticos = diagnosticos.value_counts()
peças_diagnosticos.plot(kind='barh', ax=ax1)
ax1.set_xlabel('Quantidade')
ax1.set_ylabel('Diagnósticos')
ax1.set_title('Diagnóstico x Quantidade de Trabalhos Realizados')

# Gráfico 2 - Gráfico de Pizza dos Componentes
nomes_componentes = componentes.value_counts()
nomes_componentes.plot(kind='pie', ax=ax2, autopct='%1.1f%%')
ax2.set_ylabel('')
ax2.set_title('Distribuição de Diagnósticos')

# Gráfico 3 - Linha do Tempo de Componentes Trocados
ax3.plot(datas, componentes, marker='x', linestyle='--', color='r', label='Componentes')
ax3.set_xlabel('Data')
ax3.set_ylabel('Componentes')
ax3.set_title('Linha do Tempo de Componentes Trocados')

# Gráfico 4 - Linha do Tempo Combinada (Diagnósticos e Componentes)
ax4.plot(datas, diagnosticos, marker='o', linestyle='-', color='b', label='Diagnósticos')
ax4.set_xlabel('Data')
ax4.set_ylabel('Diagnósticos', color='b')
ax4.tick_params(axis='y', labelcolor='b')

# Grafico 4 - Eixo y 
ax4_2 = ax4.twinx()
ax4_2.plot(datas, componentes, marker='x', linestyle='--', color='r', label='Componentes')
ax4_2.set_ylabel('Componentes', color='r')
ax4_2.tick_params(axis='y', labelcolor='r')

ax4.set_title('Linha do Tempo Combinada (Diagnósticos e Componentes)')

fig.suptitle('Análise de Trabalhos Realizados', fontsize=16)
fig.tight_layout()
fig.subplots_adjust(top=0.92)

plt.show()

# Testes
print(peças)