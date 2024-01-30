from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import criar_db
from src.routers import rotas_usuario, rotas_itemDesejos


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
