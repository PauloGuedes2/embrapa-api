from dataclasses import dataclass


@dataclass
class ExportEntity:
    country: str
    quantity: str
    value: str
