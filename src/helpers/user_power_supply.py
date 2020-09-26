from db import session, User, PowerSupply, Address

def get_user_power_supply(user):
    user_address = user.address

    ps = session.query(PowerSupply).\
        join(PowerSupply.address).\
        filter(Address.country == user_address.country,
               Address.state == user_address.state,
               Address.city == user_address.city,
               Address.neighbourhood == user_address.neighbourhood).one_or_none()

    return ps