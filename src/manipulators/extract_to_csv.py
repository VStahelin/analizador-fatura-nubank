from bs4 import BeautifulSoup
import csv

from src.manipulators.convert_nubank_date import convert_date


def html_to_csv(html, bare_html=False, control_value: int = 0):
    data = []
    last_date = None
    ignore_rows = False

    if not bare_html:
        with open(html, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
    else:
        soup = BeautifulSoup(html, "html.parser")

    table = soup.find("table", class_="css-1cohq0g")
    rows = table.find_all("tr", class_="css-1luwt7m")  # noqa
    for row in rows:
        if ignore_rows:
            continue

        columns = row.find_all("td")

        try:
            data_date = columns[0].find("p", class_="css-1737x48").text.strip()
            data_date = convert_date(data_date) if data_date else None
        except AttributeError:
            data_date = None

        data_purchase = columns[3].find("p", class_="css-32almw").text.strip()
        data_value = (
            columns[4]
            .find("p", class_="css-d9h716")
            .text.strip()
            .replace("R$", "")
            .strip()
        )

        if data_value.startswith("-"):
            data_value = -float(data_value[1:].replace(".", "").replace(",", "."))
        else:
            data_value = float(data_value.replace(".", "").replace(",", "."))

        if (
                control_value
                and data_purchase == "Pagamento recebido"
                and data_value >= control_value
        ):
            ignore_rows = True
            continue

        try:
            purchase_type = (
                columns[2].find("div", class_="operation-type").text.strip()
            )
        except AttributeError:
            print(
                f"Não foi possível encontrar o tipo da compra para {data_purchase}"
            )
            purchase_type = None

        if not data_date:
            data_date = last_date
        last_date = data_date

        data.append([data_date, data_purchase, data_value, purchase_type])

    return data


def save_to_csv(data, filename, columns=None):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        sep = ","

        writer = csv.writer(
            file, delimiter=sep, quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        if columns:
            writer.writerow(columns)
        else:
            writer.writerow(["Date", "Purchase", "Value", "Tag"])
        writer.writerows(data)
