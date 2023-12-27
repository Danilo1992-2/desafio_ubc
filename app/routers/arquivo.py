from commands.grava_dados_no_solr import grava_dados_solr
from commands.processar_arquivo import processar_arquivo
import io
from fastapi.responses import JSONResponse

from fastapi import File, UploadFile,APIRouter

router = APIRouter()

@router.post("/add-arquivo")
async def upload_do_arquivo(arquivo: UploadFile = File(...)) -> bool:
    if arquivo.filename.endswith(".csv"):
        arquivo_lido: File = await arquivo.read()
        file_stream = io.BytesIO(arquivo_lido)
        dados_arquivo: 'list[dict]' = processar_arquivo(file_stream).to_dict(orient='records')
        
        return grava_dados_solr(dados_arquivo)

    return JSONResponse(content={"message": "Arquivo não é trátavel."})
