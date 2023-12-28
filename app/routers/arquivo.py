from commands.processa_envia import main
from fastapi.responses import JSONResponse

from fastapi import File, UploadFile,APIRouter

router = APIRouter()


@router.post("/add-arquivo")
async def upload_do_arquivo(arquivo: UploadFile = File(...)) -> JSONResponse:
    if arquivo.filename.endswith(".csv"):
        caminho_arquivo: str = f"app/arquivos/{arquivo.filename}"
        with open(f"app/arquivos/{arquivo.filename}", "wb") as novo_arquivo:
            novo_arquivo.write(arquivo.file.read())
        main(caminho_arquivo)
        return JSONResponse(content={"message": "Ok"})

    return JSONResponse(content={"message": "Arquivo não é trátavel."})
