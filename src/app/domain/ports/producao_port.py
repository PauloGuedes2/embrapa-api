from abc import ABC, abstractmethod
from typing import List

from src.app.domain.entities.producao_entity import ProducaoEntity



class ProducaoInterface(ABC):
    @abstractmethod
    def buscar_producao(self, ano: int) -> List[ProducaoEntity]: ...


class ProducaoRepository(ABC):
    @abstractmethod
    def salvar_producao(self, producao: List[ProducaoEntity]) -> None: ...
