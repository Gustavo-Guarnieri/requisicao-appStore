from fastapi import FastAPI 
from pipeline import executa_pipeline

app = FastAPI()

#para rodar o código local, executar no terminal: uvicorn api:app --reload

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import os

security = HTTPBearer()

def bearer_auth(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    expected_token = os.getenv("INTERNAL_API_TOKEN")

    if token != expected_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token"
        )


@app.get("/")
async def pipeline(auth=Depends(bearer_auth)):
    return executa_pipeline()