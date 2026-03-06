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


def carregar_arquivo(pasta: str, nome: str, logging: logging) -> List[Dict[str, Any]]:
    """
    Carrega o csv no formato de lista
    """
    logging.info("Iniciando processo de carregar os dados de um arquivo CSV")
    file_name = os.path.join(pasta, nome)

    lista_dos_livros = []

    with open(file_name, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        lista_dos_livros = list(leitor)

    for livro in lista_dos_livros:
        print(f"Título: {livro['Titulo']}")
        print(f"Descrição: {livro['Descricao']}")
        print(f"Foto: {livro['Imagem']}")
        print(f"Quantidade: {livro['Quantidade']}")

        preco = float(livro["Preço"])

        print(f"Preço: £{preco:.2f}")
        print(f"Avalição: {livro['Avaliação']}")
        print(f"Disponível: {livro['Status']}")
        print("-" * 40)

    logging.info("Finalizando processo de carregar os dados de um arquivo CSV")
