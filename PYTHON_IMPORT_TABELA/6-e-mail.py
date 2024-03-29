import smtplib
import ssl
import mimetypes
from email.message import EmailMessage
from dotenv import load_dotenv
import os 

load_dotenv()

# 1 - Dados do E-mail
password = os.getenv("PASSWORD")
from_email = "mc2798353@gmail.com"
to_email = "mc2798353@gmail.com"
subject = "Automação Planilha"
body = """
Olá. Segue em Anexo a Automação da Planilha, 
Para a Empresa XYZ Automação.
Qualquer dúvida estou a disposição
"""
# 2 - Montando a estrutura do e-mail
message = EmailMessage()
message["From"] = from_email
message["To"] = to_email
message["Subject"] = subject
message.set_content(body)
safe = ssl.create_default_context()
# 3 - Adicionar Anexo
anexo = "data/relatório.xlsx"
mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split('/')
with open(anexo, 'rb') as a:
     message.add_attachment(
        a.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename=anexo
    )
    
# 4 - envio do E-mail
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )