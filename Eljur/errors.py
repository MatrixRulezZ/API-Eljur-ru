import re
from requests import Session


def _findData(soup):
    for tag in soup.find_all("script"):
        contents = tag.contents
        for content in contents:
            if "sentryData" in content:
                return content


def _checkStatus(err, url):
    if not err.status_code:
        return {"error": {"error_code": -102,
                          "error_msg": f"Возникла ошибка при отправке запроса по ссылке {url}"}}
    if err.status_code >= 400:
        return {"error": {"error_code": -102,
                          "error_msg": f"Возникла ошибка {err.status_code} при отправке запроса  по ссылке {url}"}}
    else:
        return {"answer": "Ok",
                "result": True}


def _checkSubdomain(subdomain):
    subdomain = re.search(r"[a-zA-Z0-9]+", subdomain)
    if not subdomain:
        return {"error": {"error_code": -101,
                          "error_msg": "Поддомен не найден"}}
    else:
        return subdomain[0]


def _checkSession(session):
    if not isinstance(session, Session):
        return {"error": {"error_code": -201,
                          "error_msg": "Вы передали не сессию."}}
    else:
        return {"answer": "Ok",
                "result": True}
