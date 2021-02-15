import pandas as pd
from IPython.display import display
# Pacote para criar um gráfico interativo
import plotly.express as px
import plotly.io as pio

# Para forçar o pacote plotly rodar no browser
pio.renderers.default = "browser"

pd.options.display.max_columns = None
pd.options.display.max_rows = None

#######################################
# Passo 1: Importar base de dados #####
#######################################
## r: significa que o python irá ler a string crua
## encoding='latin1': para garantis não dar erros de encoding
tabela_clientes = pd.read_csv(r'ClientesBanco.csv', encoding='latin1')
# Excluindo coluna CLIENTNUM, pois não será útil para a análise
## axis=1 => coluna; axis=0 => linha
tabela_clientes = tabela_clientes.drop(['CLIENTNUM'], axis=1)
#print(tabela_clientes)

############################################
# Passo 2: Tratamento da base de dados #####
############################################
#    - Excluir/Corrigir linhas e colunas vazias
## info(): mostra um panorama com todas as colunas
display(tabela_clientes.info())
## Vemos que a coluna 'Categoria Cartão' tem um valor vazio
#    - Ajustar as colunas importadas
#    - Excluir colunas inúteis
tabela_clientes = tabela_clientes.dropna() # Exclui as linhas que têm itens vazios
display(tabela_clientes.info())
## describe(): várias informações sobre as colunas da tabela
##   Tais como: qntos itens tem; média de valores; desvio padrão; mínimo; máxima; 25%; 50%; 75%
display(tabela_clientes.describe())

##########################################
# Passo 3: Analisar a base de dados ######
##########################################
#    - Queremos descobrir o motivo dos clientes cancelarem
# Faz um somatório (count distinct) na coluna Categoria
display(tabela_clientes['Categoria'].value_counts())
# normalize=True -> exibe esses valores em %
display(tabela_clientes['Categoria'].value_counts(normalize=True))

####################################################
# Passo 4: Analisar o 80/20 - Regra de Pareto ######
#   Olhar todas as características dos clientes e  #
#  descobrir os principais motivos de cancelamento #
####################################################
# Olhar todas as características dos clientes e descobrir os principais motivos de cancelamento

# Para um laço nas linhas:
#for linha in tabela_clientes.index:

# "http://plotly.com/python/histograms/"
for coluna in tabela_clientes:
    coluna = 'Limite'
    # Criar a figura do grático
    fig = px.histogram(tabela_clientes, x=coluna, color='Categoria', )
    # Exibir a figura do gráfico
    fig.show()

# Análise Exploratória a partir dos gráficos gerados (Clientes que cancelaram)
# O que salta aos olhos???
# Coluna 'Categoria': 16% dos clientes cancelaram
# Coluna 'Idade': Não diz nada. A maioria dos clientes que cancelaram tem entre 35 e 50 anos, porém, tb é o mesmo crescimento com o total de clientes
# Coluna 'Sexo': Tb não diz nada
# Coluna 'Dependentes': Tb não diz nada
# Coluna 'Ensino': Tb não diz nada
# Coluna 'Estado Civil': Tb não diz nada
# Coluna 'Faixa Salarial': Tb não diz nada
# Coluna 'Categoria de cartão': Na categoria 'Blue' cancelaram bastante
# Coluna 'Meses como cliente':  Tb não diz nada
# Coluna 'Produtos contratados':  Tb não diz nada
# Coluna 'Inatividade': Qnto mais é o tempo de inatividade, mais cancelamentos
# Coluna 'Contatos': Qnto mais contatos o cliente fez com a operadora, mais cancelamento. Plano de ação: analisar o motivo do contato
# Coluna 'Limites': muito proporcional entre qnde de clientes e qnde de cancelados
# Coluna 'Qde de Transaçoes 12m': qnto menos transações, mais cancelamentos. Com mais de 80 transações, o cliente não cancela mais o cartão.