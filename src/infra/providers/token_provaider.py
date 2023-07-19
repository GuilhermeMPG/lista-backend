from datetime import datetime, timedelta
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
    carga = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    return carga.get('sub')
