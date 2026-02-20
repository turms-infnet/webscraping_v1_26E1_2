import requests
import logging
from typing import Optional


def extrair_conteudo_html(url: str, logging: logging) -> Optional[str]:
    """
    Make a request to the website to
    fetch the HTML content and
    deliver it as text (String)
    to another function for further processing.
    """
    try:
        logging.info(f"Iniciando captura da url: {url}")
        resposta = requests.get(url)
        logging.info(f"Finalizando captura da url: {url}")
        resposta.raise_for_status()
        logging.info(f"Retornando valor da url: {url}")
        return resposta.text
    except requests.exceptions.RequestException as erro:
        logging.error(f"Um erro ocorreu ao tentar acessar a urk {url}. Erro: {erro}")
        return None
