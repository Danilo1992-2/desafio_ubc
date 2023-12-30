from fastapi.responses import JSONResponse
from fastapi import File, UploadFile, APIRouter

from commands.processa_envia import main
from logs.commands.inserir_logs import add_log

router = APIRouter()


@router.post("/add-arquivo")
async def upload_do_arquivo(arquivo: UploadFile = File(...)) -> JSONResponse:
    try:
        if arquivo.filename.endswith(".csv"):
            caminho_arquivo: str = f"arquivos/{arquivo.filename}"
            with open(f"{caminho_arquivo}", "wb") as novo_arquivo:
                novo_arquivo.write(arquivo.file.read())
            resultado: str = main(caminho_arquivo)

            return (
                JSONResponse(content={"message": f"{resultado}"})
                if resultado == "OK"
                else JSONResponse(content={"message": f"{resultado}"})
            )

        return JSONResponse(content={"message": "Arquivo não é trátavel."})

    except Exception as e:
        add_log("Erro", "API", str(e), arquivo.filename)
        return JSONResponse(content={f"message": f"{e}."})
