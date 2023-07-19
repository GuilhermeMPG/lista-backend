from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from infra.sqlalchemy.config.database import criar_db
from routers import rotas_usuario








app = FastAPI()

origins = ['http://localhost:3000',
           'https://myapp.vercel.com'
          ]
criar_db()
#CORS
app.add_middleware(CORSMiddleware,allow_origins=origins,
                                  allow_credentials=True,
                                  allow_methods=["*"],
                                  allow_headers=["*"]                            
)
app.include_router(rotas_usuario.router)
