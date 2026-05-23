from random import randint

print(randint(1,6))

from datetime import date, timedelta

ein_tag = date(2025, 3, 28)
delta = timedelta(days=3)
davor = ein_tag - delta
print(ein_tag, "Delta:",delta, "davor:", davor)





