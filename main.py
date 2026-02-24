import logging

from extracao import extrair_conteudo_html
from carga import salvar_csv, ler_csv
from transformacao import limpar_preco, transformar_html_em_objeto

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
        livros = transformar_html_em_objeto(html)
    print(livros)
    logging.info("Finalizando execução do webscrapping")


if __name__ == "__main__":
    main()
