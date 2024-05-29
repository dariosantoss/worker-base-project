# FastAPI Worker Project

Este é um projeto de exemplo que demonstra como criar um aplicativo FastAPI que escuta uma fila do RabbitMQ e se conecta a múltiplos bancos de dados (MongoDB, PostgreSQL e Oracle).

## Requisitos

Antes de executar o projeto, certifique-se de ter as seguintes dependências instaladas:

- Python 3.7 ou superior
- Todas as dependências listadas no arquivo `requirements.txt`

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/fastapi-worker-project.git
   ```
   
2. Instalar as libs bases
 ```bash
    cd fastapi-worker-project
    pip install -r requirements.txt
```

3. Docker Postgres
 ```bash 
   docker run -d --name postgres -e POSTGRES_USER=root -e POSTGRES_PASSWORD=12345 -p 5432:5432 --restart always postgres
```

4. Executar
 ```bash 
   uvicorn app.main:app --reload
```

5. Estrutura do Projeto
 ```bash 
   fastapi-worker-project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── rabbitmq.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── mongodb.py
│   │   ├── postgresql.py
│   │   └── oracle.py
├── requirements.txt
└── README.md

```

