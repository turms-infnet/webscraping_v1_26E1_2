import logging

from extracao import extrair_conteudo_html

logging.basicConfig(
    filename="server.log",
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s no arquivo %(filename)s e função %(funcName)s na linha %(lineno)d: %(message)s",
)


def main():
    logging.info("Iniciando execução do webscrapping")
    html = extrair_conteudo_html("http://books.toscrape.com/", logging)
    if html:
        ...
    logging.info("Finalizando execução do webscrapping")


if __name__ == "__main__":
    main()
