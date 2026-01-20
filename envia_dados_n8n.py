import requests, os
from dotenv import load_dotenv

#Carrega dados do .env
load_dotenv()

def envia_dados_n8n(comentarios):
    try:
        url = os.getenv('URL')
        body = {'lista reviews': comentarios}

        request = requests.get(url=url,json=body)

        if request.status_code == 200:
            status = 'Sucesso!'
    
        return status
    except:
        print(f'{KeyError} - {request.status_code}')