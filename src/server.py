import sys
import os

# Obtém o caminho absoluto do diretório pai do diretório atual (onde está este script)
caminho_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Adiciona o caminho do projeto ao sys.path
sys.path.append(caminho_projeto)


from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import criar_db
from routers import rotas_usuario, rotas_itemDesejos



app = FastAPI()

# origins = ['http://localhost:3000',
#            'http://localhost:4200',
#            'https://myapp.vercel.com'
#            ]

origins = ["*"]
criar_db()
# CORS
app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"]
                   )
app.include_router(rotas_usuario.router)
app.include_router(rotas_itemDesejos.router)
