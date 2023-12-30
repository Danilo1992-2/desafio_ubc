from routers import arquivo
from routers import logs
from routers import consultas
from fastapi import FastAPI


app = FastAPI()

app.include_router(
    arquivo.router, prefix="/processar_arquivo", tags=["processar_arquivo"]
)
app.include_router(logs.router, prefix="/logs", tags=["logs"])
app.include_router(consultas.router, prefix="/metricas", tags=["metricas"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
