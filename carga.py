import logging
from typing import Any, Dict, List


def salvar_csv(livros: List[Dict[str, Any]], nome: str, logging: logging) -> None:
    """
    Salva a lista enviada adicionando-a ao csv.
    """
    logging.info("Iniciando processo de salvar os dados em um arquivo CSV")
    ...
    logging.info("Finalizando processo de salvar os dados em um arquivo CSV")


def ler_csv(nome: str) -> List[Dict[str, Any]]:
    """
    Carrega o csv no formato de lista
    """
    logging.info("Iniciando processo de carregar os dados de um arquivo CSV")
    ...
    logging.info("Finalizando processo de carregar os dados de um arquivo CSV")
