from db import session, User, Address, Bill, Occurrence, PowerSupply

from random import randint, random, uniform
from datetime import datetime, timedelta, date


def generate_test_user():

    generated_cpf = "".join([str(randint(0, 9)) for i in range(11)])
    user = User.where(User.document == generated_cpf).first()
    while user is not None:
        generated_cpf = "".join([str(randint(0, 9)) for i in range(11)])
        user = User.where(User.document == generated_cpf).first()

    user = User(
        document=generated_cpf,
        first_name="Test User",
        last_name=generated_cpf,
        email=f"test_{generated_cpf}@email.com",
        phone_number=f"55119{generated_cpf[0:8]}")

    generated_cep = "".join([str(randint(0, 9)) for i in range(8)])
    address = Address.where(Address.postal_code == generated_cep).first()
    while address is not None:
        generated_cep = "".join([str(randint(0, 9)) for i in range(8)])
        address = Address.where(Address.postal_code == generated_cep).first()

    address = Address(
        postal_code=generated_cep,
        country="BR",
        state="SP",
        city="São Paulo",
        neighbourhood=f"Bairro {generated_cep}",
        street=f"Rua {generated_cep}"
    )

    power_supply = PowerSupply(
        status="up",
        description=f"Power Supply {generated_cep}")

    occurrence = Occurrence(power_supply=power_supply,
                            category=("power_outage" if random()
                                      < 0.5 else "maintenance"),
                            description=f"Occurance 1",
                            status=("done" if power_supply.is_up(
                            ) else "in_progress" if random() < 0.5 else "cancelled"),
                            start_time=datetime.now()-timedelta(weeks=2),
                            end_time=(datetime.now()-timedelta(weeks=1)
                                      if power_supply.is_up() else None),
                            estimated_end_time=(datetime.now()-timedelta(hours=1) if random() < 0.5 else None))

    today = date.today()
    day = today.day
    month = today.month
    year = today.year
    due_dates = []
    for i in range(24):
        due_dates.append(datetime.strptime(f"{day}-{month}-{year}", "%d-%m-%Y").date())
        month = month-1 if month > 1 else 12
        year = year-1 if month == 12 else year

    bills = [Bill(user=user,
                  value=round(uniform(0.0, 500.0), 2),
                  paid=random() < 0.5,
                  due_date=due_date)
             for due_date in due_dates]

    power_supply.address = address
    user.address = address

    session.add(address)
    session.add(user)
    session.add(power_supply)
    session.add(occurrence)
    session.add_all(bills)

    session.commit()
    
    return {
        "cpf": generated_cpf,
        "cep": generated_cep,
        "oldest_bill": due_dates[-1],
        "most_recent_bill": due_dates[0]
    }
