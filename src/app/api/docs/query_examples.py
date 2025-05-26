from fastapi import Query

from domain.enum.enums import ExportSubOption, ImportSubOption, ProcessingSubOption


class QueryExamples:
    YEAR = Query(
        None,
        description="Ano dos dados (1970 - 2024).",
        example=2023
    )

    PRODUCTION_YEAR = Query(
        None,
        description="Ano dos dados de produção (1970 - 2023).",
        example=2023
    )

    COMMERCIALIZATION_YEAR = Query(
        None,
        description="Ano dos dados de comercialização (1970 - 2023).",
        example=2023
    )

    PROCESSING_YEAR = Query(
        None,
        description="Ano dos dados de processamento (1970 - 2024).",
        example=2024
    )

    PROCESSING_SUBOPTION = Query(
        None,
        description="Subopção da aba Processamento.",
        example=ProcessingSubOption.subopt_01
    )

    IMPORT_YEAR = Query(
        None,
        description="Ano dos dados de importação (1970 - 2024).",
        example=2024
    )

    IMPORT_SUBOPTION = Query(
        None,
        description="Subopção da aba Importação.",
        example=ImportSubOption.subopt_01
    )

    EXPORT_YEAR = Query(
        None,
        description="Ano dos dados de exportação (1970 - 2024).",
        example=2024
    )

    EXPORT_SUBOPTION = Query(
        None,
        description="Subopção da aba Exportação.",
        example=ExportSubOption.subopt_01
    )
