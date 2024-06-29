import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv('Data/trabalhos.csv')

# Preparar dados
datas = pd.to_datetime(df['Data'], dayfirst=True)
clientes = df['Cliente']
trabalho = df['Trabalho Realizado']
componentes = df['Troca do Componente']
peças = df['Peças Trocadas']
diagnosticos = df['Diagnostico']

# Criar a figura e subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))

# Gráfico 1 - Diagnóstico x Quantidade de Trabalhos Realizados
peças_diagnosticos = diagnosticos.value_counts()
peças_diagnosticos.plot(kind='barh', ax=ax1)
ax1.set_xlabel('Quantidade')
ax1.set_ylabel('Diagnósticos')
ax1.set_title('Diagnóstico x Quantidade de Trabalhos Realizados')

# Gráfico 2 - Gráfico de Pizza das Peças Trocadas
peças.value_counts().plot(kind='pie', ax=ax2, autopct='%1.1f%%')
ax2.set_ylabel('')
ax2.set_title('Distribuição de Peças Trocadas')

# Gráfico 3 - Gráfico de Dispersão de Data x Trabalho Realizado
ax3.scatter(datas, trabalho, marker='o', color='b', alpha=0.7)
ax3.set_xlabel('Data')
ax3.set_ylabel('Trabalho Realizado')
ax3.set_title('Data x Trabalho Realizado')
ax3.grid(True)

# Gráfico 4 - Linha do Tempo Combinada (Diagnósticos e Componentes)
ax4.plot(datas, diagnosticos, marker='o', linestyle='-', color='b', label='Diagnósticos')
ax4.set_xlabel('Data')
ax4.set_ylabel('Diagnósticos', color='b')
ax4.tick_params(axis='y', labelcolor='b')

# Segundo eixo y no mesmo gráfico para Componentes Trocados
ax4_componentes = ax4.twinx()
ax4_componentes.plot(datas, componentes, marker='x', linestyle='--', color='r', label='Componentes')
ax4_componentes.set_ylabel('Componentes Trocados', color='r')
ax4_componentes.tick_params(axis='y', labelcolor='r')

ax4.set_title('Linha do Tempo Combinada (Diagnósticos e Componentes)')

# Título da figura
fig.suptitle('Análise de Trabalhos Realizados @CarroExato', fontsize=16)

# Ajustes de layout
fig.tight_layout()
fig.subplots_adjust(top=0.92)

# Exibir gráfico
plt.show()

# Testes
print(componentes)