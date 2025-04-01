import requests
from bs4 import BeautifulSoup

from domain.entities.producao_entity import ProducaoEntity
from domain.ports.producao_port import ProducaoInterface


class ProducaoScraper(ProducaoInterface):
    def buscar_producao(self, ano: int) -> dict:
        url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02&ano={ano}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table', {'class': 'tb_base tb_dados'})
        producoes = []
        for row in table.find_all('tr')[1:]:
            cols = row.find_all('td')
            produto = cols[0].text.strip()
            quantidade = cols[1].text.strip()
            producoes.append(ProducaoEntity(produto, quantidade))

        return {"ano": ano, "producoes": producoes}