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
