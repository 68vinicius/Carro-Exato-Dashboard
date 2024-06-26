plt.figure(figsize=(10, 6))  
plt.plot(datas, valores, marker='o', linestyle='-', color='b', label='Diagnósticos')

plt.xlabel('Data')
plt.ylabel('Diagnóstico')
plt.title('Linha do Tempo de Diagnósticos')

plt.legend()

plt.grid(True)  
plt.tight_layout()  
plt.xticks(rotation=45)  

df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

contagem_data = df['Data'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
plt.scatter(contagem_data.index, contagem_data.values, color='green', alpha=0.7)
plt.title('Linha do Tempo de Diagnósticos')
plt.xlabel('Data')
plt.ylabel('Número de Trabalhos')
plt.grid(True)
plt.tight_layout()

plt.show()