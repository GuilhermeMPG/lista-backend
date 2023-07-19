from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])

def gerar_hash(text):
    return pwd_context.hash(text)

def verificar_hash(texto,hash):
    return pwd_context.verify(texto, hash)