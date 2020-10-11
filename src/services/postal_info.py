import requests
import re

from db import Address


def get_postal_info(postal_code):
    r = requests.get(f"https://viacep.com.br/ws/{postal_code}/json")
    r_json = r.json()

    return {
        "postal_code": re.sub('[^0-9]', '', r_json["cep"]),
        "street": r_json["logradouro"],
        "number": r_json["complemento"],
        "neighbourhood": r_json["bairro"],
        "city": r_json["localidade"],
        "state": r_json["uf"]
    }


def build_address(postal_code):
    address = Address(country="BR")
    postal_info = get_postal_info(postal_code)
    address.from_dict(postal_info)

    return address
