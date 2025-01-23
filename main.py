from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurar CORS para permitir o frontend acessar o backend
origins = ["http://localhost:3000"]  # URL onde o Next.js estará rodando
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI"}

@app.get("/data")
async def get_data():
    return {"key": "value", "other_key": "other_value"}
