from src.constants import TAGS, GROUPS, NUBANK_ALIAS, TYPES, FIXES


class Movimentation:
    def __init__(
        self, date, purchase, value, tag, type: str = None, group: str = GROUPS.OUTROS
    ):
        self.date = date
        self.purchase = purchase
        self.value = value
        self.tag = tag
        self.type = type
        self.group = group

    def __str__(self):
        return f"Compra: {self.purchase}, Valor: {self.value}"

    @property
    def as_list(self):
        return [self.date, self.purchase, self.value, self.tag, self.type, self.group]


GROUP_FOOD = [TAGS.MERCADO, TAGS.RESTAURANTE]


def pre_analyzer(csv_row):
    mov = Movimentation(*csv_row)

    if "Pagamento recebido" in mov.purchase:
        mov.type = TYPES.RECEBIMENTO
    else:
        mov.type = TYPES.COMPRA

    if "posto" in mov.purchase.lower():
        mov.tag = TAGS.ABASTECIMENTO
        mov.group = GROUPS.CARRO

    if NUBANK_ALIAS.SEM_PARAR in mov.purchase:
        mov.tag = TAGS.SEM_PARAR
        mov.group = GROUPS.CARRO

    if NUBANK_ALIAS.IFOOD in mov.purchase:
        mov.tag = TAGS.RESTAURANTE
        mov.group = GROUPS.ALIMENTACAO

    if mov.tag in GROUP_FOOD and mov.group != TAGS.RESTAURANTE:
        mov.group = GROUPS.ALIMENTACAO

    if mov.purchase in FIXES:
        mov.group = GROUPS.FIXO

    if "IOF" in mov.purchase:
        mov.tag = TAGS.OUTROS
        mov.group = GROUPS.IMPOSTOS

    return mov.as_list
