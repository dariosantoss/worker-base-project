import asyncio
from fastapi import FastAPI
# from app.rabbitmq import consume
# from app.database.mongodb import db
from app.database.postgresql import AsyncSessionLocal as PostgresSession
# from app.database.oracle import AsyncSessionLocal as OracleSession

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # Inicialização das conexões com bancos de dados
    app.state.pg_session = PostgresSession()
    # app.state.oracle_session = OracleSession()
    # Iniciar o consumidor RabbitMQ
    # loop = asyncio.get_event_loop()
    # loop.run_in_executor(None, consume)

@app.on_event("shutdown")
async def shutdown_event():
    await app.state.pg_session.close()
    # await app.state.oracle_session.close()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}


