import logging
import re
from typing import Any, Dict, List
from bs4 import BeautifulSoup

from extracao import extrair_conteudo_html


def limpar_preco(texto_preco: str) -> float:
    """
    Retorna o preço sem os caractéres monetários, no formato ponto flutuante.
    """
    return 0.0


def transformar_html_em_objeto(
    html: str, url: str, logging: logging
) -> List[Dict[str, Any]]:
    """
    Faz o parse do HTML string usando a biblioteca BeautifulSoup para o formato de List do Python.
    Retorna essa list para quem o aciona, seguindo o padrão do livro.
    """

    soup = BeautifulSoup(html, "html.parser")
    artigos = soup.find_all("article", class_="product_pod")

    livros = []

    for artigo in artigos:
        title = artigo.h3.a["title"]
        path = artigo.h3.a["href"]

        description = ""
        image = ""
        quantity_available = 0

        # try:
        #     description, image, quantity_available = getBookInfos(url, path, logging)
        # except Exception as e:
        #     logging.error(
        #         f"Um error ocorreu ao tentar pegar as informações do livro {str(e)}"
        #     )

        price = artigo.find("p", class_="price_color").text
        rating = getRating(artigo)
        status = artigo.find("p", class_="availability").text

        livros.append(
            {
                "Titulo": title,
                "Descricao": description,
                "Imagem": image,
                "Quantidade": quantity_available,
                "Preço": limpar_preco(price),
                "Avaliação": rating,
                "Status": limpar_in_stock(status),
            }
        )

    return livros


def getBookInfos(url: str, path: str, logging: logging) -> Any:
    html_item: str = extrair_conteudo_html(f"{url}{path}", logging)
    soup = BeautifulSoup(html_item, "html.parser")
    item = soup.find("article", class_="product_page")

    availability_text = item.find("p", class_="availability").text
    quantity_available = limpar_quantity(availability_text, logging)

    image_url = item.find("img")["src"].replace("../../", "")

    description: str = item.find_all("p")[3].text
    image: str = f"{url}{image_url}"

    return description, image, quantity_available


def limpar_quantity(availability_text, logging: logging):
    try:
        resultado = re.search(r"\((\d+)", availability_text)
        if resultado:
            return resultado.group(1)
    except Exception as e:
        logging.error(f"Um erro ocorreu ao limpar a quantidade. {str(e)}")

    return 0


def limpar_in_stock(status):
    try:
        return re.sub(r"^\s+|\s+$", "", status, flags=re.IGNORECASE)
    except Exception as e:
        logging.error(f"Um erro ocorreu ao limpar o status de estoque. {str(e)}")

    return status


def getRating(artigo: Any) -> Any:
    rating_tag = artigo.find("p", class_="star-rating").get("class", [])
    if rating_tag[1] == "One":
        return 1
    elif rating_tag[1] == "Two":
        return 2
    elif rating_tag[1] == "Three":
        return 3
    elif rating_tag[1] == "Four":
        return 4
    elif rating_tag[1] == "Five":
        return 5
