from db.models import power_supply
from db import session
from db import User, Address, Bill, Occurrence, PowerSupply

from services.postal_info import build_address

import random
from datetime import date, timedelta, datetime

postal_code_samples = ["05429100", "02420060", "03803140", "08245590",
                       "08141710", "04575020", "01543971", "02308201",
                       "02807100", "05657110"]

ps_addresses = [build_address(postal_code)
                for postal_code in postal_code_samples]

power_supplies = [
    PowerSupply(address=address,
                description=f"Power Supply {i}",
                status=("up" if random.random() < 0.5 else "down"))
    for i, address in enumerate(ps_addresses)]

occurrences = [
    Occurrence(power_supply=power_supply,
               category=("power_outage" if random.random() < 0.5
                         else "maintenance"),
               description=f"Occurance {i}",
               status=("done" if power_supply.status == "up"
                       else "in_progress" if random.random() < 0.5
                       else "cancelled"),
               start_time=datetime.now()-timedelta(weeks=i+1),
               end_time=(datetime.now()-timedelta(weeks=i)
                         if power_supply.status == "up"
                         else None),
               estimated_end_time=(datetime.now()+timedelta(hours=i)
                                   if random.random() < 0.5
                                   else None))
    for i, power_supply in enumerate(power_supplies)]

user_addresses = [build_address(postal_code)
                  for postal_code in postal_code_samples]

users = [User(document=f"0123456789{i}",
              first_name="User",
              last_name=str(i),
              email=f"user{i}@example.com",
              phone_number=f"551191234567{i}"[0:13],
              address=address)
         for i, address in enumerate(user_addresses)]

bills = [Bill(user=user,
              value=round(random.uniform(0.0, 500.0), 2),
              paid=random.random() < 0.5,
              due_date=date.today()+timedelta(weeks=4*i))
         for i in range(5)
         for user in users]

session.add_all(ps_addresses)
session.add_all(power_supplies)
session.add_all(occurrences)
session.add_all(user_addresses)
session.add_all(users)
session.add_all(bills)

session.commit()
