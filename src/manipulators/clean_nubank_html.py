from bs4 import BeautifulSoup

from src.constants import TAGS, CLEANED_HTML

alias_compras = {
    "tools": TAGS.FERRAMENTAS,
    "chevron": TAGS.CHEVRON,
    "card": TAGS.CARTAO,
    "taxi_car": TAGS.CARRO,
    "restaurant": TAGS.RESTAURANTE,
    "shopping_cart": TAGS.MERCADO,
    "airplane": TAGS.VIAGEM,
    "games": TAGS.COMPRA_ONLINE,
    "others": TAGS.OUTROS,
    "shopping_bag_outlined": TAGS.COMPRAS,
    "house": TAGS.OUTROS,
    "ping_pong": TAGS.OUTROS,
}


def remove_everything_except_table(html: str, bare_html=False):
    if not bare_html:
        with open(html, "r", encoding="utf-8") as file:
            html_content = file.read()
        soup = BeautifulSoup(html_content, "lxml")
    else:
        html_content = html
        soup = BeautifulSoup(html_content, "html.parser")

    table = soup.find("table", class_="css-1cohq0g")

    with open(CLEANED_HTML, "w") as file:
        file.write(str(table))

    return str(table)


def remove_svgs_from_html(html: str, bare_html=False):
    if not bare_html:
        with open(html, "r", encoding="utf-8") as file:
            html_content = file.read()
    else:
        html_content = html

    soup = BeautifulSoup(html_content, "lxml")

    for svg in soup.find_all("svg"):
        title = svg.find("title").text

        if not title == "chevron":
            div = soup.new_tag("div", attrs={"class": "operation-type"})
            div.string = alias_compras.get(title, TAGS.OUTROS)
            svg.insert_before(div)
        svg.decompose()

    with open(CLEANED_HTML, "w") as file:
        file.write(str(soup))

    return str(soup)


def clean_html(html: str, bare_html=False):
    html_content = remove_everything_except_table(html, bare_html)
    html_content = remove_svgs_from_html(html_content, bare_html=True)
    return html_content
