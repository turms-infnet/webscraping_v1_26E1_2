import logging
import os

from extracao import extrair_conteudo_html
from carga import salvar_csv, ler_csv
from transformacao import limpar_preco, transformar_html_em_objeto

logging.basicConfig(
    filename="server.log",
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s no arquivo %(filename)s e função %(funcName)s na linha %(lineno)d: %(message)s",
)

URL: str = "http://books.toscrape.com/"
FILE_NAME: str = "output.csv"
FOLDER_NAME = os.path.dirname(os.path.abspath(__file__))

def main():
    logging.info("Iniciando execução do webscrapping")
    livros_totais = []

    html = extrair_conteudo_html(URL, logging)
    if html:
        livros = transformar_html_em_objeto(html, URL, logging)
        livros_totais.extend(livros)

    if len(livros_totais) > 0:
        salvar_csv(livros, FOLDER_NAME, FILE_NAME, logging)

    logging.info("Finalizando execução do webscrapping")


if __name__ == "__main__":
    main()
