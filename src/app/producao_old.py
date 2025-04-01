import requests
from bs4 import BeautifulSoup
from typing import Dict, List

BASE_URL = "http://vitibrasil.cnpuv.embrapa.br/index.php"


def get_dados_producao(ano: int = None) -> Dict[str, List[Dict[str, str]]]:
    """
    Extrai dados da tabela principal de Produção (colunas: Produto e Quantidade).

    Args:
        ano (int, optional): Ano específico. Se None, pega o ano mais recente.

    Returns:
        Exemplo: {"2020": [{"Produto": "Vinho de mesa", "Quantidade": "500.000 L"}, ...]}
    """
    params = {'opcao': 'opt_02'}
    if ano:
        params['ano'] = ano

    response = requests.get(BASE_URL, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar a tabela de dados
    table = soup.find('table', {'class': 'tb_base tb_dados'})
    if not table:
        return {"error": "Tabela não encontrada"}

    # Extrair linhas da tabela (ignorando cabeçalho)
    rows = []
    for tr in table.find_all('tr')[1:]:  # Pula a primeira linha (cabeçalho)
        cols = tr.find_all('td')
        if len(cols) == 2:  # Garantir que há 2 colunas (Produto e Quantidade)
            produto = cols[0].text.strip()
            quantidade = cols[1].text.strip()
            rows.append({"Produto": produto, "Quantidade": quantidade})

    return {str(ano) if ano else "Último ano disponível": rows}