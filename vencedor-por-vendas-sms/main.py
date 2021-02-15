# Bibliotecas:
#   pip install pandas: integração do python com o excel
#   pip install openpyxl: integração do python com o excel
#   pip install twilio: integração do python com o sms

import pandas as pd
from twilio.rest import Client

## Your Account SID from twilio.com/console
account_sid = "AC2628af3ef76cd40c0089afb9bfa8d7bf"
## Your Auth Token from twilio.com/console
auth_token  = "efcf79aafdb10f0a995188d8825be60d"
client = Client(account_sid, auth_token)

## Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# tabela_venda_jan = pd.read_excel('janeiro.xlsx')
# print(tabela_venda_jan['Vendas'])

## Para cada arquivo:
for mes in lista_meses:
    # 'f' formatação de texto
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    # print[tabela_vendas]
    ## Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
    if (tabela_vendas['Vendas'] > 55000).any(): # 'any()' se algum valor da coluna Vendas for > 55000
        #loc: localizar uma informação numa determinada linha e coluna;
        #     retorna uma prop value, que é um array de valores
        linha = tabela_vendas['Vendas'] > 55000
        vendedor = tabela_vendas.loc[linha, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[linha, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5521972795556",
            from_="+16093364135",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)
    ## Caso não seja maior do que 55.000 não quero fazer nada
    else:
        print('Ninguém ganhou')