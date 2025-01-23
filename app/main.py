from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import users, finance, reports, investments
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

print(settings.ALLOWED_ORIGINS)
print(settings.ALLOWED_ORIGINS.split(","))

# Configurar CORS para permitir o frontend acessar o backend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=settings.ALLOWED_ORIGINS.split(","),
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# Registrar rotas
app.include_router(finance.router, prefix="/api/v1/finance", tags=["Finance"])
app.include_router(investments.router, prefix="/api/v1/investments", tags=["Investments"])
app.include_router(reports.router, prefix="/api/v1/reports", tags=["Reports"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
