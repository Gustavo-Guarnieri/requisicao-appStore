import requests, json, os
from dotenv import load_dotenv

#Carrega dados do .env
load_dotenv()

def ajusta_data(data_toda):
        data = data_toda.split('T')[0]
        data_ajustada = f'{data.split('-')[2]}/{data.split('-')[1]}/{data.split('-')[0]}'
        return data_ajustada

def requisicao_store(token):
    #Dados para requisição
    url = f'https://api.appstoreconnect.apple.com/v1/apps/{os.getenv('APP_ID')}/customerReviews'

    headers = {
        'Authorization': f'Bearer {token}'
    }

    parameters = {
        'limit': 10,
        'sort': '-createdDate',
        'exists[publishedResponse]': 'false'
    }

    #Faz requisição
    response = requests.get(url=url, headers=headers, params=parameters)

    dados = response.json()

    with open('request_response.json','w',encoding='utf-8') as f:
        json.dump(dados,f,indent=4, ensure_ascii=False)

    #Trabalha dado para ser enviado ao n8n
    listResult = []

    for item in dados['data']:
        nota = int(item['attributes']['rating'])

        if nota < 3:
             tipo_nota = 'negativo 😡' or ''
        if nota == 3:
             tipo_nota = 'neutro 😐' or ''
        else:
            tipo_nota = 'positivo ✅' or ''
        
        listResult.append({
            'id' : item['id'],
            'nome' : item['attributes']['reviewerNickname'],
            'nota' : nota,
            'tipo_nota': tipo_nota,
            'titulo' : item['attributes']['title'],
            'texto' : item['attributes']['body'],
            'data_criacao' : ajusta_data(item['attributes']['createdDate']),
            'territorio' : item['attributes']['territory']
        })
    
    return listResult

