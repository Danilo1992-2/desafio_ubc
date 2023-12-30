from fastapi.responses import JSONResponse
from fastapi import APIRouter

from logs.commands.inserir_logs import add_log
from queries.consultas_arquivo_solr import qtd_registros
from queries.consultas_arquivo_solr import qtd_alunos_agrupado

router = APIRouter()


@router.get("/metricas")
async def consulta_metricas_arquivo() -> JSONResponse:
    try:
        qtd_docs: "list[dict]" = qtd_registros()
        agrupado_idade: "list[dict]" = qtd_alunos_agrupado("idade")
        agrupado_nota: "list[dict]" = qtd_alunos_agrupado("nota_media")
        agrupado_serie: "list[dict]" = qtd_alunos_agrupado("serie")
        nota_corte = 8
        notas_aprovados: "list[dict]" = [
            {i: agrupado_nota[i]} for i in agrupado_nota if float(i) >= nota_corte
        ]
        notas_reprovados: "list[dict]" = [
            {i: agrupado_nota[i]} for i in agrupado_nota if float(i) < nota_corte
        ]

        resultado: dict = {
            "Qtd_registros": qtd_docs,
            "Qtd_alunos_idade": [agrupado_idade],
            "Qtd_alunos_serie": [agrupado_serie],
            "Qtd_alunos_aprovados": [notas_aprovados],
            "Qtd_alunos_removados": [notas_reprovados],
        }

        return JSONResponse(content=resultado)
    except Exception as e:
        add_log("Erro", "API", str(e), "Consulta metricas")
        return JSONResponse(content={f"message": f"{e}."})
