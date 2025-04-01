from fastapi import FastAPI, Query, HTTPException
from typing import Optional

from producao_old import get_dados_producao

app = FastAPI(
    title="API Vitibrasil - Produção",
    description="Consulta dados de produção vitivinícola da Embrapa.",
    version="1.0.0"
)

@app.get(
    "/producao",
    summary="Dados de Produção",
    description="Retorna a tabela de Produção (Produto e Quantidade) para um ano específico.",
    response_description="Dicionário com ano e lista de produtos/quantidades."
)
async def ler_producao(
    ano: Optional[int] = Query(
        None,
        description="Ano de referência (ex: 2023). Deixe vazio para o ano mais recente.",
        example=2023
    )
):
    """
    Produtos incluídos:
    - Vinho de mesa
    - Vinho fino de mesa (vinifera)
    - Suco
    - Derivados
    - Total
    """
    dados = get_dados_producao(ano)
    if "error" in dados:
        raise HTTPException(status_code=404, detail=dados["error"])
    return dados