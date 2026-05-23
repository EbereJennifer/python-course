import datetime
from calendar import month

tour_start = datetime.date(2025, 7, 15)
print(type(tour_start), tour_start)

tour_ende = tour_start + datetime.timedelta(days=5)
print(type(tour_ende), tour_ende)

tour_ende = tour_start + datetime.timedelta(weeks=2)
print(type(tour_ende), tour_ende)

print()

# Ungünstige Namen
mittagspause_start = datetime.datetime(2026, 4, 9, 12, 30)
print(type(mittagspause_start), mittagspause_start)
mittagspause_ende = mittagspause_start + datetime.timedelta(minutes=45)


# Anton
# Ü: mittagspause_ende soll 45 Minuten später sein
delta_45_min = datetime. timedelta(minutes=45)
mittagspause_end = mittagspause_start + delta_45_min
print(type(mittagspause_end), mittagspause_end)

delta_1_tag = datetime.timedelta(days=1)
print(delta_45_min + delta_1_tag)

