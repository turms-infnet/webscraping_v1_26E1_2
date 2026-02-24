from typing import Any, Dict, List
from bs4 import BeautifulSoup


def limpar_preco(texto_preco: str) -> float:
    """
    Retorna o preço sem os caractéres monetários, no formato ponto flutuante.
    """
    return 0.0


def transformar_html_em_objeto(html: str) -> List[Dict[str, Any]]:
    """
    Faz o parse do HTML string usando a biblioteca BeautifulSoup para o formato de List do Python.
    Retorna essa list para quem o aciona, seguindo o padrão do livro.
    """
    soup = BeautifulSoup(html, "html.parser")
    artigos = soup.find_all("article", class_="product_pod")

    livros = []

    for artigo in artigos:
        title = artigo.h3.a["title"]
        description = ""
        image = ""
        quantity_available = 0
        price = artigo.find("p", class_="price_color").text
        rating = getRating(artigo)
        status = artigo.find("p", class_="availability").text

        livros.append(
            {
                "title": title,
                "description": description,
                "image": image,
                "quantity_available": quantity_available,
                "price": limpar_preco(price),
                "rating": rating,
                "status": status,
            }
        )

    return livros


def getBookInfos() -> Any: ...


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
