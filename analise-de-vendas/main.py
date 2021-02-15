# Bibliotecas:
#   pip install pandas: integração do python com o excel

import pandas as pd
import sendEmail

tabela_vendas = pd.read_excel('Vendas.xlsx')
#print(tabela_vendas)

## Calculando o faturamento por loja
#### Filtra colunas; agrupa pela 'ID Loja'; e soma o agrupamento
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
#print(faturamento)
### Ordena de forma decrescente por 'Valor Final'
faturamento = faturamento.sort_values(by='Valor Final', ascending=False)
#print(faturamento)

#### Filtra colunas; agrupa pela 'ID Loja'; e soma o agrupamento
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
#print(quantidade)
### Ordena de forma decrescente por 'ID Loja'
quantidade = quantidade.sort_values(by='ID Loja', ascending=False)
#print(quantidade)

# to_frame: para estruturar uma nova coluna, ou seja, cria uma nova base de dados (dataframe)
# A coluna é criada por padrão com o nome '0'
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
#print(ticket_medio)
# Modificando o nome da nova coluna
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
#print(ticket_medio)
ticket_medio = ticket_medio.sort_values(by='Ticket Médio', ascending=False)
#print(ticket_medio)

#Trazer apenas a coluna 'ID Loja', sem repetir valor (unique)
lojas = tabela_vendas['ID Loja'].unique()
#print(lojas)

#for i, loja in enumerate(lojas):
for loja in lojas:
    # Retorna colunas específicas onde o 'ID Loja' = loja específica do looping
    tabela_lojas = tabela_vendas.loc[tabela_vendas['ID Loja'] == loja, ['ID Loja', 'Quantidade', 'Valor Final']]
    # Agrupa e sumariza valores das 3 colunas por 'ID Loja'
    resumo_loja = tabela_lojas.groupby('ID Loja').sum()
    # Cria novo elemento do array
    resumo_loja['Ticket Médio'] = resumo_loja['Valor Final'] / resumo_loja['Quantidade']
    # Envia primeiro email com os dados
    sendEmail.enviar_email(resumo_loja, loja)
    # Uni as informações de faturamento + quantidade + ticket_médio
    tabela_diretoria = faturamento.join(quantidade).join(ticket_medio)
    print(tabela_diretoria)
    # Envia email para a diretoria
    sendEmail.enviar_email(tabela_diretoria, 'Todas as Lojas')