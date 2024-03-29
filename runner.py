from src.constants import CSV_FILE
from src.manipulators.clean_nubank_html import clean_html
from src.manipulators.extract_to_csv import html_to_csv, save_to_csv
from src.manipulators.pre_analyzer import pre_analyzer

HTML_FILE = "data/Resumo de faturas _ Nubank Web App.html"

if __name__ == "__main__":
    columns = ["Date", "Purchase", "Value", "Tag", "Type", "Group"]
    try:
        try:
            cleaned_file = clean_html(HTML_FILE, bare_html=False)
            data = html_to_csv(cleaned_file, bare_html=True)
            for index, row in enumerate(data):
                data[index] = pre_analyzer(row)

            save_to_csv(data, CSV_FILE, columns)
            print(f"Dados salvos em {CSV_FILE}")
        except Exception as e:
            print(f"Erro ao carregar os dados: {e}")
            raise e

        try:
            import subprocess

            command = ["streamlit", "run", "src/dashboard/dashboards.py"]

            subprocess.run(command)
        except Exception as e:
            print(f"Erro ao rodar o dashboard: {e}")
            raise e
    except KeyboardInterrupt:
        print("Saindo do programa")
        exit(0)
