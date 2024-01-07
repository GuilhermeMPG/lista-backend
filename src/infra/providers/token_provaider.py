from datetime import datetime, timedelta
from http.client import HTTPException
from jose import jwt

#CONFIG
SECRET_KEY = '18cbbee3b2d14f83679875b11869e261'
ALGORITHM = 'HS256'
ESPIRES_IN_MIN = 3000

def criar_acess_token(data: dict):
    dados  = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=ESPIRES_IN_MIN)
    dados.update({'exp':expiracao})
    token_jwt = jwt.encode(dados,SECRET_KEY,algorithm=ALGORITHM)
    return token_jwt
def verificar_acess_token(token: str):
    try:
        carga = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Retorna alguma informação do payload, como o identificador do usuário ('sub')
        return carga.get('sub')
    except jwt.ExpiredSignatureError:
        # Lidar com token expirado
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        # Lidar com token inválido
        raise HTTPException(status_code=401, detail="Token inválido")
