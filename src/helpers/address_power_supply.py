from db import session, User, PowerSupply, Address
from services.postal_info import build_address


def get_address_power_supply(address):
    ps = session.query(PowerSupply)\
         .join(PowerSupply.address)\
         .filter(Address.country == address.country,
                 Address.state == address.state,
                 Address.city == address.city,
                 Address.neighbourhood == address.neighbourhood)\
         .one_or_none()

    return ps


def get_postal_code_power_supply(postal_code):
    address = build_address(postal_code)
    return get_address_power_supply(address)


def get_user_power_supply(user):
    address = user.address
    return get_address_power_supply(address)
