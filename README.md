# Titanic Analysis


## Antes de tudo


**Configure seu ambiente:**

recomendo criar um ambiente virtual, rode esse comando para cria-lo:
``` shell
python -m venv .env
./env/Scripts/activate
```
execulte esses comandos no seu terminal no diretorio root do projeto:

``` shell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```


### **Fluxo que vou serguir:**

<p>
🔍 1. Exploração e Limpeza de Dados
📌 Objetivo: entender e preparar os dados antes da análise.

✅ Desafios

<ul>
  <li>
    Liste as 5 colunas com mais valores ausentes. Como pode lidar com eles?
  </li>
  <li>
    Verifique se existem dados duplicados e, se houver, remova-os.
  </li>
  <li>
    Existem outliers na coluna "Fare"? (Dica: Use um boxplot)
  </li>
  <li>
    Descubra se há correlação entre as variáveis "Age" e "Fare".
  </li>
</ul>
</p>

<p>
📊 2. Análise Estatística e Agrupamento
📌 Objetivo: obter insights usando estatísticas e agrupamentos.

✅ Desafios

<ul>
  <li>
    Qual a idade média e mediana dos passageiros por classe?
  </li>
  <li>
    Qual a taxa de sobrevivência por sexo e classe?
  </li>
  <li>
    Quem pagou a tarifa mais cara? Qual a relação entre idade e tarifa paga?
  </li>
  <li>
    Qual a proporção de passageiros que estavam sozinhos versus acompanhados? (Use as colunas SibSp e Parch para definir isso).
  </li>
</ul>
</p>

<p>
📈 3. Visualizações Avançadas
📌 Objetivo: comunicar insights de maneira clara com gráficos eficientes.

✅ Desafios

<ul>
  <li>
    Crie um gráfico de barras mostrando a distribuição de sobreviventes por classe e sexo.
  </li>
  <li>
    Faça um gráfico de dispersão (scatter plot) para mostrar a relação entre idade e tarifa.
  </li>
  <li>
    Crie um gráfico de pizza mostrando a proporção de passageiros que estavam sozinhos vs acompanhados.
  </li>
  <li>
    Gere um heatmap de correlação entre as variáveis numéricas para identificar padrões ocultos. (Dica: use seaborn.heatmap()).
  </li>
  <li>
    Use um violin plot para comparar a distribuição de idades entre passageiros que sobreviveram e os que não sobreviveram.
  </li>
</ul>
</p>

<p>
🚀 4. Desafios de Otimização
📌 Objetivo: melhorar eficiência e performance na manipulação dos dados.

✅ Desafios

<ul>
  <li>
    Converta colunas categóricas em tipo category e meça a diferença no consumo de memória antes e depois.
  </li>
  <li>
    Crie uma função para substituir apply() por operações vetorizadas e medir o tempo de execução.
  </li>
  <li>
    Utilize groupby() e agg() para calcular a média e o desvio padrão das idades por classe e sexo em uma única operação.
  </li>
  <li>
    Faça um pipeline de pré-processamento que automatize limpeza e transformação dos dados.
  </li>
</ul>
</p>

<p>
🧠 5. Desafios Extras para Pensamento Analítico
📌 Objetivo: desenvolver a capacidade de interpretar e extrair informações úteis dos dados.

✅ Desafios
<ul>
  <li>
    Baseado nos dados, qual perfil de passageiro (idade, sexo, classe) teve maior chance de sobrevivência?
  </li>
  <li>
    Se fosse criar um modelo simples para prever sobrevivência, quais colunas escolheria como mais relevantes?
  </il>
  <li>
    Existe algum padrão na distribuição de passageiros por porto de embarque?
  </li>
  <li>
    Como poderia transformar os dados para facilitar uma futura modelagem em Machine Learning?
  </li>
</ul>
</p>



