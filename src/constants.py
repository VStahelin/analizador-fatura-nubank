from collections import namedtuple

CSV_FILE = "data/report.csv"
CLEANED_HTML = "data/cleaned_table.html"

TAGS = namedtuple(
    "TAGS",
    [
        "FERRAMENTAS",
        "CHEVRON",
        "CARTAO",
        "CARRO",
        "RESTAURANTE",
        "MERCADO",
        "VIAGEM",
        "COMPRA_ONLINE",
        "OUTROS",
        "COMPRAS",
        "ABASTECIMENTO",
        "SEM_PARAR",
    ],
)(
    "Ferramentas",
    "Chevron",
    "Cartao",
    "Carro",
    "Restaurante",
    "Mercado",
    "Viagem",
    "Compra online",
    "Outros",
    "Compras",
    "Abastecimento",
    "Sem Parar",
)

GROUPS = namedtuple("GROUPS", ["CARRO", "OUTROS", "ALIMENTACAO", "FIXO", "IMPOSTOS"])(
    "Carro", "Outros", "Alimentação", "Fixo", "Impostos"
)

TYPES = namedtuple("TYPES", ["COMPRA", "RECEBIMENTO"])("Compra", "Recebimento")

NUBANK_ALIAS = namedtuple(
    "NAMES",
    [
        "ABASTECIMENTO",
        "RECEBIMENTO",
        "SEM_PARAR",
        "IFOOD",
        "TIM",
        "SPOTIFY",
        "GITHUB",
        "JETBRAINS",
        "GOOGLEDOMAIN",
        "GOOGLEELLATION",
        "YOUTUBEPREMIUM",
        "TWITCH",
        "MELIMAIS",
        "DISCORD",
        "NUBANK",
    ],
)(
    "Abastecimento",
    "Recebimento",
    "sem Par*sem Parar *",
    "iFood",
    "Tim S A",
    "Ebn*Spotify",
    "Github, Inc.",
    "Jetbrains Americas Inc",
    "Google Domains",
    "Dl *Google Ellation",
    "Google Youtubepremium",
    "Google Twitch",
    "Mp *Melimais",
    "Discord* Nitromonthly",
    "Nubank - Tarifa de assinatura",
)

FIXES = [
    NUBANK_ALIAS.TIM,
    NUBANK_ALIAS.SPOTIFY,
    NUBANK_ALIAS.GITHUB,
    NUBANK_ALIAS.JETBRAINS,
    NUBANK_ALIAS.GOOGLEDOMAIN,
    NUBANK_ALIAS.GOOGLEELLATION,
    NUBANK_ALIAS.YOUTUBEPREMIUM,
    NUBANK_ALIAS.TWITCH,
    NUBANK_ALIAS.MELIMAIS,
    NUBANK_ALIAS.DISCORD,
    NUBANK_ALIAS.NUBANK,
]
