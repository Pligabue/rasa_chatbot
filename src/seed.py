from db import session
from db import User, Address, Bill, Occurrence, PowerSupply

from services.postal_info import build_address

import random
from datetime import date, timedelta, datetime

postal_code_samples = ["05429100", "02420060", "03803140", "08245590", "08141710", "04575020", "01543971", "02308201", "02807100", "05657110"]

ps_addresses = [build_address(postal_code_samples[i]) for i in range(10)]
power_supplies = [
    PowerSupply(
        address=ps_addresses[i],
        description=f"Power Supply {i}",
        status=("up" if bool(random.getrandbits(1)) else "down")
    ) for i in range(10)
]

occurrences = [
    Occurrence(
        power_supply=power_supplies[i],
        category=("power_outage" if bool(random.getrandbits(1)) else "maintenance"),
        description=f"Occurance {i}",
        status="done" if power_supplies[i].status == "up" else ("in_progress" if bool(random.getrandbits(1)) else "cancelled"),
        start_time=datetime.now()-timedelta(weeks=i+1),
        end_time=datetime.now()-timedelta(weeks=i) if power_supplies[i].status == "up" else None,
        estimated_end_time=(datetime.now()+timedelta(hours=i) if bool(random.getrandbits(1)) else None)
    ) for i in range(5)
]

user_addresses = [build_address(postal_code_samples[i]) for i in range(10)]
users = [
    User(
        document=f"0123456789{i}",
        first_name="User",
        last_name=str(i),
        email=f"user{i}@example.com",
        address=user_addresses[i]
    ) for i in range(10)]

bills = []
for user in users:
    bills = [
        Bill(
            user=user, 
            value=round(random.uniform(0.0, 500.0), 2), 
            paid=bool(random.getrandbits(1)), 
            due_date=date.today()+timedelta(weeks=4*i)
        ) for i in range(5)
    ]

session.add_all(ps_addresses)
session.add_all(power_supplies)
session.add_all(occurrences)
session.add_all(user_addresses)
session.add_all(users)
session.add_all(bills)

session.commit()
