import smtplib
import email.message as message

def enviar_email(resumo_loja, loja):
    # Usando servidor gmail
    server = smtplib.SMTP('smtp.gmail.com:587')

    # f''' ''': Para formatar um bloco inteiro de texto
    email_content = f'''
    <p>Coe, Lira,</p>
    {resumo_loja.to_html()}
    <p>Tmj</p>'''

    msg = message.Message()
    msg['Subject'] = f'Lira Rules - Loja: {loja}'
    msg['From'] = 'shjovem.ti@gmail.com'
    msg['To'] = 'shjovem.ti@gmail.com'

    password = 'shalomjovem'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    # Inicializando o gmail
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    # Enviando email codificado para utf-8
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))