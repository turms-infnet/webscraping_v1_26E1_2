import logging
import os
import csv
from typing import Any, Dict, List


def salvar_csv(
    livros: List[Dict[str, Any]], pasta, nome: str, logging: logging
) -> None:
    """
    Salva a lista enviada adicionando-a ao csv.
    """
    logging.info("Iniciando processo de salvar os dados em um arquivo CSV")
    file_name = os.path.join(pasta, nome)

    file = open(file_name, mode="w", newline="", encoding="utf-8")
    colunas = [
        "Titulo",
        "Descricao",
        "Imagem",
        "Quantidade",
        "Preço",
        "Avaliação",
        "Status",
    ]
    writer = csv.DictWriter(file, fieldnames=colunas)
    writer.writeheader()
    for livro in livros:
        writer.writerow(livro)

    file.close()

    logging.info("Finalizando processo de salvar os dados em um arquivo CSV")


def ler_csv(nome: str) -> List[Dict[str, Any]]:
    """
    Carrega o csv no formato de lista
    """
    logging.info("Iniciando processo de carregar os dados de um arquivo CSV")
    ...
    logging.info("Finalizando processo de carregar os dados de um arquivo CSV")
