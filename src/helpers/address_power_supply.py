from db import session, User, PowerSupply, Address
from services.postal_info import build_address


def get_address_power_supply(address):
    ps = session.query(PowerSupply)\
         .join(PowerSupply.address)\
         .filter(Address.country == address.country,
                 Address.state == address.state,
                 Address.city == address.city,
                 Address.neighbourhood == address.neighbourhood)\
         .first()

    return ps


def get_power_supply_by_postal_code(postal_code):
    ps = session.query(PowerSupply)\
         .join(PowerSupply.address)\
         .filter(Address.postal_code == postal_code)\
         .first()

    return ps


def get_user_power_supply(user):
    address = user.address
    return get_address_power_supply(address)
