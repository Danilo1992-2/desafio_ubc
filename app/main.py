from fastapi import FastAPI
from routers import arquivo
from routers import logs

app = FastAPI()

app.include_router(
    arquivo.router, prefix="/processar_arquivo", tags=["processar_arquivo"]
)
app.include_router(logs.router, prefix="/logs", tags=["logs"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
