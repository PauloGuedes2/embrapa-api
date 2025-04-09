from enum import Enum


class Option(str, Enum):
    PRODUCTION = "?opcao=opt_02"
    PROCESSING = "?opcao=opt_03"
    COMMERCIALIZATION = "?opcao=opt_04"
    IMPORT = "?opcao=opt_05"
    EXPORT = "?opcao=opt_06"


class ImportSubOption(str, Enum):
    subopt_01 = "Vinhos de mesa"
    subopt_02 = "Espumantes"
    subopt_03 = "Uvas frescas"
    subopt_04 = "Uvas passas"
    subopt_05 = "Suco de uva"


class ExportSubOption(str, Enum):
    subopt_01 = "Vinhos de mesa"
    subopt_02 = "Espumantes"
    subopt_03 = "Uvas frescas"
    subopt_04 = "Suco de uva"
