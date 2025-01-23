# backend_manage_finances_and_investments

Gerencie finanças e investimentos pessoais

## Instalar ambiente

Se não tiver o `virtualenv` instalado ainda, pode instalá-lo pelo comando:

```shellscript
pip install virtualenv
```

Instalar a máquina virtual para o projeto python

```shellscript
virtualenv venv
```

Ativar a máquina virtual para o projeto

```shellscript
# On Windows
.\venv\Scripts\Activate

# On Unix
source venv/bin/activate
```

Instalar as dependências do projeto

```shellscript
# On Windows
pip install -r .\requirements.txt

# On Unix
pip install -r ./requirements.txt
```

Para rodar o FastAPI, execute o seguinte comando:

```shellscript
uvicorn main:app --reload
```
