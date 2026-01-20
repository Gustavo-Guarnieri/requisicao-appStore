from cria_jtw import cria_token;
from requisicao_app_store import requisicao_store;
from envia_dados_n8n import envia_dados_n8n;

def executa_pipeline():
    #Cria token JWT para requisição
    token = cria_token()

    #Faz requisição e trabalha dado
    listaComentarios = requisicao_store(token)

    #Envia dados n8n
    status = envia_dados_n8n(listaComentarios)

    return {'status': status, 'lista comentários': listaComentarios}