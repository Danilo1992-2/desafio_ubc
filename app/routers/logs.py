import pandas as pd
from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

from logs.queries.consulta_logs import todos_logs


router = APIRouter()


@router.get("/extrair-logs")
async def pegar_todos_logs() -> Response or JSONResponse:
    try:
        dados: "list[list[str]]" = [
            [i.tipo, i.timestamp, i.processo, i.menssagem, i.nome_arquivo]
            for i in todos_logs()
        ]
        df: pd.DataFrame = pd.DataFrame(dados)
        df.columns = ["tipo", "timestamp", "processo", "menssagem", "arquivo"]
        csv: pd.DataFrame = df.to_csv(index=False)
        return Response(
            content=csv,
            media_type="text/csv",
            headers={"Content-Disposition": 'attachment; filename="logs.csv"'},
        )

    except Exception as e:
        return JSONResponse(content={f"message": "{e}."})
