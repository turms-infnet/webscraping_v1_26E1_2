import logging
import os
import argparse

from extracao import extrair_conteudo_html
from carga import salvar_csv
from transformacao import transformar_html_em_objeto

logging.basicConfig(
    filename="server.log",
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s no arquivo %(filename)s e função %(funcName)s na linha %(lineno)d: %(message)s",
)

URL: str = ""
FILE_NAME: str = ""
FOLDER_NAME = os.path.dirname(os.path.abspath(__file__))


def main():
    logging.info("Capturando argumentos")
    parser = argparse.ArgumentParser(description="Web Scraping de livros")

    parser.add_argument(
        "--url",
        type=str,
        required=True,
        default="http://books.toscrape.com/",
        help="URL do site a ser raspado",
    )
    parser.add_argument(
        "--file",
        type=str,
        required=True,
        default="output.csv",
        help="Nome do arquivo CSV de saída",
    )

    args = parser.parse_args()
    URL = args.url
    FILE_NAME = args.file

    logging.info("Iniciando execução do webscrapping")
    livros_totais = []

    url_pagina = f"{URL}catalogue/page-1.html"

    while True:
        logging.info(f"Extraindo conteúdo HTML da página: {url_pagina}")
        html = extrair_conteudo_html(url_pagina, logging)
        if html:
            livros, next_btn = transformar_html_em_objeto(html, URL, logging)
            livros_totais.extend(livros)

        if next_btn:
            url_pagina = f"{URL}catalogue/{next_btn.find('a')['href']}"
        else:
            break

    logging.info("Finalizando execução do webscrapping")

    if len(livros_totais) > 0:
        salvar_csv(livros_totais, FOLDER_NAME, FILE_NAME, logging)


if __name__ == "__main__":
    main()
