# Análise de Dados Automotivos

![Carro Exato](https://github.com/68vinicius/Carro-Exato-Dashboard/assets/167829379/979a4ca6-2f06-4e32-9bcd-cb345648a351)

O projeto visa analisar dados de manutenções de veículos feitos pela Carro Exato afim de entender padrões de diagnósticos, troca de componentes e outras métricas relevantes.

## Resultados e Conclusões

### Insights Obtidos

Após analisar os dados de manutenções utilizando este dashboard, foram identificados diversos insights relevantes:

- **Principais Diagnósticos**:
  - Problemas de freios, como "Freios Rangendo", aparecem com frequência, exigindo trocas frequentes de pastilhas e outros componentes relacionados.
  - "Carro Falhando" é outro diagnóstico comum, frequentemente resolvido com substituições de velas, cabos e outros componentes de ignição.

- **Trabalhos Mais Realizados**:
  - A troca de pastilhas de freio é um trabalho recorrente, indicando uma demanda constante por manutenção preventiva nessa área.
  - Limpezas e substituições de componentes do sistema de injeção de combustível, como "Limpeza de Bicos Injetores", são frequentes, sugerindo uma preocupação com o desempenho do motor.

- **Padrões de Serviço**:
  - Algumas manutenções estão correlacionadas com estações do ano, como trocas de óleo de transmissão e preparativos para condições climáticas adversas.

### Melhorias Sugeridas

Com base nos insights obtidos, algumas melhorias podem ser consideradas para aumentar ainda mais a eficiência e satisfação do cliente:

- Implementar programas de manutenção preventiva mais agressivos, especialmente para problemas recorrentes como os relacionados aos freios.
- Explorar oportunidades de oferecer serviços adicionais de limpeza e manutenção de sistemas críticos do veículo.
- Investigar a possibilidade de expandir o leque de serviços oferecidos para atender a uma gama mais ampla de necessidades de manutenção automotiva.

### Componentes

O código está estruturado em seções principais:

- **Carga e Preparação de Dados**:
  - Utiliza o pandas para carregar dados de um arquivo CSV (`data/trabalhos.csv`).
  - Usa `LabelEncoder` do sklearn para codificar variáveis categóricas.

- **Configuração da Página**:
  - Define o título e configurações da página utilizando `st.set_page_config()`.

- **Gráficos e Tabelas**:
  - Exibe um gráfico de barras interativo (`st.bar_chart()`) mostrando a contagem de diagnósticos.
  - Permite selecionar um diagnóstico específico através de um seletor (`st.selectbox()`) e exibe os detalhes correspondentes em uma tabela.
