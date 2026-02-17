import time, jwt
from dotenv import load_dotenv
import os

#Carrega dados do .env
load_dotenv()

def cria_token():

    #with open("AuthKey_APPLE.p8", "r") as f:
    #    private_key = f.read()
    private_key = os.getenv("API_KEY")

    jwt_headers = {
        'alg': 'ES256',
        'kid':os.getenv('API_ID'),
        'typ': 'JWT'
    }

    iat = int(time.time())
    exp = iat + 3 * 60

    jwt_payload = {
        "iss": os.getenv('ISSUER_ID'),
        "iat": iat,
        "exp": exp,
        "aud": "appstoreconnect-v1",
        "scope": [
            "GET /v1/apps/1466577398/customerReviews?limit=10&sort=-createdDate&exists[publishedResponse]=false"
        ]
    }


    jwt_sign = jwt.encode(payload=jwt_payload, headers=jwt_headers, key=private_key, algorithm='ES256')

    return jwt_sign
