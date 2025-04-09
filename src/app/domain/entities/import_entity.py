from dataclasses import dataclass


@dataclass
class ImportEntity:
    country: str
    quantity: str
    value: str
